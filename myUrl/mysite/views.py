from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def homepage(request):
    return HttpResponse("Hello world!")

def homepage1(request):
    year = 2019
    month = 10
    day = 30
    postid = 3
    html = "<a href='/post/{}/{}/{}/{}/'>Show the Post</a>".format(year,month,day,postid)
    return HttpResponse(html)

def homepage2(request):
    year = 2019
    month = 10
    day = 30
    postid = 3
    html = "<a href='{}'>Show the Post Link</a>".format(reverse('post-url', args=(year, month, day, postid,)))
    return HttpResponse(html)

def about(request, author_no = 0):
    html= "<h2>Here is No:{}'s about page!</h2><hr>".format(author_no)
    return HttpResponse(html)

def company(request):
    return HttpResponse("My Company")
def sales(request):
     return HttpResponse("My Sales")
def contact(request):
    return HttpResponse("My Contact")

def listing(request, yr, mon, day):
    html = "<h2>Your List Date is {}/{}/{}</h2><hr>".format(yr, mon, day)
    return HttpResponse(html)
def post(request, yr, mon, day, post_num):
    html = "<h2>Today is {}/{}/{}: Your Post Number:{}</h2><hr>".format(yr, mon, day, post_num)
    return HttpResponse(html)

def post2(request, yr, mon, day, post_num):
    return render(request, 'post2.html', locals()) 