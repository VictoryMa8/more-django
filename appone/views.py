from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre

# Create your views here.
def index(request):
    """View function for the home page"""

    # Get the number of rows (entries) for some of our tables
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Get available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Here, the 'all()' is implied by default
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# Using a class-based generic list view (ListView) - a class that inherits from an existing view
# The generic view already implements most of the functionality we need and follows Django best-practice
class BookList(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 10
    # With paginate_by, when we have >10 records, the view will start paginating the data it sends to the template
    # The different pages are accessed using GET parameters — to access page 2 we use the URL /appone/books/?page=2

class BookDetail(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class AuthorList(generic.ListView):
    model = Author
    template_name = 'author_list.html'
    paginate_by = 10

class AuthorDetail(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'