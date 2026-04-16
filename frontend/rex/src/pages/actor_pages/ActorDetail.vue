<template>
  <div v-if="actorData">
    <h1>{{ actorData.name }}</h1>

    <p>{{ actorData.description }}</p>

    <ul v-if="actorData.actor_events.length">
      <li v-for="event in actorData.actor_events">
        <router-link :to="`/usecases/${event.usecase}`">{{ event.name }}</router-link>
      </li>
    </ul>

  </div>
  <p v-else>Loading...</p>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import { getActor } from '@/services/api/actors'

const route = useRoute()
const actorData = ref(null)

onMounted(async () => {
  const id = route.params.id
  actorData.value = await getActor(id)
})
</script>