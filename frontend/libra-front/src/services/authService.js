import axios from "axios";
// import { getCSRFToken } from './getCSRFToken';
// function getCSRFToken() {
//   const cookies = document.cookie.split(';');
//   for (let cookie of cookies) {
//     const [name, value] = cookie.trim().split('=');
//     if (name === 'csrftoken') return value;
//   }
//   return '';
// }

function getCSRFToken() {
  const csrfToken = document.cookie
    .split('; ')
    .find((row) => row.startsWith('csrftoken='))
    ?.split('=')[1];

  if (!csrfToken) {
    console.warn('CSRFトークンが見つかりません。');
  }
  return csrfToken || '';
}


export async function  login(email, password) {
    try {
        const csrfToken = getCSRFToken();
        const response = await axios.post('http://localhost:8000/api/auth/login/', 
            {email, password},
            {
                headers: {
                    'Content-Type': "application/json",
                    'X-CSRFToken': csrfToken,
                },
                withCredentials: true,
            },
        );
        console.log("Login Success: ", response.data);
        if (response.data && response.data.key) {
          localStorage.setItem('token', response.data.key)
          return response.data;
        } else {
          throw new Error('Tokenが見つかりません。レスポンスを確認してください。')
        }
    } catch (error) {
        console.error("Login Error: ", error.response || error.message);
        throw error
    }
}
export async function register(email, username, password1, password2) {
  try{
    const csrfToken = getCSRFToken();
    const response = await axios.post('http://localhost:8000/api/auth/registration/', 
      {email, username, password1, password2},
      {
        headers: {
          "Content-Type": "application/json",
          'X-CSRFToken': csrfToken,
        },
        withCredentials: true,
      },
    );
    console.log("Register Response: ", response.data);
    if (response.data &&  response.data.key) {
      localStorage.setItem('token', response.data.key); // トークンを保存
      return response.data;
    } else{
      throw new Error("Tokenが見つかりません。レスポンスを確認してください。");
    }
  } catch(error) {
    console.error("Register Error: ", error.response || error.message);
    throw error
  }
}

export async function refreshToken() {
  try {
    const response = await axios.post('http://localhost:8000/api/auth/refresh/', {
      refresh: localStorage.getItem('refresh_token'),
    });

    const newAccessToken = response.data.access;
    localStorage.setItem('token', newAccessToken);
    console.log('トークンが正常にリフレッシュされました:', newAccessToken);
    return newAccessToken;
  } catch (error) {
    console.error('トークンのリフレッシュに失敗しました:', error.response || error.message);
    throw error;
  }
}


export async function logout() {
  try {
    const csrfToken = getCSRFToken();
    const response = await axios.post("http://localhost:8000/api/auth/logout/", 
      {},
      {
        headers: {
          "Content-Type": "application/json",
          'X-CSRFToken': csrfToken,
          Authorization: `Token ${localStorage.getItem('token')}`,
        },
        withCredentials: true,
      },
    );
    console.log("Logout Success: ", response.data);
    localStorage.removeItem("token");
    localStorage.removeItem("refresh_token");
  } catch(error){
    console.log("Logout Error: ", error.response || error.message);
    throw error;
  }
}
export async function HelloWorld(message) {
  try {
    const csrfToken = getCSRFToken();
    const response = await axios.get("http://localhost:8000/api/hello/", 
      {message},
      {
        headers: {
          'Content-Type': "application/json",
          'X-CSRFToken': csrfToken,
        },
        withCredentials: true,
      },
    );
    console.log('APIの認証: ', response.data);
    return response.data;
  } catch(error) {
    console.error("APIの接続に失敗しました。", error.response || error.message);
    throw error;
  }
}

export async function searchBooks(query){
  try{
    const csrfToken = getCSRFToken();
    const response = await axios.get('http://localhost:8000/api/search/',
      {q: query},
      {
        params: { q: query },
        headers: {
          'Content-Type': "application/json",
          'X-CSRFToken': csrfToken,
          Authorization: `Token ${localStorage.getItem('token')}`, 
        },
        withCredentials: true,
      },
    );
    console.log('検索結果:', response.data);
    return response.data;
  } catch(error){
    console.error("検索に失敗しました。", error.response || error.message);
    throw error;
  }
}