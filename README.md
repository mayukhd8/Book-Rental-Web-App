# 📚 Book Rental Web Application (Django)

A Django-based web application that allows users to create accounts, list books for rental, rent books from other users, manage their rentals, and track book return status. The app also supports book uploads with images, user dashboards, and rental management features.

---

## 🚀 Features

- ✅ User Registration, Login, and Logout
- 📖 List books for rental with images
- 🔍 Browse available books
- 🛒 Rent books for 1, 3, or 6 months
- 📦 Track ongoing and completed rentals
- 🔁 Return rented books
- 📁 User dashboard to manage listed books and rentals
- 🖼 Upload and display book cover images
- ⚙️ Admin panel for backend management

---

## 📂 Project Structure
  boek/
├── accounts/ # User auth & profiles
├── books/ # Book listing and rental models
├── rentals/ # Rental logic, dashboard views
├── static/ # Static files (CSS, JS, Images)
├── templates/ # HTML templates
├── media/ # Uploaded book images
├── manage.py # Django entry point



📸 Screenshots

![Screenshot (48)](https://github.com/user-attachments/assets/aca0d167-d256-46f2-a5e3-2629ff2cbe5f)
![Screenshot (47)](https://github.com/user-attachments/assets/cd5ebf22-bb32-46d6-b48b-990a6d3a70cd)
![Screenshot (46)](https://github.com/user-attachments/assets/f7c03b45-a6d7-4200-9953-17d76585a485)
![Screenshot (45)](https://github.com/user-attachments/assets/41c42f8b-d0f2-4283-926d-1a7934867b05)
![Screenshot (44)](https://github.com/user-attachments/assets/414f10e2-cfeb-49a9-ad59-3eb191fc8177)
![Screenshot (43)](https://github.com/user-attachments/assets/6bed0b0b-4c7c-453a-9236-e789c834b9f9)
![Screenshot (42)](https://github.com/user-attachments/assets/5f36e9b7-9b2d-450d-ac13-ff7435a29675)
![Screenshot (41)](https://github.com/user-attachments/assets/ed1d10a5-fdfa-458a-83cb-5b9a4abe629f)
![Screenshot (40)](https://github.com/user-attachments/assets/d68b40e9-9362-4f8c-8d04-52cd8cdc8965)
---

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/bookrental.git
cd boek
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

2.  Create a virtual environment:
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

'''


📡 APIs & Integration
✅ Open Library API — fetch book data and populate model

✅ Image upload with Django's ImageField

🧩 Dependencies
Python 3.x

Django 4.x

Pillow (for image uploads)

Bootstrap (via CDN in templates)

📌 TODOs / Future Improvements
Add search and filter functionality

Add categories/genres to books

Add email notifications

Add pagination and ratings/reviews

Add payment gateway (for real-world deployment)

Author
Mayukh Dutta

GitHub: @mayukhd8

Email: dutta.mayukh8@gmail.com

