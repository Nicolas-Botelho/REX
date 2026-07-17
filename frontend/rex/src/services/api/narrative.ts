import request from './api'

export function getNarrative() {
  return request('narrative/narrative', {'method': 'GET'})
}