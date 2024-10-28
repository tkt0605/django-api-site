-- ユーザーの作成と権限の付与
CREATE USER IF NOT EXISTS 'takato'@'%' IDENTIFIED WITH mysql_native_password BY '0605';
-- takatoというユーザーを作成して、それにプラグインのmysql_native_passwordで作成。
ALTER USER 'takato'@'%' IDENTIFIED WITH mysql_native_password BY '0605';
GRANT ALL PRIVILEGES ON *.* TO 'takato'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

-- データベースの作成
CREATE DATABASE IF NOT EXISTS bookstore CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE bookstore;

-- users テーブルの作成
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,  -- 'usrname' を 'username' に修正
    password VARCHAR(100) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- books テーブルの作成
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    author VARCHAR(50),  -- 'auther' を 'author' に修正
    isbn VARCHAR(13) UNIQUE NOT NULL,
    description TEXT,
    stock INT DEFAULT 0,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- orders テーブルの作成
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,  -- 'title_id' を 'book_id' に修正
    quantity INT NOT NULL,
    status VARCHAR(50) DEFAULT 'Pending',
    total_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
);

-- stocks テーブルの作成
CREATE TABLE IF NOT EXISTS stocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    stock INT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
);
