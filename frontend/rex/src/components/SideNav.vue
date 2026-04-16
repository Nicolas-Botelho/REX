<template>
  <nav class="sidenav">
    <router-link to="/">Home</router-link>
    <router-link to="/generate">Generate Artifacts</router-link>
    <router-link to="/classes">Classes</router-link>
    <router-link to="/classes/new">New Class</router-link>
    <router-link to="/enums">Enums</router-link>
    <router-link to="/enums/new">New Enum</router-link>
    <router-link to="/usecases">Use Cases</router-link>
    <router-link to="/usecases/new">New Use Case</router-link>
    <router-link to="/actors">Actors</router-link>
    <router-link to="/actors/new">New Actor</router-link>
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
}

.sidenav a {
  color: white;
  margin-bottom: 10px;
  text-decoration: none;
}

.sidenav a.router-link-active {
  font-weight: bold;
  color: #42b983;
}
</style>