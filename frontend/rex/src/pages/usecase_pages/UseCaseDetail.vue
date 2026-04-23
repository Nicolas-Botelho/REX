<template>
  <div v-if="ucData">
    <h1>{{ ucData.name }}</h1>

    <h2 v-if="ucData.usecase_events.length">Events</h2>
    <div v-for="event in ucData.usecase_events">
      <h3>{{ event.name }}</h3>
      <router-link :to="`/actors/${event.actor.id}`">{{ event.actor.name }}</router-link>
      <ul v-if="event.event_steps">
        <li v-for="step in event.event_steps">
          <p v-if="step.system">System: {{ step.description }}</p>
          <p v-else>{{ event.actor.name }}: {{ step.description }}</p>
        </li>
      </ul>
    </div>
    
  </div>
  <p v-else>Loading...</p>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import { getUseCase } from '@/services/api/usecases'

const route = useRoute()
const ucData = ref(null)

onMounted(async () => {
  const id = route.params.id
  ucData.value = await getUseCase(id)
})
</script>

<style scoped>
@import '@/css/style.css';
</style>