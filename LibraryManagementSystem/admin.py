from django.contrib import admin
from .models import User,Book, PaymentDetails,cartBooks


# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(PaymentDetails)
admin.site.register(cartBooks)