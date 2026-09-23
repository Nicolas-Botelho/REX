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

      <br/>
      <button class="edit-button" @click="updateFromCL()">{{ loading ? "Loading..." : "Update next Artifacts"}}</button>
      <p v-if="successMessage">{{ successMessage }}</p>

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
import { generateFromCL } from '@/services/api/utils'
import { useRoute } from 'vue-router'

const reload = ref(0)
const errorMessage = ref('')
const successMessage = ref()
const loading = ref(false)

const route = useRoute()
const pId = Number(route.params.p_id)

const ucData = ref()
const qData = ref()

const isQuestionModalOpen = ref(false)

const question = ref(new UsecaseQuestion(-1, "", []))

const updateFromCL = async () => {
  try {
    loading.value = true
    await generateFromCL(pId, "Given the Domain Narrative, the Requirements and the Use Cases, build the next artifacts")
    successMessage.value = "Artifacts generated sucessfully"
    loading.value = false
  } catch (error) {
  }
}

const addUsecase = async () => {
  await postUseCase(pId, new Usecase("New Usecase", []))
  reload.value = 1 - reload.value
}

const removeUsecase = async (uc_id: number) => {
  await deleteUseCase(pId, uc_id)
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
  await postUsecaseQuestion(pId, question.value)
}

const updateQuestion = async () => {
  await putUsecaseQuestion(pId, question.value.id, question.value)
}

const removeQuestion = async (ucq_id: number) => {
  await deleteUsecaseQuestion(pId, ucq_id)
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
    ucData.value = (await getUseCases(pId)).data
    qData.value = (await getUsecaseQuestions(pId)).data
  } catch (error) {
    errorMessage.value = 'Failed to fetch'
  }
}, { immediate: true })
</script>

<style scoped>
@import '@/css/style.css';
</style>