from flask import Flask, render_template, Blueprint, redirect, request 
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint('books', __name__)

# INDEX
# GET '/books'
@books_blueprint.route("/books")
def book():  
    book = book_repository.select_all()
    return render_template("books/index.html", all_books=book)


# NEW
# GET '/books/new'
@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)



# CREATE
# POST '/books'
@books_blueprints.route("/books", methods=['POST'])
def create_book():
    title    = request.form['title']
    genre = request.form['genre']
    publisher   = request.form['publisher']
    author  = author_repository.select(request.form['author_id'])
    book = Book(title, genre, publisher, author)
    book_repository.save(book)
    return redirect('/books')


# EDIT
# GET '/books/<id>/edit'
@books_blueprint.route("/books/<id>/edit", methods=['GET'])
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('books/edit.html', book = book, all_authors = authors)

# UPDATE
# PUT '/books/<id>'
@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    title    = request.form['title']
    genre = request.form['genre']
    publisher   = request.form['publisher']
    author  = author_repository.select(request.form['author_id'])
    book = Book(title, genre, publisher, author, id)
    print(book.author.full_name())
    book_repository.update(book)
    return redirect('/books')

# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')
