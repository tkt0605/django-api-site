import axios from "axios";
const API_URL = 'http://localhost:8000/api/auth/';
export async function refreshToken() {
  const refreshToken = localStorage.getItem('refresh_token');
  try{
    const response = await axios.post(`${API_URL}token/refresh/`, {
      refresh: refreshToken,
    });
    const newAccessToken = response.data.access;
    localStorage.setItem('token', newAccessToken);
    return newAccessToken;
  }catch(error){
    console.error("Error Create NewAccessToken:", error.message);
    return null;
  }
}
export async function searchBooks(query){
  try{
    const response = await axios.get('http://localhost:8000/api/search/',
      {
        params: { q: query },
        headers: {
          'Content-Type': "application/json",
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

//新規アカウント作成のコード
// export async function register(username, email, password1, password2) {
//   try{
//     const response =  await axios.post('http://localhost:8000/api/accounts/register/', {
//       emial: email,
//       username: username,
//       password1: password1,
//       password2: password2,
//     });
//     return response.data;
//   } catch (error) {
//     console.error('Register Error:', error.message);
//   }
// }
export async function register({email, username, password}) {
  try{
    const response = await axios.post('http://localhost:8000/api/accounts/register/', {
      email: email,
      username: username,
      password: password,
    },{
      headers: {
        'Content-Type': 'application/json'  // JSON形式でデータを送信
      }
    });
    return response.data;
  }catch(error){
    console.error("Register Error:",  error.response?.data);
    throw error; // エラーを上位に伝搬
  }
}
export async function login(email, password) {
  try{
    const response = await axios.post('http://localhost:8000/api/accounts/login/', {
      email: email,
      password: password
    });
    console.log("Login Response:", response.data);
    if (response.data.access &&  response.data.refresh){
      localStorage.setItem('token', response.data.access);
      localStorage.setItem('refresh_token', response.data.refresh);
      axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
      return response.data
    }
  } catch (error){
    console.error("Login Error", error.message);
  }
}

export async function logout() {
  try {
    const refreshToken = localStorage.getItem('refresh_token');  // refresh_tokenを取得
    if (!refreshToken) {
      console.error("No refresh token found");
      return;
    }

    const response = await axios.post(
      'http://localhost:8000/api/accounts/logout/',
      { refresh: refreshToken },  // refreshトークンをリクエストボディに追加
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      }
    );

    localStorage.removeItem('token');
    localStorage.removeItem('refresh_token');
    delete axios.defaults.headers.common['Authorization'];
    return response.data;
  } catch (error) {
    console.error("Logout Error:", error.message);
  }
}


export async function fetchUser() {
  const token = localStorage.getItem('token'); // ログイン時に保存したJWTトークンを取得
  try {
      const response = await axios.get('http://localhost:8000/api/users/', {
          headers: {
              Authorization: `Bearer ${token}`,
          },
          withCredentials: true,
      });
      return response.data;
  } catch (error) {
      console.error("ユーザー情報の取得に失敗しました:", error);
      throw error;
  }
}