from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.models import User


from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'cuberecords/index.html', {})


def preparation(request):
    return render(request, 'cuberecords/preparation.html', {})


def stage_one(request):
    return render(request, 'cuberecords/Stage1.html', {})


def stage_two(request):
    return render(request, 'cuberecords/Stage2.html', {})


def stage_three(request):
    return render(request, 'cuberecords/Stage3.html', {})


def log_in(request):
    if request.method == 'POST':
        logout(request)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
            else:
                form.add_error('Invalid credentials!')
    else:  # GET
        form = LoginForm()
    return render(request, 'cuberecords/login.html', {'form': form})


def log_out(request):
    logout(request)
    redirect_url = request.GET.get('next') or reverse('index')
    return redirect(redirect_url)


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            logout(request)

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_again = form.cleaned_data['password_again']

            if User.objects.filter(username=username).exists():
                form.add_error('username', 'User already exists!')
            elif password != password_again:
                form.add_error('password_again', 'Passwords mismatch!')
            else:
                user = User.objects.create_user(username, email, password)
                login(request, user)
                notes = Note.objects.order_by('spent_time')
                context = {
                    'notes': notes,
                }
                return render(request, 'cuberecords/records.html', context)
    else: # GET
        form = RegistrationForm()
    return render(request, 'cuberecords/signup.html', {'form': form})


def records(request):
    notes = Note.objects.order_by('spent_time')
    return render(request, 'cuberecords/records.html', {'notes': notes})


def record_and_comments(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = request.user
            comment = form.cleaned_data['comment']
            Comment(note=note, text=comment, author=author).save()

    form = CommentForm()
    context = {
        'note': note,
        'comments': note.comment_set.order_by('-created_at'),
        'form': form,
    }
    return render(request, 'cuberecords/record_and_comments.html', context)


def account(request):
    if request.method == 'POST':
        form = RecordRequestForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            spent_time = form.cleaned_data['spent_time']

            Record_request(text=description, spent_time=spent_time).save()

    form = RecordRequestForm()
    requests = Record_request.objects.all()
    context = {
        'form': form,
        'requests': requests,
    }
    return render(request, 'cuberecords/account.html', context)


def accept(request, req_id):
    req = get_object_or_404(Record_request, id=req_id)
    Note(text=req.text, spent_time=req.spent_time).save()
    req.delete()

    form = RecordRequestForm()
    requests = Record_request.objects.all()
    context = {
        'form': form,
        'requests': requests,
    }
    return render(request, 'cuberecords/account.html', context)


def reject(request, req_id):
    req = get_object_or_404(Record_request, id=req_id)
    req.delete()

    form = RecordRequestForm()
    requests = Record_request.objects.all()
    context = {
        'form': form,
        'requests': requests,
    }
    return render(request, 'cuberecords/account.html', context)


def record_request(request):
    if request.method == 'POST':
        form = RecordRequestForm(request.POST)  # , request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                spent_time = float(form.cleaned_data['spent_time'])
            except ValueError:
                form.add_error('spent_time', 'Should be time in seconds')

            #document = request.FILES['document']

            Record_request(spent_time=spent_time, text=username).save()

            return redirect('records')

    else:  # GET
        form = RecordRequestForm()
    return render(request, 'cuberecords/make_request.html', {'form': form})
