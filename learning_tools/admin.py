from django.contrib import admin
from .models import Beheerder, Docent, Student, Verantwoording

# Register your models here.

admin.site.register(Beheerder)
admin.site.register(Docent)
admin.site.register(Student)
admin.site.register(Verantwoording)
