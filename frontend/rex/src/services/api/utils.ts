import request from './api'

export async function generateAll(project_id: number, text_input: string) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/ai/run_all/`, {'method': 'POST', 'data': {input_text: text_input}})
  }
  catch (error) {
    throw error
  }
}

export async function generateFromRQ(project_id: number, text_input: string) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/ai/run_all/?start_from=1`, {'method': 'POST', 'data': {input_text: text_input}})
  } catch (error) {
    throw error
  }
}

export async function generateFromUC(project_id: number, text_input: string) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/ai/run_all/?start_from=2`, {'method': 'POST', 'data': {input_text: text_input}})
  } catch (error) {
    throw error
  }
}

export async function generateFromCL(project_id: number, text_input: string) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/ai/run_all/?start_from=3`, {'method': 'POST', 'data': {input_text: text_input}})
  } catch (error) {
    throw error
  }
}

export async function generateJson(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/json/`, {method: 'GET'})
  }
  catch (error) {
    throw error
  }
}

export async function importJson(project_id: number, data: any) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/manual_update/`, {'method': 'POST', 'data': data})
  }
  catch (error) {
    throw error
  }
}

export async function getNarrativeMd(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/document/narrative/`, {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function getRequirementMd(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/document/requirements/`, {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function getUsecaseMd(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/document/usecase/`, {'method': 'GET'})
  } catch (error) {
    throw error
  }
}

export async function getClassMd(project_id: number) {
  try {
    return await request(`project/${encodeURIComponent(project_id)}/document/class/`, {'method': 'GET'})
  } catch (error) {
    throw error
  }
}