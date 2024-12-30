from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,name):
        if not email:
            raise ValueError("Email not inputted")
    
        user = self.model(
            email = self.normalize_email(email),
            name = name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password):
        user = self.create_user(email=email,password=password,name="Admin")
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class MyUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    points = models.IntegerField(default=0)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_superuser
    
    def has_module_perms(self,app_label):
        return self.is_superuser
    
class Hotelbook(models.Model):
    suite_choices = {
        "suite1":"Standard",
        "suite2":"Deluxe",
        "suite3":"Joint",
        "suite4":"Suite",
    }
    suite = models.CharField(max_length=10,choices=suite_choices,default="suite1",verbose_name="Suite Type")
    people_choices = {
        "p1":"1 Person",
        "p2":"2 People",
        "p3":"3 People",
        "p4":"4 People",
    }
    people = models.CharField(max_length=10,choices=people_choices,default="p1",verbose_name="Number of People")
    room_choices = {
        "1r":"1",
        "2r":"2",
        "3r":"3",
        "4r":"4",
    }
    numrooms = models.CharField(max_length=10,choices=room_choices,default="1r",verbose_name="Number of Rooms")
    checkin = models.DateField(null=True,default=None,verbose_name="Check in date")
    checkout = models.DateField(null=True,default=None,verbose_name="Check out date")
    email = models.EmailField(verbose_name='Email address', max_length=255,default=None)
    price = models.FloatField(default=0.0,verbose_name="Price")

    class Meta:
        verbose_name_plural = "Hotel Bookings"

    def __str__(self):
        return self.email

class Tickbooking(models.Model):
    ticket1 = models.BooleanField(default=False,verbose_name="Children (2 to 15 years)")
    ticket1num = models.IntegerField(default=0,verbose_name="Child tickets purchased")
    ticket2 = models.BooleanField(default=False,verbose_name="Standard")
    ticket2num = models.IntegerField(default=0,verbose_name="Standard tickets purchased")
    ticket3 = models.BooleanField(default=False,verbose_name="Off Peak Weekday")
    ticket3num = models.IntegerField(default=0,verbose_name="Off Peak tickets purchased")
    ticket4 = models.BooleanField(default=False,verbose_name="Seniors")
    ticket4num = models.IntegerField(default=0,verbose_name="Senior tickets purchased")

    date = models.DateField(null=True,default=None,verbose_name="Booking Date")
    email = models.EmailField(verbose_name='Email address', max_length=255,default=None)

    price = models.FloatField(default=0.0,verbose_name="Price")

    class Meta:
        verbose_name_plural = "Ticket Bookings"

    def __str__(self):
        return self.email