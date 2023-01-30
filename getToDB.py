import face_recognition
import sqlite3
import numpy as np

def get_face_encodings():
    conn = sqlite3.connect('faces.db')
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT name, encoding
        FROM faces
    """)
    
    face_encodings = cursor.fetchall()
    
    conn.close()
    
    return face_encodings

known_face_names = []
known_face_encodings = []

face_encodings = get_face_encodings()
for face_encoding in face_encodings:
    known_face_names.append(face_encoding[0])
    known_face_encodings.append(np.frombuffer(face_encoding[1], dtype=np.float64))

# Carrega a imagem para reconhecimento
image = face_recognition.load_image_file("")

# Encontra todas as codificações de rosto na imagem
face_encodings = face_recognition.face_encodings(image)

# Inicializa uma lista para armazenar os nomes das pessoas reconhecidas
face_names = []

for face_encoding in face_encodings:
    # Compara a codificação de rosto da imagem com as codificações conhecidas
    distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    
    # Seleciona o índice da codificação de rosto mais próxima
    best_match_index = np.argmin(distances)
    
    # Adiciona o nome da pessoa correspondente à lista de nomes
    face_names.append(known_face_names[best_match_index])

# Imprime os nomes das pessoas reconhecidas
print(face_names)
