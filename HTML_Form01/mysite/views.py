from django.shortcuts import render

# Create your views here.
def get_example(request):
    try:
        urid= request.GET['user_id']
        urpass= request.GET['user_pass']
        se_byear = request.GET['byear']
        urfcolor = request.GET.getlist('fcolor')
        favorite_movie = request.GET.get('fmovie')
    except:
        urid= None
    
    if urid != None and urpass == '12345':
        verified = True
    else:
        verifeid= False
        
    years = range(1960, 2022 + 1)
        
    return render(request, 'get_example.html', locals())