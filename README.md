# Online Sales Analysis System

## 📌 Project Description

This project is a Python-based online sales management system developed as part of a Git and OOP practice assignment.

The system allows:
- Managing products (add, display, remove)
- Calculating total inventory value
- Managing a customer shopping cart
- Calculating total cart price

The project demonstrates:
- Object-Oriented Programming (OOP)
- Git version control
- Branching and merging
- .gitignore usage for secure file handling

---

## 🧱 Project Structure

ONLINE_SALES_ANALYSIS/
│
├── product.py
├── product_manager.py
├── cart.py
├── main.py
├── .gitignore
└── README.md

---

## 🧩 Classes Overview

### 🔹 Product
Represents a product in the store.

Attributes:
- name
- price
- quantity

Methods:
- display_info()
- update_quantity()

---

### 🔹 ProductManager
Manages all available products.

Methods:
- add_product()
- show_products()
- total_inventory_value()
- remove_product()

---

### 🔹 Cart
Represents a customer's shopping cart.

Attributes:
- cart_items

Methods:
- add_to_cart()
- calculate_total()
- show_cart()

---

## ▶️ How to Run the Project

Make sure Python is installed.

Run the following command in terminal:


---

## 🛡 Security

The project includes a `.gitignore` file to ignore:
- config.json (API keys and sensitive data)
- __pycache__/
- *.pyc files
- Screenshots (*.png, *.jpg, *.jpeg)

---

## 👤 Author

Suad Kurgas


