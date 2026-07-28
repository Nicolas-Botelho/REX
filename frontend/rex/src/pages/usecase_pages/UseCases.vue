<template>
  <div>
    <h1>Use Cases</h1>
    
    <p v-if="loading">Loading...</p>
    <p v-if="error">{{ error }}</p>

    <ul v-if="ucs">
      <li v-for="(uc, index) in ucs" :key="index">
        <router-link :to="`usecases/${index}`">{{ uc.name }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getUseCases } from '@/services/api/usecases'

const ucs = ref()
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    ucs.value = await getUseCases()
    ucs.value = ucs.value.data
  } catch (err: any) {
    error.value = err.message
  } finally {
    loading.value = false
  }
})

// const removeUseCase = async (id) => {
//   await deleteUseCase(id)
//   ucs.value = await getUseCases()
// }
</script>

<style scoped>
@import '@/css/style.css';
</style>