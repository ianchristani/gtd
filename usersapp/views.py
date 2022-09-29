from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# pagina de usuario nao logado
def index(request):
    return render(request, 'index.html')

# pagina de registro
def signup_view(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)    
        if signup_form.is_valid():
            validated_user = signup_form.save()
            login(request, validated_user)
            return redirect('crud:list_products')
    else:
        signup_form = UserCreationForm()
    return render(request, 'signup.html', {'signupform':signup_form})

# pagina de login
def login_view(request):
    if request.method == 'POST':
        authform = AuthenticationForm(data=request.POST)
        if authform.is_valid():
            validated_user = authform.get_user()
            login(request, validated_user)
            return redirect('crud:list_products')
    else:
        authform = AuthenticationForm()
    return render(request, 'login.html', {'auth_form':authform})


# pagina de logout
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('usersapp:index')
    else:
        return render(request, 'logout.html')