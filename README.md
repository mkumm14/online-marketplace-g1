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

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/online-marketplace.git
    cd online-marketplace
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

5. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Register a new user or log in with an existing account.
- Browse products, add items to your cart, and proceed to checkout.
