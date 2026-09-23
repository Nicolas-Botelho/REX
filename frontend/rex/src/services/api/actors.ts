import request from './api'
import { Actor } from '@/models/requirement_models'

export async function getActors(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/actor/actor/`, {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function getFRByActor(project_id: number, actor: string) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/actor/fr_by_actor/?name=${encodeURIComponent(actor)}`, {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function getUcByActor(project_id: number, actor: string) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/actor/uc_by_actor/?name=${encodeURIComponent(actor)}`, {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function postActor(project_id: number, actor: Actor) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/actor/actor/`, {'method': 'POST', 'data': actor})
  } catch (error) {
    throw error
  }
}

export async function putActor(project_id: number, ac_id: number, actor: Actor) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/actor/actor/${encodeURIComponent(ac_id)}/`, {'method': 'PUT', 'data': actor})
  } catch (error) {
    throw error
  }
}

export async function deleteActor(project_id: number, ac_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/actor/actor/${encodeURIComponent(ac_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}