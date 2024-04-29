from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, ProfileForm, UserForm
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-jobs')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'registration/profile.html', {'profile': profile})

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        profileform = ProfileForm(request.POST,request.FILES,instance=profile )
        if profileform.is_valid():
            profileform.save()
            return redirect('profile')
        
    else :
        profileform = ProfileForm(instance=profile)
    return render(request,'registration/profile_edit.html',{'profileform':profileform})

def user_edit(request):
    user = request.user
    if request.method=='POST':
        userform = UserForm(request.POST, instance=user )
        if userform.is_valid():
            userform.save()
            return redirect('profile')
        
    else :
        userform = UserForm(instance=user)
    return render(request,'registration/useredit.html',{'userform':userform})