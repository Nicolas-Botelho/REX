import { sys } from 'typescript'
import request from './api'

// Use Cases
export function getUseCases() {
  return request('usecases/usecase/', {'method': 'GET'})
}

export function getUseCase(id: number) {
  return request(`usecases/usecase/${id}/`, {'method': 'GET'})
}

export function createUseCase(name: string) {
  return request('usecases/usecase/', {'method': 'POST', 'data': {name: name}})
}

export function updateUseCase(id: number, name: string) {
  return request(`usecases/usecase/${id}/`, {'method': 'PUT', 'data': {name: name}})
}

export function deleteUseCase(id: number) {
  return request(`usecases/usecase/${id}/`, {'method': 'DELETE'})
}

// Events
export function createEvent(name: string, actor_id: number, usecase_id: number) {
  return request('usecases/event/', {
    'method': 'POST',
    'data': {name: name, actor_id: actor_id, usecase: usecase_id}})
}

export function updateEvent(
  id: number, name: string, actor_id: number, usecase_id: number
) {
  return request(`usecases/event/${id}/`, {
    'method': 'PUT',
    'data': {name: name, actor_id: actor_id, usecase: usecase_id}})
}

export function deleteEvent(id: number) {
  return request(`usecases/event/${id}/`, {'method': 'DELETE'})
}

// Steps
export function createStep(system: boolean, description: string, event_id: number) {
  return request('usecases/step/', {
    'method': 'POST',
    'data': {system: system, description: description, event: event_id}})
}

export function updateStep(
  id: number, system: boolean, description: string, event_id: number
) {
  return request(`usecases/step/${id}/`, {
    'method': 'PUT',
    'data': {system: system, description: description, event: event_id}})
}

export function deleteStep(id: number) {
  return request(`usecases/step/${id}/`, {'method': 'DELETE'})
}