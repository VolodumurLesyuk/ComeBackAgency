<h1>Come Back Agency testing task using Django and Postgres</h1>

Для запуску додатку локально потрібно зробити наступні дії

+ Створити віртуальне середовище ```python3 -m venv venv``` та активувати ```source venv/bin/activate```
+ Встановити всі залежності ```pip install -r requirements.txt```
+ Створити файл .env у кореневій дирикторії та заповнити шаблон


```
DATABASE_NAME='dbname'
DATABASE_USER='dbuser'
DATABASE_PASSWORD='dbpassword'
DATABASE_HOST=host
DATABASE_PORT=yourport

SECRET_KEY='django_secret_key'
```
! використовувати потрібно базу даних postgresql
+ Виконати міграцію бд ```python manage.py migrate```
+ Створити супер-користувача ```python manage.py createsuperuser``` та заповнити відповідні поля
+ Запуск серверу ```python manage.py runserver```

<h1>Documentation</h1>

### 📚 Book API Documentation

### 📌 Overview
This API allows managing books and authors, supporting CRUD operations, filtering, ordering, JWT authentication, and bulk importing of books.

---

### 🔑 Authentication
All endpoints require JWT authentication. Obtain a token via `/api/token/` and include it in the `Authorization` header:

```http
Authorization: Bearer <your_token>
```


### 📌 Retrieve All Books (with optional filters)
```GET /api/books/```
Retrieves all books, with optional filters by title, author, or genre.

Query Parameters:

| Parameter | Type  |  Description | 
| ---      |-------|---|
| search | string |  Search by title, author name, or genre |
| ordering | string |   Sort by title, published_year, or author|   |
|   page | int |   Pagination parameter |

Example Request
```GET /api/books/?search=Django&ordering=published_year```

### 📌 Retrieve a Single Book

```GET /api/books/{uuid}/```
Fetch a book by its UUID.

Example Request
```GET /api/books/123e4567-e89b-12d3-a456-426614174000/```

### 📌 Create a New Book
```POST /api/books/```

Creates a new book record.

Request Body json
```
{
  "title": "Django for APIs",
  "author": "William S. Vincent",
  "published_year": 2020,
  "genre": "Non-Fiction"
}
```

### 📌 Update a Book
```PUT/PATCH /api/books/{uuid}/```

Updates an existing book.

Example Request

```PUT /api/books/987e4567-e89b-12d3-a456-426614174000/```

### 📌 Delete a Book
```DELETE /api/books/{uuid}/```

Deletes a book by its UUID.

Example Request

```DELETE /api/books/987e4567-e89b-12d3-a456-426614174000/```

<h1>📦 Bulk Import Books</h1>

### 📌 Import Multiple Books

```POST /books/import/```

Imports multiple books from a JSON array.

Request Body json

```
[
  {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "published_year": 1937,
    "genre": "Fiction"
  },
  {
    "title": "1984",
    "author": "George Orwell",
    "published_year": 1949,
    "genre": "Fiction"
  }
]
```

### 📌 Export Books

```POST /books/export/```

Export books into a JSON array.

<h1>📖 Authors API</h1>

### 📌 Retrieve All Authors

```GET /api/authors/```

Retrieves a list of all authors.

Example Request

```GET /api/authors/```

### 📌 Retrieve a Single Author

```GET /api/authors/{uuid}/```

Fetch an author by UUID.

Example Request

```GET /api/authors/abc12345-e89b-12d3-a456-426614174000/```

### 📌 Create an Author

```POST /api/authors/```

Creates a new author.

Request Body json

```
{
  "name": "Leo Tolstoy"
}
```

### 📌 Update an Author

```PUT/PATCH /api/authors/{uuid}/```

Updates an author's details.

Request Body json

```
{
  "name": "Leo Nikolayevich Tolstoy"
}
```

### 📌 Delete an Author

```DELETE /api/authors/{uuid}/```

Deletes an author by UUID.

Example Request

```DELETE /api/authors/xyz54321-e89b-12d3-a456-426614174000/```

<h1>⚙️ API Security & Authentication</h1>

This API uses JWT authentication.

### 📌 Obtain Token

```POST /api/token/```

### 📌 Refresh Token
```POST /api/token/refresh/```
