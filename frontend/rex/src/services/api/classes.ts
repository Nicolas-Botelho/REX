import request from './api'

// Classes
export function getClasses() {
  return request('classes/class/', {'method': 'GET'})
}

export function getClass(id: number) {
  return request(`classes/class/${id}/`, {'method': 'GET'})
}

export function createClass(name: string) {
  return request('classes/class/', {'method': 'POST', 'data': {'name': name}})
}

export function updateClass(id: number, name: string) {
  return request(`classes/class/${id}/`, {'method': 'PUT', 'data': {name: name}})
}

export function deleteClass(id: number) {
  return request(`classes/class/${id}/`, {'method': 'DELETE'})
}

// Primitive Attributes
export function createPrimAttr(name: string, attr_type: string, klass_id: number) {
  return request('classes/class_attribute_prim/', {
    'method': 'POST',
    'data': {name: name, attr_type: attr_type, klass: klass_id}
  })
}

export function updatePrimAttr(id: number, name: string, attr_type: string, klass_id: number) {
  return request(`classes/class_attribute_prim/${id}/`, {
    'method': 'PUT',
    'data': {name: name, attr_type: attr_type, klass: klass_id}})
}

export function deletePrimAttr(id: number) {
  return request(`classes/class_attribute_prim/${id}/`, {'method': 'DELETE'})
}

// Enum Attributes
export function createEnumAttr(name: string, enum_id: number, klass_id: number) {
  return request('classes/class_attribute_enum/', {
    'method': 'POST',
    'data': {name: name, enum_id: enum_id, klass: klass_id}})
}

export function updateEnumAttr(id: number, name: string, enum_id: number, klass_id: number) {
  return request(`classes/class/${id}/`, {
    'method': 'PUT',
    'data': {name: name, enum_id: enum_id, klass: klass_id}})
}

export function deleteEnumAttr(id: number) {
  return request(`classes/class_attribute_enum/${id}/`, {'method': 'DELETE'})
}

// Relations
export function createRCR(
  minim: number|undefined, maxim: number|undefined, class_id: number
) {
  return request('classes/relation_class_reference/', {
    'method': 'POST',
    'data': {minim: minim, maxim: maxim, ref_class: class_id}})
}

export function updateRCR(
  id: number, minim: number|undefined, maxim: number|undefined, class_id: number
) {
  return request(`classes/relation_class_reference/${id}/`, {
    'method': 'PUT',
    'data': {minim: minim, maxim: maxim, ref_class: class_id}})
}

export function deleteRCR(id: number) {
  return request(`classes/relation_class_reference/${id}/`, {'method': 'DELETE'})
}

export function createRelation(src_id: number, tgt_id: number) {
  return request('classes/relation/', {
    'method': 'POST',
    'data': {src_id: src_id, tgt_id: tgt_id}})
}

export function updateRelation(id: number, src_id: number, tgt_id: number) {
  return request(`classes/relation/${id}/`, {
    'method': 'PUT',
    'data': {src_id: src_id, tgt_id: tgt_id}})
}

export function deleteRelation(id: number) {
  return request(`classes/relation/${id}/`, {'method': 'DELETE'})
}