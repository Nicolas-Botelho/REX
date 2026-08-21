import type { BusinessRule, FunctionalRequirement, NonFunctionalRequirement } from '@/models/requirement_models'
import request from './api'
import type { RequirementQuestion } from '@/models/question_models'

////////////////////////////
// Functional Requirement //
////////////////////////////

export async function getFRs() {
  try {
    return await request('requirements/functional_requirement/', {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function postFR(fr: FunctionalRequirement) {
  try {
    return await request('requirements/functional_requirement/', {'method': 'POST', 'data': fr})
  } catch (error) {
    throw error
  }
}

export async function putFR(fr_id: number, fr: FunctionalRequirement) {
  try {
    return await request(`requirements/functional_requirement/${encodeURIComponent(fr_id)}/`, {'method': 'PUT', 'data': fr})
  } catch (error) {
    throw error
  }
}

export async function deleteFR(fr_id: number) {
  try {
    return await request(`requirements/functional_requirement/${encodeURIComponent(fr_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

////////////////////////////////
// Non Functional Requirement //
////////////////////////////////

export async function getNFRs() {
  try {
    return await request('requirements/non_functional_requirement/', {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function postNFR(nfr: NonFunctionalRequirement) {
  try {
    return await request('requirements/non_functional_requirement/', {'method': 'POST', 'data': nfr})
  } catch (error) {
    throw error
  }
}

export async function putNFR(nfr_id: number, nfr: NonFunctionalRequirement) {
  try {
    return await request(`requirements/non_functional_requirement/${encodeURIComponent(nfr_id)}/`, {'method': 'PUT', 'data': nfr})
  } catch (error) {
    throw error
  }
}

export async function deleteNFR(nfr_id: number) {
  try {
    return await request(`requirements/non_functional_requirement/${encodeURIComponent(nfr_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

///////////////////
// Business Rule //
///////////////////

export async function getBRs() {
  try {
    return await request('requirements/business_rule/', {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function postBR(br: BusinessRule) {
  try {
    return await request('requirements/business_rule/', {'method': 'POST', 'data': br})
  } catch (error) {
    throw error
  }
}

export async function putBR(br_id: number, br: BusinessRule) {
  try {
    return await request(`requirements/business_rule/${encodeURIComponent(br_id)}/`, {'method': 'PUT', 'data': br})
  } catch (error) {
    throw error
  }
}

export async function deleteBR(br_id: number) {
  try {
    return await request(`requirements/business_rule/${encodeURIComponent(br_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

//////////////
// Question //
//////////////

export async function getRequirementQuestions() {
  try {
    return await request('requirements/questions', {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function postRequirementQuestion(question: RequirementQuestion) {
  try {
    return await request('requirements/questions', {'method': 'POST', 'data': {'question': question.question, 'requirement_codes': question.requirement_codes}})
  } catch (error) {
    throw error
  }
}

export async function putRequirementQuestion(q_id: number, question: RequirementQuestion) {
  try {
    return await request(`requirements/questions/${encodeURIComponent(q_id)}`, {'method': 'PUT', 'data': {'question': question.question, 'requirement_codes': question.requirement_codes}})
  } catch (error) {
    throw error
  }
}

export async function deleteRequirementQuestion(q_id: number) {
  try {
    return await request(`requirements/questions/${encodeURIComponent(q_id)}`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}