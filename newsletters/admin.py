from django.contrib import admin

# Register your models here.
from .models import NewsletterUser, Newsletter

admin.site.register(NewsletterUser)
admin.site.register(Newsletter)