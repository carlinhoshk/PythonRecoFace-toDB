import sqlite3
import face_recognition
import numpy

# Connect to the database
conn = sqlite3.connect('faces.db')
cursor = conn.cursor()

# Create the table to store the face encodings
cursor.execute('''
CREATE TABLE IF NOT EXISTS faces (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    encoding BLOB NOT NULL
)
''')
conn.commit()

# Load an image and get its face encoding
filename = input("coloque path da imagem: ")
person_name = filename.split(".")[0]

image = face_recognition.load_image_file(filename)
face_encoding = face_recognition.face_encodings(image)[0]

# Store the face encoding in the database
cursor.execute("INSERT INTO faces (name, encoding) VALUES (?, ?)", (person_name, face_encoding.tobytes()))
conn.commit()

# Load the face encodings from the database
cursor.execute("SELECT * FROM faces")
faces = cursor.fetchall()

# Convert the face encodings from bytes back to numpy arrays
known_face_encodings = [numpy.frombuffer(face[2], dtype=numpy.float64) for face in faces]

# Use the face encodings in your face recognition code
# ...

# Close the connection
conn.close()
