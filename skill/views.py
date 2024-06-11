from django.shortcuts import render

# Create your views here.
def skill_view(request):
    return render(request, 'skill/skill.html')