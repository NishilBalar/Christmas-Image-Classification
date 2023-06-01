from flask import Flask, request, jsonify
from app.torch_utils import transform_image, get_prediction


app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
classes = ['christmas_cookies', 'christmas_presents', 'christmas_tree', 'fireworks', 'penguin', 'reindeer', 'santa', 'snowman']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error': 'no file'})
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'format not supported'})
        
        try:
            image = file.read()
            tensor = transform_image(image)
            prediction = get_prediction(tensor)
            data = {'class_name':classes[prediction.item()]}
            return jsonify(data)
        
        except:
            return jsonify({'error': 'error during prediction'})
        
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)