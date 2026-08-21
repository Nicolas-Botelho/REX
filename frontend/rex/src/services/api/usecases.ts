import type { Usecase } from '@/models/usecase_models'
import request from './api'
import type { UsecaseQuestion } from '@/models/question_models'

///////////////
// Use Cases //
///////////////

export async function getUseCases() {
  try {
    return await request('usecases/usecase/', {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function getUseCase(uc_id: number) {
  try {
    return await request(`usecases/usecase/${encodeURIComponent(uc_id)}/`, {'method': 'GET'})  
  }
  catch (error) {
    throw error
  }
}

export async function postUseCase(usecase: Usecase) {
  try {
    return await request('usecases/usecase/', {'method': 'POST', 'data': usecase})
  } catch (error) {
    throw error
  }
}

export async function putUseCase(uc_id: number, usecase: Usecase) {
  try {
    return request(`usecases/usecase/${encodeURIComponent(uc_id)}/`, {'method': 'PUT', 'data': usecase})
  } catch (error) {
    throw error
  }
}

export async function deleteUseCase(uc_id: number) {
  try {
    return await request(`usecases/usecase/${encodeURIComponent(uc_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

//////////////
// Question //
//////////////

export async function getUsecaseQuestions() {
  try {
    return await request('usecases/questions', {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function postUsecaseQuestion(question: UsecaseQuestion) {
  try {
    return await request('usecases/questions', {'method': 'POST', 'data': {'question': question.question, 'usecase_names': question.usecase_names}})
  } catch (error) {
    throw error
  }
}

export async function putUsecaseQuestion(q_id: number, question: UsecaseQuestion) {
  try {
    return await request(`usecases/questions/${encodeURIComponent(q_id)}`, {'method': 'PUT', 'data': {'question': question.question, 'usecase_names': question.usecase_names}})
  } catch (error) {
    throw error
  }
}

export async function deleteUsecaseQuestion(q_id: number) {
  try {
    return await request(`usecases/questions/${encodeURIComponent(q_id)}`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}