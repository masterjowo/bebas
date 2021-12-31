from django.shortcuts import render

def index(request):
    context={
        'judul': 'sasasasasas'
    }
    return render(request,'index.html',context)