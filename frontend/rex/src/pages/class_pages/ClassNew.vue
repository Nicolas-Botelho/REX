<template>
  <div>
    <h1>New Class</h1>

    <p>Define a New Class</p>
    <textarea v-model="def_class" placeholder='Class{
attribute1:type
attribute2:enum
}
Class"0..1"-->"1..N"AnotherClass'></textarea>
    <br/><br/>
    <button type="button" @click="addClass">Add Class</button>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getClasses, createClass, createPrimAttr, createEnumAttr, createRCR, createRelation } from '@/services/api/classes'
import { getEnums } from '@/services/api/enums'
import { parse } from '@/services/parser/class_parser'

const enums = ref([])
const classes = ref([])
const def_class = ref('')

const check = (class_string) => {
  parse(class_string)
}

const transform = (class_string) => {
  const LINE_EXPRESSION = /\r\n|\n|\r|\s/g
  const name = String(class_string.slice(0,class_string.indexOf('{')).trim())
  const attrs = class_string.slice(class_string.indexOf('{')+1,class_string.indexOf('}')).split('\n')
  const rels = class_string.slice(class_string.indexOf('}')+1,class_string.length).split('\n')

  const attrs_obj = ref([])
  const rels_obj = ref([])

  for (const item of attrs) {
    const no_space_item = String(item.replace(LINE_EXPRESSION,''))
    if (no_space_item != '') {
      const attr = no_space_item.toLowerCase().split(':')
      const attr_name = attr[0]
      const attr_type = attr[1]
      if (['string', 'integer', 'float', 'boolean'].includes(attr_type)) {
        attrs_obj.value.push({'name': attr_name, 'attr_type': attr_type})      
      }
      else {
        const enum_id = ref(null)
        for (const enum_item of enums.value) {
          if (String(enum_item.name).replace(LINE_EXPRESSION, '').toLowerCase() == attr_type.toLowerCase()) {
            enum_id.value = enum_item.id
          }
        }
        if (enum_id.value) {
          attrs_obj.value.push({'name': attr_name, 'enum_id': enum_id.value})
        }
      }
    } 
  }

  for (const item of rels) {
    const no_space_item = String(item.replace(LINE_EXPRESSION, ''))
    if (no_space_item != '') {
      const rel_values = no_space_item.replace("'", '"').split('"')
      const src_name = rel_values[0]
      const src_cardin = rel_values[1].split('..')
      const tgt_cardin = rel_values[3].split('..')
      const tgt_name = rel_values[4]

      src_cardin[0] = Number(src_cardin[0])
      if (src_cardin[1] == 'n') src_cardin[1] = null
      else src_cardin[1] = Number(src_cardin[1])

      tgt_cardin[0] = Number(tgt_cardin[0])
      if (tgt_cardin[1] == 'n') tgt_cardin[1] = null
      else tgt_cardin[1] = Number(tgt_cardin[1])

      if (src_name == name) {
        const ref_class_id = ref(null)
        for (const class_item of classes.value) {
          if (String(class_item.name).replace(LINE_EXPRESSION, '').toLowerCase() == tgt_name.toLowerCase()) {
            ref_class_id.value = class_item.id
          }
        }
        if (ref_class_id.value) {
          rels_obj.value.push({'src': {'minim': src_cardin[0], 'maxim': src_cardin[1]}, 'tgt': {'minim': tgt_cardin[0], 'maxim': tgt_cardin[1], 'ref_class': ref_class_id.value}})
        }
      }
      else if (tgt_name == name) {
        const ref_class_id = ref(null)
        for (const class_item of classes.value) {
          if (String(class_item.name).replace(LINE_EXPRESSION, '').toLowerCase() == src_name.toLowerCase()) {
            ref_class_id.value = class_item.id
          }
        }
        if (ref_class_id.value) {
          rels_obj.value.push({'src': {'minim': src_cardin[0], 'maxim': src_cardin[1], 'ref_class': ref_class_id.value}, 'tgt': {'minim': tgt_cardin[0], 'maxim': tgt_cardin[1]}})
        }
      }
    }
  }

  console.log(rels_obj.value)
  return {'name': name, 'attributes': attrs_obj.value, 'relations': rels_obj.value}

}

const addClass = async () => {
  try{
    check(def_class.value)
    const class_obj = transform(def_class.value)

    const newClass = await createClass(class_obj.name)
    for (const item of class_obj.attributes) {
      if (item.enum_id) {
        await createEnumAttr(item.name, item.enum_id, newClass.id)
      }
      else {
        await createPrimAttr(item.name, item.attr_type, newClass.id)
      }
    }
    for (const item of class_obj.relations) {
      if (item.tgt.ref_class) {
        const newSrc = await createRCR(item.src.minim, item.src.maxim, newClass.id)
        const newTgt = await createRCR(item.tgt.minim, item.tgt.maxim, item.tgt.ref_class)
        await createRelation(newSrc.id, newTgt.id)
      } else if (item.src.ref_class) {
        const newSrc = await createRCR(item.src.minim, item.src.maxim, item.src.ref_class)
        const newTgt = await createRCR(item.tgt.minim, item.tgt.maxim, newClass.id)
        await createRelation(newSrc.id, newTgt.id)
      }
      
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