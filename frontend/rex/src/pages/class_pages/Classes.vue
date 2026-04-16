<template>
  <div>
    <h1>Classes</h1>

    <p v-if="loading">Loading...</p>
    <p v-if="error">{{ error }}</p>

    <ul v-if="clazzes">
      <li v-for="clazz in clazzes" :key="clazz.id">
        <router-link :to="`classes/${clazz.id}`">{{ clazz.name }}</router-link>
        <button type="button" @click=""> Update Class </button>
        <button type="button" @click="removeClass(clazz.id)"> Delete Class </button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getClasses, deleteClass } from '@/services/api/classes'

const clazzes = ref([])
const loading = ref(true)
const error = ref(null)

const removeClass = async (id) => {
  await deleteClass(id)
  clazzes.value = await getClasses()
}

onMounted(async () => {
  try {
    clazzes.value = await getClasses()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
h1 {
  font-size: 24px;
}
</style>