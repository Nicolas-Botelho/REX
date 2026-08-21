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
          {{ step.step_code }}: {{ step.description }} <template v-if="step.category">({{ step.category }})</template><template v-else>(decision)</template> <template v-if="step.class_name">-> <a href="#" @click.prevent="goToClass(step.class_name)">{{ step.class_name }}</a></template>
        </p>
      </BaseItemBox>
      <button class="create-button" @click="openStepModal(Number(event_index), -1)">Add New</button>

      <BaseModal title="Action" :is-open="isActionModalOpen" @close="isActionModalOpen=false" @confirm="updateStep(Number(event_index), new_action.step_id)">
        <form class="modal-form" @submit.prevent>
          <div class="form-group">
            <label>Step Code</label>
            <input v-model="new_action.step.step_code">
          </div>
          <div class="form-group">
            <label>Step Description</label>
            <input v-model="new_action.step.description">
          </div>
          <div class="form-group">
            <label>Step Category</label>
            <select v-model="new_action.step.category" size="4">
              <option v-for="(item, index) in categories" :key="index" :value="item">{{ item }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Class related to the Step</label>
            <select v-model="new_action.step.class_name" size="4">
              <option v-for="(item, index) in clData" :key="index" :value="item.name">{{ item.name }}</option>
            </select>
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
            <label>Class related to the Step</label>
            <select v-model="new_decision.step.class_name" size="4">
              <option v-for="(item, index) in clData" :key="index" :value="item.name">{{ item.name }}</option>
            </select>
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
              <label>Step Code</label>
              <input v-model="new_action.step.step_code">
            </div>
            <div class="form-group">
              <label>Step Description</label>
              <input v-model="new_action.step.description">
            </div>
            <div class="form-group">
              <label>Step Category</label>
              <select v-model="new_action.step.category" size="4">
                <option v-for="(item, index) in categories" :key="index" :value="item">{{ item }}</option>
              </select>
            </div>
            <div class="form-group">
              <label>Class related to the Step</label>
              <select v-model="new_action.step.class_name" size="4">
                <option v-for="(item, index) in clData" :key="index" :value="item.name">{{ item.name }}</option>
              </select>
            </div>
            <div class="form-group">
              <label>Next Step</label>
              <select v-model="new_action.step.next_step" size="4">
                <option v-for="(item, index) in event.event_steps" :key="index" :value="item.step_code">{{ item.step_code }}</option>
              </select>
            </div>
          </div>
          <div v-else>
            <div class="form-group">
              <label>Step Code</label>
              <input v-model="new_decision.step.step_code">
            </div>
            <div class="form-group">
              <label>Step Description</label>
              <input v-model="new_decision.step.description">
            </div>
            <div class="form-group">
              <label>Class related to the Step</label>
              <select v-model="new_decision.step.class_name" size="4">
                <option v-for="(item, index) in clData" :key="index" :value="item.name">{{ item.name }}</option>
              </select>
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
import { ref, toRaw, watch } from 'vue'
import { getUseCase, putUseCase } from '@/services/api/usecases'
import { getClassByName, getClasses } from '@/services/api/classes'
import { mermaidSvgCreator } from '@/utils/mermaid_utils'
import BaseItemBox from '@/components/BaseItemBox.vue'
import BaseModal from '@/components/BaseModal.vue'
import { Action, CategoryEnum, Decision, Event, Usecase } from '@/models/usecase_models'
import { getActors } from '@/services/api/actors'

const route = useRoute()
const reload = ref(0)
const router = useRouter()
const ucData = ref()
const acData = ref()
const clData = ref()
const events_w_render = ref()

const errorMessage = ref('')

const uc_id = Number(route.params.id)

const new_uc = ref(new Usecase('', []))
const new_event = ref(new Event("", [], [], []))
const new_action = ref({'event_id': -1, 'step_id': -1, 'step': new Action("S000", "", "", "", CategoryEnum.INPUT)})
const new_decision = ref({'event_id': -1, 'step_id': -1, 'step': new Decision("S000", "", "", [])})

const categories = Object.values(CategoryEnum)

const isAction = ref(true)

const isUsecaseModalOpen = ref(false)
const isEventModalOpen = ref(false)
const isStepModalOpen = ref(false)
const isActionModalOpen = ref(false)
const isDecisionModalOpen = ref(false)

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

function checkIsDecision(step: unknown): step is Decision {
  return typeof step === 'object' && step !== null && 'next_steps' in step;
}

const updateStep = async (ev_id: number, st_id: number) => {
  const usecase = new Usecase(ucData.value.name, ucData.value.usecase_events)

  let step = usecase.usecase_events[ev_id]?.event_steps[st_id]
  if (usecase.usecase_events[ev_id] && step) {
    if (checkIsAction(step)) {
      step = new_action.value.step
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
    new_action.value.step = new Action("S000", "", "", "", CategoryEnum.INPUT)
    
    new_decision.value.event_id = -1
    new_decision.value.step_id = -1
    new_decision.value.step = new Decision("S000", "", "", [])

    isStepModalOpen.value = true
  }
}

async function goToClass(className: string) {
  const data = await getClassByName(className)
  router.push(`/classes/${data.data[0].index}`)
}

watch(reload, async () => {
  try {
    ucData.value = (await getUseCase(Number(uc_id))).data
    acData.value = (await getActors()).data
    clData.value = (await getClasses()).data

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