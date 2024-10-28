import axios from "axios";
// function getCSRFToken() {
//     const value = `; ${document.cookie}`;
//     const parts = value.split(`; csrftoken=`);
//     if (parts.length === 2) return parts.pop().split(';').shift();
// }
function getCSRFToken() {
  const cookies = document.cookie.split(';');
  for (let cookie of cookies) {
    const [name, value] = cookie.trim().split('=');
    if (name === 'csrftoken') return value;
  }
  return '';
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
        console.log('Login Response:', response.data);  // レスポンスを確認
        if (response.data && response.data.key) {
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
    const response = await axios.post('http://localhost:8000/api/auth/login/', 
      {email, username, password1, password2},
      {
        headers: {
          "Content-Type": "application/json",
          'X-CSRFToken': csrfToken,
        },
        withCredentials: true,
      },
    );
    console.log('Register Success: ', response.data);
    console.log("Register Response: ", response.data);
    if (response.data && response.data.access && response.key) {
      return response.data && response.key;
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

    // 新しいアクセストークンを保存
    localStorage.setItem('token', response.data.access);
    return response.data.access;
  } catch (error) {
    console.error('トークンのリフレッシュに失敗しました:', error);
    
    // トークンが無効な場合、ログアウト処理
    localStorage.removeItem('token');
    localStorage.removeItem('refresh_token');
    window.location.href = '/login';  // ログイン画面にリダイレクト
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
