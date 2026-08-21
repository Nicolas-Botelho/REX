<template>
  <h1>Requirements</h1>

  <div v-if="frData || nfrData || brData">

    <div>
      <h2>Functional Requirements</h2>
      <BaseItemBox v-for="(item, index) in frData" :key="index" @edit="openFRModal(Number(index))" @del="removeFR(Number(index))">
        <h3>{{ item.code }}</h3>
        <p>Objective: {{ item.objective }}</p>
        <p>Description: {{ item.description }}</p>
        <p>Performed by: {{ item.actor_name }}</p>
        <p>Priority: {{ item.priority }} do</p>
        <h4 v-if="(item.depends_on_requirements_codes && item.depends_on_requirements_codes != 0) || (item.apply_business_rules_codes && item.apply_business_rules_codes.length != 0)">Depends on</h4>
        <ul>
          <li v-for="(code, index) in item.depends_on_requirements_codes" :key="index">
            {{ code }}
          </li>
          <li v-for="(code, index) in item.apply_business_rules_codes" :key="index">
            {{ code }}
          </li>
        </ul>
      </BaseItemBox>

      <button class="create-button" @click="openFRModal(-1)">Add New</button>

      <BaseModal title="Functional Requirement (FR)" :is-open="isFRModalOpen" @close="isFRModalOpen=false" @confirm="addOrUpdateFR()">
        <form class="modal-form" @submit.prevent>
          <div class="form-group">
            <label>FR Code</label>
            <input v-model="fr.req.code">
          </div>
          <div class="form-group">
            <label>FR Objective</label>
            <input v-model="fr.req.objective">
          </div>
          <div class="form-group">
            <label>FR Description</label>
            <input v-model="fr.req.description">
          </div>
          <div class="form-group">
            <label>Performer</label>
            <select v-model="fr.req.actor_name" size="4">
              <option v-for="(item, index) in acData" :key="index" :value="item.name">{{ item.name }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Priority</label>
            <select v-model="fr.req.priority" size="4">
              <option v-for="(item, index) in priorities" :key="index" :value="item">{{ item }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Dependencies</label>
            <select v-model="fr.req.depends_on_requirements_codes" multiple :size="4">
              <option v-for="(item, index) in frData" :key="index" :value="item.code">{{ item.code }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Applied Business Rules</label>
            <select v-model="fr.req.apply_business_rules_codes" multiple :size="4">
              <option v-for="(item, index) in brData" :key="index" :value="item.code">{{ item.code }}</option>
            </select>
          </div>
        </form>
      </BaseModal>
    </div>

    <div>
      <h2>Non Functional Requirements</h2>
      <BaseItemBox v-for="(item, index) in nfrData" :key="index" @edit="openNFRModal(Number(index))" @del="removeNFR(Number(index))">
        <h3>{{ item.code }}</h3>
        <p>Description: {{ item.description }}</p>
        <p>Category: {{ item.category }}</p>
        <p>Priority: {{ item.priority }} do</p>
        <h4>Applied on</h4>
        <p v-if="item.applies_on_requirements_codes && item.applies_on_requirements_codes.length == 0">Whole system</p>
        <ul v-if="item.applies_on_requirements_codes && item.applies_on_requirements_codes.length != 0">
          <li v-for="(code, index) in item.applies_on_requirements_codes" :key="index">
            {{ code }}
          </li>
        </ul>
      </BaseItemBox>

      <BaseModal title="Non Functional Requirement (NFR)" :is-open="isNFRModalOpen" @close="isNFRModalOpen=false" @confirm="addOrUpdateNFR()">
        <form class="modal-form" @submit.prevent>
          <div class="form-group">
            <label>NFR Code</label>
            <input v-model="nfr.req.code">
          </div>
          <div class="form-group">
            <label>NFR Description</label>
            <input v-model="nfr.req.description">
          </div>
          <div class="form-group">
            <label>NFR Category</label>
            <select v-model="nfr.req.category" size="4">
              <option v-for="(item, index) in categories" :key="index" :value="item">{{ item }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Priority</label>
            <select v-model="nfr.req.priority" size="4">
              <option v-for="(item, index) in priorities" :key="index" :value="item">{{ item }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Applied on which Functional Requirements (empty to apply to the whole system)</label>
            <select v-model="nfr.req.applies_on_requirements_codes" multiple size="4">
              <option v-for="(item, index) in frData" :key="index" :value="item.code">{{ item.code }}</option>
            </select>
          </div>
        </form>
      </BaseModal>

      <button class="create-button" @click="openNFRModal(-1)">Add New</button>
    </div>

    <div>
      <h2>Business Rules</h2>
      <BaseItemBox v-for="(item, index) in brData" :key="index" @edit="openBRModal(Number(index))" @del="removeBR(Number(index))">
        <h3>{{ item.code }}</h3>
        <p>{{ item.description }}</p>
      </BaseItemBox>

      <button class="create-button" @click="openBRModal(-1)">Add New</button>

      <BaseModal title="Business Rule (BR)" :is-open="isBRModalOpen" @close="isBRModalOpen=false" @confirm="addOrUpdateBR()">
        <form class="modal-form" @submit.prevent>
          <div class="form-group">
            <label>BR Code</label>
            <input v-model="br.req.code">
          </div>
          <div class="form-group">
            <label>BR Description</label>
            <input v-model="br.req.description">
          </div>
        </form>
      </BaseModal>
    </div>

    <div>
      <h2>Requirement Questions</h2>
      <BaseItemBox v-for="(item, index) in qData" :key="index" @edit="openQuestionModal(Number(index))" @del="removeQuestion(Number(index))">
        <p>{{ item.question }}</p>
        <ul>
          <li v-for="(rel_req, rq_idx) in item.requirement_codes" :key="rq_idx">{{ rel_req }}</li>
        </ul>
      </BaseItemBox>

      <button class="create-button" @click="openQuestionModal(-1)">Add New</button>

      <BaseModal title="Requirement Question" :is-open="isQuestionModalOpen" @close="isQuestionModalOpen=false" @confirm="addOrUpdateQuestion()">
        <form class="modal-form" @submit.prevent>
          <div class="form-group">
            <label>Question</label>
            <input v-model="question.question">
          </div>
          <div class="form-group">
            <label>Requirements related to the question</label>
            <select v-model="question.requirement_codes" multiple size="4">
              <option v-for="(item, index) in frData" :key="index" :value="item.code">{{ item.code }}</option>
              <option v-for="(item, index) in nfrData" :key="index" :value="item.code">{{ item.code }}</option>
              <option v-for="(item, index) in brData" :key="index" :value="item.code">{{ item.code }}</option>
            </select>
          </div>
        </form>
      </BaseModal>
    </div>

  </div>
  <p v-else-if="errorMessage">{{ errorMessage }}</p>
  <p v-else>Loading...</p>
</template>

<script setup lang="ts">
import { ref, watch, toRaw } from 'vue'
import { getFRs, getNFRs, getBRs, getRequirementQuestions, postFR, putFR, deleteFR, putNFR, postNFR, deleteNFR, putBR, postBR, deleteBR, postRequirementQuestion, putRequirementQuestion, deleteRequirementQuestion } from '@/services/api/requirement'
import BaseItemBox from '@/components/BaseItemBox.vue'
import BaseModal from '@/components/BaseModal.vue'
import { BusinessRule, CategoryEnum, FunctionalRequirement, NonFunctionalRequirement, PriorityEnum } from '@/models/requirement_models'
import { RequirementQuestion } from '@/models/question_models'
import { getActors } from '@/services/api/actors'

const reload = ref(0)

const frData = ref()
const nfrData = ref()
const brData = ref()
const acData = ref()
const qData = ref()

const isFRModalOpen = ref(false)
const isNFRModalOpen = ref(false)
const isBRModalOpen = ref(false)
const isQuestionModalOpen = ref(false)

const fr = ref({'fr_id': -1, 'req': new FunctionalRequirement("FR000", "", "", "", PriorityEnum.WONT, [], [])})
const nfr = ref({'nfr_id': -1, 'req': new NonFunctionalRequirement("", "", CategoryEnum.COMPATIBILITY, PriorityEnum.WONT, [])})
const br = ref({'br_id': -1, 'req': new BusinessRule("", "")})
const question = ref(new RequirementQuestion(-1, "", []))

const priorities = Object.values(PriorityEnum)
const categories = Object.values(CategoryEnum)

const errorMessage = ref('')

const addOrUpdateFR = async () => {
  if (fr.value.fr_id >= 0) {
    await updateFR()
  } else {
    await addFR()
  }
  isFRModalOpen.value = false
  reload.value = 1 - reload.value
}

const addFR = async () => {
  await postFR(fr.value.req)
}

const updateFR = async () => {
  await putFR(fr.value.fr_id, fr.value.req)
}

const removeFR = async (fr_id: number) => {
  await deleteFR(fr_id)
  reload.value = 1 - reload.value
}

const openFRModal = (fr_id: number) => {
  if (fr_id >= 0) {
    fr.value.fr_id = fr_id
    fr.value.req = structuredClone(toRaw(frData.value[fr_id]))
  } else {
    fr.value.fr_id = -1
    fr.value.req = new FunctionalRequirement("FR000", "", "", "", PriorityEnum.WONT, [], [])
  }
  isFRModalOpen.value = true
}

const addOrUpdateNFR = async () => {
  if (nfr.value.nfr_id >= 0) {
    await updateNFR()
  } else {
    await addNFR()
  }
  isNFRModalOpen.value = false
  reload.value = 1 - reload.value
}

const updateNFR = async () => {
  await putNFR(nfr.value.nfr_id, nfr.value.req)
}

const addNFR = async () => {
  await postNFR(nfr.value.req)
}

const removeNFR = async (nfr_id: number) => {
  await deleteNFR(nfr_id)
  reload.value = 1 - reload.value
}

const openNFRModal = (nfr_id: number) => {
  if (nfr_id >= 0) {
    nfr.value.nfr_id = nfr_id
    nfr.value.req = structuredClone(toRaw(nfrData.value[nfr_id]))
  } else {
    nfr.value.nfr_id = -1
    nfr.value.req = new NonFunctionalRequirement("NFR000", "", CategoryEnum.COMPATIBILITY, PriorityEnum.WONT, [])
  }
  isNFRModalOpen.value = true
}

const addOrUpdateBR = async () => {
  if (br.value.br_id >= 0) {
    await updateBR()
  } else {
    await addBR()
  }
  isBRModalOpen.value = false
  reload.value = 1 - reload.value
}

const updateBR = async () => {
  await putBR(br.value.br_id, br.value.req)
}

const addBR = async () => {
  await postBR(br.value.req)
}

const removeBR = async (br_id: number) => {
  await deleteBR(br_id)
  reload.value = 1 - reload.value
}

const openBRModal = (br_id: number) => {
  if (br_id >= 0) {
    br.value.br_id = br_id
    br.value.req = structuredClone(toRaw(brData.value[br_id]))
  } else {
    br.value.br_id = -1
    br.value.req = new BusinessRule("BR000", "")
  }
  isBRModalOpen.value = true
}

const addOrUpdateQuestion = async () => {
  if (question.value.id >= 0) {
    await updateQuestion()
  } else {
    await addQuestion()
  }
  isQuestionModalOpen.value = false
  reload.value = 1 - reload.value
}

const addQuestion = async () => {
  await postRequirementQuestion(question.value)
}

const updateQuestion = async () => {
  await putRequirementQuestion(question.value.id, question.value)
}

const removeQuestion = async (q_id: number) => {
  await deleteRequirementQuestion(q_id)
  reload.value = 1 - reload.value
}

const openQuestionModal = (q_id: number) => {
  if (q_id >= 0) {
    question.value.question = qData.value[q_id].question
    question.value.requirement_codes = qData.value[q_id].requirement_codes
    question.value.id = q_id
  }
  else {
    question.value.question = ''
    question.value.requirement_codes = []
    question.value.id = -1
  }
  isQuestionModalOpen.value = true
}

watch(reload, async () => {
  try {
    frData.value = (await getFRs()).data
    nfrData.value = (await getNFRs()).data
    brData.value = (await getBRs()).data
    acData.value = (await getActors()).data
    qData.value = (await getRequirementQuestions()).data
  } catch (error) {
    errorMessage.value = 'Failed to fetch'
  }
}, { immediate: true })
</script>

<style scoped>
@import '@/css/style.css';
</style>