from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ItemForm
from .models import Profile
from .models import Profile, Item
from .models import Item, Purchase
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm



def home_view(request):
    return render(request, 'home.html') 

def about_view(request):
    return render(request, 'about.html')

# Registration view
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from .models import Profile

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # creates User and hashes password

            # Safely create a Profile only if it doesn't exist
            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={
                    'phone_number': form.cleaned_data.get('phone_number'),
                    'university_id': form.cleaned_data.get('university_id')
                }
            )

            messages.success(request, "Registration successful! You can now log in.")
            login(request, user)  # optional: auto login after register
            return redirect('home')  # change to your home URL
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # logs the user in
                messages.success(request, f'Welcome back, {username}!')
                return redirect('exchange')  # redirect directly to exchange page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Profile view
def profile_view(request):
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

# History view
def history_view(request):
    return render(request, 'history.html')

def exchange_view(request):
    form = None

    # If logged in and submitting a form to add item
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ItemForm(request.POST)
            if form.is_valid():
                item = form.save(commit=False)
                item.owner = request.user
                item.save()
                return redirect('exchange')
        else:
            form = ItemForm()

    # Search query
    query = request.GET.get('q', '')
    if query:
        items = Item.objects.filter(title__icontains=query).order_by('-created_at')
    else:
        items = Item.objects.all().order_by('-created_at')

    return render(request, 'exchange.html', {
        'form': form,
        'items': items,
        'query': query
    })

@login_required
def buy_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    Purchase.objects.create(user=request.user, item=item)
    return redirect('profile')

@login_required
def profile_view(request):
    purchases = Purchase.objects.filter(user=request.user).select_related('item')
    return render(request, 'profile.html', {'purchases': purchases})




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = f"Message from {form.cleaned_data['name']} ({form.cleaned_data['email']}):\n\n{form.cleaned_data['message']}"
            sender = form.cleaned_data['email']

            send_mail(
                subject,
                message,
                sender,
                ['your_email@example.com'],  # Change to your email
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
