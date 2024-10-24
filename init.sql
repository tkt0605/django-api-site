--データベースの作成--
CREATE DATABASE IF NOT EXISTS bookstore CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
--使用するデータベース--
USE bookstore;

--ユーザー情報のテーブル--
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usrname VARCHAR(50) UNIQUE NOT NULL,
    password INT VARCHAR(100) UNIQUE NOT NULL,
    first_name VARCHAR(50) UNIQUE NOT NULL,
    last_name VARCHAR(50) UNIQUE NOT NULL,
    is_admin BOOLEAN DEFULT FALSE,
    created_at TIMESTAMP DEFULT CURRENT_TIMESTAMP,
);

--書籍テーブルの作成--
CREATE TABLE IF NOT EXISTS books(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    auther VARCHAR(50),
    isbn VARCHAR(13) UNIQUE NOT NULL,
    description TEXT,
    stock INT DEFULT 0,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFULT CURRENT_TIMESTAMP,
);

--注文情報テーブルの作成--
CREATE TABLE IF NOT EXISTS order(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title_id INT NOT NULL,
    quantity INT NOT NULL,
    status VARCHAR(50) DEFULT "Pending",
    total_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFULT CURRENT_TIMESTAMP,
    --REFERENCES--
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (title_id) REFERENCES books(id) ON DELETE CASCADE,
);

--在庫数テーブルの作成--
CREATE IF NOT EXISTS stocks(
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    stock INT NOT NULL,
    updated_at TIMESTAMP DEFULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,

)