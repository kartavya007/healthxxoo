from django.shortcuts import render
# Create your views here.
from .models import plan , track , diet , login
def index(request):
    return render(request,"index.html")
def display(request):
    entry = track.objects.get(i_d = 1)
    entry1 = diet.objects.get(i_d = 1)
    p_p = int(((entry.pro)/entry1.pro) * 100)
    c_p = int(((entry.carbs)/entry1.carbs) * 100)
    f_p = int(((entry.fats)/entry1.fat) * 100)
    dic = {
        "p_t" : entry.pro ,
        "c_t" : entry.carbs ,
        "f_t" : entry.fats , 
        "p_r" : entry1.pro ,
        "c_r" : entry1.carbs ,
        "f_r" : entry1.fat , 
        "p_p" : p_p ,
        "c_p" : c_p ,
        "f_p" : f_p ,
        "t_p" : int((p_p + c_p + f_p)//3)
    }
    return render(request , "display.html" ,dic)
def index2(request):
    return render(request,"index2.html")