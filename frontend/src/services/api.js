import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000',
  timeout: 300000,
})

export const getHealth = async () => {
  const response = await api.get('/')
  return response.data
}

export const runWorkflow = async () => {
  const response = await api.get('/workflow/test')
  return response.data
}

export const analyzeBusiness = async () => {
  return runWorkflow()
}
