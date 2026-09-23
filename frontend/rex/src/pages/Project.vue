<template>
  <div>
    <h1>🦖 REX - Requirement EXtractor</h1>
    <p>A requirement management tool with a requirement from text extraction.</p>
  </div>

  <div v-if="projData">
    <h2>{{ projData.name }}</h2>
    <p>{{ projData.description }}</p>
    <button class="edit-button" @click="openProjectModal()">Edit</button>

    <BaseModal title="Project" :is-open="isProjectModalOpen" @close="isProjectModalOpen=false" @confirm="updateProject()">
      <form class="modal-form" @submit.prevent>
        <div class="form-group">
          <label>Project Name</label>
          <input v-model="project.name">
        </div>
        <div class="form-group">
          <label>Project Description</label>
          <textarea v-model="project.description"></textarea>
        </div>
      </form>
    </BaseModal>
  </div>

  <p v-else-if="errorMessage">{{ errorMessage }}</p>
  <p v-else>Loading...</p>
</template>

<script setup lang="ts">
import BaseModal from '@/components/BaseModal.vue';
import { Project } from '@/models/project_models';
import { getProject, putProject } from '@/services/api/project';
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';

const reload = ref(0)
const errorMessage = ref('')
const projData = ref()
const route = useRoute()

const isProjectModalOpen = ref(false)

const pId = Number(route.params.p_id)
const project = ref(new Project("", ""))

const updateProject = async () => {
  await putProject(pId, project.value)
  reload.value = 1 - reload.value
  isProjectModalOpen.value = false
}

const openProjectModal = () => {
  project.value.name = projData.value.name
  project.value.description = projData.value.description
  isProjectModalOpen.value = true
}

watch(reload, async () => {
  projData.value = (await getProject(pId)).data
}, {'immediate': true})

</script>

<style scoped>
@import '@/css/style.css';
</style>