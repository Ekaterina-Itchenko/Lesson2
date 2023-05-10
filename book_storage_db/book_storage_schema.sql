PRAGMA foreign_keys = ON;
CREATE TABLE genres (
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre_name TEXT UNIQUE NOT NULL,
    genre_description TEXT,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date NUMERIC,
    date_of_death NUMERIC,
    information TEXT,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    price REAL CHECK (price > 0),
    description TEXT,
    pages INTEGER CHECK (price > 0),
    format TEXT NOT NULL,
    age_limit INTEGER NOT NULL CHECK(age_limit >= 0),
    amount INTEGER NOT NULL CHECK(age_limit >= 0),
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE books_genres (
    book_id INTEGER,
    genre_id INTEGER,
    PRIMARY KEY (book_id, genre_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE
);
CREATE TABLE books_authors (
    book_id INTEGER,
    author_id INTEGER,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE
);
CREATE TABLE permissions (
    permission_id INTEGER PRIMARY KEY AUTOINCREMENT,
    permission_name TEXT UNIQUE NOT NULL,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE roles (
    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
    role_name TEXT UNIQUE NOT NULL,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE permissions_roles (
    permission_id INTEGER,
    role_id INTEGER,
    PRIMARY KEY (permission_id, role_id),
    FOREIGN KEY (permission_id) REFERENCES permissions(
        permission_id
        ) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE
);
CREATE TABLE baskets (
    basket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE NOT NULL,
    status TEXT NOT NULL,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
CREATE TABLE baskets_books (
    basket_id INTEGER,
    book_id INTEGER,
    quantity INTEGER NOT NULL,
    PRIMARY KEY (basket_id, book_id),
    FOREIGN KEY (basket_id) REFERENCES baskets(basket_id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE
);
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    user_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone_number TEXT,
    password TEXT UNIQUE NOT NULL,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE users_roles (
    user_id INTEGER,
    role_id INTEGER,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE
);
CREATE TABLE addresses (
    address_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country TEXT NOT NULL,
    city TEXT NOT NULL,
    street TEXT NOT NULL,
    home_number INTEGER NOT NULL,
    post_code INTEGER NOT NULL,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE users_addresses (
    user_id INTEGER,
    address_id INTEGER,
    PRIMARY KEY (user_id, address_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (address_id) REFERENCES addresses(address_id) ON DELETE CASCADE
);
CREATE TABLE bankcards (
    bankcard_id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    cvc INTEGER NOT NULL,
    expiry_date TEXT NOT NULL,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE users_bankcards (
    user_id INTEGER,
    bankcard_id INTEGER,
    PRIMARY KEY (user_id, bankcard_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (bankcard_id) REFERENCES bankcards(bankcard_id) ON DELETE CASCADE
);
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    basket_id INTEGER NOT NULL,
    bankcard_id INTEGER NOT NULL,
    amount REAL NOT NULL CHECK (amount > 0),
    address_id INTEGER NOT NULL,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (basket_id) REFERENCES baskets(basket_id),
    FOREIGN KEY (bankcard_id) REFERENCES bankcards(bankcard_id),
    FOREIGN KEY (address_id) REFERENCES addresses(address_id)
);
