from django.shortcuts import render

# Index Page
def home(request):
    return render(request, 'templates/home/index.html')