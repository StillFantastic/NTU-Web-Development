from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.template.loader import get_template
from django.shortcuts import redirect
from .models import Registration, Post
from datetime import datetime

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

def homepage(request):
    # posts = Post.objects.all()
    # post_lists= list()
    # for count, post in enumerate(posts):
    #     post_lists.append("No.{}:".format(str(count)) +str(post)+"<br>")
    #     post_lists.append("<small>"+str(post.body)+"</small><br><br>")
    # return HttpResponse(post_lists)

    template = get_template('index2.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')