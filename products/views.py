from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect ,get_object_or_404
from .models import Package
from .forms import PackageForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib import messages
from .models import Profile

def home(request):
    packages = Package.objects.filter(status='approved', expiry_date__gte=timezone.now().date())
    return render(request, 'index.html', {'packages': packages})

@login_required
def product_detail(request,id):

    product = Package.objects.filter(id=id)

    if request.user.profile.role == 'vendor':
        return redirect('logout')
    return render(request, 'product-detail.html',{'packages':product})

@login_required
def create_package(request):
    if request.user.profile.role != 'vendor':
        return redirect('home')

    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            pkg = form.save(commit=False)
            pkg.vendor = request.user
            pkg.save()
            return redirect('dashboard')
    else:
        form = PackageForm()
    return render(request, 'create_package.html', {'form': form})

@login_required
def dashboard(request):
    packages = Package.objects.filter(vendor=request.user)
    return render(request, 'products.html', {'packages': packages})




def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! Please log in.")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'sign-up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            role = user.profile.role
            if role == 'vendor':
                return redirect('dashboard')
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'sign-in.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def edit_package(request, pk):
    package = get_object_or_404(Package, pk=pk, vendor=request.user)
    print(package.description)

    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PackageForm(instance=package)

    return render(request, 'edit_packages.html', {'form': form, 'package': package})

@login_required
def delete_package(request, pk):
    package = get_object_or_404(Package, pk=pk, vendor=request.user)
    package.delete()
    return redirect('dashboard')

def payment(request):
    return render(request,'payment.html')


