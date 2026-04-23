<template>
  <div>
    <h1>Use Cases</h1>
    
    <p v-if="loading">Loading...</p>
    <p v-if="error">{{ error }}</p>

    <ul v-if="ucs">
      <li v-for="uc in ucs" :key="uc.id">
        <router-link :to="`usecases/${uc.id}`">{{ uc.name }}</router-link>
        <button type="button" @click=""> Update Use Case </button>
        <button type="button" @click="removeUseCase(uc.id)"> Delete Use Case </button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { deleteUseCase, getUseCases } from '@/services/api/usecases'

const ucs = ref([])
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    ucs.value = await getUseCases()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
})

const removeUseCase = async (id) => {
  await deleteUseCase(id)
  ucs.value = await getUseCases()
}
</script>

<style scoped>
@import '@/css/style.css';
</style>