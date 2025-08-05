from flask import Flask
from routes.books import books_bp
from routes.phones import phones_bp

app = Flask(__name__)
app.register_blueprint(books_bp)
app.register_blueprint(phones_bp)







if __name__ == '__main__':
    app.run(debug= True, host='0.0.0.0', port= 5000)