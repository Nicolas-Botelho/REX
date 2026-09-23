<template>
  <nav class="sidenav">
    <router-link to="/">Home</router-link>
    <template v-if="isProject">
      <router-link :to="`/project/${pId}`">Project Description</router-link>
      <router-link :to="`/project/${pId}/generate`">Generate Artifacts</router-link>
      <router-link :to="`/project/${pId}/json_data`">JSON Data</router-link>
      <router-link :to="`/project/${pId}/markdown`">Markdown</router-link>
      <router-link :to="`/project/${pId}/narrative`">Domain Narrative</router-link>
      <router-link :to="`/project/${pId}/requirements`">Requirements</router-link>
      <router-link :to="`/project/${pId}/usecases`">Use Cases</router-link>
      <router-link :to="`/project/${pId}/classes`">Classes</router-link>
    </template>
  </nav>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute()

const pId = computed(() => {
  const id = Array.isArray(route.params.p_id) ? route.params.p_id[0] : route.params.p_id
  return id ? Number(id) : NaN
})

const isProject = computed(() => !isNaN(pId.value))
</script>

<style>
.sidenav {
  width: 200px;
  height: auto;
  background: #2c3e50;
  display: flex;
  flex-direction: column;
  padding: 20px;
  font-family: Arial, Helvetica, sans-serif;
}

.sidenav a {
  color: #e8edf2;
  margin-bottom: 10px;
  text-decoration: none;
}

.sidenav a.router-link-active {
  font-weight: bold;
  color: #42b983;
}
</style>