<template>
  <div>
    <h1>Generate Artifacts</h1>

    <h2>System Description</h2>
    <textarea type="text" v-model="system_description"></textarea>
    <br/><br/>
    <button type="button" @click="handleClick">
      {{ loading ? 'Loading...' : 'Submit Description' }}
    </button>


    <p v-if="successMessage">{{ successMessage }}</p>
    <p v-if="errorMessage">{{ errorMessage }}</p>
    
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { generateAll } from '@/services/api/utils'
import { useRoute } from 'vue-router'

const system_description = ref('')
const successMessage = ref('')
const errorMessage = ref('')
const loading = ref(false)

const route = useRoute()
const pId = Number(route.params.p_id)

const handleClick = async () => {
  loading.value = true
  successMessage.value = ''

  try {
    await generateAll(pId, system_description.value)
    successMessage.value = 'Artifacts generated sucessfully'
  }
  catch (error) {
    errorMessage.value = 'Failed to generate the artifacts'
    console.error(error)
  }
  finally {
    loading.value = false
  }
}
</script>

<style scoped>
@import '@/css/style.css';
</style>