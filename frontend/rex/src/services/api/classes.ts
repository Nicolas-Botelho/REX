import { Association, Class, Inheritance } from '@/models/class_models'
import request from './api'
import type { ClassQuestion } from '@/models/question_models'

/////////////
// Classes //
/////////////

export async function getClasses() {
  try {
    return await request('classes/class/', {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function getClass(id: number) {
  try {
    return await request(`classes/class/${id}/`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function getClassByName(name: string) {
  try {
    return await request(`classes/class_by_name?class_name=${encodeURIComponent(name)}`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function postClass(cls: Class) {
  try {
    return await request('classes/class/', {'method': 'POST', 'data': cls})
  } catch (error) {
    throw error
  }
}

export async function putClass(cls_id: number, cls: Class) {
  try {
    return await request(`classes/class/${cls_id}/`, {'method': 'PUT', 'data': cls})
  } catch (error) {
    throw error
  }
}

export async function deleteClass(cls_id: number) {
  try {
    return await request(`classes/class/${cls_id}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

/////////////////
// Association //
/////////////////

export async function getClassAssociations(name: string) {
  try {
    return await request(`classes/class_associations?class_name=${encodeURIComponent(name)}`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function postAssociation(assoc: Association) {
  try {
    return await request('classes/association/', {'method': 'POST', 'data': assoc})
  } catch (error) {
    throw error
  }
}

export async function putAssociation(assoc_id: number, assoc: Association) {
  try {
    return await request(`classes/association/${encodeURIComponent(assoc_id)}/`, {'method': 'PUT', 'data': assoc})    
  } catch (error) {
    throw error
  }
}

export async function deleteAssociation(assoc_id: number) {
  try {
    return await request(`classes/association/${encodeURIComponent(assoc_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

/////////////////
// Inheritance //
/////////////////

export async function getClassInheritances(name: string) {
  try {
    return await request(`classes/class_inheritances?class_name=${encodeURIComponent(name)}`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function postInheritance(inher: Inheritance) {
  try {
    return await request('classes/inheritance/', {'method': 'POST', 'data': inher})
  } catch (error) {
    throw error
  }
}

export async function putInheritance(inher_id: number, inher: Inheritance) {
  try {
    return await request(`classes/inheritance/${encodeURIComponent(inher_id)}/`, {'method': 'PUT', 'data': inher})    
  } catch (error) {
    throw error
  }
}

export async function deleteInheritance(inher_id: number) {
  try {
    return await request(`classes/inheritance/${encodeURIComponent(inher_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

//////////////
// Question //
//////////////

export async function getClassQuestions() {
  try {
    return await request('classes/questions', {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function postClassQuestion(question: ClassQuestion) {
  try {
    return await request('classes/questions', {'method': 'POST', 'data': {'question': question.question, 'class_names': question.class_names}})
  } catch (error) {
    throw error
  }
}

export async function putClassQuestion(q_id: number, question: ClassQuestion) {
  try {
    return await request(`classes/questions/${encodeURIComponent(q_id)}`, {'method': 'PUT', 'data': {'question': question.question, 'class_names': question.class_names}})
  } catch (error) {
    throw error
  }
}

export async function deleteClassQuestion(q_id: number) {
  try {
    return await request(`classes/questions/${encodeURIComponent(q_id)}`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}