from django.shortcuts import render
from .models import personnalInfo,diplomaInfo,languageInfo,phoneInfo,hobbiesInfo,ExperienceInfo,skillsInfo
# Create your views here.
def myCV_view(request):
    info = personnalInfo.objects.get(id=1)
    diploma = diplomaInfo.objects.all()
    langua = languageInfo.objects.all()
    phone = phoneInfo.objects.all()
    hobbies = hobbiesInfo.objects.all()
    Experience = ExperienceInfo.objects.all()
    skills = skillsInfo.objects.all()
    context = {
        "info":info,
        "diploma":diploma,
        "langua":langua,
        "phone":phone,
        "hobbies":hobbies,
        "Experience":Experience,
        "skills":skills,
        "home_active": "active"
    }
    return render(request,'home.html',context)

def contact_view(request):
    context = {
        "contact": "active"
    }
    return render(request,'comming_soon.html',context)

def tupperware_view(request):
    context = {
        "tupperware": "active"
    }
    return render(request,'comming_soon.html',context)

def contact_test_view(request):
    context = {
    }
    return render(request,'contact_test.html',context)

def comming_soon_view(request):
    context = {

    }
    return render(request,'comming_soon.html',context)