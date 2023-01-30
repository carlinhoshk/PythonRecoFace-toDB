from flask import Flask, jsonify, request
import face_recognition

app = Flask(__name__)

known_image = face_recognition.load_image_file("1.jpg")
face_encoding_1 = face_recognition.face_encodings(known_image)[0]
# Armazene as codificações faciais de referência em uma lista
known_face_encodings = [
    face_encoding_1,
    ...
]

# Armazene os nomes correspondentes às codificações de referência em outra lista
known_face_names = [
    "Biden",
    ...
]

@app.route("/recognize", methods=["POST"])
def recognize():
    # Obtenha a imagem da requisição
    image = request.files["image"]
    
    
    unknown_image = face_recognition.load_image_file(image)
    face_encoding_2 = face_recognition.face_encodings(unknown_image)[0]
   
    resultado = str(face_recognition.compare_faces([face_encoding_1], face_encoding_2))
    

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)
