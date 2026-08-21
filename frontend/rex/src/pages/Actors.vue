<template>
  <h1>Actors</h1>

  <BaseItemBox v-for="(act, index) in acData" :key="index" @del="removeActor(Number(index))" @edit="openActorModal(Number(index))">
    <p>{{ act.name }}: {{ act.description }}</p>
  </BaseItemBox>

  <BaseModal title="Actor" :is-open="isActorModalOpen" @close="isActorModalOpen=false" @confirm="addOrUpdateActor()">
    <form class="modal-form" @submit.prevent">
      <div class="form-group">
        <label>Name</label>
        <input v-model="actor.actor.name">
      </div>
      <div class="form-group">
        <label>Description</label>
        <textarea v-model="actor.actor.description"></textarea>
      </div>
    </form>
  </BaseModal>

  <button class="create-button" @click="openActorModal(-1)">Add New</button>
</template>

<script setup lang="ts">
import BaseItemBox from '@/components/BaseItemBox.vue';
import BaseModal from '@/components/BaseModal.vue';
import { Actor } from '@/models/requirement_models';
import { deleteActor, getActors, postActor, putActor } from '@/services/api/actors';
import { ref, toRaw, watch } from 'vue';

const reload = ref(0)

const acData = ref()
const errorMessage = ref('')

const isActorModalOpen = ref(false)
const actor = ref({'actor_id': -1, 'actor': new Actor("", "")})

const addOrUpdateActor = async () => {
  if (actor.value.actor_id >= 0) {
    await updateActor()
  } else {
    await addActor()
  }
  isActorModalOpen.value = false
  reload.value = 1 - reload.value
}

const addActor = async () => {
  await postActor(actor.value.actor)
}

const updateActor = async () => {
  await putActor(actor.value.actor_id, actor.value.actor)
}

const removeActor = async (ac_id: number) => {
  await deleteActor(ac_id)
  reload.value = 1 - reload.value
}

const openActorModal = async (ac_id: number) => {
  if (ac_id >= 0) {
    actor.value.actor_id = ac_id
    actor.value.actor = structuredClone(toRaw(acData.value[ac_id]))
  } else {
    actor.value.actor_id = -1
    actor.value.actor = new Actor("", "")
  }
  isActorModalOpen.value = true
}

watch(reload, async () => {
  try {
    acData.value = (await getActors()).data
  } catch (error) {
    errorMessage.value = 'Failed to fetch.'
  }
}, {'immediate': true})

</script>

<style scoped>
@import '@/css/style.css';
</style>