from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (can be replaced with actual data retrieval logic)
items = {
    1: {'id': 1, 'name': 'Item 1', 'description': 'This is item 1.'},
    2: {'id': 2, 'name': 'Item 2', 'description': 'This is item 2.'}
}

@app.route('/items/<int:item_id>', methods=['GET'])
def read_item(item_id):
    # Check if the item exists in the database
    if item_id not in items:
        return jsonify({'error': 'Item not found'}), 404

    # Return the item
    return jsonify(items[item_id])

if __name__ == '__main__':
    app.run(debug=True)
