from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *
# Register your models here.


class MemberAdmin(UserAdmin):
    add_form = MemberCreationForm
    form = MemberChangeForm
    model = Member
    list_display = ['id', 'username', 'last_name', 'first_name', 'gen', 'is_staff', 'is_superuser']
    list_editable = ['first_name', 'last_name', 'gen']
    list_filter = ['gen']
    list_per_page = 20
    search_fields = ['first_name', 'last_name']


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['name']


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['member', 'challenge', 'file', 'result', 'time']


admin.site.register(Member, MemberAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Submission, SubmissionAdmin)
