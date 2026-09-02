<template>
  <div v-if="ucData">
    <h1>{{ ucData.name }}</h1>

    <button class="edit-button" @click="openUsecaseModal()">Edit Name</button>

    <BaseModal title="Usecase" :is-open="isUsecaseModalOpen" @close="isUsecaseModalOpen=false" @confirm="updateUsecase()">
      <form class="modal-form" @submit.prevent>
        <div class="form-group">
          <label>Use Case Name</label>
          <input v-model="new_uc.name">
        </div>
      </form>
    </BaseModal>

    <h2 v-if="events_w_render && events_w_render.length">Events</h2>
    <div v-for="(event, event_index) in events_w_render" :key="event_index">
      <h3>{{ event.name }}</h3>

      <button class="delete-button" @click="removeEvent(Number(event_index))">Delete Event</button>

      <p>Performed by: <template v-for="actor in event.actor_name">{{ actor }}; </template></p>

      <button class="edit-button" @click="openEventModal(Number(event_index))">Edit Event</button>

      <BaseModal title="Event" :is-open="isEventModalOpen" @close="isEventModalOpen=false" @confirm="updateEvent(Number(event_index))">
        <form class="modal-form" @submit.prevent>
          <div class="form-group">
            <label>Event Name</label>
            <input v-model="new_event.name">
          </div>
          <div class="form-group">
            <label>Event Performers</label>
            <select v-model="new_event.actor_name" multiple size="4">
              <option v-for="(item, actor_index) in acData" :key="actor_index" :value="item.name">{{ item.name }}</option>
            </select>
          </div>
        </form>
      </BaseModal>

      <div v-html="event.svg"></div>

      <BaseItemBox v-for="(step, step_index) in event.event_steps" :key="step_index" @del="removeStep(Number(event_index), Number(step_index))" @edit="openStepModal(Number(event_index), Number(step_index))">
        <p>
          {{ step.step_code }}: {{ step.description }}

          <template v-if="step.next_steps">(decision)</template>
          
          <template v-else-if="step.category && step.category.attributes">({{ step.category.operation_type }})<br/><template v-for="cls in Object.keys(step.category.attributes)">{{ step.category.attributes[cls].join(", ") }} ({{ cls }}); </template></template>

          <template v-else-if="step.category && step.category.operation_type === IOOutputEnum.INPUT || step.category.operation_type === IOOutputEnum.OUTPUT">({{ step.category.operation_type }}): {{ step.category.description }}</template>
          
          <template v-else-if="step.category && step.category.description">(complex operation ({{ step.category.operation_type }}): {{ step.category.description }})</template>
          
          <template v-else-if="step.category && step.category.usecase_name">(navigate to {{ step.category.usecase_name }} - {{ step.category.event_name }}) ({{ step.category.operation_type }})</template>
        </p>
      </BaseItemBox>
      <button class="create-button" @click="openStepModal(Number(event_index), -1)">Add New</button>

      <BaseModal title="Action" :is-open="isActionModalOpen" @close="isActionModalOpen=false" @confirm="updateStep(Number(event_index), new_action.step_id)">
        <form class="modal-form" @submit.prevent>
          <div class="form-group">
            <select v-model="new_action.step.category" size="4">
              <!-- <option :value="null"></option> -->
              <option :value="new_data_op">Data Operation</option>
              <option :value="new_comp_op">Complex Operation</option>
              <option :value="new_inou_op">Input/Output Operation</option>
              <option :value="new_navi_op">Navigation Operation</option>
            </select>
          </div>
          <div class="form-group">
            <label>Step Code</label>
            <input v-model="new_action.step.step_code">
          </div>
          <div class="form-group">
            <label>Step Description</label>
            <input v-model="new_action.step.description">
          </div>
          <div v-if="new_action.step.category instanceof DataOperation">
            <div class="form-group">
              <label>Operation Type</label>
              <select v-model="new_action.step.category.operation_type" size="4">
                <option v-for="(item, index) in do_types" :key="index" :value="item">{{ item }}</option>
              </select>
            </div>
            <div class="form-group">
              <label>Attributes</label>
              <select v-model="new_action.step.category.attributes" multiple size="4">
                <optgroup v-for="(cls, cls_idx) in clData" :key="cls_idx" :label="cls.name">
                  <option v-for="(attr, atr_idx) in getAttributesAndAssociationsByClassName(cls.name)" :key="atr_idx" :value="{ group: cls.name, value: attr.name }">{{ attr.name }}</option>
                </optgroup>
              </select>
            </div>
          </div>
          <div v-else-if="new_action.step.category instanceof ComplexOperation">
            <div class="form-group">
              <label>Operation Type</label>
              <select v-model="new_action.step.category.operation_type" size="4">
                <option v-for="(item, index) in co_types" :key="index" :value="item">{{ item }}</option>
              </select>
            </div>
            <div class="form-group">
              <label>Description</label>
              <input v-model="new_action.step.category.description">
            </div>
          </div>
          <div v-else-if="new_action.step.category instanceof IOOperation">
            <div class="form-group">
              <label>Operation Type</label>
              <select v-model="new_action.step.category.operation_type" size="4">
                <option v-for="(item, index) in io_types" :key="index" :value="item">{{ item }}</option>
              </select>
            </div>
            <div class="form-group">
              <label>Description</label>
              <input v-model="new_action.step.category.description">
            </div>
          </div>
          <div v-else-if="new_action.step.category instanceof NavOperation">
            <div class="form-group">
              <label>Operation Type</label>
              <select v-model="new_action.step.category.operation_type" size="4">
                <option v-for="(item, index) in no_types" :key="index" :value="item">{{ item }}</option>
              </select>
            </div>
            <div class="form-group">
              <label>Usecase</label>
              <select v-model="new_action.step.category.usecase_name" size="4">
                <option v-for="(uc, uc_idx) in usecases" :key="uc_idx" :value="uc.name">{{ uc.name }}</option>
              </select>
            </div>
            <div class="form-group">
              <label>Usecase Event</label>
              <select v-model="new_action.step.category.event_name" size="4">
                <option v-for="(ev, ev_idx) in getEventsByUsecaseName(new_action.step.category.usecase_name)" :key="ev_idx" :value="ev.name">{{ ev.name }}</option>
              </select>
            </div>
          </div>
          <div class="form-group">
            <label>Next Step</label>
            <select v-model="new_action.step.next_step" size="4">
              <option v-for="(item, index) in event.event_steps" :key="index" :value="item.step_code">{{ item.step_code }}</option>
            </select>
          </div>
        </form>  
      </BaseModal>

      <BaseModal title="Decision" :is-open="isDecisionModalOpen" @close="isDecisionModalOpen=false" @confirm="updateStep(Number(event_index), new_decision.step_id)">
        <form class="modal-form" @submit.prevent>
          <div class="form-group">
            <label>Step Code</label>
            <input v-model="new_decision.step.step_code">
          </div>
          <div class="form-group">
            <label>Step Description</label>
            <input v-model="new_decision.step.description">
          </div>
          <div class="form-group">
            <label>Next Steps</label>
            <select v-model="new_decision.step.next_steps" multiple size="4">
              <option v-for="(item, index) in event.event_steps" :key="index" :value="item.step_code">{{ item.step_code }}</option>
            </select>
          </div>
        </form>
      </BaseModal>

      <BaseModal title="Step" :is-open="isStepModalOpen" @close="isStepModalOpen=false" @confirm="addStep(Number(event_index), isAction)">
        <form class="modal-form" @submit.prevent>
          <div v-if="isAction">
            <button @click="isAction=!isAction">Action</button>
            <div class="form-group">
              <select v-model="new_action.step.category" size="4">
                <!-- <option :value="null"></option> -->
                <option :value="new_data_op">Data Operation</option>
                <option :value="new_comp_op">Complex Operation</option>
                <option :value="new_inou_op">Input/Output Operation</option>
                <option :value="new_navi_op">Navigation Operation</option>
              </select>
            </div>
            <div class="form-group">
              <label>Step Code</label>
              <input v-model="new_action.step.step_code">
            </div>
            <div class="form-group">
              <label>Step Description</label>
              <input v-model="new_action.step.description">
            </div>
            <div v-if="new_action.step.category instanceof DataOperation">
              <div class="form-group">
                <label>Operation Type</label>
                <select v-model="new_action.step.category.operation_type" size="4">
                  <option v-for="(item, index) in do_types" :key="index" :value="item">{{ item }}</option>
                </select>
              </div>
              <div class="form-group">
                <label>Attributes</label>
                <select v-model="new_action.step.category.attributes" multiple size="4">
                  <optgroup v-for="(cls, cls_idx) in clData" :key="cls_idx" :label="cls.name">
                    <option v-for="(attr, atr_idx) in getAttributesAndAssociationsByClassName(cls.name)" :key="atr_idx" :value="{ group: cls.name, value: attr.name }">{{ attr.name }}</option>
                  </optgroup>
                </select>
              </div>
            </div>
            <div v-else-if="new_action.step.category instanceof ComplexOperation">
              <div class="form-group">
                <label>Operation Type</label>
                <select v-model="new_action.step.category.operation_type" size="4">
                  <option v-for="(item, index) in co_types" :key="index" :value="item">{{ item }}</option>
                </select>
              </div>
              <div class="form-group">
                <label>Description</label>
                <input v-model="new_action.step.category.description">
              </div>
            </div>
            <div v-else-if="new_action.step.category instanceof IOOperation">
              <div class="form-group">
                <label>Operation Type</label>
                <select v-model="new_action.step.category.operation_type" size="4">
                  <option v-for="(item, index) in io_types" :key="index" :value="item">{{ item }}</option>
                </select>
              </div>
              <div class="form-group">
                <label>Description</label>
                <input v-model="new_action.step.category.description">
              </div>
            </div>
            <div v-else-if="new_action.step.category instanceof NavOperation">
              <div class="form-group">
                <label>Operation Type</label>
                <select v-model="new_action.step.category.operation_type" size="4">
                  <option v-for="(item, index) in no_types" :key="index" :value="item">{{ item }}</option>
                </select>
              </div>
              <div class="form-group">
                <label>Usecase</label>
                <select v-model="new_action.step.category.usecase_name" size="4">
                  <option v-for="(uc, uc_idx) in usecases" :key="uc_idx" :value="uc.name">{{ uc.name }}</option>
                </select>
              </div>
              <div class="form-group">
                <label>Usecase Event</label>
                <select v-model="new_action.step.category.event_name" size="4">
                  <option v-for="(ev, ev_idx) in getEventsByUsecaseName(new_action.step.category.usecase_name)" :key="ev_idx" :value="ev.name">{{ ev.name }}</option>
                </select>
              </div>
            </div>
            <div class="form-group">
              <label>Next Step</label>
              <select v-model="new_action.step.next_step" size="4">
                <option v-for="(item, index) in event.event_steps" :key="index" :value="item.step_code">{{ item.step_code }}</option>
              </select>
            </div>
          </div>
          <div v-else>
            <button @click="isAction=!isAction">Decision</button>
            <div class="form-group">
              <label>Step Code</label>
              <input v-model="new_decision.step.step_code">
            </div>
            <div class="form-group">
              <label>Step Description</label>
              <input v-model="new_decision.step.description">
            </div>
            <div class="form-group">
              <label>Next Steps</label>
              <select v-model="new_decision.step.next_steps" multiple size="4">
                <option v-for="(item, index) in event.event_steps" :key="index" :value="item.step_code">{{ item.step_code }}</option>
              </select>
            </div>
          </div>
        </form>
      </BaseModal>

    </div>

    <br/>
  
    <button class="create-button" @click="addEvent()">Add New Event</button>

  </div>
  <p v-else-if="errorMessage">{{ errorMessage }}</p>
  <p v-else>Loading...</p>
