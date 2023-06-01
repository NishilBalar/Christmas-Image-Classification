import torch
import torchvision
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import io

#load model
class Network(nn.Module):

    def __init__(self):
        super().__init__()


        self.pretrained = True
        
        self.model = torchvision.models.efficientnet_b4(self.pretrained)


        self.model.fc = nn.Sequential(nn.Flatten(),
                                      nn.Linear(1792, 625),
                                      nn.ReLU(),
                                      nn.Dropout(0.3),
                                      nn.Linear(625, 256),
                                      nn.ReLU(),
                                      nn.Linear(256, 8))

    def forward(self, x):
       
        x = self.model(x)

        
        return x
    
model = Network()
PATH = "app/model"
model.load_state_dict(torch.load(PATH, map_location=torch.device('cpu')))
model.eval()

#image to tensor
def transform_image(image):
    eval_transforms = transforms.Compose(
                [transforms.Resize(224),
                 transforms.Grayscale(num_output_channels = 3),
                 transforms.ToTensor(),
                 transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
    
    image = Image.open(io.BytesIO(image))
    
    return eval_transforms(image).unsqueeze(0)

#predict
def get_prediction(img_tensor):

    _, prediction = model(img_tensor).max(dim=1)
    return prediction
