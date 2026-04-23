<template>
  <div>
    <h1>New Use Case</h1>

    <p>Define a New Use Case</p>
    <textarea v-model="def_uc" placeholder="UseCase{
Event{
performer: Actor Name
Actor: action description
System: action description
}
}"></textarea>
    <br/><br/>
    <button type="button" @click="addUseCase">Add Use Case</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { createUseCase, createEvent, createStep } from '@/services/api/usecases'
import { getActors } from '@/services/api/actors'

const def_uc = ref('')
const actors = ref([])

const transform = (uc_string) => {

  const LINE_EXPRESSION = /\r\n|\n|\r/g
  const name = String(uc_string.slice(0,uc_string.indexOf('{')).trim())
  const body = uc_string.slice(uc_string.indexOf('{')+1,uc_string.length-1).split('}')

  const events_obj = ref([])
  for (const item of body) {
    if (item.replace(LINE_EXPRESSION, '') != '') {
      const event = item.split('{')
      const event_name = event[0].replace(LINE_EXPRESSION, '')
      const steps = event[1].split('\n')

      const steps_obj = ref([])
      const actor = ref(null)

      for (const step of steps) {
        const step_list = step.split(':')
        if (step_list[0].trim() != null && step_list[0].trim() != '') {
          if (step_list[0].trim() == 'performer') {
            for (const actor_item of actors.value) {
              if (actor_item.name.toLowerCase() == step_list[1].trim().toLowerCase()) {
                actor.value = {'id': actor_item.id, 'name': actor_item.name}
              }
            }
          }
          else if (step_list[0].trim().toLowerCase() == actor.value.name.toLowerCase()
            || step_list[0].trim().toLowerCase() =='actor') {
            steps_obj.value.push({'system': false, 'description': step_list[1].trim()})
          }
          else if (step_list[0].trim().toLowerCase() == 'system') {
            steps_obj.value.push({'system': true, 'description': step_list[1].trim()})
          }
        }
      }

      events_obj.value.push({'name': event_name, 'steps': steps_obj.value, 'actor': actor.value.id})
    }
  }
  return {'name': name, 'events': events_obj.value}
}

const addUseCase = async () => {
  try {
    const uc_obj = transform(def_uc.value)

    const newUC = await createUseCase(uc_obj.name)

    for (const uc_event of uc_obj.events) {
      const newEvent = await createEvent(uc_event.name, uc_event.actor, newUC.id)
      for (const event_step of uc_event.steps) {
        await createStep(event_step.system, event_step.description, newEvent.id)
      }
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