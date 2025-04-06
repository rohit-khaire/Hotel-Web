from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__, static_folder='static', template_folder='templates')

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Add your password
    database="hotel_system"
)
cursor = conn.cursor(dictionary=True)

@app.route("/admin")
def dashboard():
    cursor.execute("SELECT * FROM rooms")
    rooms = cursor.fetchall()
    return render_template("admin_dashboard.html", rooms=rooms)

@app.route("/admin/add", methods=["GET", "POST"])
def add_room():
    if request.method == "POST":
        hotel_id = request.form["hotel_id"]
        room_number = request.form["room_number"]
        image_url = request.form["image_url"]
        cursor.execute("INSERT INTO rooms (hotel_id, room_number, image_url) VALUES (%s, %s, %s)", (hotel_id, room_number, image_url))
        conn.commit()
        return redirect("/admin")
    return render_template("add_room.html")

@app.route("/admin/delete/<int:room_id>")
def delete_room(room_id):
    cursor.execute("DELETE FROM rooms WHERE id=%s", (room_id,))
    conn.commit()
    return redirect("/admin")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
