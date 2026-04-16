<template>
  <div>
    <h1>Actors</h1>
    
    <p v-if="loading">Loading...</p>
    <p v-if="error">{{ error }}</p>

    <ul v-if="actors">
      <li v-for="actor in actors" :key="actor.id">
        <router-link :to="`actors/${actor.id}`">{{ actor.name }}</router-link>
        <button type="button" @click=""> Update Actor </button>
        <button type="button" @click="removeActor(actor.id)"> Delete Actor </button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getActors, deleteActor } from '@/services/api/actors'

const actors = ref([])
const loading = ref(true)
const error = ref(null)

const removeActor = async (id) => {
  await deleteActor(id)
  actors.value = await getActors()
}

onMounted(async () => {
  try {
    actors.value = await getActors()
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