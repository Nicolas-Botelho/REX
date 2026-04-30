<!-- BaseButton.vue -->
<template>
  <button
    :class="['butn', variant, { loading }]"
    :disabled="disabled || loading"
    @click="$emit('click')"
  >
    <span v-if="loading" class="spinner"></span>
    <span><slot /></span>
  </button>
</template>

<script setup>
defineProps({
  variant: {
    type: String,
    default: 'primary', // primary, secondary, danger, etc.
  },
  disabled: Boolean,
  loading: Boolean,
});
</script>

<style scoped>
.btn {
  border: none;
  padding: 12px 20px;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.25s ease;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

/* Variants */
.primary {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: white;
}

.secondary {
  background: #f3f4f6;
  color: #111827;
}

.danger {
  background: #ef4444;
  color: white;
}

/* Hover effects */
.btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

/* Active */
.btn:active:not(:disabled) {
  transform: scale(0.97);
}

/* Disabled */
.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Spinner */
.spinner {
  width: 16px;
  height: 16px;
  border: 2px solid white;
  border-top: 2px solid transparent;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>