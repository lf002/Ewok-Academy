# 🌲 Endor Ewok Academy — Cafeteria Portal

> *"Yub Nub!" — The Empire shall never taste our Gorax Ribs.*

A secure Django web portal for the Endor Ewok Academy. The landing page is public, but the Secret Lunch Menu is locked behind authentication to keep Imperial Scout Troopers out.

---

## 🛡️ Setup Instructions

### 1. Clone & Create Virtual Environment

```bash
# Clone the repo
git clone <your-repo-url>
cd ewok_academy

# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Create the Superuser (Required for Grading)

```bash
python manage.py createsuperuser
```

Enter these exact credentials when prompted:
- **Username:** `Wicket`
- **Password:** `YubNub2026!`
- **Email:** (can leave blank)

### 5. Add AI-Generated Images

Place your two AI-generated images in the static folder:

```
cafeteria/static/cafeteria/images/academy.jpg     ← Endor Ewok Academy building
cafeteria/static/cafeteria/images/ewok_lunch.jpg  ← Ewok lunch spread
```

Then open the template files and uncomment the `<img>` tags (and comment out the placeholder divs).

**Templates to update:**
- `cafeteria/templates/cafeteria/landing.html`
- `cafeteria/templates/cafeteria/secret_menu.html`

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 📄 Project Structure

```
ewok_academy/
├── ewok_academy/          # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── cafeteria/             # The cafeteria app
│   ├── views.py           ← Core logic with @login_required
│   ├── urls.py
│   ├── models.py
│   ├── templates/
│   │   └── cafeteria/
│   │       ├── base.html
│   │       ├── landing.html    ← Public homepage
│   │       ├── login.html      ← Login form
│   │       └── secret_menu.html ← Protected menu page
│   └── static/
│       └── cafeteria/images/   ← Put AI images here
├── manage.py
├── requirements.txt
├── .gitignore             ← Excludes venv/ and db.sqlite3
└── README.md
```

---

## 🔐 Security Design

The `secret_menu` view in `views.py` uses Django's built-in `@login_required` decorator:

```python
from django.contrib.auth.decorators import login_required

@login_required
def secret_menu(request):
    ...
```

If an unauthenticated user tries to access `/menu/`, Django automatically redirects them to `/login/`. No manual if/else credential checking needed — Django handles it!

---

## 🍖 The Secret Menu

Once logged in as `Wicket`, you'll find:

- 🍖 **Roasted Gorax Ribs** — Slow-roasted, glazed with Endorian honey-sap
- 🍲 **Endorian Sunberry Stew** — Golden sunberries and wild forest herbs
- 🍢 **Logray's Mushroom Skewers** — Secret spice blend from the Medicine Man
- 🍞 **Wicket's Acorn Bread** — Freshly baked with a crispy bark crust
- 🍮 **Bantha Milk Pudding** — Creamy dessert topped with starberries
