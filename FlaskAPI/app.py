from flask import Flask, jsonify, request, Response
from BookModel import *
from settings import *
import json

app = Flask(__name__)

#Get all books
@app.route('/books')
def get_books():
    return jsonify({'books': Book.get_all_books()})


@app.route('/books/<int:isbn>')
def get_books_by_isbn(isbn):
    return_value = Book.get_book(isbn)
    return jsonify(return_value)


def validBookObject(bookObject):
    if('name' in bookObject and 'price' in bookObject and 'isbn' in bookObject):
        return True
    else:
        return False

#POST
@app.route('/books/', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if(validBookObject(request_data)):
        Book.add_book(request_data['name'], request_data['price'], request_data['isbn'])
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = '/books/' + str(request_data['isbn'])
        return response
    else:
        invalidBookObjectErrorMsg = {
            "error": "Invalid book object in request",
            "helpString": "Data passsed not in correct format"
        }
        response = Response(invalidBookObjectErrorMsg, status= 400, mimetype= 'application/json')
        return response


#PUT route
@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    Book.replace_book(isnb, request_data['name'],request_data['price'])
    response = Response("", status=204)
    return response

#Patch
@app.route('/books/<int:isbn>', methods=['PATCH'])
def update_book(isbn):
    request_data = request.get_json()
    update_book = {}
    if('name' in request_data):
        Book.update_book_name(isbn, request_data['name'])

    if('price' in request_data):
        Book.update_book_price(isbn, request_data['price'])

    response = Response('', status=204)
    response.headers['Location'] = '/books/' + str(isbn)
    return response


#Delete
@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    if(Book.delete_book(isbn)):
        response = Response('', status= 204)
    response = Response('', status= 404)
    return response

if __name__ == "__main__":
    app.run(debug=True)

