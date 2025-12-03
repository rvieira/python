from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Setting up logging
logging.basicConfig(level=logging.DEBUG)

# Sample data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    app.logger.info('Retrieving all books')
    return jsonify(books)

# Route to get a specific book by id
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    app.logger.info('Retrieving book with ID: %s', id)
    book = next((book for book in books if book['id'] == id), None)
    if book:
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    app.logger.info('Adding new book: %s', new_book)
    books.append(new_book)
    return jsonify({"message": "Book added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=False)

