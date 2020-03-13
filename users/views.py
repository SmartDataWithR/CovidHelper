from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def updateUser(request, id):
    user = CustomUser.objects.get(id=id)
    form = CustomUserChangeForm(instance=user)
    print(request.method)
    print(form.is_valid())
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'users/updateUser.html', {'form': form}) 
