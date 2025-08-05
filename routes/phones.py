from flask import Blueprint, jsonify, request

phones_bp = Blueprint('phones', __name__)

phone_list = [{
    "id": 1,
    "name": "Motorola",
    "year": "2002"
},
{
    "id": 2,
    "name": "Nokia 3410",
    "year" : "2000"
}]


phone_id = 3

@phones_bp.route('/phone', methods= ['GET'])
def show_phones():
    try:
        return jsonify(phone_list), 200
    
    except Exception as e:
        return jsonify({
            'message': 'Ocurrio un error en el servidor',
            'detail': str(e)
        }), 500
    
@phones_bp.route('/phone/<int:id>', methods= ['GET'])
def get_phone(id):
    try:

        for phone in phone_list:
            if id == phone['id']:
                return jsonify(phone), 202
        
        return({
                'message': 'Telefono no encontrado'
            }), 404
    
    except Exception as e:
       return ({
           'detail': str(e)
       }), 500
    
@phones_bp.route('/phone', methods= ['POST'])
def create_phone():
    global phone_id

    try:
        data = request.get_json()

        name = data.get('name')
        year = data.get('year')

        if not name or not year:
            return jsonify({
                'message': 'Rellena todos los campos atontao'
            }), 422
        
        new_phone = {
            "id": phone_id,
            "name": name,
            "year" : year
        }

        phone_id += 1

        phone_list.append(new_phone)

        return jsonify({
            'message': 'Telefono registrado',
            'phone': new_phone
        }), 201

    except Exception as e:
        return ({
           'detail': str(e)
       }), 500
    
@phones_bp.route('/phone/<int:id>', methods= ['DELETE'])
def delete_phone(id):

    try:
        for phone in phone_list:
            if id == phone['id']:
                phone_list.remove(phone)
                return jsonify({
                    'message': 'Telefono eliminado',
                    'phone': phone
                }), 200
        return jsonify({
                'message': 'Telefono no encontrado'
            }), 404
        
    
    except Exception as e:
        return ({
           'detail': str(e)
       }), 500

@phones_bp.route('/phone/<int:id>', methods= ['PUT'])
def update_phone(id):

    try: 
        data = request.get_json()

        for phone in phone_list:
            if id == phone['id']:
                phone.update(data)
                return jsonify({
                    'message': 'Telefono actualizado'
                }), 202
        
        return jsonify({
            'message': 'Telefono no encontrado'
            }), 404
    
    except Exception as e:
        return ({
           'detail': str(e)
       }), 500