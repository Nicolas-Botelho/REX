<template>
  <div>
    <h1>New Enum</h1>

    <p>Define a New Enum</p>

    <input placeholder="Enum Name" v-model="enum_name">
    <br/><br/>

    <div>
      <p>Current Enum Values</p>
      <ul>
        <li v-for="item in values">
          {{ item }}
          <button @click="delEnumValue(item)">Remove Enum Value</button>
        </li>
      </ul>
    </div>

    <div>
      <p>Add New Enum Value</p>

      <input placeholder="Enum Value" v-model="enum_value">
      <br/><br/>

      <button type="button" @click="addEnumValue">Add Enum Value</button>
      <br/><br/>
    </div>

    <button type="button" @click="addEnum">Add Enum</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { createEnum, createEnumValue } from '@/services/api/enums'

const enum_name = ref('')
const enum_value = ref('')
const values = ref([])

const addEnumValue = () => {
  values.value.push(enum_value.value)
}

const delEnumValue = (item) => {
  let item_index = values.value.indexOf(item)
  values.value.splice(item_index, 1)
}

const addEnum = async () => {
  const newEnum = await createEnum(enum_name.value)
  for (const item of values.value) {
    await createEnumValue(item, newEnum.id)
  }
}
</script>

<style scoped>
@import '@/css/style.css';
</style>