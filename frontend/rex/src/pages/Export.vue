<template>
  <div>
    <div>
      <h1>Export Data</h1>
      <br/>
      <button @click="downloadJson">Download JSON File</button>

      <p v-if="successExportMessage">{{ successExportMessage }}</p>
      <p v-if="errorExportMessage">{{ errorExportMessage }}</p>

    </div>

    <div>
      <h1>Import Data</h1>
      <br/>
      <input type="file" ref="fileInput" accept=".json" @change="handleFileChange" style="display: none;"/>
      
      <button @click="triggerFileInput">Select JSON File</button>

      <p v-if="successImportMessage">{{ successImportMessage }}</p>
      <p v-if="errorImportMessage">{{ errorImportMessage }}</p>
    </div>

    <div v-if="currentData">
      <h1>Current Data</h1>
      <br/>
      <p v-if="errorDataMessage">{{ errorDataMessage }}</p>
      <div class="scroll-box">
        <pre>{{ currentData }}</pre>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, watchEffect } from 'vue';
import { generateJson, importJson } from '@/services/api/utils';

const successExportMessage = ref('')
const errorExportMessage = ref('')

const fileInput = ref(null)
const currentData = ref(null)
const errorImportMessage = ref('')
const successImportMessage = ref('')

const errorDataMessage = ref('')

const downloadJson = async () => {
  try {
    let data = await generateJson()
    data = data.data

    const url = URL.createObjectURL(new Blob([JSON.stringify(data, null, 4)], {type: 'application/json'}))

    const link = document.createElement('a');
    link.href = url;
    link.download = 'output.json';

    document.body.appendChild(link);
    link.click();

    document.body.removeChild(link);
    URL.revokeObjectURL(url);

    successExportMessage.value = 'Json file generated sucessfully'
  }
  catch (error) {
    console.error(error)
  }
}

const triggerFileInput = () => {
  fileInput.value.click()
}

const handleFileChange = (event) => {
  const file = event.target.files[0]

  errorImportMessage.value = ''
  successImportMessage.value = ''
  
  if (!file) return

  if (file.type !== 'application/json' && !file.name.endsWith('.json')) {
    errorImportMessage.value = 'Please select a valid JSON file.'
    return
  }

  const reader = new FileReader()

  reader.onload = async (e) => {
    try {
      const parsedData = JSON.parse(e.target.result)
      await importJson(parsedData)
      successImportMessage.value = 'File imported and parsed successfully!'
    } catch (error) {
      errorImportMessage.value = 'Failed to parse JSON. The file might be corrupted or malformed.'
      console.error(error)
    }
    try{
      currentData.value = await generateJson()
      currentData.value = currentData.value.data
    }
    catch (error) {
      errorDataMessage.value = 'Failure to load the data'
    }
  }

  reader.readAsText(file)

  event.target.value = ''
}

onMounted(async () => {
  try{
    currentData.value = await generateJson()
    currentData.value = currentData.value.data
  }
  catch (error) {
    errorDataMessage.value = 'Failure to load the data'
  }
})

watchEffect(async () => {
  currentData.value = await generateJson()
  currentData.value = currentData.value.data
})

</script>

<style scoped>
@import '@/css/style.css';
</style>