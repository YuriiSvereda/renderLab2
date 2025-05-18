from flask import Flask, request, jsonify

app = Flask(__name__)

# Тестова база даних (у пам'яті)
data = {}

@app.route("/")
def home():
    return "Hello from Python + Render!"

# CREATE
@app.route("/item", methods=["POST"])
def create_item():
    item = request.json
    item_id = item["id"]
    data[item_id] = item
    return jsonify({"message": "Item created", "item": item}), 201

# READ
@app.route("/item/<item_id>", methods=["GET"])
def get_item(item_id):
    item = data.get(item_id)
    if not item:
        return jsonify({"error": "Not found"}), 404
    return jsonify(item)

# UPDATE
@app.route("/item/<item_id>", methods=["PUT"])
def update_item(item_id):
    if item_id not in data:
        return jsonify({"error": "Not found"}), 404
    data[item_id].update(request.json)
    return jsonify({"message": "Item updated", "item": data[item_id]})

# DELETE
@app.route("/item/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    if item_id in data:
        del data[item_id]
        return jsonify({"message": "Item deleted"})
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
