# TradeLocal

A small local marketplace built with Django. Users can sign up, post listings with a photo, price and contact details, search everything that's for sale, and manage their own listings.

## Features

- **Accounts:** sign up, log in and log out, with duplicate username/email checks
- **Listings:** create, edit and delete your own listings (title, description, price, image, phone, email)
- **Search:** keyword search across listing titles and descriptions
- **Ownership checks:** only the owner can edit or delete a listing; deleting a listing also removes its image from disk
- **Responsive UI** with Bootstrap 5

## Project structure

```
TradeLocal/   project settings and root URLs
core/         landing page
user/         signup, login, logout
listings/     Listing model, CRUD views and templates
templates/    shared base layout
```

## Tech stack

Python · Django · django-phonenumber-field · Pillow · SQLite · Bootstrap 5

## Running locally

```bash
git clone https://github.com/TomassSaulite/TradeLocal.git
cd TradeLocal
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000.

## Possible next steps

- Categories and price filters
- Pagination on the listings page
- Messaging between buyer and seller
