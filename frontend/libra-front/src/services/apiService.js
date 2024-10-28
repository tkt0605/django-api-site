// /src/services/authService.js

import axios from 'axios';

export async function login(email, password) {
  try {
    const response = await axios.post('http://localhost:8000/api/auth/login/', {
      email,
      password,
    });
    const { key } = response.data; // Django Rest Authが返すキー

    localStorage.setItem('authToken', key);
    console.log('Login Success:', key);
    return response.data;
  } catch (error) {
    console.error('Login Error:', error.response || error.message);
    throw error;
  }
}

export async function refreshToken() {
  try {
    const response = await axios.post('http://localhost:8000/api/auth/refresh/', {
      refresh: localStorage.getItem('refresh_token'),
    });

    const newAccessToken = response.data.access;
    localStorage.setItem('authToken', newAccessToken);
    console.log('トークンが正常にリフレッシュされました:', newAccessToken);
    return newAccessToken;
  } catch (error) {
    console.error('トークンのリフレッシュに失敗しました:', error.response || error.message);
    throw error;
  }
}

export async function logout() {
  try {
    await axios.post('http://localhost:8000/api/auth/logout/', {}, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('authToken')}`,
      },
      withCredentials: true,
    });

    localStorage.removeItem('authToken');
    localStorage.removeItem('refresh_token');
    console.log('Logout Successful');
  } catch (error) {
    console.error('Logout Error:', error.response || error.message);
    throw error;
  }
}
