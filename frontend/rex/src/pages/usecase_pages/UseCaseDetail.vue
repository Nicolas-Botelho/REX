<template>
  <div v-if="ucData">
    <h1>{{ ucData.name }}</h1>

    <h2 v-if="events_w_render.length">Events</h2>
    <div v-for="event in events_w_render">
      <h3>{{ event.name }}</h3>
      <p> Actor: <router-link :to="`/actors/${event.actor.id}`">{{ event.actor.name }}</router-link></p>

      <div v-html="event.svg"></div>

      <p v-for="step in event.event_steps">{{ step.step_code }}: {{ step.description }} ({{ step.category }}) -> {{ step.clazz.name }} <<{{ step.clazz.stereotype }}>></p>

    </div>
    
  </div>
  <p v-else>Loading...</p>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import { getUseCase } from '@/services/api/usecases'
import { mermaidSvgCreator } from '@/utils/mermaid_utils'

const route = useRoute()
const ucData = ref(null)
const events_w_render = ref([])

onMounted(async () => {
  const id = route.params.id
  ucData.value = await getUseCase(id)

  events_w_render.value = await Promise.all(
    ucData.value.usecase_events.map(async (event) => ({
      ...event,
      svg: await mermaidSvgCreator(event.event_steps)
    }))
  )
})
</script>

<style scoped>
@import '@/css/style.css';
</style>