<template>
  <div>
    <h1>New Class</h1>

    <p>Define a New Class</p>

    <input placeholder="Class Name" v-model="class_name">
    <br/><br/>

    <div>
      <p>Current Attributes</p>
      <ul>
        <li v-for="item in attrs">
          {{ item.name }} : {{ item.type_name ?? item.enum_name }}
          <button @click="delAttribute(item)">Remove Attribute</button>
        </li>
      </ul>
    </div>

    <div>
      <p>Add New Attribute</p>

      <input placeholder="Attribute Name" v-model="attr_name">
      <br/><br/>

      <select placeholder="Attribute Type" v-model="attr_type">
        <option value="boolean">Boolean</option>
        <option value="float">Float</option>
        <option value="integer">Integer</option>
        <option value="string">String</option>
        <option v-for="item in enums"> {{ item.name }} </option>
      </select>
      <br/><br/>

      <button type="submit" @click="addAttribute()">Add Attribute</button>
      <br/><br/>
    </div>

    <div>
      <p>Current Relations</p>
      <ul>
        <li v-for="item in rels">
          {{ item.src.name }} "{{ item.src.min }}..{{ item.src.max ?? 'N' }}" -> "{{ item.tgt.min ?? 'N' }}..{{ item.tgt.max ?? 'N' }}" {{ item.tgt.name }}
          <button @click="delRelation(item)">Remove Relation</button>
        </li>
      </ul>
    </div>

    <div>
      <p>Add New Relation</p>

      <select placeholder="Related Class" v-model="other_cls">
        <option v-for="item in classes">{{ item.name }}</option>
      </select>
      <br/><br/>

      <select placeholder="Cardinality" v-model="card">
        <option value='{"src":1,"tgt":1}'>One To One</option>
        <option value='{"src":1,"tgt":null}'>One To Many</option>
        <option value='{"src":null,"tgt":1}'>Many To One</option>
        <option value='{"src":null,"tgt":null}'>Many To Many</option>
      </select>
      <br/><br/>

      <select placeholder="Mandatory" v-model="opt">
        <option value='{"src":0,"tgt":0}'>None</option>
        <option value='{"src":1,"tgt":0}'>{{ class_name ?? "Class" }}</option>
        <option value='{"src":0,"tgt":1}'>Other</option>
        <option value='{"src":1,"tgt":1}'>Both</option>
      </select>
      <br/><br/>

      <button type="submit" @click="addRelation()">Add Relation</button>
      <br/><br/>
    </div>

    <button type="button" @click="addClass">Add Class</button>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getClasses, createClass, createPrimAttr, createEnumAttr, createRCR, createRelation } from '@/services/api/classes'
import { getEnums } from '@/services/api/enums'

const enums = ref([])
const classes = ref([])
const primitive_types = ['boolean', 'float', 'integer', 'string']

const class_name = ref('')
const attrs = ref([])
const rels = ref([])

const attr_name = ref('')
const attr_type = ref('')

const other_cls = ref('')
const card = ref('')
const opt = ref('')

const addAttribute = () => {
  if (attr_name.value != '' && attr_type.value != '') {
    if (primitive_types.includes(attr_type.value)) {
      attrs.value.push({name: attr_name.value, type_name: attr_type.value})
    }
    else {
      attrs.value.push({name: attr_name.value, enum_name: attr_type.value})
    }
  }
}

const delAttribute = (item) => {
  let item_index = attrs.value.indexOf(item)
  attrs.value.splice(item_index, 1)
}

const addRelation = () => {
  if (other_cls.value != '' && card.value != '' && opt.value != '') {
    let card_obj = JSON.parse(card.value)
    let opt_obj = JSON.parse(opt.value)
    
    rels.value.push({
      src: {name: class_name.value, min: opt_obj.src, max: card_obj.src},
      tgt: {name: other_cls.value, min: opt_obj.tgt, max: card_obj.tgt}
    })
  }
}

const delRelation = (item) => {
  let item_index = rels.value.indexOf(item)
  rels.value.splice(item_index, 1)
}

const enumByName = (name) => {
  for (const item of enums.value) {
    if (item.name == name) {
      return item
    }
  }
  return null
}

const classByName = (name) => {
  for (const item of classes.value) {
    if (item.name == name) {
      return item
    }
  }
  return null
}

const addClass = async () => {
  try{
    const newClass = await createClass(class_name.value)

    for (const item of attrs.value) {
      if (item.enum_name) {
        // console.log(item.name, enumByName(item.enum_name).id)
        await createEnumAttr(item.name, enumByName(item.enum_name).id, newClass.id)
      }
      else {
        await createPrimAttr(item.name, item.type_name, newClass.id)
      }
    }
    for (const item of rels.value) {
      const newSrc = await createRCR(item.src.min, item.src.max, newClass.id)
      const newTgt = await createRCR(item.tgt.min, item.tgt.max, classByName(item.tgt.name).id)
      await createRelation(newSrc.id, newTgt.id)
    }
  }
  catch (error) {
    console.error(error)
  }
}

onMounted(async () => {
  enums.value = await getEnums()
  classes.value = await getClasses()
})
</script>

<style scoped>
@import '@/css/style.css';
</style>