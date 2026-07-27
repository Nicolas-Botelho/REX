<template>
  <div>
    <h1>Classes</h1>

    <p v-if="loading">Loading...</p>
    <p v-if="error">{{ error }}</p>

    <ul v-if="clazzes">
      <li v-for="(clazz, index) in clazzes" :key="index">
        <router-link :to="`classes/${index}`">{{ clazz.name }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getClasses } from '@/services/api/classes'

const clazzes = ref()
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    clazzes.value = await getClasses()
    clazzes.value = clazzes.value.data
  } catch (err: any) {
    error.value = err.message
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
@import '@/css/style.css';
</style>