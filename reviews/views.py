from django.shortcuts import render
from .utils import average_rating
from .models import Review, Book,  Publisher,  Profile
def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()

        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
            book_list.append({'book': book, 'book_rating': book_rating, 'number_of_reviews': number_of_reviews})
        else:
            book_rating = None
            number_of_reviews = 0
            book_list.append({'book': book, 'book_rating': book_rating, 'number_of_reviews': number_of_reviews})
    #books = Book.objects.all()
    context = {
        'books':books,
        'book_list': book_list,
    }
    return render(request, 'reviews/book_list.html', context)

def index(request):
    return render(request, 'reviews/index.html')

def book_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        review = None

    context = {
        'review':review
    }

    return render(request, 'reviews/book_detail.html', context)
