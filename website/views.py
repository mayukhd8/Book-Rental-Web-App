from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import Book, Category,Rental
from .forms import BookForm, RegisterForm,LoginForm,RentBookForm
from django.shortcuts import get_object_or_404
import datetime
import json






def book_list(request):
    """View to list all books"""
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, book_id):
    """View to show details of a single book"""
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def book_create(request):
    """View to add a new book"""
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def book_update(request, book_id):
    """View to edit a book"""
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

def book_delete(request, book_id):
    """View to delete a book"""
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')



# ----------------------#
#Login , Logout , Registration



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Complete ")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'registrations/register.html',{'form':form})


# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('book_list')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'registrations/login.html', {'form': form})

# Logout View
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


#++++++++++++++++++++++++++++++++++++++++++++++++#

@login_required
def rent_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Pre-calculate prices for all durations to pass to the template
    rental_prices = {
        1: float(book.calculate_rental_price(1)),
        3: float(book.calculate_rental_price(3)),
        6: float(book.calculate_rental_price(6)),
        9: float(book.calculate_rental_price(9)),
    }

    if not book.available_copies:
        messages.error(request, "Sorry, this book is currently unavailable for rent.")
        return redirect('book_list')

    if book.owner == request.user:
        messages.error(request, "You can't rent your own book!")
        return redirect('book_list')

    if request.method == 'POST':
        form = RentBookForm(request.POST)
        if form.is_valid():
            rental_duration = int(form.cleaned_data['rental_duration'])
            rental_price = rental_prices[rental_duration]

            # Create the rental with the selected duration
            rental = Rental.objects.create(book=book, renter=request.user, rental_duration=rental_duration,total_fee=rental_price)
            book.available = False
            book.save()

            messages.success(request, f'You have successfully rented "{book.title}" for {rental_duration} month(s) and Total Fee is {rental.total_fee}!')
            return redirect('book_list')
    else:
        form = RentBookForm()
        #rental_price = rental_prices[1]

    return render(request, 'Books/rent_book.html', {'book': book, 'form': form , 'rental_prices':json.dumps(rental_prices)})

#++++++++++++++++++++# User Dashboard

def get_greeting():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"



@login_required
def user_dashboard(request):
    # Books rented by the user
    rented_books = Rental.objects.filter(renter=request.user)

    # Books provided for rental by the user
    provided_books = Book.objects.filter(owner=request.user)

    # Earnings calculation
    total_earnings = sum(rental.book.price * rental.rental_duration * 30 for rental in Rental.objects.filter(book__owner=request.user))

    context = {
        'rented_books': rented_books,
        'provided_books': provided_books,
        'total_earnings': total_earnings,
        'greeting': get_greeting(),
    }
    return render(request, 'dashboard.html', context)