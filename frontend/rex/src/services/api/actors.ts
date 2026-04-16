import request from './api'

export function getActors() {
  return request('usecases/actor/', {'method': 'GET'})
}

export function getActor(id: number) {
  return request(`usecases/actor/${id}/`, {'method': 'GET'})
}

export function createActor(name: string, description: string) {
  return request('usecases/actor/', {
    'method': 'POST',
    'data': {name: name, description: description}})
}

export function updateActor(id: number, name: string, description: string) {
  return request(`usecases/actor/${id}/`, {
    'method': 'PUT',
    'data': {name: name, description: description}})
}

export function deleteActor(id: number) {
  return request(`usecases/actor/${id}/`, {'method': 'DELETE'})
}