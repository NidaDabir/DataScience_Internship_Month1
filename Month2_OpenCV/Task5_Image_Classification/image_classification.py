import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Dataset path
dataset_path = "datasets"


data = []
labels = []

# Image size
img_size = 100

# Load Cats
cats_path = os.path.join(dataset_path, "cats")

for file in os.listdir(cats_path):

    img_path = os.path.join(cats_path, file)

    img = cv2.imread(img_path)

    img = cv2.resize(img, (img_size, img_size))

    img = img.flatten()

    data.append(img)

    labels.append(0)   # Cat


# Load Dogs
dogs_path = os.path.join(dataset_path, "dogs")

for file in os.listdir(dogs_path):

    img_path = os.path.join(dogs_path, file)

    img = cv2.imread(img_path)

    img = cv2.resize(img, (img_size, img_size))

    img = img.flatten()

    data.append(img)

    labels.append(1)   # Dog


# Convert to numpy
data = np.array(data)
labels = np.array(labels)


# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, random_state=42
)


# Train Model
model = SVC()

model.fit(X_train, y_train)


# Prediction
prediction = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, prediction)

print("Accuracy:", accuracy)



# Test image

test_img = cv2.imread("datasets/cats/cat1.jpg")

test_img = cv2.resize(test_img, (img_size, img_size))

test_img = test_img.flatten().reshape(1, -1)

result = model.predict(test_img)

if result == 0:
    print("Cat Detected")
else:
    print("Dog Detected")
