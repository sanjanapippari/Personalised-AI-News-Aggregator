from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignupForm, LoginForm
from .models import CustomUser, UserFeedback
from news.models import Headline  # ✅ Import your Headline model
from twilio.rest import Client
from django.contrib.auth.decorators import login_required
from django import forms


# ------------------------------
# Signup Form (with phone, location)
# ------------------------------
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'location', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


#
# ------------------------------
# Signup View
# ------------------------------
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)

            # ✅ Send SMS to user's phone with location-based headlines
           

            return redirect('home')
        else:
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})


# ------------------------------
# Login View
# ------------------------------
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'users/login.html')


# ------------------------------
# Logout View
# ------------------------------
def logout_view(request):
    logout(request)
    return redirect('login')


# ------------------------------
# Liked Articles View
# ------------------------------
@login_required
def liked_articles_view(request):
    liked = UserFeedback.objects.filter(user=request.user, action='like')
    return render(request, 'liked_articles.html', {'articles': liked})


# ------------------------------
# Disliked Articles View
# ------------------------------
@login_required
def disliked_articles_view(request):
    disliked = UserFeedback.objects.filter(user=request.user, action='dislike')
    return render(request, 'disliked_articles.html', {'articles': disliked})
