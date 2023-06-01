
# Christmas-Image-Classification
Nueral network model deployed using Heroku and Flask to classify Christmas Images 

## Important To Know
Model is trained on dataset with 8 different classes of christmans images namely:
- christmas cookies
- christmas presents 
- christmas_tree
- fireworks
- penguin 
- reindeer
- santa 
- snowman

## How To Use?
### step 1
Download test folder from [here](https://github.com/NishilBalar/Christmas-Image-Classification/tree/main/test). It consists of `test.py` python file and sample images which can be used to check model's prediction. 

### step 2
Add image to this folder which needed to be classified in mentioned classes. Image should be suitable to 8 different classes.

### step 3
Minor change in `test.py` file:

```
import requests

resp = requests.post("https://christmas-model-b04.herokuapp.com/predict", files={'file':open('santa.png', 'rb')})

print(resp.text)
```
Change `santa.png` with the name of your image as `image_name.extension`

**Note**: This model will only allow `.jpg`, `.jpeg` and `.png` formats of image. Please consider it before.

### step 4
Move to test folder by typing `cd test` in terminal

Run `test.py` file using following command in terminal ` python test.py `

## Acknowledgements
This classification challenge was organized as a part of Deep Learning subject at Universität Siegen by Computer Vision Group via Kaggle platform.

One can easily find mentioned challenge, training dataset and its leaderboard for year 2022/23 [HERE](https://www.kaggle.com/competitions/deep-learning-classification-challenge-ws2223)



