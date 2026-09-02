# Mechanic Service API

A REST API built using Django REST Framework for managing mechanics and customer service requests.

## Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL

## Project Features

- Create and list mechanics
- Get mechanic details by ID
- Update mechanic details
- Delete a mechanic
- Create service requests
- List service requests
- Get service request by ID
- Update service request status
- Input validation
- Error handling
- JSON API responses
- PostgreSQL database integration

---

## Project Structure

```text
mechanic_service_api/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
│
├── mechanics/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   └── __init__.py
│
├── manage.py
├── requirements.txt
└── README.md