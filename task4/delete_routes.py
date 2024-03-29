from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (can be replaced with actual data retrieval and storage logic)
items = {
    1: {'id': 1, 'name': 'Item 1', 'description': 'This is item 1.'},
    2: {'id': 2, 'name': 'Item 2', 'description': 'This is item 2.'}
}

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    # Check if the item exists in the database
    if item_id not in items:
        return jsonify({'error': 'Item not found'}), 404

    # Delete the item from the database
    del items[item_id]

    # Return a success message
    return jsonify({'message': 'Item deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
