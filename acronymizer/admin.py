from django.contrib import admin

from .models import Submission, AcronymToken

admin.site.register((Submission, AcronymToken))