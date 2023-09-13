import os
import uuid
from flask import Flask, request, render_template, send_file
from deepface import DeepFace
import hashlib

app = Flask(__name__)

# Create a folder for storing registered faces if it doesn't exist
registered_faces_folder = 'registered_faces_images'
if not os.path.exists(registered_faces_folder):
    os.makedirs(registered_faces_folder)

# Create a dictionary to store registered faces (name as key and image path as value)
registered_faces = {}

# Placeholder route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to register a face
@app.route('/register-face', methods=['POST'])
def register_face():
    try:
        # Get the face image and the name of the person
        face_image = request.files['image']
        person_name = request.form['person_name']

        # Generate a unique filename using uuid
        unique_filename = f"{person_name}_{str(uuid.uuid4())}.jpg"
        face_image_path = os.path.join(registered_faces_folder, unique_filename)

        # Save the face image
        if face_image:
            face_image.save(face_image_path)

            # Store the face image path in the registered_faces dictionary
            registered_faces[person_name] = face_image_path

            return 'Face registered successfully!'
        else:
            return 'No image file provided for registration'
    except KeyError:
        return 'Name field is missing in the request'

# Route to recognize a face
@app.route('/recognize-face', methods=['POST'])
def recognize_face():
    # Assuming we receive an image file in the request
    face_image = request.files['image']

    if face_image:
        try:
            # Verify the face using DeepFace
            image_path_list = [face_image]
            img2_path = face_image.filename
            face_image_hash = hashlib.sha1(face_image.read()).hexdigest()

            # Iterate over the registered faces
            for name, registered_face_path in registered_faces.items():
                # Get the registered face hash
                registered_face_hash = hashlib.sha1(open(registered_face_path, 'rb').read()).hexdigest()

                # Compare the face image hashes
                if face_image_hash == registered_face_hash:
                    print(person_name)
                    return send_file(registered_face_path, mimetype='image/jpg')
                    

            return 'Face not recognized'
        except Exception as e:
            return f'Error recognizing face: {str(e)}'
    else:
        return 'No image file provided for recognition'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
