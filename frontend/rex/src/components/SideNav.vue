<template>
  <nav class="sidenav">
    <router-link to="/">Home</router-link>
    <router-link to="/generate">Generate Artifacts</router-link>
    <router-link to="/json_data">JSON Data</router-link>
    <router-link to="/narrative">Domain Narrative</router-link>
    <router-link to="/requirements">Requirements</router-link>
    <router-link to="/usecases">Use Cases</router-link>
    <router-link to="/classes">Classes</router-link>
  </nav>
</template>

<style>
.sidenav {
  width: 200px;
  height: auto;
  background: #2c3e50;
  display: flex;
  flex-direction: column;
  padding: 20px;
  font-family: Arial, Helvetica, sans-serif;
}

.sidenav a {
  color: #e8edf2;
  margin-bottom: 10px;
  text-decoration: none;
}

.sidenav a.router-link-active {
  font-weight: bold;
  color: #42b983;
}
</style>