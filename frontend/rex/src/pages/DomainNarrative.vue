<template>
  <h1>Domain Narrative</h1>
  <div v-if="dnData">
    <h2>Context</h2>
    <p>{{ dnData.system_context }}</p>

    <h2 v-if="dnData.users && dnData.users.length > 0">Users</h2>
    <ul>
      <li v-for="(item, index) in dnData.users" :key="index">
        {{ item.name }}: {{ item.description }}
      </li>
    </ul>

    <h2 v-if="dnData.system_functionalities && dnData.system_functionalities.length > 0">Functionalities</h2>
    <ul>
      <li v-for="(item, index) in dnData.system_functionalities" :key="index">
        {{ item }}
      </li>
    </ul>
    
  </div>
  <p v-else-if="errorMessage">{{ errorMessage }}</p>
  <p v-else>Loading...</p>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getNarrative } from '@/services/api/narrative'

const dnData = ref(null)
const errorMessage = ref('')

onMounted(async () => {
  try {
    dnData.value = await getNarrative()
    dnData.value = dnData.value.data
  }
  catch (error) {
    errorMessage.value = 'Failed to fetch'
  }
})

</script>

<style scoped>
@import '@/css/style.css';
</style>