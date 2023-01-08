from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})


from django.http import HttpResponse


from djangoproject2.models import User

def ccu408310044_function(request):
    user=request.GET['UserName']
    mail=request.GET['UserMail']

    u = User(username=user, email=mail)
    u.save()
    return render(request, 'users_template.html', {'users_list': User.objects.all()})