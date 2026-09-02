from django.db import models


class Mechanic(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    rating = models.FloatField(default=0)
    is_open = models.BooleanField(default=True)
    services = models.TextField()

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    vehicle_number = models.CharField(max_length=20)

    mechanic = models.ForeignKey(
        Mechanic,
        on_delete=models.CASCADE
    )

    service = models.CharField(max_length=100)
    problem_description = models.TextField()

    status = models.CharField(max_length=20, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name