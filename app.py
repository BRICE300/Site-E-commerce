from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

products = [
    {
        'id': 1,
        'name': 'Laptop',
        'price': 1200
    },
    {
        'id': 2,
        'name': 'Keyboard',
        'price': 100
    },
    {
        'id': 3,
        'name': 'Mouse',
        'price': 50
    }
]

cart = []

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    for product in products:
        if product['id'] == product_id:
            cart.append(product)
            break

    return redirect(url_for('home'))

@app.route('/cart')
def view_cart():
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/remove/<int:index>')
def remove_from_cart(index):
    if index < len(cart):
        cart.pop(index)

    return redirect(url_for('view_cart'))

if __name__ == '__main__':
    app.run(debug=True)