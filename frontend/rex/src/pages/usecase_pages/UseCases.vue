<template>
  <div>
    <h1>Use Cases</h1>

    <div v-if="ucData">

      <div>
        <GoToItemBox v-for="(uc, index) in ucData" :key="index" @del="removeUsecase(Number(index))" @go-to="goToUseCase(Number(index))">
          <p>{{ uc.name }}</p>
        </GoToItemBox>

        <button class="create-button" @click="addUsecase()">Add New</button>
      </div>

      <h2>Use Cases Questions</h2>

      <div>
        <BaseItemBox v-for="(item, index) in qData" :key="index" @del="removeQuestion(Number(index))" @edit="openQuestionModal(Number(index))">
          <p>{{ item.question }}</p>
          <ul>
            <li v-for="(rel_uc, uc_idx) in item.usecase_names" :key="uc_idx">{{ rel_uc }}</li>
          </ul>
        </BaseItemBox>

        <BaseModal title="Use Case Question" :is-open="isQuestionModalOpen" @close="isQuestionModalOpen=false" @confirm="addOrUpdateQuestion()">
          <form class="modal-form" @submit.prevent>
            <div class="form-group">
              <label>Question</label>
              <input v-model="question.question">
            </div>
            <div>
              <label>Use Cases related to the question</label>
              <select v-model="question.usecase_names" multiple size="4">
                <option v-for="(item, index) in ucData" :key="index" :value="item.name">{{ item.name }}</option>
              </select>
            </div>
          </form>
        </BaseModal>

        <button class="create-button" @click="openQuestionModal(-1)">Add New</button>
      </div>
    </div>

    <p v-else-if="errorMessage">{{ errorMessage }}</p>
    <p v-else>Loading...</p>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { deleteUseCase, deleteUsecaseQuestion, getUsecaseQuestions, getUseCases, postUseCase, postUsecaseQuestion, putUsecaseQuestion } from '@/services/api/usecases'
import BaseItemBox from '@/components/BaseItemBox.vue'
import { Usecase } from '@/models/usecase_models'
import router from '@/router'
import BaseModal from '@/components/BaseModal.vue'
import { UsecaseQuestion } from '@/models/question_models'
import GoToItemBox from '@/components/GoToItemBox.vue'

const reload = ref(0)
const errorMessage = ref('')

const ucData = ref()
const qData = ref()

const isQuestionModalOpen = ref(false)

const question = ref(new UsecaseQuestion(-1, "", []))

const addUsecase = async () => {
  await postUseCase(new Usecase("New Usecase", []))
  reload.value = 1 - reload.value
}

const removeUsecase = async (uc_id: number) => {
  await deleteUseCase(uc_id)
  reload.value = 1 - reload.value
}

const goToUseCase = (uc_id: number) => {
  router.push(`usecases/${uc_id}`)
}

const addOrUpdateQuestion = async () => {
  if (question.value.id >= 0) {
    await updateQuestion()
  } else {
    await addQuestion()
  }
  reload.value = 1 - reload.value
  isQuestionModalOpen.value = false
}

const addQuestion = async () => {
  await postUsecaseQuestion(question.value)
}

const updateQuestion = async () => {
  await putUsecaseQuestion(question.value.id, question.value)
}

const removeQuestion = async (ucq_id: number) => {
  await deleteUsecaseQuestion(ucq_id)
  reload.value = 1 - reload.value
}

const openQuestionModal = (ucq_id: number) => {
  if (ucq_id >= 0) {
    question.value.id = ucq_id
    question.value.question = qData.value[ucq_id].question
    question.value.usecase_names = qData.value[ucq_id].usecase_names
  } else {
    question.value.id = -1
    question.value.question = ""
    question.value.usecase_names = []
  }
  isQuestionModalOpen.value = true
}

watch(reload, async () => {
  try {
    ucData.value = (await getUseCases()).data
    qData.value = (await getUsecaseQuestions()).data
  } catch (error) {
    errorMessage.value = 'Failed to fetch'
  }
}, { immediate: true })
</script>

<style scoped>
@import '@/css/style.css';
</style>