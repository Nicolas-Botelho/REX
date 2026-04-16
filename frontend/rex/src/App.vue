<script setup lang="ts"></script>

<template>
  <title>REX</title>

  <div class="layout">
    <SideNav />
    <main class="content">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import SideNav from './components/SideNav.vue'
</script>

<style>
.layout {
  display: flex;
}

.content {
  flex: 1;
  padding: 20px;
}
</style>

<style scoped></style>
