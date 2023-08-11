from django.shortcuts import render

# Index Page
def about(request):
    return render(request, 'templates/about/about.html')
