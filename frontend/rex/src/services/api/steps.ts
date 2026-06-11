import request from './api'

// Step
export function getStep(id: number) {
  return request(`usecases/step/${id}/`, {'method': 'GET'})
}

export function deleteStep(id: number) {
  return request(`usecases/step/${id}/`, {'method': 'DELETE'})
}

// Action
export function createAction(description: string, next_step: number) {
  return request('usecases/action/', {
    'method': 'POST',
    'data': {description: description, next_step: next_step}})
}

export function updateAction(
  id: number, description: string, next_step: number
) {
  return request(`usecases/action/${id}/`, {
    'method': 'PUT',
    'data': {description: description, next_step: next_step}})
}

// Decision
export function createDecision(description: string, next_steps: [number]) {
  return request('usecases/decision/', {
    'method': 'POST',
    'data': {description: description, next_steps: next_steps}})
}

export function updateDecison(
  id: number, description: string, next_steps: [number]
) {
  return request(`usecases/decision/${id}/`, {
    'method': 'PUT',
    'data': {description: description, next_steps: next_steps}})
}

// Modify Action
export function createModifyAction(description: string, next_step: number, action_type: string, related_classes: [number]) {
  return request('usecases/modify_action/', {
    'method': 'POST',
    'data': {description: description, next_step: next_step, action_type: action_type, related_classes: related_classes}})
}

export function updateModifyAction(
  id: number, description: string, next_step: number, action_type: string, related_classes: [number]
) {
  return request(`usecases/modify_action/${id}/`, {
    'method': 'PUT',
    'data': {description: description, next_step: next_step, action_type: action_type, related_classes: related_classes}})
}

// Read Action
export function createReadAction(description: string, next_step: number, action_type: string, related_classes: [number], read_attributes: [number]) {
  return request('usecases/read_action/', {
    'method': 'POST',
    'data': {description: description, next_step: next_step, action_type: action_type, related_classes: related_classes, read_attributes_id: read_attributes}})
}

export function updateReadAction(
  id: number, description: string, next_step: number, action_type: string, related_classes: [number], read_attributes: [number]
) {
  return request(`usecases/read_action/${id}/`, {
    'method': 'PUT',
    'data': {description: description, next_step: next_step, action_type: action_type, related_classes: related_classes, read_attributes_id: read_attributes}})
}

// Text Read Action
export function createTextReadAction(description: string, next_step: number, action_type: string, related_classes: [number], read_attributes: [number], match_percent: number) {
  return request('usecases/text_read_action/', {
    'method': 'POST',
    'data': {description: description, next_step: next_step, action_type: action_type, related_classes: related_classes, read_attributes_id: read_attributes, match_percent: match_percent}})
}

export function updateTextReadAction(
  id: number, description: string, next_step: number, action_type: string, related_classes: [number], read_attributes: [number], match_percent: number
) {
  return request(`usecases/text_read_action/${id}/`, {
    'method': 'PUT',
    'data': {description: description, next_step: next_step, action_type: action_type, related_classes: related_classes, read_attributes_id: read_attributes, match_percent: match_percent}})
}