from django.shortcuts import get_object_or_404, render, redirect

from django.views.decorators.csrf import csrf_exempt

from .models import Note
from .forms import CreateNote, CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.

## Vulnerability:
## Page can be accessed without logging in
## How to fix:
## add decorator @login_required(login_url="login") to fix access control
def home(request):
    return render(request, "home.html")

## Vulnerability:
## Page can be accessed without logging in
## How to fix:
## add decorator @login_required(login_url="login") to fix access control
def notes(request):
    items = Note.objects.all()
    return render(request, "notes.html", {"notes": items})


## Vulnerability:
## csrf_exempt decorator allows form to be created without csrf-protection
## How to fix:
## Remove decorator, also add csrf_token in new_note.html template

## Vulnerability:
## Page can be accessed without logging in
## How to fix:
## add decorator @login_required(login_url="login") to fix access control
@csrf_exempt
def new_note(request):
    form = CreateNote()
    if request.method == "POST":
        form = CreateNote(request.POST)
        if form.is_valid():
            newnote = form.save(commit=False)
            newnote.author = request.user
            newnote.save()
            return redirect("notes")

    return render(request, "new_note.html", {"form": form})

## Vulnerability:
## Function uses raw SQL query to find note by given id.
## How to fix:
## remove get_note and replace note variable with following code:
## note = get_object_or_404(Note, pk=note_id)

## Vulnerability:
## Page can be accessed without logging in
## How to fix:
## add decorator @login_required(login_url="login") to fix access control
def detail(request, note_id):
    get_note = Note.objects.raw(f"SELECT * FROM main_note WHERE id LIKE '%{note_id}%'")
    note = get_note[0]
    return render(request, 'detail.html', {"note": note})

## Vulnerability:
## Any user can delete notes by just accessing url /notes/<note_id>/delete
## even though the user who added the note should be the only one able to do this
## How to fix:
## fix by replacing delete function with following code:
    ##note = get_object_or_404(Note, pk=note_id)
    ##if request.method == "POST":
        ##note.delete()
        ##return redirect("notes")
    ##return render(request, 'detail.html', {"note": note})

## Vulnerability:
## Page can be accessed without logging in
## How to fix:
## add decorator @login_required(login_url="login") to fix access control
def delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect("notes")

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    
    return render(request, "register.html", {"form": form})

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("home")

    return render(request, "login.html", {"form": form})

## Vulnerability:
## Page can be accessed without logging in
## How to fix:
## add decorator @login_required(login_url="login") to fix access control
def logout(request):
    auth.logout(request)

    return redirect("login")