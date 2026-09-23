import { Association, Class, Inheritance } from '@/models/class_models'
import request from './api'
import type { ClassQuestion } from '@/models/question_models'

/////////////
// Classes //
/////////////

export async function getClasses(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/class/`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function getClass(project_id: number, id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/class/${id}/`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function getClassByName(project_id: number, name: string) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/class_by_name?class_name=${encodeURIComponent(name)}`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function postClass(project_id: number, cls: Class) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/class/`, {'method': 'POST', 'data': cls})
  } catch (error) {
    throw error
  }
}

export async function putClass(project_id: number, cls_id: number, cls: Class) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/class/${cls_id}/`, {'method': 'PUT', 'data': cls})
  } catch (error) {
    throw error
  }
}

export async function deleteClass(project_id: number, cls_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/class/${cls_id}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

/////////////////
// Association //
/////////////////

export async function getClassAssociations(project_id: number, name: string) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/class_associations?class_name=${encodeURIComponent(name)}`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function postAssociation(project_id: number, assoc: Association) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/association/`, {'method': 'POST', 'data': assoc})
  } catch (error) {
    throw error
  }
}

export async function putAssociation(project_id: number, assoc_id: number, assoc: Association) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/association/${encodeURIComponent(assoc_id)}/`, {'method': 'PUT', 'data': assoc})
  } catch (error) {
    throw error
  }
}

export async function deleteAssociation(project_id: number, assoc_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/association/${encodeURIComponent(assoc_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

/////////////////
// Inheritance //
/////////////////

export async function getClassInheritances(project_id: number, name: string) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/class_inheritances?class_name=${encodeURIComponent(name)}`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function postInheritance(project_id: number, inher: Inheritance) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/inheritance/`, {'method': 'POST', 'data': inher})
  } catch (error) {
    throw error
  }
}

export async function putInheritance(project_id: number, inher_id: number, inher: Inheritance) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/inheritance/${encodeURIComponent(inher_id)}/`, {'method': 'PUT', 'data': inher})
  } catch (error) {
    throw error
  }
}

export async function deleteInheritance(project_id: number, inher_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/inheritance/${encodeURIComponent(inher_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

//////////////
// Question //
//////////////

export async function getClassQuestions(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/questions`, {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function postClassQuestion(project_id: number, question: ClassQuestion) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/questions`, {'method': 'POST', 'data': {'question': question.question, 'class_names': question.class_names}})
  } catch (error) {
    throw error
  }
}

export async function putClassQuestion(project_id: number, q_id: number, question: ClassQuestion) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/questions/${encodeURIComponent(q_id)}`, {'method': 'PUT', 'data': {'question': question.question, 'class_names': question.class_names}})
  } catch (error) {
    throw error
  }
}

export async function deleteClassQuestion(project_id: number, q_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/classes/questions/${encodeURIComponent(q_id)}`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}