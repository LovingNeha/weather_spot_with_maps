from django.shortcuts import render
import requests
from .models import City,Temp_imp_climate,Earthquake_data,Temp_changes_couses,Feedback,City1
from .forms import Cform
from django.views.generic import ListView
from django.conf import settings
from .forms import FeedbackForm
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail


# Create your views here.
def index(request):
    #appid="a0d5659a015c8b72076e37f18fb9b18b";
    cities = City.objects.all() #return all the cities in the database
    print("cities>>>",cities)
    if request.method=="POST":
            form=Cform(request.POST)
            if form.is_valid():
                city=form.cleaned_data.get('name')
                url="http://api.openweathermap.org/data/2.5/find?q={}&units=metric&appid=a0d5659a015c8b72076e37f18fb9b18b"
                response=requests.get(url.format(city))
                json_response=response.json()
                if response.status_code==200 and json_response['list']:
                        

                            name=json_response['list'][0]['name']
                            temp=json_response['list'][0]['main']['temp']
                            des=json_response['list'][0]['weather'][0]['description']
                            icon=json_response['list'][0]['weather'][0]['icon']
                            wind=json_response['list'][0]['wind']['speed']
                            country=json_response['list'][0]['sys']['country']
                            rain=json_response['list'][0]['rain']
                            snow=json_response['list'][0]['snow']
                            weather={
                                "city":name,"temp":temp,
                                "des":des,"icon":icon,"wind":wind,"country":country,"rain":rain,"snow":snow
                            }
                            return render(request,"weather/index.html",{"weather":weather,"form":form,"valid":True})
                        
                else:
                        return render(request,"weather/index.html",{"valid":False,"touser":"Sorry for inconvenience! Please check your spellings.","form":form})
                
    
    form=Cform()
    return render(request,"weather/index.html",{"form":form})


















class Temp_imp_climate(ListView):
    model = Temp_imp_climate
    template_name = 'weather/index2.html'





def index1(request):
    qs1 = Temp_changes_couses.objects.all()
    qs2 = Earthquake_data.objects.all()
    context = {
        'qs1':qs1,
        'qs2':qs2
    }
    return render (request, 'weather/index2.html', context)




def FeedBack(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        Name =form.cleaned_data ['Name']
        Email = form.cleaned_data['Email']
        message = form.cleaned_data['message']

        try:
            send_mail(Name,message,Email, ['mail@gmail.com'])
        
        except BadHeaderError:
            return HttpResponse('invalid Header Found.')
        
        return render(request, "weather/thankyou.html")
    return render(request, "weather/FeedBack.html")


def admin_login(request):
    return render(request,'weather/admin_login.html')
