from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout
from . import forms
from . import models
import numpy as np
import joblib

model = joblib.load('E:/Diwakar/Project/Machine learning/ITPML29/Deploy/latest/new/RFC.pkl')

# Create your views here.
def home_view(request):
    if request.method == "POST":
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(password)
        name = request.POST['user']
        if name == "user":
            user = authenticate(request, username=username, password=password)
            #print(user)
            if user is not None:
                auth_login(request, user)
                return render(request, 'new/index.html')
            else:
                msg = 'Invalid Credentials'
                form = AuthenticationForm(request.POST)
                return render(request, 'new/user_login.html', {'form': form, 'msg': msg})
        else:
            user = authenticate(request, username=username, password=password)
            #print(user)
            if user is not None:
                auth_login(request, user)
                model = models.UserPredictDataModel.objects.latest('id')
                form = forms.FeedForm(request.POST)
                #print(model)
                return render(request, 'new/last.html', {'model':model,'form':form})
            else:
                msg = 'Invalid Credentials'
                form = AuthenticationForm(request.POST)
                return render(request, 'new/user_login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
    return render(request, 'new/user_login.html', {'form': form})


def login(request):
    form = AuthenticationForm()
    return render(request, 'new/login.html', {'form': form})

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #print('saving')
            form.save()
            return render(request, 'new/user_signup.html', {'msg':"Registered Successfully",'form':form})
    else:
        form = UserCreationForm()
    return render(request, 'new/user_signup.html',{'form':form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #print('saving')
            form.save()
            return render(request, 'new/user_signup.html', {'msg':"Registered Successfully",'form':form})
    else:
        form = UserCreationForm()
    return render(request, 'new/signup.html',{'form':form})




def predict_view(request):
    if request.method == 'POST':
        print('IF')
        fieldss = ['gravity', 'ph', 'osmo', 'cond', 'urea', 'calc']
        form = forms.UserPredictDataForm(request.POST)
        features = []
        for i in fieldss:
            info = request.POST[i]
            features.append(info)
        final_features = [np.array(features)]
        #print(final_features)
        prediction = model.predict(final_features)
        #print(prediction)
        output = prediction[0]
        if output == 0:
            output = 'You Are Not In A Risk'
        elif output == 1:
            output = 'You Are In A Risk. Please Visit A Nephrologist.'
        print(features)
        print(output)
        if form.is_valid():
            print('saving')
            form.save()
        ob = models.UserPredictDataModel.objects.latest('id')
        ob.Attack_type = output
        ob.save()
        return render(request, 'new/index.html', {'prediction_text':output,'form':form})
    else:
        print('ELSE')
        form = forms.UserPredictDataForm(request.POST)
    return render(request, 'new/index.html', {'form':form})



def view_all(request):
    model = models.UserPredictDataModel.objects.all()
    #print(model)
    return render(request, 'new/all.html', {'model':model})



def view_last(request):
    if request.method == "POST":
        form = forms.FeedForm(request.POST)
        #print('form',form)
        if form.is_valid():
            form.save()
            model = models.UserPredictDataModel.objects.latest('id')
            #print(model)
            return render(request, 'new/last.html', {'model':model,'msg':'Feedback sent'})
        else:
            model = models.UserPredictDataModel.objects.latest('id')
            return render(request, 'new/last.html', {'model':model,'msg':'Feedback Error'})
    else:
        form = forms.FeedForm()
        model = models.UserPredictDataModel.objects.latest('id')
    return render(request, 'new/last.html', {'model':model,'form':form})
        


def feedback(request):
    model = models.FeedModel.objects.latest('id')
    return render(request, 'new/feedback.html', {'model':model})

def apredict(request):
    return render(request, 'new/index.html')

def logout_view(request):
    logout(request)
    return redirect('home_view')

