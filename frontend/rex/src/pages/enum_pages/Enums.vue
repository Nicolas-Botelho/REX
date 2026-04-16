<template>
  <div>
    <h1>Enums</h1>

    <p v-if="loading">Loading...</p>
    <p v-if="error">{{ error }}</p>

    <ul v-if="eenums">
      <li v-for="eenum in eenums" :key="eenum.id">
        <router-link :to="`enums/${eenum.id}`">{{ eenum.name }}</router-link>
        <button type="button" @click=""> Update Enum </button>
        <button type="button" @click="removeEnum(eenum.id)"> Delete Enum </button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getEnums, deleteEnum } from '@/services/api/enums'

const eenums = ref([])
const loading = ref(true)
const error = ref(null)

const removeEnum = async (id) => {
  await deleteEnum(id)
  eenums.value = await getEnums()
}

onMounted(async () => {
  try {
    eenums.value = await getEnums()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
h1 {
  font-size: 24px;
}
</style>