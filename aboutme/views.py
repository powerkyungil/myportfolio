from django.shortcuts import render

# Create your views here.
def aboutme_view(request):
    return render(request, 'aboutme/aboutme.html')