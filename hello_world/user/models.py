from django.db import models


# Create your models here.
class Address(models.Model):
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.address}, district {self.district}"

    class Meta:
        # table name in db will save address
        db_table = 'address'


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=50)
    vehicle_id = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicle_type

    class Meta:
        # table name in db will save vehicle
        db_table = 'vehicle'


class Member(models.Model):
    no = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.BooleanField(default=True)
    # default null = False
    date_of_birth = models.DateTimeField(null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f"id: {self.pk}, firstname: {self.first_name}, lastname: {self.last_name}, address: {self.address}, vehicle: {self.vehicle}"

    class Meta:
        # table name in db will save member
        db_table = 'member'
