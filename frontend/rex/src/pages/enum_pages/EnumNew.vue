<template>
  <div>
    <h1>New Enum</h1>

    <p>Define a New Enum</p>
    <textarea v-model="def_enum" placeholder="Enum{
ENUM_VALUE
ANOTHER_VALUE
}"></textarea>
    <br/><br/>
    <button type="button" @click="addEnum">Add Enum</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { createEnum, createEnumValue } from '@/services/api/enums'

const def_enum = ref('')

const transform = (enum_string) => {
  const LINE_EXPRESSION = /\r\n|\n|\r|\s/g
  const name = String(enum_string.slice(0,enum_string.indexOf('{')).trim())
  const values = enum_string.slice(enum_string.indexOf('{')+1,enum_string.indexOf('}')).split('\n')

  const values_obj = ref([])
  for (const item of values) {
    if (item.replace(LINE_EXPRESSION, '') != '') {
      values_obj.value.push(item)
    }
  }

  return {'name': name, 'values': values_obj.value}
}

const addEnum = async () => {
  const enum_obj = transform(def_enum.value)
  const newEnum = await createEnum(enum_obj.name)
  for (const item of enum_obj.values) {
    await createEnumValue(item, newEnum.id)
  }
}
</script>

<style scoped>
@import '@/css/style.css';
</style>