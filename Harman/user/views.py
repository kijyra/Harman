from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View
from user.forms import UserCreationForm
class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
