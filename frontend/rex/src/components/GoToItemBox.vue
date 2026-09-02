<template>
  <div class="box">
    <div>
      <slot />
    </div>

    <div class="box-actions">
      <button v-for="btn in buttons" :key="btn.id" :class="btn.type" @click="emit(btn.id)">{{ btn.label }}</button>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  buttons: {
    type: Array<any>,
    default: () => [
      {id: 'del', label: 'Delete', type: 'delete-button'},
      {id: 'goTo', label: 'Go To', type: 'edit-button'}
    ]
  }
})

const emit = defineEmits(['del', 'goTo'])

const del = () => {
  emit('del')
}
const goTo = () => {
  emit('goTo')
}
</script>

<style scoped>
  @import '@/css/style.css';

  .box {
    border-left: 2px solid #2c3e50;
    border-bottom: 2px solid #2c3e50;
    border-top-left-radius: 3px;
    border-bottom-left-radius: 6px;
    border-bottom-right-radius: 3px;
    /* border-style: solid;
    border-radius: 10px;
    border-color: #2c3e50; */

    padding: 4px;
    padding-left: 16px;
    margin-bottom: 16px;
  }

  .box-actions {
    display: flex;
    justify-content: flex-end;
    gap: 8px;
  }
</style>