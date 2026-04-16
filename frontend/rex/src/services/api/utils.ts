import request from './api'

export function generateAll(text_input: string) {
  return request('ai/run_all/', {method: 'POST', data: {input_text: text_input}})
}

export function generateJson() {
  return request('json/json_generate', {method: 'GET'})
}