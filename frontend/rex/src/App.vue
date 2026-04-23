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
body {
  margin: 0;
  padding: 0;
  background: #e8edf2;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
}

.layout {
  display: flex;
  min-height: 100vh;
}

.content {
  flex: 1;
  padding: 20px;
}
</style>