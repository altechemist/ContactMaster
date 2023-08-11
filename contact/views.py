from django.shortcuts import render

# Contact Page
def contact(request):
    return render(request, 'templates/about/about.html')
