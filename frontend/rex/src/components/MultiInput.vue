<template>
  <div class="dynamic-list-container">
    <div v-for="(_, index) in itemArray" :key="index" class="list-row">
      <input
        v-model="items[index]"
        type="text"
        placeholder="Type a value..."
        class="list-input"
      />
      <button 
        type="button" 
        class="delete-button btn-compact" 
        @click="removeItem(index)"
      >
        Remove
      </button>
    </div>
    
    <button 
      type="button" 
      class="create-button btn-compact add-btn" 
      @click="addItem"
    >
      + Add item
    </button>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  itemArray: string[]
}>()

const emit = defineEmits<{
  (e: 'update:itemArray', value: string[]): void
}>()

const items = computed({
  get: () => props.itemArray,
  set: (val) => emit('update:itemArray', val)
})

const addItem = () => {
  emit('update:itemArray', [...props.itemArray, ''])
}

const removeItem = (index: number) => {
  const updated = [...props.itemArray]
  updated.splice(index, 1)
  emit('update:itemArray', updated)
}
</script>

<style scoped>
.dynamic-list-container {
  display: flex;
  flex-direction: column;
  gap: 8px;
  max-width: 400px;
  font-family: Arial, Helvetica, sans-serif;
}

.list-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.list-input {
  flex: 1;
  padding: 6px 10px;
  font-size: 14px;
  font-family: Arial, Helvetica, sans-serif;
  color: #2c3e50;
  border: 1px solid #2c3e50;
  border-radius: 6px;
  outline: none;
  box-sizing: border-box;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.list-input:focus {
  border-color: #42b983;
  box-shadow: 0 0 0 2px rgba(66, 185, 131, 0.2);
}

/* .btn-compact {
  color: #dfdfdf;
  font-size: 13px;
  font-weight: 600;
  font-family: Arial, Helvetica, sans-serif;
  border: none;
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
}

.btn-compact:hover {
  transform: translateY(-1px) scale(1.01);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
}

.delete-button {
  background: #960404;
}
.delete-button:hover {
  background: #b94242;
}

.create-button {
  background: #219604;
}
.create-button:hover {
  background: #5ab942;
}

.add-btn {
  align-self: flex-start;
  margin-top: 4px;
} */
</style>