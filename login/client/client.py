from flask import Flask, render_template, request, redirect
import mysql.connector
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Add your password
    database="hotel_system"
)
cursor = conn.cursor(dictionary=True)

@app.route("/")
def user_dashboard():
    cursor.execute("SELECT * FROM hotels")
    hotels = cursor.fetchall()
    return render_template("user_dashboard.html", hotels=hotels)

@app.route("/rooms/<int:hotel_id>")
def show_rooms(hotel_id):
    cursor.execute("SELECT * FROM rooms WHERE hotel_id=%s AND is_booked=FALSE", (hotel_id,))
    rooms = cursor.fetchall()
    return render_template("checkin.html", rooms=rooms, hotel_id=hotel_id)

@app.route("/book/<int:room_id>", methods=["POST"])
def book_room(room_id):
    username = request.form['username']
    cursor.execute("UPDATE rooms SET is_booked=TRUE WHERE id=%s", (room_id,))
    cursor.execute("INSERT INTO bookings (room_id, username, checkin_date) VALUES (%s, %s, %s)", (room_id, username, datetime.now()))
    conn.commit()
    return redirect("/")

@app.route("/checkout/<int:room_id>", methods=["POST"])
def checkout(room_id):
    cursor.execute("UPDATE rooms SET is_booked=FALSE WHERE id=%s", (room_id,))
    cursor.execute("UPDATE bookings SET checkout_date=%s WHERE room_id=%s AND checkout_date IS NULL", (datetime.now(), room_id))
    conn.commit()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True, port=5002)
