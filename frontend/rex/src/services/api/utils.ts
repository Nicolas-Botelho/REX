import request from './api'

export async function generateAll(text_input: string) {
  try {
    return await request('ai/run_all/', {method: 'POST', data: {input_text: text_input}})
  }
  catch (error) {
    throw error
  }
}

export async function generateJson() {
  try {
    return await request('json/', {method: 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function importJson(data: any) {
  try {
    return await request('manual_update/', {'method': 'POST', 'data': data})
  }
  catch (error) {
    throw error
  }
}

export async function getNarrativeMd() {
  try {
    return await request('document/narrative/', {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function getRequirementMd() {
  try {
    return await request('document/requirements/', {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function getUsecaseMd() {
  try {
    return await request('document/usecase/', {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function getClassMd() {
  try {
    return await request('document/class/', {'method': 'GET'})
  } catch (error) {
    throw error
  }
}