import axios from "axios";
import store from "@/store"
// const API_URL = 'http://localhost:8000/api/auth/';
// export async function refreshToken() {
//   const refreshToken = localStorage.getItem('refresh_token');
//   try{
//     const response = await axios.post(`${API_URL}token/refresh/`, {
//       refresh: refreshToken,
//     });
//     const newAccessToken = response.data.access;
//     localStorage.setItem('token', newAccessToken);
//     return newAccessToken;
//   }catch(error){
//     console.error("Error Create NewAccessToken:", error.message);
//     return null;
//   }
// }
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
    const { access, refresh } = response.data;
    if (access &&  refresh){
      localStorage.setItem('token', access);
      localStorage.setItem('refresh_token', refresh);
      axios.defaults.headers.common['Authorization'] = `Bearer ${access}`;
      console.log("Token stored and Authorization header set.");
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


// export async function fetchUser() {
//   const token = localStorage.getItem('token'); // ログイン時に保存したJWTトークンを取得
//   try {
//       const response = await axios.get('http://localhost:8000/api/accounts/profile/', {
//           headers: {
//               Authorization: `Bearer ${token}`,
//           },
//           withCredentials: true,
//       });
//       console.log("fetchUser response: ", response.data);
//       return response.data;
//   } catch (error) {
//       console.error("ユーザー情報の取得に失敗しました:", error);
//       throw error;
//   }
// }
export async function fetchUser() {
  try {
    const response = await axios.get("http://localhost:8000/api/accounts/profile/", {
      headers: {
        Authorization: `Bearer ${store.state.authToken}`
      }
    });
    return response.data;
  } catch (error) {
    if (error.response && error.response.status === 401) {
      console.log("認証エラー: トークンをリフレッシュします。");
      await refreshToken(); // リフレッシュ関数の呼び出し
      return fetchUser();   // リフレッシュ後に再リクエスト
    } else {
      console.error("Fetch User Error:", error);
    }
  }
}

// export async function refreshToken() {
//   const refreshToken = localStorage.getItem('refresh_token');  // リフレッシュトークンを取得
//   if (refreshToken) {
//     try {
//       const response = await axios.post('http://localhost:8000/api/accounts/token/refresh/', {
//         refresh: refreshToken
//       });
//       const newAccessToken = response.data.access;
//       localStorage.setItem('token', newAccessToken);  // 新しいアクセストークンを保存
//       return newAccessToken;
//     } catch (error) {
//       console.error("Token refresh failed:", error);
//       return null;
//     }
//   }
//   return null;
// }
export async function refreshToken() {
  const refreshToken = store.state.refreshToken; // リフレッシュトークンを取得
  try {
    const response = await axios.post("http://localhost:8000/api/accounts/token/refresh/", {
      refresh: refreshToken
    });
    store.commit('setAuthToken', response.data.access); // 新しいアクセストークンを保存
  } catch (error) {
    console.error("トークンのリフレッシュに失敗しました。再ログインが必要です。");
    router.push("http://localhost:8080/accounts/login");
  }
}

// 認証付きでユーザー情報を取得
export async function fetchUserWithAuth() {
  let token = localStorage.getItem('token');

  if (!token) {
    token = await refreshToken();  // アクセストークンがない場合にリフレッシュを試みる
    if (!token) {
      throw new Error("Authentication failed. Please log in again.");
    }
  }

  try {
    const response = await axios.get('http://localhost:8000/api/accounts/profile/', {
      headers: { Authorization: `Bearer ${token}` }
    });
    return response.data;
  } catch (error) {
    // if (error.response && error.response.status === 401) {
    //   // アクセストークンが無効だった場合、リフレッシュを試みる
    //   token = await refreshToken();
    //   if (token) {
    //     return await fetchUserWithAuth();  // 新しいトークンで再リクエスト
    //   }
    // }
    if (error.response && error.response.status === 401) {
      console.error("認証エラーが発生しました。再ログインが必要です。");
      // 例: ログインページへのリダイレクト
      // router.push();
      this.$router.push("/accounts/login");
    }
    throw error;
  }
}