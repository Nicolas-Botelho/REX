<template>
  <div v-if="classData">
    <h1>{{ classData.name }}</h1>
    <p style="text-align: center;"><<{{ classData.stereotype }}>></p>

      <h2 v-if="classData.class_attributes.length">Attributes</h2>

      <ul>
        <li v-for="item in classData.class_attributes" :key="item.id">
          <p v-if="item.attr_type">{{ item.name }} : {{ item.attr_type }}
            <p v-for="value in item.valid_values">- {{ value }}</p>
          </p>  
        </li>
      </ul>

      <h2 v-if="classData.class_associations.length">Relations</h2>

      <ul>
        <li v-for="item in classData.class_associations" :key="item.id">
          <p v-if="item.acr_as_src">
            {{ classData.name }} "{{ item.class_min ?? "N" }}..{{ item.class_max ?? "N" }}" --> "{{ item.acr_as_src.tgt.class_min ?? "N" }}..{{ item.acr_as_src.tgt.class_max ?? "N" }}" <router-link :to="`/classes/${item.acr_as_src.tgt.clazz.id}`"> {{ item.acr_as_src.tgt.clazz.name }} </router-link>
          </p>
          <p v-else-if="item.acr_as_tgt">
            <router-link :to="`/classes/${item.acr_as_tgt.src.clazz.id}`"> {{ item.acr_as_tgt.src.clazz.name }} </router-link> "{{ item.acr_as_tgt.src.class_min ?? "N" }}..{{ item.acr_as_tgt.src.class_max ?? "N" }}" --> "{{ item.class_min ?? "N" }}..{{ item.class_max ?? "N" }}" {{ classData.name }}
          </p>
        </li>
      </ul>
  </div>
  <p v-else>Loading...</p>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted, watchEffect } from 'vue'
import { getClass } from '@/services/api/classes'

const route = useRoute()
const classData = ref(null)

onMounted(async () => {
  const id = route.params.id
  classData.value = await getClass(id)
})

watchEffect(async () => {
  const id = route.params.id
  classData.value = await getClass(id)
})
</script>

<style scoped>
@import '@/css/style.css';
</style>