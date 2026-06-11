<template>
  <div>
    <h1>New Use Case</h1>

    <p>Define a New Use Case</p>
    <!-- <textarea v-model="def_uc" placeholder="UseCase{
Event{
performer: Actor Name
Actor: action description
System: action description
}
}"></textarea> -->

    <input placeholder="Use Case Name" v-model="uc_name">

    <div>
      <p>Current Events</p>
      <ul>
        <li v-for="item in events">
          {{ item.name }} ({{ item.actor }})
          <button @click="delEvent(item)">Remove Event</button>
        </li>
      </ul>
    </div>

    <div>
      <p>Add New Event</p>

      <input placeholder="Event Name" v-model="event_name">
      <br/><br/>

      <select placeholder="Select Actor" v-model="event_actor">
        <option v-for="item of actors">{{ item.name }}</option>
      </select>
      <br/><br/>

      <button type="button" @click="addEvent">Add Event</button>
      <br/><br/>
    </div>

    <button type="button" @click="addUseCase">Add Use Case</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { createUseCase, createEvent } from '@/services/api/usecases'
import { getActors } from '@/services/api/actors'

const actors = ref([])

const uc_name = ref('')
const events = ref([])
const event_name = ref('')
const event_actor = ref('')

const addEvent = () => {
  events.value.push({name: event_name.value, actor: event_actor.value})
}

const delEvent = (item) => {
  let event_index = events.value.indexOf(item)
  events.value.splice(event_index, 1)
}

const addUseCase = async () => {
  try {
    const newUC = await createUseCase(uc_name.value)

    for (const uc_event of events.value) {
      const newEvent = await createEvent(uc_event.name, uc_event.actor, newUC.id)
      // for (const event_step of uc_event.steps) {
      //   await createStep(event_step.system, event_step.description, newEvent.id)
      // }
    }
  }
  catch (error) {
    console.error(error)
  }
}

onMounted(async () => {
  actors.value = await getActors()
})
</script>

<style scoped>
@import '@/css/style.css';
</style>