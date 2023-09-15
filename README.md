# Face Recognition App

This is a simple face recognition app that allows users to register their faces and then recognize them later. The app is built using Python, Flask, and DeepFace.

## Prerequisites

To run this app, you will need the following:

* Python 3.6 or later
* Flask
* DeepFace
* Docker


## Installation

To install the app, clone the repository and then run the following commands:

```
pip install -r requirements.txt
python app.py
```

## Usage

To use the app, open your web browser and go to `http://localhost:8080`. You will see two forms: one for registering a face and one for recognizing a face.

To register a face, click the "Choose File" button and select an image of your face. Then, enter your name and click the "Register" button.

To recognize a face, click the "Choose File" button and select an image of a face you want to recognize. Then, click the "Recognize" button.

The app will then use DeepFace to compare the image to the registered faces and return the name of the person if it finds a match.

## Docker

A Dockerfile is included in this repository. To build the Docker image, run the following command:

```
docker build -t face-recognition-app .
```

To run the Docker container, run the following command:


```
docker run -p 8080:8080 face-recognition-app
```

## Conclusion

This is a simple face recognition app that can be used for a variety of purposes. It is easy to use and can be deployed on a variety of platforms.

## Demo 

https://github.com/Jasleenjassi/WeppApp/assets/118040693/1df4d922-d588-4785-8696-c4b803739809
