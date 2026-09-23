import type { Project } from "@/models/project_models"
import request from "./api"

export async function getProjects() {
  try {
    return request(`project/project/`, {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function getProject(project_id: number) {
  try {
    return request(`project/project/${encodeURIComponent(project_id)}/`, {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function postProject(project: Project) {
  try {
    return request(`project/project/`, {'method': 'POST', 'data': project})
  } catch (error) {
    throw error
  }
}

export async function putProject(project_id: number, project: Project) {
  try {
    return request(`project/project/${encodeURIComponent(project_id)}/`, {'method': 'PUT', 'data': project})
  } catch (error) {
    throw error
  }
}

export async function deleteProject(project_id: number) {
  try {
    return request(`project/project/${encodeURIComponent(project_id)}/`, {'method': 'DELETE'})
  } catch (error) {
    throw error
  }
}