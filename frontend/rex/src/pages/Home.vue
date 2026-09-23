<template>
  <div>
    <h1>🦖 REX - Requirement EXtractor</h1>
    <p>A requirement management tool with a requirement from text extraction.</p>
  </div>

  <div v-if="projData">
    <GoToItemBox v-for="(proj, index) in projData.projects" :key="index" @del="openRemProjectModal(Number(index))", @go-to="goToProject(Number(index))">
      <p>{{ proj.name }}</p>
    </GoToItemBox>

    <BaseModal title="Project" :is-open="addProjectModalIsOpen" @close="addProjectModalIsOpen=false" @confirm="addProject()">
      <form class="modal-form" @submit.prevent">
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

    <BaseModal title="Project" :is-open="remProjectModalIsOpen" @close="remProjectModalIsOpen=false" @confirm="removeProject(proj_id)">
      <form class="modal-form" @submit.prevent>
        <div class="form-group">
          <p>Are you sure you want to delete this project?</p>
        </div>
      </form>
    </BaseModal>

    <button class="create-button" @click="openAddProjectModal()">Add New</button>
  </div>

  <p v-else-if="errorMessage">{{ errorMessage }}</p>
  <p v-else>Loading...</p>
</template>

<script setup lang="ts">
import BaseModal from '@/components/BaseModal.vue';
import GoToItemBox from '@/components/GoToItemBox.vue';
import { Project } from '@/models/project_models';
import router from '@/router';
import { deleteProject, getProjects, postProject } from '@/services/api/project';
import { ref, watch } from 'vue';

const reload = ref(0)
const errorMessage = ref('')
const projData = ref()

const project = ref(new Project("", ""))
const proj_id = ref(-1)

const addProjectModalIsOpen = ref(false)
const remProjectModalIsOpen = ref(false)

const addProject = async () => {
  await postProject(project.value)
  reload.value = 1 - reload.value
  addProjectModalIsOpen.value = false
}

const removeProject = async (project_id: number) => {
  if (project_id >= 0) {
    await deleteProject(project_id)
  }
  reload.value = 1 - reload.value
  remProjectModalIsOpen.value = false
}

const goToProject = (project_id: number) => {
  router.push(`project/${project_id}`)
}

const openAddProjectModal = () => {
  project.value = new Project("", "")
  proj_id.value = -1
  addProjectModalIsOpen.value = true
}

const openRemProjectModal = (project_id: number) => {
  proj_id.value = project_id
  remProjectModalIsOpen.value = true
}

watch(reload, async () => {
  projData.value = (await getProjects()).data
}, {'immediate': true})

</script>

<style scoped>
@import '@/css/style.css';
</style>