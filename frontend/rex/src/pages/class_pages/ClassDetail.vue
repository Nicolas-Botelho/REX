<template>
  <div v-if="classData">
    <h1>{{ classData.name }}</h1>
    <p v-if="classData.stereotype" style="text-align: center;"><<{{ classData.stereotype }}>></p>

    <button class="edit-button" @click="openClassModal()">Edit Class</button>

    <BaseModal title="Class" :is-open="isClassModalOpen" @close="isClassModalOpen=false" @confirm="updateClass()">
      <form class="modal-form" @submit.prevent>
        <div class="form-group">
          <label>Class Name</label>
          <input v-model="clazz.name">
        </div>
        <div class="form-group">
          <label>Class Stereotype</label>
          <input v-model="clazz.stereotype">
        </div>
      </form>
    </BaseModal>

      <h2 v-if="classData.class_attributes">Attributes</h2>

      <BaseItemBox v-for="(item, index) in classData.class_attributes" :key="index" @del="removeAttribute(Number(index))" @edit="openAttributeModal(Number(index))">
        <p>{{ item.name }} : {{ item.attr_type }} <template v-if="item.is_multiple">(many)</template>
            <p v-for="value in item.valid_values">- {{ value }}</p>
          </p>
      </BaseItemBox>

      <button class="create-button" @click="openAttributeModal(-1)">Add New</button>

      <BaseModal title="Class Attribute" :is-open="isAttributeModalOpen" @close="isAttributeModalOpen=false" @confirm="addOrUpdateAttribute()">
        <form class="modal-form" @submit.prevent>
          <div class="form-group">
            <label>Attribute Name</label>
            <input v-model="attr.attr.name">
          </div>
          <div class="form-group">
            <label>Attribute Type</label>
            <select v-model="attr.attr.attr_type" size="4">
              <option v-for="(item, index) in types" :key="index" :value="item">{{ item }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Is Multiple?</label>
            <input v-model="attr.attr.is_multiple" type="checkbox">
          </div>
          <div class="form-group">
            <label>Valid Values (empty for all values)</label>
            <MultiInput v-model:item-array="attr.attr.valid_values"></MultiInput>
          </div>
        </form>
      </BaseModal>

      <h2 v-if="classData.associations">Associations</h2>

      <BaseItemBox v-for="item in classData.associations" :key="item.id" @del="removeAssociation(Number(item.id))" @edit="openAssociationModal(Number(item.id))">
        <p v-if="item.assoc.src.class_name == classData.name">
          {{ classData.name }} "{{ item.assoc.src.class_min }}..{{ item.assoc.src.class_max ?? "N" }}" -> "{{ item.assoc.tgt.class_min }}..{{ item.assoc.tgt.class_max ?? "N" }}" <a href="#" @click.prevent="goToClass(item.assoc.tgt.class_name)">{{ item.assoc.tgt.class_name }}</a>
        </p>
        <p v-else-if="item.assoc.tgt.class_name == classData.name">
          <a href="#" @click.prevent="goToClass(item.assoc.src.class_name)">{{ item.assoc.src.class_name }}</a> "{{ item.assoc.src.class_min }}..{{ item.assoc.src.class_max ?? "N" }}" -> "{{ item.assoc.tgt.class_min }}..{{ item.assoc.tgt.class_max ?? "N" }}" {{ classData.name }}
        </p>
      </BaseItemBox>

      <button class="create-button" @click="openAssociationModal(-1)">Add New</button>

      <BaseModal title="Association" :is-open="isAssociationModalOpen" @close="isAssociationModalOpen=false" @confirm="addOrUpdateAssociation()">
        <form class="modal-form" @submit.prevent>
          <div class="form-group">
            <label>Association Source</label>
            <p>{{ classData.name }}</p>
          </div>
          <div class="form-group">
            <label>Association Source Cardinality (empty for Many)</label>
            <input v-model="assoc.assoc.src.class_min" type="number">
            <input v-model="assoc.assoc.src.class_max" type="number">    
          </div>
          <div class="form-group">
            <label>Association Target</label>
                <select v-model="assoc.assoc.tgt.class_name" size="4">
              <option v-for="(item, index) in classes" :key="index" :value="item.name">{{ item.name }}</option>
            </select>    
          </div>
          <div class="form-group">
            <label>Association Target Cardinality (empty for Many)</label>
            <input v-model="assoc.assoc.tgt.class_min" type="number">
            <input v-model="assoc.assoc.tgt.class_max" type="number">    
          </div>
        </form>
      </BaseModal>

      <h2 v-if="classData.inheritances">Inheritances</h2>

      <BaseItemBox v-for="item in classData.inheritances" :key="item.id" @del="removeInheritance(Number(item.id))" @edit="openInheritanceModal(Number(item.id))">
        <p v-if="item.inher.parent_class_name == classData.name">
          {{ classData.name }} <|- <a href="#" @click.prevent="goToClass(item.inher.child_class_name)">{{ item.inher.child_class_name }}</a>
        </p>
        <p v-else-if="item.inher.child_class_name == classData.name">
          <a href="#" @click.prevent="goToClass(item.inher.parent_class_name)">{{ item.inher.parent_class_name }}</a> <|- {{ classData.name }}
        </p>
      </BaseItemBox>

      <button class="create-button" @click="openInheritanceModal(-1)">Add New</button>

      <BaseModal title="Inheritance" :is-open="isInheritanceModalOpen" @close="isInheritanceModalOpen=false" @confirm="addOrUpdateInheritance()">
        <form class="modal-form" @submit.prevent>
          <div class="form-group">
            <label>Parent Class</label>
            <select v-model="inher.inher.parent_class_name" size="4">
              <option v-for="(item, index) in classes" :key="index" :value="item.name">{{ item.name }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Child Class</label>
            <select v-model="inher.inher.child_class_name" size="4">
              <option v-for="(item, index) in classes" :key="index" :value="item.name">{{ item.name }}</option>
            </select>
          </div>
        </form>
      </BaseModal>

  </div>
  <p v-else-if="errorMessage">{{ errorMessage }}</p>
  <p v-else>Loading...</p>
</template>

<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import { ref, watch, toRaw } from 'vue'
import { getClass, getClassAssociations, getClassInheritances, getClassByName, putClass, postAssociation, putAssociation, deleteAssociation, postInheritance, putInheritance, deleteInheritance, getClasses } from '@/services/api/classes'
import BaseItemBox from '@/components/BaseItemBox.vue'
import BaseModal from '@/components/BaseModal.vue'
import { Association, AssociationClassReference, Class, ClassAttribute, Inheritance, TypeEnum } from '@/models/class_models'
import MultiInput from '@/components/MultiInput.vue'

const route = useRoute()
const router = useRouter()
const classData = ref()

let cls_id = Number(route.params.id)

const reload = ref(0)
const errorMessage = ref('')

const isClassModalOpen = ref(false)
const isAttributeModalOpen = ref(false)
const isAssociationModalOpen = ref(false)
const isInheritanceModalOpen = ref(false)

const clazz = ref(new Class('', '', []))
const attr = ref({'attr_id': -1, 'attr': new ClassAttribute('', TypeEnum.STRING, false, [])})
const assoc = ref({'assoc_id': -1, 'assoc': new Association(new AssociationClassReference("", 0, null), new AssociationClassReference('', 0, null))})
const inher = ref({'inher_id': -1, 'inher': new Inheritance('', '')})

const types = Object.values(TypeEnum)
const classes = ref()

///////////
// Class //
///////////

const updateClass = async () => {
  await putClass(cls_id, clazz.value)
  isClassModalOpen.value = false
  reload.value = 1 - reload.value
}

const openClassModal = () => {
  clazz.value.name = classData.value.name
  clazz.value.stereotype = classData.value.stereotype
  clazz.value.class_attributes = structuredClone(toRaw(classData.value.class_attributes))

  isClassModalOpen.value = true
}

///////////////
// Attribute //
///////////////

const addOrUpdateAttribute = async () => {
  if (attr.value.attr_id >= 0) {
    await updateAttribute()
  } else {
    await addAttribute()
  }
  isAttributeModalOpen.value = false
  reload.value = 1 - reload.value
}

const addAttribute = async () => {
  const new_class = new Class(classData.value.name, classData.value.stereotype, structuredClone(toRaw(classData.value.class_attributes)))

  new_class.class_attributes.push(attr.value.attr)

  await putClass(cls_id, new_class)
}

const updateAttribute = async () => {
  const new_class = new Class(classData.value.name, classData.value.stereotype, structuredClone(toRaw(classData.value.class_attributes)))

  new_class.class_attributes[attr.value.attr_id] = attr.value.attr

  await putClass(cls_id, new_class)
}

const removeAttribute = async (at_id: number) => {
  const new_class = new Class(classData.value.name, classData.value.stereotype, structuredClone(toRaw(classData.value.class_attributes)))

  if (new_class.class_attributes[at_id]) {
    const index = new_class.class_attributes.indexOf(new_class.class_attributes[at_id], 0)
    if (index > -1) {
      new_class.class_attributes.splice(index, 1)
    }
  }

  await putClass(cls_id, new_class)
  reload.value = 1 - reload.value
}

const openAttributeModal = (at_id: number) => {
  if (at_id >= 0) {
    attr.value.attr_id = at_id
    attr.value.attr = structuredClone(toRaw(classData.value.class_attributes[at_id]))
  } else {
    attr.value.attr_id = -1
    attr.value.attr = new ClassAttribute('', TypeEnum.STRING, false, [])
  }
  isAttributeModalOpen.value = true
}

/////////////////
// Association //
/////////////////

const addOrUpdateAssociation = async () => {
  if (assoc.value.assoc_id >= 0) {
    await updateAssociation()
  } else {
    await addAssociation()
  }
  isAssociationModalOpen.value = false
  reload.value = 1 - reload.value
}

const addAssociation = async () => {
  await postAssociation(assoc.value.assoc)
}

const updateAssociation = async () => {
  await putAssociation(assoc.value.assoc_id, assoc.value.assoc)
}

const removeAssociation = async (as_id: number) => {
  await deleteAssociation(as_id)
  reload.value = 1 - reload.value
}

const openAssociationModal = (as_id: number) => {
  if (as_id >= 0) {
    assoc.value.assoc_id = classData.value.associations[as_id].id
    assoc.value.assoc = structuredClone(toRaw(classData.value.associations[as_id].assoc))
  } else {
    assoc.value.assoc_id = -1
    assoc.value.assoc = new Association(new AssociationClassReference(classData.value.name, 0, null), new AssociationClassReference("", 0, null))
  }
  isAssociationModalOpen.value = true
}

/////////////////
// Inheritance //
/////////////////

const addOrUpdateInheritance = async () => {
  if (inher.value.inher_id >= 0) {
    await updateInheritance()
  } else {
    await addInheritance()
  }
  isInheritanceModalOpen.value = false
  reload.value = 1 - reload.value
}

const addInheritance = async () => {
  await postInheritance(inher.value.inher)
}

const updateInheritance = async () => {
  await putInheritance(inher.value.inher_id, inher.value.inher)
}

const removeInheritance = async (ih_id: number) => {
  await deleteInheritance(ih_id)
  reload.value = 1 - reload.value
}

const openInheritanceModal = (ih_id: number) => {
  if (ih_id >= 0) {
    inher.value.inher_id = classData.value.inheritances[ih_id].id
    inher.value.inher = structuredClone(toRaw(classData.value.inheritances[ih_id].inher))
  } else {
    inher.value.inher_id = -1
    inher.value.inher = new Inheritance(classData.value.name, "")
  }
  isInheritanceModalOpen.value = true
}

async function goToClass(className: string) {
  const data = await getClassByName(className)
  cls_id = data.data[0].index
  router.push(`/classes/${cls_id}`)
  reload.value = 1 - reload.value
}

watch(reload, async () => {
  try {
    classData.value = (await getClass(cls_id)).data
    
    classes.value = (await getClasses()).data

    const assocRaw = await getClassAssociations(classData.value.name)
    const inherRaw = await getClassInheritances(classData.value.name)

    let assoc_index = 0
    classData.value.associations = []
    while (assoc_index < assocRaw.data.length) {
      classData.value.associations.push({'id': assocRaw.data[assoc_index][0], 'assoc': assocRaw.data[assoc_index][1]})
      assoc_index += 1
    }

    let inher_index = 0
    classData.value.inheritances = []
    while (inher_index < inherRaw.data.length) {
      classData.value.inheritances.push({'id': inherRaw.data[inher_index][0], 'inher': inherRaw.data[inher_index][1]})
      inher_index += 1
    }

  } catch (error) {
    errorMessage.value = 'Failed to fetch'
  }
}, {'immediate': true})
</script>

<style scoped>
@import '@/css/style.css';
</style>