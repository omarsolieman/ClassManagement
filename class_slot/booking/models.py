from asyncio.windows_events import NULL
from django.db import models
from login.models import Customer,RoomManager
from datetime import date
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.TextField(max_length=2000)
    def __str__(self):
        return self.name
class Rooms(models.Model):
    manager=models.ForeignKey(RoomManager, on_delete=models.CASCADE)
    class_no=models.CharField(max_length=5)
    room_type=models.CharField(max_length=50)
    is_available=models.BooleanField(default=True)
    price=models.FloatField(default=1000.00)
    no_of_days_advance=models.IntegerField()
    class_time=models.TimeField(auto_now=False, auto_now_add=False, default="08:00:00")
    vehicle_type=models.CharField(max_length=100)
    registration_number=models.CharField(max_length=8, default=0)
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    room_image=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,default='0.jpeg')
    def __str__(self):
        return "Class No: "+str(self.id)
'''
class RoomImage(models.Model):
    room=models.ForeignKey(Rooms, on_delete=models.CASCADE)
    room_image=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)
'''
class Booking(models.Model):
    class_no=models.ForeignKey(Rooms, on_delete=models.CASCADE)
    user_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_day=models.DateField(auto_now=False, auto_now_add=False)
    #end_day=models.DateField(auto_now=False, auto_now_add=False)
    amount=models.FloatField()
    booking_time=models.TimeField(auto_now=True, auto_now_add=False)
    booked_on=models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return "Booking ID: "+str(self.id)
    @property
    def is_past_due(self):
        return date.today()>self.start_day


