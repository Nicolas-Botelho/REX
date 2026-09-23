import type { Usecase } from '@/models/usecase_models'
import request from './api'
import type { UsecaseQuestion } from '@/models/question_models'

///////////////
// Use Cases //
///////////////

export async function getUseCases(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/usecases/usecase/`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function getUseCase(project_id: number, uc_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/usecases/usecase/${encodeURIComponent(uc_id)}/`, {'method': 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function postUseCase(project_id: number, usecase: Usecase) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/usecases/usecase/`, {'method': 'POST', 'data': usecase})
  } catch (error) {
    throw error
  }
}

export async function putUseCase(project_id: number, uc_id: number, usecase: Usecase) {
  try {
    return request(`project/${encodeURIComponent(project_id)}/usecases/usecase/${encodeURIComponent(uc_id)}/`, {'method': 'PUT', 'data': usecase})
  } catch (error) {
    throw error
  }
}

export async function deleteUseCase(project_id: number, uc_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/usecases/usecase/${encodeURIComponent(uc_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}

//////////////
// Question //
//////////////

export async function getUsecaseQuestions(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/usecases/questions`, {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function postUsecaseQuestion(project_id: number, question: UsecaseQuestion) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/usecases/questions`, {'method': 'POST', 'data': {'question': question.question, 'usecase_names': question.usecase_names}})
  } catch (error) {
    throw error
  }
}

export async function putUsecaseQuestion(project_id: number, q_id: number, question: UsecaseQuestion) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/usecases/questions/${encodeURIComponent(q_id)}`, {'method': 'PUT', 'data': {'question': question.question, 'usecase_names': question.usecase_names}})
  } catch (error) {
    throw error
  }
}

export async function deleteUsecaseQuestion(project_id: number, q_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/usecases/questions/${encodeURIComponent(q_id)}`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}