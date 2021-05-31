from django.shortcuts import render, redirect
import random 

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        characters = 'abcdefghijklmnoprstuwvxyz'
        capital = 'ABCDEFGHIJKLMNOPRS'
        numbers = '1234567890'
        special = '!@#$%&'

        if request.POST.get('numbers'):
            characters += numbers
        
        if request.POST.get('special characters'):
            characters += special 
        
        if request.POST.get('capital'):
            characters += capital
           

        length = int(request.POST.get('length'))
        

        password = ''
        
        for _ in range(length):
            password += random.choice(characters)
        
        
        
        return render(request, 'result.html', {'password' : password, })
    else:
        return redirect('password:home')

def about(request):
    return render(request, 'about.html')