from django.shortcuts import render

# Users Page
def users(request):
    return render(request, 'templates/users/users.html')
