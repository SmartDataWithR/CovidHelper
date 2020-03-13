from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.db import transaction

# Create your views here.
@login_required
@transaction.atomic
def updateUser(request, id):
    user = CustomUser.objects.get(id=id)
    form = CustomUserChangeForm(instance=user)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = CustomUserChangeForm(request.POST, instance=user)
            context = {'form': form}
    return render(request, 'users/updateUser.html', {'form': form}) 
