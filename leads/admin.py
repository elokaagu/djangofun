from django.contrib import admin

from .models import Category, User, Lead, Agent, UserProfile

admin.site.register(Category)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Lead)
admin.site.register(Agent)