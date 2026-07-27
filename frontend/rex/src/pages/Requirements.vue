<template>
  <h1>Requirements</h1>

  <div v-if="frData || nfrData || brData">

    <div v-if="frData && frData.length > 0">
      <h2>Functional Requirements</h2>

      <div v-for="(item, index) in frData" :key="index">
        <h3>{{ item.code }}</h3>
        <p>{{ item.description }}</p>
        <h4>Depends on:</h4>
        <ul>
          <li v-for="(code, index) in item.depends_on_requirements_codes" :key="index">
            {{ code }}
          </li>
        </ul>
        
      </div>
    </div>

    <div v-if="nfrData && nfrData.length > 0">
      <h2>Non Functional Requirements</h2>

      <div v-for="(item, index) in nfrData" :key="index">
        <h3>{{ item.code }}</h3>
        <p>{{ item.description }}</p>
        <h4>Depends on:</h4>
        <ul>
          <li v-for="(code, index) in item.depends_on_requirements_codes" :key="index">
            {{ code }}
          </li>
        </ul>
      </div>
    </div>

    <div v-if="brData && brData.length > 0">
      <h2>Business Rules</h2>

      <div v-for="(item, index) in brData" :key="index">
        <h3>{{ item.code }}</h3>
        <p>{{ item.description }}</p>
        <h4>Depends on:</h4>
        <ul>
          <li v-for="(code, index) in item.depends_on_requirements_codes" :key="index">
            {{ code }}
          </li>
        </ul>
      </div>
    </div>

  </div>
  <p v-else-if="errorMessage">{{ errorMessage }}</p>
  <p v-else>Loading...</p>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getFRs, getNFRs, getBRs } from '@/services/api/requirement'

const frData = ref()
const nfrData = ref()
const brData = ref()

const errorMessage = ref('')

onMounted(async () => {
  try {
    frData.value = await getFRs()
    nfrData.value = await getNFRs()
    brData.value = await getBRs()

    frData.value = frData.value.data
    nfrData.value = nfrData.value.data
    brData.value = brData.value.data

  }
  catch (error) {
    errorMessage.value = 'Failed to fetch'
  }
})

</script>

<style scoped>
@import '@/css/style.css';
</style>