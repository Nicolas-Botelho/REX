import request from './api'
import { Actor } from '@/models/requirement_models'

export async function getActors() {
  try {
    return await request('actor/actor/', {'method': 'GET'})    
  } catch (error) {
    throw error
  }
}

export async function postActor(actor: Actor) {
  try {
    return await request('actor/actor/', {'method': 'POST', 'data': actor})    
  } catch (error) {
    throw error
  }
}

export async function putActor(ac_id: number, actor: Actor) {
  try {
    return await request(`actor/actor/${encodeURIComponent(ac_id)}/`, {'method': 'PUT', 'data': actor})    
  } catch (error) {
    throw error
  }
}

export async function deleteActor(ac_id: number) {
  try {
    return await request(`actor/actor/${encodeURIComponent(ac_id)}/`, {'method': 'DELETE'})    
  } catch (error) {
    throw error
  }
}