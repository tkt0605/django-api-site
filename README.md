# オンライン書店システム

## 概要

このプロジェクトは、Vue.js と Django を使用して構築されたウェブアプリケーションです。ユーザーは、アカウントの登録・ログイン・ログアウトを行い、本を追加および表示することができます。管理者のみが本を追加できるように制限されています。

## 特徴

- ユーザー登録・ログイン・ログアウト機能
- ユーザー名の表示
- 管理者専用の「AddBook」ボタン
- 本の追加機能（JSON フォーマットの画像 URL に対応）

## 技術スタック

- フロントエンド: Vue.js
- バックエンド: Django
- データベース: MySQL (または使用しているデータベースに応じて変更)
- 認証: Django 標準のユーザー認証システム
- コンテナ管理: Docker

## 開発環境のセットアップ (Docker 使用)
0. Ubuntuをセットアップ。
　```bash
    wsl --install
  ```
1. リポジトリをクローンします。

    ```bash
    git clone https://github.com/tkt0605/django-api-site.git
    cd project-name
    ```

2. Docker コンテナをビルドして起動します。

    ```bash
    # Docker Compose を使用してビルドと起動
    docker-compose up --build
    ```

    ※バックエンドとフロントエンドのコンテナがセットアップされ、アプリケーションが起動します。

3. ブラウザで [http://localhost:8080](http://localhost:8080) にアクセスして、アプリケーションを確認してください。

### Docker コンテナの操作

- **コンテナの停止**: 

    ```bash
    docker-compose down
    ```

- **マイグレーションの実行**:

    Django コンテナ内で以下を実行します。

    ```bash
    docker-compose exec backend python manage.py migrate
    ```

- **スーパーユーザーの作成**:

    ```bash
    docker-compose exec backend python manage.py createsuperuser
    ```

## 使用方法

1. **ユーザー登録**: 最初にユーザーアカウントを作成してください。
2. **ログイン/ログアウト**: アカウントでログインし、ユーザー名が画面に表示されることを確認してください。
3. **本の追加**: 管理者アカウントでログインすると、「AddBook」ボタンが表示され、JSON 形式で本の画像 URL を追加できます。

## 注意事項

- 管理者権限が必要な操作には「AddBook」ボタンが含まれています。一般ユーザーには表示されません。

## ライセンス

このプロジェクトのライセンスについての情報があればここに記載します。
