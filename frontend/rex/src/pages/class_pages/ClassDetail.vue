<template>
  <div v-if="classData">
    <h1>{{ classData.name }}</h1>

      <h2 v-if="classData.class_primitive_attrs.length">Primitive Type Attributes</h2>

      <ul>
        <li v-for="item in classData.class_primitive_attrs" :key="item.id">
          {{ item.name }} : {{ item.attr_type }}
        </li>
      </ul>

      <h2 v-if="classData.class_enum_attrs.length">Enum Type Attributes</h2>

      <ul>
        <li v-for="item in classData.class_enum_attrs" :key="item.id">
          {{ item.name }} : <router-link :to="`/enums/${item.enum.id}`"> {{ item.enum.name }} </router-link> 
        </li>
      </ul>

      <h2 v-if="classData.class_relations.length">Relations</h2>

      <ul>
        <li v-for="item in classData.class_relations" :key="item.id">
          <p v-if="item.rcr_as_src">
            {{ classData.name }} "{{ item.minim ?? "N" }}..{{ item.maxim ?? "N" }}" --> "{{ item.rcr_as_src.tgt.minim ?? "N" }}..{{ item.rcr_as_src.tgt.maxim ?? "N" }}" <router-link :to="`/classes/${item.rcr_as_src.tgt.ref_class.id}`"> {{ item.rcr_as_src.tgt.ref_class.name }} </router-link>
          </p>
          <p v-else-if="item.rcr_as_tgt">
            <router-link :to="`/classes/${item.rcr_as_tgt.src.ref_class.id}`"> {{ item.rcr_as_tgt.src.ref_class.name }} </router-link> "{{ item.rcr_as_tgt.src.minim ?? "N" }}..{{ item.rcr_as_tgt.src.maxim ?? "N" }}" --> "{{ item.minim ?? "N" }}..{{ item.maxim ?? "N" }}" {{ classData.name }}
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