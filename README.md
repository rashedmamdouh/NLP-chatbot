# NLP Chatbot using Python Frameworks

This is a Natural Language Processing (NLP) chatbot developed using various Python frameworks such as Openfabric-pysdk, Flask-SocketIO, Marshmallow, nltk, wikipedia and Werkzeug. The chatbot uses NLP techniques to understand natural language input and provide appropriate responses.

## Requirements

The following libraries are required to run the chatbot:

* Python 3.x
* Openfabric-pysdk
* Flask-SocketIO
* Marshmallow
* Werkzeug
* nltk
* wikipedia

## Installation

1. Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/rashedmamdouh/NLP-chatbot
   ```

2. Change directory to the project folder:

   ```
   cd nlp-chatbot
   ```

3. Install the required libraries

## Usage

1. Start the server by running the following command:

   ```
   python app.py
   ```

2. Once the server is running, open a web browser and go to `http://localhost:5000` to access the chatbot.

## Configuration

The chatbot can be configured by modifying the `config.py` function. The following configuration options are available:

* `DEBUG`: Whether or not to run the app in debug mode.
* `HOST`: The hostname to listen on.
* `PORT`: The port to listen on.
* `SECRET_KEY`: The secret key used to sign session cookies.
* `SESSION_TYPE`: The type of session interface to use.

## Acknowledgments

* Special thanks to the developers of the Python frameworks used in this project.
