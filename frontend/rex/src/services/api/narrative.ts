import request from './api'

export async function getNarrative(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/narrative/narrative/`, {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function putNarrative(project_id: number, narrative: string) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/narrative/narrative/`, {'method': 'PUT', 'data':{'narrative': narrative}})
  } catch(error) {
    throw error
  }
}

export async function deleteNarrative(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/narrative/narrative/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

export async function getNarrativeQuestions(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/narrative/questions/`, {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function postNarrativeQuestion(project_id: number, question: string) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/narrative/questions/`, {'method': 'POST', 'data': {'question': question}})
  } catch (error) {
    throw error
  }
}

export async function putNarrativeQuestion(project_id: number, q_id: number, question: string) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/narrative/questions/${encodeURIComponent(q_id)}/`, {'method': 'PUT', 'data': {'question': question}})
  } catch (error) {
    throw error
  }
}

export async function deleteNarrativeQuestion(project_id: number, q_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/narrative/questions/${encodeURIComponent(q_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}