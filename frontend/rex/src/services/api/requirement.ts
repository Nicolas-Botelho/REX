import type { BusinessRule, FunctionalRequirement, NonFunctionalRequirement } from '@/models/requirement_models'
import request from './api'
import type { RequirementQuestion } from '@/models/question_models'

////////////////////////////
// Functional Requirement //
////////////////////////////

export async function getFRs(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/functional_requirement/`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function postFR(project_id: number, fr: FunctionalRequirement) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/functional_requirement/`, {'method': 'POST', 'data': fr})
  } catch (error) {
    throw error
  }
}

export async function putFR(project_id: number, fr_id: number, fr: FunctionalRequirement) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/functional_requirement/${encodeURIComponent(fr_id)}/`, {'method': 'PUT', 'data': fr})
  } catch (error) {
    throw error
  }
}

export async function deleteFR(project_id: number, fr_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/functional_requirement/${encodeURIComponent(fr_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

////////////////////////////////
// Non Functional Requirement //
////////////////////////////////

export async function getNFRs(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/non_functional_requirement/`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function postNFR(project_id: number, nfr: NonFunctionalRequirement) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/non_functional_requirement/`, {'method': 'POST', 'data': nfr})
  } catch (error) {
    throw error
  }
}

export async function putNFR(project_id: number, nfr_id: number, nfr: NonFunctionalRequirement) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/non_functional_requirement/${encodeURIComponent(nfr_id)}/`, {'method': 'PUT', 'data': nfr})
  } catch (error) {
    throw error
  }
}

export async function deleteNFR(project_id: number, nfr_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/non_functional_requirement/${encodeURIComponent(nfr_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

///////////////////
// Business Rule //
///////////////////

export async function getBRs(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/business_rule/`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function postBR(project_id: number, br: BusinessRule) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/business_rule/`, {'method': 'POST', 'data': br})
  } catch (error) {
    throw error
  }
}

export async function putBR(project_id: number, br_id: number, br: BusinessRule) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/business_rule/${encodeURIComponent(br_id)}/`, {'method': 'PUT', 'data': br})
  } catch (error) {
    throw error
  }
}

export async function deleteBR(project_id: number, br_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/business_rule/${encodeURIComponent(br_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

//////////////
// Question //
//////////////

export async function getRequirementQuestions(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/questions`, {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function postRequirementQuestion(project_id: number, question: RequirementQuestion) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/questions`, {'method': 'POST', 'data': {'question': question.question, 'requirement_codes': question.requirement_codes}})
  } catch (error) {
    throw error
  }
}

export async function putRequirementQuestion(project_id: number, q_id: number, question: RequirementQuestion) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/questions/${encodeURIComponent(q_id)}`, {'method': 'PUT', 'data': {'question': question.question, 'requirement_codes': question.requirement_codes}})
  } catch (error) {
    throw error
  }
}

export async function deleteRequirementQuestion(project_id: number, q_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/requirements/questions/${encodeURIComponent(q_id)}`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}