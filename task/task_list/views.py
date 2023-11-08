from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import CustomUserCreationForm, LoginForm
from .models import CustomUser, Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def registration(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        context = {
            "form": CustomUserCreationForm(),
        }
        if request.method == "POST":
            user_form = CustomUserCreationForm(request.POST, request.FILES)
            if user_form.is_valid():
                clean_data = user_form.cleaned_data
                user = CustomUser(
                    name=clean_data["name"],
                    email=clean_data["email"],
                )
                user.set_password(clean_data["password1"])
                user.is_staff = True
                user.is_superuser = True
                user.save()

                return redirect("/")
            else:
                context[
                    "error"
                ] = "Пороли не совпадают. Либо длинна пороля меньше 5 символов"

        return render(request, "registration.html", context)


def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(
                email=clean_data["email"], password=clean_data["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("task_list")
                else:
                    return HttpResponse("Disable account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def task_list(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.filter(user=request.user)
    return render(request, "tasks/task_list.html", {"tasks": tasks})


@login_required
def create_task(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(user=request.user, title=title, description=description)
        return redirect("task_list")
    return render(request, "tasks/create_task.html")


@login_required
def complete_task(request: HttpRequest, task_id: int) -> HttpResponse:
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")


@login_required
def update_task(request: HttpRequest, task_id: int) -> HttpResponse:
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.save()
        return redirect("task_list")
    context = {
        "task": task,
    }
    return render(request, "tasks/update_task.html", context)


@login_required
def delete_task(request: HttpRequest, task_id: int) -> HttpResponse:
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("task_list")
