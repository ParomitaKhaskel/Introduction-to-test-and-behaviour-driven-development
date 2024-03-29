from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (can be replaced with actual data retrieval and storage logic)
items = [
    {'id': 1, 'name': 'Item 1', 'category': 'Category A', 'availability': True, 'description': 'This is item 1.'},
    {'id': 2, 'name': 'Item 2', 'category': 'Category B', 'availability': False, 'description': 'This is item 2.'}
]

@app.route('/items', methods=['GET'])
def list_all_items():
    return jsonify(items)

@app.route('/items/search', methods=['GET'])
def search_items():
    name = request.args.get('name')
    category = request.args.get('category')
    availability = request.args.get('availability')

    filtered_items = items

    if name:
        filtered_items = [item for item in filtered_items if name.lower() in item['name'].lower()]

    if category:
        filtered_items = [item for item in filtered_items if category.lower() == item['category'].lower()]

    if availability:
        availability = availability.lower() == 'true'  # Convert 'true' string to boolean
        filtered_items = [item for item in filtered_items if item['availability'] == availability]

    return jsonify(filtered_items)

if __name__ == '__main__':
    app.run(debug=True)
