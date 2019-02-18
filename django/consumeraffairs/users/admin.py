from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Reviewer

admin.site.register(Reviewer, UserAdmin)
