from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContact

# Create your views here.


def login(request):
    if request.method != 'POST':
        return render(request, 'account/login.html')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')

    # Authenticating
    login_user = auth.authenticate(request, username=user, password=pwd)
    if not login_user:
        messages.error(request, 'Your login or password is incorrect.')
        return render(request, 'account/login.html')
    else:
        auth.login(request, login_user)
        messages.success(request, 'You was log in with successful  :)')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect(login)


def register(request):
    if request.method != 'POST':
        return render(request, 'account/register.html')

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    user = request.POST.get('user')
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    repeat_pwd = request.POST.get('repeat_pwd')

    # Checking fields (are empty or not).

    # Checking all fields.
    if not first_name or not last_name or not user or not email or not pwd or not repeat_pwd:
        messages.error(request, 'Please complete your subscription.')
        return render(request, 'account/register.html')

    # Checking passwords
    if len(pwd) < 8:
        messages.error(request, 'Please insert a password with 8 characters or more.')
        return render(request, 'account/register.html')
    if pwd != repeat_pwd:
        messages.error(request, 'Yours passwords not is same.')
        return render(request, 'account/register.html')

    # Checking email
    try:
        validate_email(email)
    except:
        messages.error(request, 'Invalid email')
        return render(request, 'account/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'This email already was registered.')
        return render(request, 'account/register.html')

    # Checking user
    if len(user) < 6:
        messages.error(request, 'Your user have should  6 character in minimum.')
        return render(request, 'account/register.html')

    if User.objects.filter(username=user).exists():
        messages.error(request, 'This user already exist.')
        return render(request, 'account/register.html')

    # Success in register
    messages.success(request, 'User registered with success. Now, log in.')
    new_user = User.objects.create_user(username=user, email=email, password=pwd, first_name=first_name,
                                        last_name=last_name)
    new_user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContact()
        return render(request, 'account/dashboard.html', { 'form' : form})

    form = FormContact(request.POST, request.FILES)
    if not form.is_valid():
        messages.error(request, 'Error in send form.')
        form = FormContact(request.POST)
        return render(request, 'account/dashboard.html', {'form': form})

    form.save()
    messages.success(request, f'Contact {request.POST.get("nome")} saved with success.')
    return redirect('dashboard')



