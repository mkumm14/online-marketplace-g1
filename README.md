# Online Marketplace

This is an online marketplace application built with Django. It allows users to register, log in, browse products, add items to their cart, apply discount codes, and checkout.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

- User registration and authentication
- Product browsing and filtering
- Shopping cart management
- Discount code application
- Checkout process

## Installation

### Using Docker

1. Clone the repository:

    ```sh
    git clone https://github.com/mkumm14/online-marketplace-g1.git
    cd online-marketplace-g1
    ```

2. Build and run the Docker containers:

    ```sh
    docker-compose -f docker-compose.dev.yml up --build
    ```

3. Run migrations and collect static files:

    ```sh
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py collectstatic --noinput
    ```

4. Create a superuser:

    ```sh
    docker-compose exec web python manage.py createsuperuser
    ```

### Without Docker

1. Clone the repository:

    ```sh
    git clone https://github.com/mkumm14/online-marketplace-g1.git
    cd online-marketplace-g1
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```sh
    python manage.py migrate
    ```

5. Collect static files:

    ```sh
    python manage.py collectstatic --noinput
    ```

6. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```sh
    python manage.py runserver
    ```

## Usage

- Acess the application at `http://localhost:1337` if using docker.
- Access the application at `http://127.0.0.1:8000/`.
- Register a new user or log in with an existing account.
- Browse products, add items to your cart, and proceed to checkout.

