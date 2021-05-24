from django.shortcuts import render

from .models import Destination

# Create your views here.

def index(request):
    des1=Destination()
    des1.name = "mumbai"
    des1.desc = "good city"
    des1.img =""
    des1.price = 500

    des2=Destination()
    des2.name = "kolkata"
    des2.desc = "very good city"
    des2.img =""
    des2.price = 700

    des3=Destination()
    des3.name = "delhi"
    des3.desc = "heart city"
    des3.img =""
    des3.price = 200

    des4=Destination()
    des4.name = "delhi"
    des4.desc = "heart city"
    des4.img =""
    des4.price = 200

    des5=Destination()
    des5.name = "delhi"
    des5.desc = "heart city"
    des5.img =""
    des5.price = 200

    des6=Destination()
    des6.name = "delhi"
    des6.desc = "heart city"
    des6.img =""
    des6.price = 200

    alldest=[des1,des2,des3,des4,des5,des6]


    return render(request, 'index.html' , {'dest':alldest})
