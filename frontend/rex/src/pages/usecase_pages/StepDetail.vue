<template>
  <div v-if="stepData">
    <h1>Step</h1>

    <p>{{ stepData.description }}</p>

    <ul v-if="stepData.read_attributes">
      <li v-for="attr in stepData.read_attributes" :key="attr.id">
        attr.name (<router-link :to="`/classes/${attr.klass.id}`">{{attr.klass.name}}</router-link>)
      </li>
    </ul>

    <ul v-else-if="stepData.related_classes">
      <li v-for="cls in stepData.related_classes" :key="cls.id">
        <router-link :to="`/classes/${cls.id}`">{{cls.name}}</router-link>
      </li>
    </ul>

    <br><br>

    <router-link v-if="stepData.next_step" :to="`/steps/${stepData.next_step}`">Next Step</router-link>

    <ul v-else-if="stepData.next_steps">
      <li v-for="step in stepData.next_steps" :key="step">
        <router-link :to="`/steps/${step}`">Next Step ({{ step }})</router-link>
      </li>
    </ul>
    
  </div>
  <p v-else>Loading...</p>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import { getStep } from '@/services/api/steps'

const route = useRoute()
const stepData = ref(null)

onMounted(async () => {
  const id = route.params.id
  stepData.value = await getStep(id)
})
</script>

<style scoped>
@import '@/css/style.css';
</style>