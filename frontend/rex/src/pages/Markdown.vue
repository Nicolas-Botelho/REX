<template>
  <div>
    <div>
      <h1>Export Data</h1>
      <br/>
      <select v-model="doc">
        <option :value="0">Domain Narrative</option>
        <option :value="1">Requirements</option>
        <option :value="2">Usecases</option>
        <option :value="3">Classes</option>
      </select>

      <br/>

      <p v-if="successExportMessage">{{ successExportMessage }}</p>
      <p v-if="errorExportMessage">{{ errorExportMessage }}</p>

      <br/>

      <div v-if="doc == 0">
        <button @click="domainNarrative">Download Domain Narrative</button>
        <div v-html="dnHtml"/>
      </div>
      <div v-if="doc == 1">
        <button @click="requirement">Download Requirements</button>
        <div v-html="rqHtml"/>
      </div>
      <div v-if="doc == 2">
        <button @click="useCase">Download Use Cases</button>
        <div v-html="ucHtml"/>
      </div>
      <div v-if="doc == 3">
        <button @click="clazz">Download Classes</button>
        <div v-html="clHtml"/>
      </div>

    </div>
  </div>
</template>

<script setup lang="ts">
import { getClassMd, getNarrativeMd, getRequirementMd, getUsecaseMd } from '@/services/api/utils';
import MarkdownIt from 'markdown-it';
import { ref, watch } from 'vue';

const successExportMessage = ref('')
const errorExportMessage = ref('')
const reload = ref(0)
const doc = ref(-1)

const dnMd = ref('')
const rqMd = ref('')
const ucMd = ref('')
const clMd = ref('')

const dnHtml = ref()
const rqHtml = ref()
const ucHtml = ref()
const clHtml = ref()

const md = MarkdownIt()

const domainNarrative = async () => {
  try {
    let data = dnMd.value

    const url = URL.createObjectURL(new Blob([data])) 

    const link = document.createElement('a')
    link.href = url
    link.download = 'domain_narrative.md'

    document.body.appendChild(link)
    link.click()

    document.body.removeChild(link)
    URL.revokeObjectURL(url)

    successExportMessage.value = 'Exported sucessfully'
  } catch (error) {
    errorExportMessage.value = 'Failed to export'
  }
}

const requirement = async () => {
  try {
    let data = rqMd.value

    const url = URL.createObjectURL(new Blob([data])) 

    const link = document.createElement('a')
    link.href = url
    link.download = 'requirements.md'

    document.body.appendChild(link)
    link.click()

    document.body.removeChild(link)
    URL.revokeObjectURL(url)

    successExportMessage.value = 'Exported sucessfully'
  } catch (error) {
    errorExportMessage.value = 'Failed to export'
  }
}

const useCase = async () => {
  try {
    let data = ucMd.value

    const url = URL.createObjectURL(new Blob([data])) 

    const link = document.createElement('a')
    link.href = url
    link.download = 'use_cases.md'

    document.body.appendChild(link)
    link.click()

    document.body.removeChild(link)
    URL.revokeObjectURL(url)

    successExportMessage.value = 'Exported sucessfully'
  } catch (error) {
    errorExportMessage.value = 'Failed to export'
  }
}

const clazz = async () => {
  try {
    let data = clMd.value

    const url = URL.createObjectURL(new Blob([data])) 

    const link = document.createElement('a')
    link.href = url
    link.download = 'classes.md'

    document.body.appendChild(link)
    link.click()

    document.body.removeChild(link)
    URL.revokeObjectURL(url)

    successExportMessage.value = 'Exported sucessfully'
  } catch (error) {
    errorExportMessage.value = 'Failed to export'
  }
}

watch(reload, async () => {
  try {
    dnMd.value = (await getNarrativeMd()).data
    dnHtml.value = md.render(dnMd.value)

    rqMd.value = (await getRequirementMd()).data
    rqHtml.value = md.render(rqMd.value)

    ucMd.value = (await getUsecaseMd()).data
    ucHtml.value = md.render(ucMd.value)

    clMd.value = (await getClassMd()).data
    clHtml.value = md.render(clMd.value)
  } catch (error) {
    errorExportMessage.value = 'Failed to fetch'
  }
}, {'immediate': true})

</script>

<style scoped>
@import '@/css/style.css';
</style>

<style>
@import '@/css/style.css';
</style>