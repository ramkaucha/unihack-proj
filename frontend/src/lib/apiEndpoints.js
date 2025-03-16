export const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL;

export const AUTH_ENDPOINTS = {
  LOGIN: `${API_BASE_URL}/user/login`,
  REGISTER: `${API_BASE_URL}/user/register`,
  LOGOUT: '/logout',
  RESET_PASSWORD: '/reset-password'
}