</template>

<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import { computed, ref, toRaw, watch } from 'vue'
import { getUseCase, getUseCases, putUseCase } from '@/services/api/usecases'
import { getClassAssociations, getClassByName, getClasses } from '@/services/api/classes'
import { mermaidSvgCreator } from '@/utils/mermaid_utils'
import BaseItemBox from '@/components/BaseItemBox.vue'
import BaseModal from '@/components/BaseModal.vue'
import { DataOperation, ComplexOperation, NavOperation, Action, Decision, Event, Usecase, DataOperationEnum, ComplexOperationEnum, NavOperationEnum, IOOutputEnum, IOOperation } from '@/models/usecase_models'
import { getActors } from '@/services/api/actors'
import { ClassAttribute, type Association, type Class } from '@/models/class_models'

const route = useRoute()
const reload = ref(0)
const router = useRouter()
const ucData = ref()
const acData = ref()
const clData = ref()
const usecases = ref()
const classAssoc = ref()
const events_w_render = ref()

const errorMessage = ref('')

const uc_id = Number(route.params.id)

const new_uc = ref(new Usecase('', []))
const new_event = ref(new Event("", [], [], []))

const new_data_op = ref(new DataOperation({}, DataOperationEnum.CREATE))
const new_comp_op = ref(new ComplexOperation("", ComplexOperationEnum.OTHER))
const new_navi_op = ref(new NavOperation("", "", NavOperationEnum.INCLUDE))
const new_inou_op = ref(new IOOperation("", IOOutputEnum.INPUT))

