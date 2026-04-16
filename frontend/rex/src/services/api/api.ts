const BASE_URL = 'http://localhost:8000/'

async function request(endpoint: string, { method = 'GET', headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}, data = null }: { method?: string, headers?: any, data?: any }) {
  const url = `${BASE_URL}${endpoint}`

  try {
    const response = await fetch(url, {
        'method': method,
        'headers': headers,
        ...(data && { 'body': JSON.stringify(data) })
      })

    if (!response.ok) {
      const errorData = await response.json().catch(() => null)
      throw new Error(errorData?.message || 'API error')
    }

    if (method == 'DELETE') {
      return
    }
    else {
      return await response.json()
    }
  } catch (error) {
    console.error('API request failed:', error)
    throw error
  }
}

export default request