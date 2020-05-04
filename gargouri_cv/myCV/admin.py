from django.contrib import admin
from .models import personnalInfo,diplomaInfo,ExperienceInfo,phoneInfo,languageInfo,hobbiesInfo,skillsInfo

# Register your models here.

admin.site.register(personnalInfo)
admin.site.register(diplomaInfo)
admin.site.register(ExperienceInfo)
admin.site.register(phoneInfo)
admin.site.register(languageInfo)
admin.site.register(hobbiesInfo)
admin.site.register(skillsInfo)
