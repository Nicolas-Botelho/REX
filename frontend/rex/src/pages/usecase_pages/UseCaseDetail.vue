<template>
  <div v-if="ucData">
    <h1>{{ ucData.name }}</h1>

    <h2 v-if="events_w_render.length">Events</h2>
    <div v-for="event in events_w_render">
      <h3>{{ event.name }}</h3>
      <p> {{ event.actor.name }}: {{ event.actor.description }}</p>

      <div v-html="event.svg"></div>

      <p v-for="step in event.event_steps">{{ step.step_code }}: {{ step.description }} ({{ step.category }}) -> <a href="#" @click.prevent="goToClass(step.class_name)">{{ step.class_name }}</a>
      
      </p>

    </div>
    
  </div>
  <p v-else-if="errorMessage">{{ errorMessage }}</p>
  <p v-else>Loading...</p>
</template>

<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import { getUseCase } from '@/services/api/usecases'
import { getClassByName } from '@/services/api/classes'
import { mermaidSvgCreator } from '@/utils/mermaid_utils'

const route = useRoute()
const router = useRouter()
const ucData = ref()
const events_w_render = ref()

const errorMessage = ref('')

async function goToClass(className: string) {
  const data = await getClassByName(className)
  router.push(`/classes/${data.data[0].index}`)
}

onMounted(async () => {
  try {
    const id = route.params.id
    ucData.value = await getUseCase(Number(id))
    ucData.value = ucData.value.data

    events_w_render.value = await Promise.all(
      ucData.value.usecase_events.map(async (event: any) => ({
        ...event,
        svg: await mermaidSvgCreator(event.event_steps)
      }))
    )
  }
  catch (error) {
    errorMessage.value = 'Failed to fetch'
  }
})
</script>

<style scoped>
@import '@/css/style.css';
</style>