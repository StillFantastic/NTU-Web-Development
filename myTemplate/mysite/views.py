from django.shortcuts import render

# Create your views here.
# def index(request):
#     return render(request, 'index.html', {'msg':'Hello'})

from datetime import datetime
# def index(request):
#     msg= 'Hello'
#     now = datetime.now()
#     return render(request, 'index.html', locals())

def index(request, tvno = 0):
    # tv_list = [{'name':'東森', 'tvcode':'dxpWqjvEKaM'},
    #     {'name':'民視', 'tvcode':'XxJKnDLYZz4'},
    #     {'name':'台視', 'tvcode':'yk2CUjbyyQY'},
    #     {'name':'華視', 'tvcode':'TL8mmew3jb8'},
    #     {'name':'TVBS', 'tvcode':'Hu1FkdAOws0'},
    #     {'name':'中視', 'tvcode':'XBne4oJGEhE'},
    #     {'name':'冰雪奇緣2', 'tvcode':'d_zVfl4bpJI'},
    # ]
    tv_list = [{'name':'錫蘭Ceylan', 'tvcode':'Kun2UoqLsK8'},
        {'name':'喬瑟夫 ChillSeph', 'tvcode':'lajz_voEhhw'},
        {'name':'人生魯宅x尊-第2頻道', 'tvcode':'5rV2umNkxDg'},
        {'name':'懶貓 LanCat', 'tvcode':'_toFpiHyuUg'},
        {'name':'微積分基礎', 'tvcode':'videoseries?list=PLBoOQl1Wawqr9hVZ21PpMXUx8CK1jMWI0'},
        {'name':'HowFun', 'tvcode':'YXb800paJhw'},
        {'name':'計畫通行', 'tvcode':'JU7pC5Oxqos'},
    ]
    now = datetime.now()
    tvno = tvno
    tv= tv_list[tvno]
    hour = now.timetuple().tm_hour
    return render(request, 'index.html', locals())

def yt(request, tvno = 0):
    tv_list = [{'name':'錫蘭Ceylan', 'tvcode':'Kun2UoqLsK8'},
        {'name':'喬瑟夫 ChillSeph', 'tvcode':'lajz_voEhhw'},
        {'name':'人生魯宅x尊-第2頻道', 'tvcode':'5rV2umNkxDg'},
        {'name':'懶貓 LanCat', 'tvcode':'_toFpiHyuUg'},
        {'name':'微積分基礎', 'tvcode':'videoseries?list=PLBoOQl1Wawqr9hVZ21PpMXUx8CK1jMWI0'},
    ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'tv.html', locals())

def carlist(request, maker=0):
    car_maker= ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan','Toyota' ]
    car_list = [ [],
        ['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
        ['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
        ['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
        ['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
        ['Camry','Altis','Yaris','86','Prius','Vios', 'RAV4', 'Wish']
    ]
    maker = maker
    maker_name=  car_maker[maker]
    cars = car_list[maker]
    return render(request, 'carlist.html', locals())


def my_view(request):
    context = {
        "author": "gaurav singhal",
    }
    return render(request, "index.html", context)