const new_action = ref({'event_id': -1, 'step_id': -1, 'step': new Action("S000", "", "", new IOOperation("", IOOutputEnum.INPUT))})
const new_decision = ref({'event_id': -1, 'step_id': -1, 'step': new Decision("S000", "", [])})

const do_types = Object.values(DataOperationEnum)
const co_types = Object.values(ComplexOperationEnum)
const no_types = Object.values(NavOperationEnum)
const io_types = Object.values(IOOutputEnum)

const isAction = ref(true)

const isUsecaseModalOpen = ref(false)
const isEventModalOpen = ref(false)
const isStepModalOpen = ref(false)
const isActionModalOpen = ref(false)
const isDecisionModalOpen = ref(false)

function getEventsByUsecaseName(name: string) {
  if (name) {
    return usecases.value.filter((uc: Usecase) => uc.name === name)[0].usecase_events
  }
}

function getAttributesAndAssociationsByClassName(name: string) {
  if (name) {
    let this_class: any = clData.value.filter((cls: Class) => cls.name === name)[0]
    let attributes: any[] = this_class.class_attributes.map((elem: ClassAttribute) => {
      return {'name': elem.name}
    })
    let associations = this_class.class_associations.map((elem: any[]) => {
      return elem[1]
    }).filter((assoc: Association) => assoc.src.class_name === name || assoc.tgt.class_name === name).map((assoc: Association) => {
      if (assoc.src.class_name === name) {
        return {'name': assoc.tgt.class_name}
      } else {
        return {'name': assoc.src.class_name}
      }
    })
    return attributes.concat(associations)
  }
}

