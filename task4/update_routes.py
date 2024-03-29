from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (can be replaced with actual data retrieval and storage logic)
items = {
    1: {'id': 1, 'name': 'Item 1', 'description': 'This is item 1.'},
    2: {'id': 2, 'name': 'Item 2', 'description': 'This is item 2.'}
}

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    # Check if the item exists in the database
    if item_id not in items:
        return jsonify({'error': 'Item not found'}), 404

    # Get the updated data from the request
    update_data = request.json

    # Update the item with the new data
    items[item_id].update(update_data)

    # Return the updated item
    return jsonify(items[item_id])

if __name__ == '__main__':
    app.run(debug=True)
