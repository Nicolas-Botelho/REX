import request from './api'

export async function getNarrative() {
  try {
    return await request('narrative/narrative/', {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function putNarrative(narrative: string) {
  try {
    return await request('narrative/narrative/', {'method': 'PUT', 'data':{'narrative': narrative}})
  } catch(error) {
    throw error
  }
}

export async function deleteNarrative() {
  try {
    return await request('narrative/narrative/', {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

export async function getNarrativeQuestions() {
  try {
    return await request('narrative/questions/', {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function postNarrativeQuestion(question: string) {
  try {
    return await request('narrative/questions/', {'method': 'POST', 'data': {'question': question}})
  } catch (error) {
    throw error
  }
}

export async function putNarrativeQuestion(q_id: number, question: string) {
  try {
    return await request(`narrative/questions/${encodeURIComponent(q_id)}/`, {'method': 'PUT', 'data': {'question': question}})
  } catch (error) {
    throw error
  }
}

export async function deleteNarrativeQuestion(q_id: number) {
  try {
    return await request(`narrative/questions/${encodeURIComponent(q_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}