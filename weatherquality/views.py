from django.shortcuts import render

# new View
def home(request):
    return render(request, 'home.html',{})

def about(request):
    return render(request, 'about.html',{})