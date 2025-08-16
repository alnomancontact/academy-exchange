from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        # Handle registration form submission here
        # For example, create a new user:
        # from django.contrib.auth.forms import UserCreationForm
        # form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('login') # Redirect to login after successful registration
        pass # Placeholder for actual registration logic
    else:
        # For GET requests, just display the registration form
        pass # Placeholder if you need a form object for the template, e.g., form = UserCreationForm()
    
    return render(request, 'register.html') # Make sure this points to your register template name

def profile_view(request):
    return render(request, 'profile.html')

def history_view(request):
    return render(request, 'history.html')