# 💊 PharmEasy - Pharmacy Management System

A comprehensive digital solution for pharmacy inventory management and online medication ordering.

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.22.0-FF4B4B.svg)](https://streamlit.io/)
[![SQLite](https://img.shields.io/badge/sqlite-3-blue.svg)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📋 Overview

PharmEasy is a modern pharmacy management system designed to streamline medication inventory, sales, and customer management. The application provides intuitive interfaces for both customers and administrators, enabling efficient pharmaceutical operations.

## 🔧 Technologies Used

### Core Stack
- **Python**: Powers the backend logic and data processing
- **Streamlit**: Creates an interactive and responsive web interface
- **SQLite**: Handles data persistence and relational database management
- **Pillow**: Processes and displays product images
- **pdfkit**: Generates PDF reports for order history

### Architecture
- **Model-View-Controller (MVC)** design pattern for clean separation of concerns
- **Database-first** approach with properly normalized SQL schema
- **Responsive UI** with intuitive user flows for both customers and administrators

## ✨ Features

### 👤 Customer Portal
- User registration and secure authentication
- Browse available medications with detailed information
- View product images, prices, and usage instructions
- Interactive shopping cart with real-time total calculation
- Order history tracking and PDF export
- User-friendly checkout process

### 👨‍💼 Admin Dashboard
- Comprehensive inventory management
  - Add, update, and delete medications
  - Monitor expiration dates
  - Track stock levels
- Customer management
  - View and manage customer accounts
  - Update contact information
- Order tracking and fulfillment
  - View all orders across the system
  - See detailed order information

## 🧩 System Architecture

The system follows a modular architecture with these key components:

1. **Database Layer**: SQLite database with tables for:
   - Customers
   - Drugs/Medications
   - Orders

2. **Backend Logic**:
   - Authentication and authorization
   - Database operations (CRUD)
   - Business logic for ordering process
   - PDF generation for reporting

3. **Frontend Interface**:
   - Streamlit-powered responsive web UI
   - Separate views for customers and administrators
   - Interactive components (sliders, buttons, forms)
   - Dynamic content rendering

## 🎯 Problem Statement

In today's pharmaceutical industry, small and medium-sized pharmacies face challenges in:

- Managing growing inventory demands efficiently
- Maintaining accurate medication records
- Processing sales quickly and accurately
- Providing quality customer service
- Reducing manual paperwork and administrative overhead

PharmEasy addresses these challenges by providing a digital solution that automates record-keeping, streamlines sales processes, and improves overall operational efficiency.

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip package manager
- wkhtmltopdf (for PDF generation)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Vinay-Basargekar/PharmEasy.git
cd pharmeasy
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install wkhtmltopdf:
   - macOS: `brew install wkhtmltopdf`
   - Windows: [Download installer](https://wkhtmltopdf.org/downloads.html)
   - Linux: `sudo apt-get install wkhtmltopdf`

4. Ensure you have the required image files in the `/images` directory:
   - dolo650.jpg
   - strepsils.JPG
   - vicks.JPG

### Running the Application

1. Start the Streamlit server:
```bash
streamlit run app.py
```

2. Open your browser and navigate to:
```
http://localhost:8501
```

### Default Credentials

- **Admin Access**:
  - Username: `admin`
  - Password: `admin`

## 📊 Database Schema

The application uses a SQLite database with the following tables:

- **Customers**: Stores user information and credentials
- **Drugs**: Maintains medication inventory with details like name, expiry date, usage, quantity
- **Orders**: Tracks customer purchases with order items, quantities, and unique order IDs

## 📱 User Interface

### Home Page
![Home Page](./images/dbms-1.jpeg)

### Product Catalog
![Product Catalog](./images/dbms-2.jpeg)

### Admin Dashboard
![Admin Dashboard](./images/dbms-3.jpeg)

### Database Schema
![ER Diagram](./images/dbms-4.jpeg)
