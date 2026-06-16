<template>
  <div>
    <h1>Export Data</h1>
    <br/><br/>
    <p>Json File</p>
    <button @click="downloadJson">Download Json</button>

    <p v-if="successMessage">{{ successMessage }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { generateJson } from '@/services/api/utils';

const successMessage = ref('')

const downloadJson = async () => {
  try {
    const data = await generateJson()

    const url = URL.createObjectURL(new Blob([JSON.stringify(data, null, 4)], {type: 'application/json'}))

    const link = document.createElement('a');
    link.href = url;
    link.download = 'output.json';

    document.body.appendChild(link);
    link.click();

    document.body.removeChild(link);
    URL.revokeObjectURL(url);

    successMessage.value = 'Json file generated sucessfully'
  }
  catch (error) {
    console.error(error)
  }
}

const downloadFile = async (url, filename) => {
  try {
    const response = await fetch(url);
    const blob = await response.blob();
    const objectURL = URL.createObjectURL(blob);
    
    const link = document.createElement('a');
    link.href = objectURL;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    
    // Cleanup
    document.body.removeChild(link);
    URL.revokeObjectURL(objectURL);
  } catch (error) {
    console.error('Download failed:', error);
  }
}

</script>

<style scoped>
@import '@/css/style.css';
</style>