from django.shortcuts import render, redirect
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .models import Book
from .forms import BookForm

def home(request):
    if request.method =='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    else:
        form = BookForm()
    return render(request,'home.html',{'form':form})

def generate_pdf(request):
    response = FileResponse(generate_pdf_file(),as_attachment = True, name = 'mypdf.pdf')
    return response

def generate_pdf_file():
    from io import BytesIO
    buffer = BytesIO
    p = canvas.Canvas(buffer)
    
    books = Book.objects.all()
    p.drawstring(100,750,"Book Catalog")

    for book in books:
        p.drawstring(100,y,f"Title: {book.title}")
        p.drawstring(100,y-20,f"Author: {book.author}")
        p.drawstring(100,y-40,f"Year: {book.publication_year}")
        y = y-60

        p.showPage()
        p.save()
        buffer.seek(0)

        return buffer
    