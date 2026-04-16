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
    
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { generateAll } from '@/services/api/utils'

const system_description = ref('')
const successMessage = ref('')
const loading = ref(false)

const handleClick = async () => {
  loading.value = true
  successMessage.value = ''

  try {
    const result = await generateAll()
    successMessage.value = 'Artifacts generated sucessfully'
  }
  catch (error) {
    console.error(error)
  }
  finally {
    loading.value = false
  }
}
</script>

<style scoped>
h1 {
  font-size: 24px;
}
</style>