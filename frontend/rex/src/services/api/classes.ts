import request from './api'

/////////////
// Classes //
/////////////

export async function getClasses() {
  try {
    return await request('classes/class/', {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function getClass(id: number) {
  try {
    return await request(`classes/class/${id}/`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function getClassByName(name: string) {
  try {
    return await request(`classes/class_by_name?class_name=${encodeURIComponent(name)}`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

// export function createClass(name: string) {
//   return request('classes/class/', {'method': 'POST', 'data': {'name': name}})
// }

// export function updateClass(id: number, name: string) {
//   return request(`classes/class/${id}/`, {'method': 'PUT', 'data': {name: name}})
// }

// export function deleteClass(id: number) {
//   return request(`classes/class/${id}/`, {'method': 'DELETE'})
// }

/////////////////
// Association //
/////////////////

export async function getClassAssociations(name: string) {
  try {
    return await request(`classes/class_associations?class_name=${encodeURIComponent(name)}`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

/////////////////
// Inheritance //
/////////////////

export async function getClassInheritances(name: string) {
  try {
    return await request(`classes/class_inheritances?class_name=${encodeURIComponent(name)}`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}