<template>
  <div>
    <h1>Classes</h1>

    <div v-if="clsData">

      <div>
        <GoToItemBox v-for="(item, index) in clsData" :key="index" @del="removeClass(Number(index))" @go-to="goToClass(Number(index))">
          <p>{{ item.name }}</p>
        </GoToItemBox>

        <button class="create-button" @click="addClass">Add New</button>
      </div>

      <h2>Classes Questions</h2>

      <div>
        <BaseItemBox v-for="(item, index) in qData" :key="index" @del="removeQuestion(Number(index))" @edit="openQuestionModal(Number(index))">
          <p>{{ item.question }}</p>
          <ul>
            <li v-for="(rel_cls, cls_idx) in item.class_names" :key="cls_idx">{{ rel_cls }}</li>
          </ul>
        </BaseItemBox>

        <BaseModal title="Class Question" :is-open="isQuestionModalOpen" @close="isQuestionModalOpen=false" @confirm="addOrUpdateQuestion()">
          <form class="modal-form" @submit.prevent>
            <div class="form-group">
              <label>Question</label>
              <input v-model="question.question">
            </div>
            <div>
              <label>Classes related to the question</label>
              <select v-model="question.class_names" multiple size="4">
                <option v-for="(item, index) in clsData" :key="index" :value="item.name">{{ item.name }}</option>
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
import { deleteClass, deleteClassQuestion, getClasses, getClassQuestions, postClass, postClassQuestion, putClassQuestion } from '@/services/api/classes'
import router from '@/router'
import BaseItemBox from '@/components/BaseItemBox.vue'
import { Class } from '@/models/class_models'
import { ClassQuestion } from '@/models/question_models'
import BaseModal from '@/components/BaseModal.vue'
import GoToItemBox from '@/components/GoToItemBox.vue'

const clsData = ref()
const qData = ref()

const errorMessage = ref('')
const reload = ref(0)

const isQuestionModalOpen = ref(false)

const question = ref(new ClassQuestion(-1, "", []))

const addClass = async () => {
  await postClass(new Class("New Class", "", []))
  reload.value = 1 - reload.value
}

const removeClass = async (cls_id: number) => {
  await deleteClass(cls_id)
  reload.value = 1 - reload.value
}

const goToClass = (cls_id: number) => {
  router.push(`classes/${cls_id}`)
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
  await postClassQuestion(question.value)
}

const updateQuestion = async () => {
  await putClassQuestion(question.value.id, question.value)
}

const removeQuestion = async (clq_id: number) => {
  await deleteClassQuestion(clq_id)
  reload.value = 1 - reload.value
}

const openQuestionModal = (clq_id: number) => {
  if (clq_id >= 0) {
    question.value.id = clq_id
    question.value.question = qData.value[clq_id].question
    question.value.class_names = qData.value[clq_id].class_names
  } else {
    question.value.id = -1
    question.value.question = ""
    question.value.class_names = []
  }
  isQuestionModalOpen.value = true
}

watch(reload, async () => {
  try {
    clsData.value = (await getClasses()).data
    qData.value = (await getClassQuestions()).data
  } catch (error) {
    errorMessage.value = 'Failed to fetch'
  }
}, {'immediate': true})
</script>

<style scoped>
@import '@/css/style.css';
</style>