import axios from "axios";
const appClient = axios.create({
  baseURL: "http://localhost:8000/api/",
  withCredentials: true,
  headers:{
    "Content-Type": "application/json",
    // 'X-CSRFToken': csrfToken,
  },
});

export function BooksList(){
  return appClient.get('');
}

export function BooksDetails(bookId) {
  return appClient.get(`books/${bookId}`);
}

export function AddBooks(bookData) {
  return appClient.post('add/book/', bookData);
}

export function OrderList(){
  return appClient.get('order/');
}

export function orderDetail(orderId) {
  return appClient.get(`order/${orderId}`);
}