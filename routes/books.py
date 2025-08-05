from flask import Blueprint, jsonify, request


books_bp= Blueprint('books', __name__)


books_list = [{
    "id": 1,
    "name": 'Pepito grillo',
    "author": "Fran",
    "date": "17/01/1150"
},
{
    "id": 2,
    "name": 'Macarena',
    "author": "Jesusito",
    "date": "17/01/1150"
}]

books_id = 3

@books_bp.route('/books', methods= ['GET'])
def show_books():
    return jsonify(books_list), 200

@books_bp.route('/books/<int:id>', methods= ['GET'])
def get_book(id):
    for book in books_list:
        if id == book['id']:
            return jsonify(book), 200
    
    return jsonify({
        'message': 'Libro no encontrado'
    }), 404

@books_bp.route('/books', methods= ['POST'])
def create_book():
    global books_id
    data = request.get_json()

    name = data.get('name')
    author = data.get('author')
    date = data.get('date')

    if not name or not author or not date:
        return jsonify({
            'message': 'Es obligatorio rellenar todos los campos'
        }), 422
    
    new_book = {
        "id": books_id,
        "name": name,
        "author": author,
        "date": date
    }

    books_id += 1

    books_list.append(new_book)

    return jsonify({
        'message': 'Libro creado correctamente',
        'book': new_book
    }), 201

@books_bp.route('/books/<int:id>', methods= ['DELETE'])
def delete_book(id):
    for book in books_list:
        if id == book['id']:
            books_list.remove(book)
            return jsonify({
                'message': 'Libro eliminado correctamente',
                'book': book
            }), 202
        
    return jsonify({
            'message': 'Libro no encontrado'
        }), 422

@books_bp.route('/books/<int:id>', methods= ['PATCH'])
def update_book(id):

    data = request.get_json()

    for book in books_list:
        if id == book['id']:
            book.update(data)
            return jsonify({
                'message': 'Libro modificado con exito',
                'book': book
            }), 202
    
    return jsonify({
            'message': 'Libro no encontrado'
        }), 422