const updateUsecase = async () => {
  await putUseCase(uc_id, new_uc.value)
  reload.value = 1 - reload.value

  isUsecaseModalOpen.value = false
}

const openUsecaseModal = () => {
  new_uc.value.name = ucData.value.name
  new_uc.value.usecase_events = ucData.value.usecase_events
  isUsecaseModalOpen.value = true
}

const updateEvent = async (ev_id: number) => {
  const usecase = new Usecase(ucData.value.name, ucData.value.usecase_events)
  usecase.usecase_events[ev_id] = new_event.value

  await putUseCase(uc_id, usecase)
  isEventModalOpen.value = false
  reload.value = 1 - reload.value
}

const addEvent = async () => {
  const usecase = new Usecase(ucData.value.name, ucData.value.usecase_events)
  usecase.usecase_events.push(new Event("New Event", [], [], []))

  await putUseCase(uc_id, usecase)
  reload.value = 1 - reload.value
}

const removeEvent = async (ev_id: number) => {
  const usecase = new Usecase(ucData.value.name, ucData.value.usecase_events)

  if (usecase.usecase_events[ev_id]){
    const index = usecase.usecase_events.indexOf(usecase.usecase_events[ev_id], 0);
    if (index > -1) {
      usecase.usecase_events.splice(index, 1);
    }
  }

  await putUseCase(uc_id, usecase)
  reload.value = 1 - reload.value
}

const openEventModal = (ev_id: number) => {
  new_event.value = structuredClone(toRaw(ucData.value.usecase_events[Number(ev_id)]))
  isEventModalOpen.value = true
}

//////////
// Step //
//////////

function checkIsAction(step: unknown): step is Action {
  return typeof step === 'object' && step !== null && 'next_step' in step;
}

function checkIsDO(cat_op: unknown): cat_op is DataOperation {
  return typeof cat_op === 'object' && cat_op !== null && 'attributes' in cat_op
}

function checkIsDecision(step: unknown): step is Decision {
  return typeof step === 'object' && step !== null && 'next_steps' in step;
}

