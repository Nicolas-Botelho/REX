<template>
  <div v-if="enumData">
    <h1>{{ enumData.name }}</h1>

      <h2 v-if="enumData.enum_values.length">Enum Values</h2>

      <ul>
        <li v-for="item in enumData.enum_values" :key="item.id">
          {{ item.value }}
        </li>
      </ul>
  </div>
  <p v-else>Loading...</p>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import { getEnum } from '@/services/api/enums'

const route = useRoute()
const enumData = ref(null)

onMounted(async () => {
  const id = route.params.id
  enumData.value = await getEnum(id)
})
</script>

<style scoped>
@import '@/css/style.css';
</style>