<p align="center">
  <img src="main/static/main/images/Main Logo.png" alt="PizzaHub Logo" width="300"/>
</p>

<h1 align="center">🍕 PizzaHub</h1>

<p align="center">
  <em>A delicious Django-powered pizza & pasta restaurant web application</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-5.1.7-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
</p>

---

## 📖 About

**PizzaHub** is a full-stack restaurant web application built with Django. It features a stunning landing page with a full-cover background image, a categorized menu system for pizzas and pastas, and a built-in JSON API — all managed through Django's powerful admin panel.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🏠 **Landing Page** | Eye-catching home page with a full-screen background and centered branding |
| 🍕 **Pizza Menu** | Browse all available pizzas sorted by price with ingredients & veg badges |
| 🍝 **Pasta Menu** | Dedicated pasta section with the same rich detail |
| 🔀 **Tab Navigation** | Seamless switching between Pizza and Pasta menus via pill-style tabs |
| 🟢 **Vegetarian Tags** | Items are clearly marked with a `VEGETARIAN` badge |
| 🔧 **Admin Panel** | Full CRUD management for pizzas & pastas with search and list views |
| 📡 **REST API** | JSON endpoint at `/api/GetPizzas` to fetch all menu items programmatically |
| 🔐 **Env Config** | Secrets managed via `.env` file using `python-dotenv` |
| 📱 **Responsive Design** | Fully responsive across desktop, tablet, and mobile with media queries |
| 🎨 **Styled UI** | Custom CSS with gradient overlays, cover backgrounds, and branded colors |

---

## 🖼️ Screenshots

<p align="center">
  <strong>Landing Page</strong><br/>
  <em>Full-screen background with centered logo and "See our menu" call-to-action</em>
</p>

![landingPage](<project screenshots/homePage.png>)

<p align="center">
  <strong>Pizza Menu</strong><br/>
  <em>Sleek dark overlay with pill-tab navigation and orange-accented pricing</em>
</p>

![pizzaMenu](<project screenshots/pizzaMenu.png>)

<p align="center">
  <strong>Pasta Menu</strong><br/>
  <em>Sleek dark overlay with pill-tab navigation and orange-accented pricing</em>
</p>

![pastaMenu](<project screenshots/pastaMenu.png>)

---

## 🗂️ Project Structure

```
pizzaHub/
├── manage.py                  # Django management script
├── .env                       # Environment variables (SECRET_KEY, DEBUG)
├── .gitignore                 # Git ignore rules
├── db.sqlite3                 # SQLite database
│
├── pizzaHub/                  # Project configuration
│   ├── settings.py            # Django settings (dotenv, apps, DB)
│   ├── urls.py                # Root URL routing
│   ├── wsgi.py                # WSGI entry point
│   └── asgi.py                # ASGI entry point
│
├── main/                      # Landing page app
│   ├── views.py               # Home page view
│   ├── urls.py                # URL routing for '/'
│   ├── templates/main/
│   │   └── index.html         # Landing page template
│   └── static/main/
│       ├── style.css           # Landing page styles
│       └── images/             # Logo & background images
│
└── menu/                      # Menu app
    ├── models.py              # Pizza & Pasta models
    ├── views.py               # Menu views + API endpoint
    ├── urls.py                # Menu URL routing (/menu, /menu/pasta)
    ├── api_urls.py            # API URL routing (/api/GetPizzas)
    ├── admin.py               # Admin configuration with search & list display
    ├── templates/menu/
    │   ├── base.html          # Base template with tab navigation
    │   ├── index.html         # Pizza listing template
    │   └── pasta.html         # Pasta listing template
    └── static/menu/
        ├── style.css           # Menu page styles
        └── images/             # Menu background & logos
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** installed
- **pip** package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ARShaikh0801/pizzaHub-django.git
   cd pizzaHub-django
   ```

2. **Create & activate a virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django python-dotenv
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ```
   > 💡 Generate a secure key with: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (to access admin panel)
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser** and visit:
   - 🏠 Home: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - 🍕 Menu: [http://127.0.0.1:8000/menu/](http://127.0.0.1:8000/menu/)
   - 🔧 Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📡 API Reference

### Get All Menu Items

```
GET /api/GetPizzas
```

Returns all pizzas and pastas in JSON format, ordered by price.

**Example Response:**
```json
[
  {
    "model": "menu.pizza",
    "pk": 1,
    "fields": {
      "name": "Margherita",
      "ingredients": "Mozzarella, Tomato, Basil",
      "price": 199,
      "vegetarian": true
    }
  }
]
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Django 5.1.7 |
| **Language** | Python 3.x |
| **Database** | SQLite 3 |
| **Templating** | Django Template Engine (with template inheritance) |
| **Styling** | Vanilla CSS (responsive, gradient overlays, media queries) |
| **Config** | python-dotenv |
| **Admin** | Django Admin (custom `ModelAdmin` with search & list display) |

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m "Add amazing feature"`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

---

## 📄 License

This project is open source.

---

<p align="center">
  Made with ❤️ and 🍕 by <a href="https://github.com/ARShaikh0801">A.R.Shaikh</a>
</p>