const updateStep = async (ev_id: number, st_id: number) => {
  const usecase = new Usecase(ucData.value.name, ucData.value.usecase_events)

  let step = usecase.usecase_events[ev_id]?.event_steps[st_id]
  if (usecase.usecase_events[ev_id] && step) {
    if (checkIsAction(step)) {
      step = new_action.value.step

      if (checkIsDO(step.category)) {
        let attrs: {[key: string]: any} = {}
        
        for (const attribute of step.category.attributes) {
          if (typeof attribute.group === 'string') {

            if (attrs[attribute.group]) {
              attrs[attribute.group].push(attribute.value)
            } else {
              attrs[attribute.group] = [attribute.value]
            }
          }
        }
        step.category.attributes = attrs
      }

    } else if (checkIsDecision(step)) {
      step = new_decision.value.step
    }
    usecase.usecase_events[ev_id].event_steps[st_id] = step
    await putUseCase(uc_id, usecase)
  }
  isActionModalOpen.value = false
  isDecisionModalOpen.value = false
  reload.value = 1 - reload.value
}

const addStep = async (ev_id: number, action: boolean) => {
  const usecase = new Usecase(ucData.value.name, ucData.value.usecase_events)

  if (action) {
    usecase.usecase_events[ev_id]?.event_steps.push(new_action.value.step)
  } else {
    usecase.usecase_events[ev_id]?.event_steps.push(new_decision.value.step)
  }
  await putUseCase(uc_id, usecase)

  isStepModalOpen.value = false
  reload.value = 1 - reload.value
}

const removeStep = async (ev_id: number, st_id: number) => {
  const usecase = new Usecase(ucData.value.name, ucData.value.usecase_events)

  let step = usecase.usecase_events[ev_id]?.event_steps[st_id]
  if (step) {
    if (usecase.usecase_events[ev_id]){
      const index = usecase.usecase_events[ev_id].event_steps.indexOf(step, 0);
      if (index > -1) {
        usecase.usecase_events[ev_id].event_steps.splice(index, 1);
      }
    }
  }
  await putUseCase(uc_id, usecase)
  reload.value = 1 - reload.value
}

const openStepModal = async (ev_id: number, st_id: number) => {
  const usecase = new Usecase(ucData.value.name, ucData.value.usecase_events)
  if (st_id >= 0) {
    const step = usecase.usecase_events[ev_id]?.event_steps[st_id]

    if (checkIsAction(step)) {

      new_action.value.event_id = ev_id
      new_action.value.step_id = st_id
      new_action.value.step = structuredClone(toRaw(step))

      isActionModalOpen.value = true
    } else if (checkIsDecision(step)) {
      new_decision.value.event_id = ev_id
      new_decision.value.step_id = st_id
      new_decision.value.step = structuredClone(toRaw(step))

      isDecisionModalOpen.value = true
    }
  } else {
    new_action.value.event_id = -1
    new_action.value.step_id = -1

    new_data_op.value = new DataOperation({}, DataOperationEnum.CREATE)
    new_comp_op.value = new ComplexOperation("", ComplexOperationEnum.OTHER)
    new_navi_op.value = new NavOperation("", "", NavOperationEnum.INCLUDE)
    new_inou_op.value = new IOOperation("", IOOutputEnum.INPUT)

    new_action.value.step = new Action("S000", "", "", new IOOperation("", IOOutputEnum.INPUT))
    
    new_decision.value.event_id = -1
    new_decision.value.step_id = -1
    new_decision.value.step = new Decision("S000", "", [])

    isStepModalOpen.value = true
  }
}

// async function goToClass(className: string) {
//   const data = await getClassByName(className)
//   router.push(`/classes/${data.data[0].index}`)
// }

watch(reload, async () => {
  try {
    ucData.value = (await getUseCase(Number(uc_id))).data
    acData.value = (await getActors()).data
    clData.value = await Promise.all((await getClasses()).data.map(async (elem: Class) => {
      return {...elem, 'class_associations': (await getClassAssociations(elem.name)).data}
    }))

    console.log(clData.value)
    usecases.value = (await getUseCases()).data

    events_w_render.value = await Promise.all(
      ucData.value.usecase_events.map(async (event: any) => ({
        ...event,
        svg: await mermaidSvgCreator(event.event_steps)
      }))
    )
  }
  catch (error) {
    errorMessage.value = 'Failed to fetch'
  }
}, { immediate: true })
</script>

<style scoped>
@import '@/css/style.css';
</style>