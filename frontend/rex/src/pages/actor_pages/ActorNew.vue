<template>
  <div>
    <h1>New Actor</h1>
    
    <p>Define a New Actor</p>
    <textarea v-model="def_actor" placeholder="Actor{
Actor description
}"></textarea>

    <button type="button" @click="addActor">Add Actor</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { createActor } from '@/services/api/actors'

const def_actor = ref('')

const transform = (actor_string) => {
  const name = String(actor_string.slice(0,actor_string.indexOf('{')).trim())
  const description = actor_string.slice(actor_string.indexOf('{')+1,actor_string.indexOf('}'))

  return {'name': name, 'description': description}
}

const addActor = async () => {
  const actor_obj = transform(def_actor.value)
  await createActor(actor_obj.name, actor_obj.description)
}
</script>

<style scoped>
h1 {
  font-size: 24px;
}
</style>