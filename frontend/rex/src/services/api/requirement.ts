import request from './api'

export async function getRequirements() {
  try {
    return await request('requirements/requirement', {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function getFRs() {
  try {
    return await request('requirements/functional_requirement', {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function getNFRs() {
  try {
    return await request('requirements/non_functional_requirement', {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function getBRs() {
  try {
    return await request('requirements/business_rule', {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}