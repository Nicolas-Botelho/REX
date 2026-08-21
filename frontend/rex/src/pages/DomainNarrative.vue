<template>
  <h1>Domain Narrative</h1>
  <div v-if="dnData">
    <p v-if="dnData.narrative">{{ dnData.narrative }}</p>
    <p v-else>No Domain Narrative</p>

    <div style="display: flex; justify-content: flex-start; gap: 8px;">
    <button class="edit-button" @click="openNarrativeModal()">Edit</button>
    <button class="delete-button" @click="clearNarrative()">Clear</button>
    </div>

    <BaseModal title="Domain Narrative" :is-open="isNarrativeModalOpen" @close="isNarrativeModalOpen=false" @confirm="updateNarrative(narrative)">
      <form class="modal-form" @submit.prevent>
        <div class="form-group">
          <label>Domain Narrative</label>
          <textarea v-model="narrative">{{ narrative }}</textarea>
        </div>
      </form>
    </BaseModal>

    <h2>Domain Narrative Questions</h2>
    <BaseItemBox v-for="(item, index) in qData" :key="index" @edit="openQuestionModal(Number(index))" @del="removeQuestion(Number(index))">
      <p>{{ item.question }}</p>
    </BaseItemBox>

    <button class="create-button" @click="openQuestionModal(-1)">Add New</button>

    <BaseModal title="Narrative Question" :is-open="isQuestionModalOpen" @close="isQuestionModalOpen=false" @confirm="addOrUpdateQuestion()">
      <form class="modal-form" @submit.prevent>
        <div class="form-group">
          <label>Question</label>
          <input v-model="question.question">
        </div>
      </form>
    </BaseModal>
  </div>
  <p v-else-if="errorMessage">{{ errorMessage }}</p>
  <p v-else>Loading...</p>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { deleteNarrative, deleteNarrativeQuestion, getNarrative, getNarrativeQuestions, postNarrativeQuestion, putNarrative, putNarrativeQuestion } from '@/services/api/narrative'
import BaseModal from '@/components/BaseModal.vue'
import BaseItemBox from '@/components/BaseItemBox.vue'
import { NarrativeQuestion as Question } from '@/models/question_models'

const reload = ref(0)

const dnData = ref()
const qData = ref()

const errorMessage = ref('')

const isNarrativeModalOpen = ref(false)
const isQuestionModalOpen = ref(false)

const narrative = ref('')
const question = ref(new Question(-1, ""))

const updateNarrative = async (text: string) => {
  try {
    await putNarrative(text)
    isNarrativeModalOpen.value = false
    await fetchNarrative()
  } catch (error) {
    errorMessage.value = `ERROR: Unable to update. ${error}`
    console.error(errorMessage.value)
  }
}

const clearNarrative = async () => {
  try {
    await deleteNarrative()
    await fetchNarrative()
  } catch (error) {
    errorMessage.value = `ERROR: Unable to delete. ${error}`
    console.error(errorMessage.value)
  }
}

const openNarrativeModal = () => {
  narrative.value = dnData.value.narrative
  isNarrativeModalOpen.value = true
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
  await postNarrativeQuestion(question.value.question)
}

const updateQuestion = async () => {
  await putNarrativeQuestion(question.value.id, question.value.question)
}

const removeQuestion = async (q_id: number) => {
  await deleteNarrativeQuestion(q_id)
  reload.value = 1 - reload.value
}

const openQuestionModal = (q_id: number) => {
  if (q_id >= 0) {
    question.value.question = qData.value[q_id].question
    question.value.id = q_id
  }
  else {
    question.value.question = ''
    question.value.id = -1
  }
  isQuestionModalOpen.value = true
}

const fetchNarrative = async () => {
  try {
    dnData.value = (await getNarrative()).data
  }
  catch (error) {
    throw error
  }
}

watch(reload, async () => {
  try {
    dnData.value = (await getNarrative()).data
    qData.value = (await getNarrativeQuestions()).data
  }
  catch (error) {
    errorMessage.value = 'Failed to fetch'
  }
}, {'immediate': true})
</script>

<style scoped>
@import '@/css/style.css';

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 24px;
  border-radius: 8px;
  min-width: 300px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

input {
  width: 100%;
  padding: 8px;
  margin: 12px 0;
  box-sizing: border-box;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}
</style>