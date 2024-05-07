from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import Registration

import json

# Create your views here.
@csrf_protect
def registration(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_name =  data['fname'] 
        email = data['email']
        birthday = data['bday']
        
        # Create a new Registrant object and save it to the database
        registrant = Registration(fname=user_name, email=email, bday=birthday)
        registrant.save()

    return render(request, 'index.html')

def registration_list(request):
    if request.method == 'GET':
        registration = Registration.objects.all()
        return JsonResponse({"registration": list(registration.values("fname", "email", "bday"))})
