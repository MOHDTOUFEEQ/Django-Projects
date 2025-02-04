# 🚀 **Django Projects Collection**

This repository includes three different Django-based projects that showcase various functionalities and features of web development with **Django**. These projects demonstrate how Django can be used to build versatile applications, from a pizza store to a real-time chatting app.

## 📌 **Project Overview**

### 1. **Django-PizzaStore**
A simple web application built with **Django** that simulates an online pizza store. Users can view different pizza categories, add items to the cart, and make an order. It also includes basic user authentication for managing orders.

**Features**:
- Pizza menu display
- User authentication (sign up, login)
- Cart management
- Order summary and checkout

### 2. **Django-WeatherApp**
A weather application where users can search for weather information for different cities. It uses an external weather API to fetch real-time data and display weather conditions, including temperature, humidity, and weather descriptions.

**Features**:
- Search functionality for cities
- Real-time weather data using a weather API
- Display of temperature, humidity, and weather description

### 3. **Django-Chatting-App**
A real-time chatting application that allows users to join chat rooms and communicate with other users. It uses **Django** for the back-end logic and **WebSockets** for real-time messaging. The app provides a live chat experience where users can send and receive messages instantly.

**Features**:
- Real-time messaging with AJAX
- Chat room creation and management
- User authentication (sign up, login)
- Instant communication with other users in chat rooms

## 📈 **How to Use Each Project**

### 1. **Django-PizzaStore**
- Clone the repository and navigate into the project directory.
- Set up the virtual environment, install dependencies, and run the server.
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver
