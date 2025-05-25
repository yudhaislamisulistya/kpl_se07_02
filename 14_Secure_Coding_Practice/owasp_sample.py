# Contoh Salah
@app.route('/user/<int:id>')
def get_user(id):
    user = db.get_user_by_id(id)
    return jsonify(user)

# Contoh Benar
@app.route('/user/<int:id>')
@login_required
def get_user(id):
    if current_user.id != id:
        abort(403)  # Forbidden
    user = db.get_user_by_id(id)
    return jsonify(user)