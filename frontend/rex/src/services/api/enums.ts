import request from './api'

// Enums
export function getEnums() {
  return request('classes/enum/', {'method': 'GET'})
}

export function getEnum(id: number) {
  return request(`classes/enum/${id}/`, {'method': 'GET'})
}

export function createEnum(name: string) {
  return request('classes/enum/', {'method': 'POST', 'data': {name: name}})
}

export function updateEnum(id: number, name: string) {
  return request(`classes/enum/${id}/`, {'method': 'PUT', 'data': {name: name}})
}

export function deleteEnum(id: number) {
  return request(`classes/enum/${id}/`, {'method': 'DELETE'})
}

// Enum Values

export function createEnumValue(value: string, enum_id: number) {
  return request('classes/enum_attribute/', {
    'method': 'POST',
    'data': {value: value, enum: enum_id}})
}

export function updateEnumValue(id: number, value: string, enum_id: number) {
  return request(`classes/enum_attribute/${id}/`, {
    'method': 'PUT',
    'data': {value: value, enum: enum_id}})
}

export function deleteEnumValue(id: number) {
  return request(`classes/enum_attribute/${id}/`, {'method': 'DELETE'})
}