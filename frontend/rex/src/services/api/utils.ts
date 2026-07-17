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