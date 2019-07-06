from django.contrib import admin
from .models import Profile_Role, Church_Background, Church_Mission, Church_Vision

# Register your models here.
class Profile_Role_Admin(admin.ModelAdmin):
    change_form_template = 'leadership/admin/change_form.html'
admin.site.register(Profile_Role, Profile_Role_Admin)

class Church_Background_Admin(admin.ModelAdmin): 
    change_form_template = 'leadership/admin/change_form.html'
admin.site.register(Church_Background, Church_Background_Admin)

class Church_Mission_Admin(admin.ModelAdmin): 
    change_form_template = 'leadership/admin/change_form.html'
admin.site.register(Church_Mission, Church_Mission_Admin)

class Church_Vision_Admin(admin.ModelAdmin): 
    change_form_template = 'leadership/admin/change_form.html'
admin.site.register(Church_Vision, Church_Vision_Admin)