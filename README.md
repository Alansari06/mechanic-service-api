# Mechanic Service API

A REST API for managing mechanics and customer service requests, built with Django REST Framework and PostgreSQL.

## Technologies

- Python
- Django
- Django REST Framework
- PostgreSQL
- psycopg2
- python-dotenv

## Features

- Create, list, update and delete mechanics
- Create and view service requests
- Update service request status
- Input validation
- Error handling
- PostgreSQL database integration

## Project Structure

```text
mechanic-service-api/
├── config/
├── mechanics/
│   └── migrations/
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Database Setup

The project uses PostgreSQL.

Create a database named:

```text
mechanic_db
```

Create a `.env` file in the project root:

```text
DB_NAME=mechanic_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DJANGO_SECRET_KEY=your_secret_key
```

Do not upload the `.env` file to GitHub.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Alansari06/mechanic-service-api.git
cd mechanic-service-api
```

### 2. Create and activate virtual environment

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run migrations

```powershell
python manage.py migrate
```

### 5. Start the server

```powershell
python manage.py runserver
```

API will run at:

```text
http://127.0.0.1:8000/
```

## API Documentation

Base URL:

```text
http://127.0.0.1:8000
```

### Mechanics

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/mechanics/` | List mechanics |
| POST | `/api/mechanics/` | Create mechanic |
| GET | `/api/mechanics/<id>/` | Get mechanic |
| PUT | `/api/mechanics/<id>/update/` | Update mechanic |
| PATCH | `/api/mechanics/<id>/update/` | Partially update mechanic |
| DELETE | `/api/mechanics/<id>/delete/` | Delete mechanic |

### Service Requests

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/service-requests/` | List service requests |
| POST | `/api/service-requests/` | Create service request |
| GET | `/api/service-requests/<id>/` | Get service request |
| PUT | `/api/service-requests/<id>/update/` | Update status |
| PATCH | `/api/service-requests/<id>/update/` | Update status |

## Sample Requests

### Create Mechanic

```http
POST /api/mechanics/
```

```json
{
    "name": "Rahul Auto Works",
    "phone": "9876543210",
    "location": "Noida",
    "rating": 4.5,
    "is_open": true,
    "services": "Oil Change, Brake Repair"
}
```

### Create Service Request

```http
POST /api/service-requests/
```

```json
{
    "customer_name": "Anas",
    "customer_phone": "9876543210",
    "vehicle_number": "UP16AB1234",
    "mechanic": 1,
    "service": "Brake Repair",
    "problem_description": "Brake making noise"
}
```

Example response:

```json
{
    "id": 1,
    "customer_name": "Anas",
    "customer_phone": "9876543210",
    "vehicle_number": "UP16AB1234",
    "mechanic": 1,
    "service": "Brake Repair",
    "problem_description": "Brake making noise",
    "status": "PENDING"
}
```

## Validation

The API validates:

- Customer phone must contain exactly 10 digits.
- Vehicle number must contain at least 6 characters.
- Service must be one of:
  - Oil Change
  - Brake Repair
  - Engine Repair
  - Tire Change
- Mechanic ID must exist.
- Service request status must be:
  - PENDING
  - IN_PROGRESS
  - COMPLETED
  - CANCELLED

## Status Codes

| Code | Meaning |
|---|---|
| 200 | Successful request |
| 201 | Resource created |
| 204 | Resource deleted |
| 400 | Validation error |
| 404 | Resource not found |
| 405 | Method not allowed |

## Tests

The project includes automated API tests in `mechanics/tests.py`.

The tests cover:

- Getting all mechanics
- Getting a mechanic by ID

Run the tests using:

```powershell
python manage.py test ```

## GitHub Repository

https://github.com/Alansari06/mechanic-service-api