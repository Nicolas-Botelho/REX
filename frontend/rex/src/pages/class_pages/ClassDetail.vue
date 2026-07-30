<template>
  <div v-if="classData">
    <h1>{{ classData.name }}</h1>
    <p style="text-align: center;"><<{{ classData.stereotype }}>></p>

      <h2 v-if="classData.class_attributes && classData.class_attributes.length">Attributes</h2>

      <ul>
        <li v-for="(item, index) in classData.class_attributes" :key="index">
          <p>{{ item.name }} : {{ item.attr_type }} <template v-if="item.is_multiple">(many)</template>
            <p v-for="value in item.valid_values">- {{ value }}</p>
          </p>
        </li>
      </ul>

      <h2 v-if="classData.associations && classData.associations.length">Associations</h2>

      <ul>
        <li v-for="(item, index) in classData.associations" :key="index">
          <p v-if="item.src.class_name == classData.name">
            {{ classData.name }} "{{ item.src.class_min }}..{{ item.src.class_max ?? "N" }}" -> "{{ item.tgt.class_min }}..{{ item.tgt.class_max ?? "N" }}" <a href="#" @click.prevent="goToClass(item.tgt.class_name)">{{ item.tgt.class_name }}</a>
          </p>
          <p v-else-if="item.tgt.class_name == classData.name">
            <a href="#" @click.prevent="goToClass(item.src.class_name)">{{ item.src.class_name }}</a> "{{ item.src.class_min }}..{{ item.src.class_max ?? "N" }}" -> "{{ item.tgt.class_min }}..{{ item.tgt.class_max ?? "N" }}" {{ classData.name }}
          </p>
        </li>
      </ul>

      <h2 v-if="classData.inheritances && classData.inheritances.length">Inheritances</h2>

      <ul>
        <li v-for="(item, index) in classData.inheritances" :key="index">
          <p v-if="item.parent_class_name == classData.name">
            {{ classData.name }} <|- <a href="#" @click.prevent="goToClass(item.child_class_name)">{{ item.child_class_name }}</a>
          </p>
          <p v-else-if="item.child_class_name == classData.name">
            <a href="#" @click.prevent="goToClass(item.parent_class_name)">{{ item.parent_class_name }}</a> <|- {{ classData.name }}
          </p>
        </li>
      </ul>

  </div>
  <p v-else-if="errorMessage">{{ errorMessage }}</p>
  <p v-else>Loading...</p>
</template>

<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import { ref, onMounted, watchEffect } from 'vue'
import { getClass, getClassAssociations, getClassInheritances, getClassByName } from '@/services/api/classes'

const route = useRoute()
const router = useRouter()
const classData = ref()
const classAssociations = ref()
const classInheritances = ref()

const errorMessage = ref('')

async function goToClass(className: string) {
  const data = await getClassByName(className)
  router.push(`/classes/${data.data[0].index}`)
}

onMounted(async () => {
  try {
    const id = route.params.id
    classData.value = await getClass(Number(id))
    classData.value = classData.value.data
    classAssociations.value = await getClassAssociations(classData.value.name)
    classInheritances.value = await getClassInheritances(classData.value.name)
    classData.value.associations = classAssociations.value.data
    classData.value.inheritances = classInheritances.value.data 
  }
  catch (error) {
    errorMessage.value = 'Failed to fetch'
  }
})

watchEffect(async () => {
  try {
    const id = route.params.id
    classData.value = await getClass(Number(id))
    classData.value = classData.value.data
    classAssociations.value = await getClassAssociations(classData.value.name)
    classInheritances.value = await getClassInheritances(classData.value.name)
    classData.value.associations = classAssociations.value.data
    classData.value.inheritances = classInheritances.value.data 
  }
  catch (error) {
    errorMessage.value = 'Failed to fetch'
  }
})
</script>

<style scoped>
@import '@/css/style.css';
</style>