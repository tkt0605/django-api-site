import axios from "axios";
const appClient = axios.create({
  baseURL: "http://localhost:8000/api/",
  withCredentials: true,
  headers:{
    "Content-Type": "application/json",
    // 'X-CSRFToken': csrfToken,
  },
});

export function fetchBooks(){
  // try{
  //   const response = appClient.get('books/',
  //     {
  //       headers: {
  //         'Content-Type': "application/json",
  //       },
  //       withCredentials: true,
  //     },
  //   );
  //   console.log('本一覧:', response.data);
  //   return response.data;
  // } catch(error){
  //   console.error("表示に失敗しました。", error.response || error.message);
  //   throw error;
  // }
  return appClient.get('books/');
}

export function fetchBookDetail(bookId) {
  return appClient.get(`books/${bookId}`);
}

export function addBook(bookData) {
  return appClient.post('add/book/', bookData);
}

export function OrderList(){
  return appClient.get('order/');
}

export function orderDetail(orderId) {
  return appClient.get(`order/${orderId}`);
}