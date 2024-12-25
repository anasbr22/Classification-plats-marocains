from flask import Flask, render_template, request, jsonify
from PIL import Image
import torch
from torch import nn
from torchvision import transforms, models
import io

app = Flask(__name__)

 


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
DEVICE = device
model = models.resnet18(pretrained=True)
model.fc = torch.nn.Linear(model.fc.in_features, 9)  # Adapter la sortie pour correspondre au nombre de classes
model.load_state_dict(torch.load("final_model.pth", map_location=device))  # Le chemin vers le modèle est maintenant relatif
model.eval()
model.to(device)




# Définir les classes de classification
class_names = ['Pastilla', 'Poulet Mhamer', 'Rfissa', 'Taktouka', 'couscous btfaya', 'couscous legumes', 'hrira', 'tajine legume', 'tajine lham barkouk']

# Définir les transformations à appliquer sur les images
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Vérifier si un fichier a été envoyé
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Charger l'image envoyée
    image = Image.open(file.stream)

    # Appliquer les transformations
    image = transform(image).unsqueeze(0)  # Ajouter une dimension batch

    # Envoyer l'image sur le même périphérique que le modèle
    image = image.to(DEVICE)

    # Prédiction avec le modèle
    with torch.no_grad():
        outputs = model(image)
        _, predicted_idx = torch.max(outputs, 1)

    # Obtenir la classe prédite
    predicted_class = class_names[predicted_idx.item()]

    return jsonify({
        'class_name': predicted_class,
        'class_id': predicted_idx.item()
    })



if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
    #ngrok http 5000

