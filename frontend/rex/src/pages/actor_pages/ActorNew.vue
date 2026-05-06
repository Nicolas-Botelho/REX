<template>
  <div>
    <h1>New Actor</h1>
    
    <p>Define a New Actor</p>

    <input placeholder="Class Name" v-model="actor_name">
    <br/><br/>

    <textarea placeholder="Actor Description" v-model="actor_description"></textarea>
    <br/><br/>

    <button type="button" @click="addActor">Add Actor</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { createActor } from '@/services/api/actors'

const actor_name = ref('')
const actor_description = ref('')

const addActor = async () => {
  await createActor(actor_name.value, actor_description.value)
}
</script>

<style scoped>
@import '@/css/style.css';
</style>