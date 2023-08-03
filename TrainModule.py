import matplotlib.pyplot as plt
import os
import cv2
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
from tkinter import messagebox
import pandas as pd
from sklearn.metrics import accuracy_score
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'

if not os.path.exists('./recognizer'):
    os.makedirs('./recognizer')

def getImagesWithID():
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    print(imagePaths)
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg,'uint8')
        print(os.path.split(imagePath)[-1].split('.')[2])
        ID = int(os.path.split(imagePath)[-1].split('.')[2])
        # Resize the image to a size of 100 x 100 pixels
        resized = cv2.resize(faceNp, (100, 100), interpolation=cv2.INTER_AREA)
        faces.append(resized)
        IDs.append(ID)
        cv2.imshow("training",resized)
        cv2.waitKey(10)
    faces = np.array(faces)
    IDs = np.array(IDs)
    # Split the dataset into 70% training data and 30% testing data
    X_train, X_test, y_train, y_test = train_test_split(faces, IDs, test_size=0.2, random_state=42)
    return X_train, y_train, X_test, y_test

def plot(X_train, y_train):
    X_train_flat = X_train.ravel()
    y_train_flat = y_train.ravel()
    plt.xticks([])
    plt.scatter(X_train_flat[:150], y_train_flat[:150])
    plt.xlabel('Input Data')
    plt.ylabel('Output Data')
    plt.title('Training Data')
    plt.show()


def train1():
    X_train, y_train, X_test, y_test = getImagesWithID()
    print("Shapes of the arrays:")
    print("X_train:", X_train.shape)
    print("y_train:", y_train.shape)
    print("X_test:", X_test.shape)
    print("y_test:", y_test.shape)
    plot(X_train,y_train)
    recognizer.train(X_train, y_train)
    recognizer.save('recognizer/trainingData.yml')
    messagebox.showinfo("Information", "Training Completed.")
    cv2.destroyAllWindows()

     # Make predictions on the test data
    predicted_labels = []
    for test_image in X_test:
        label, confidence = recognizer.predict(test_image)
        predicted_labels.append(label)

    # Calculate the accuracy of the model
    accuracy = np.mean(np.array(predicted_labels) == np.array(y_test)) * 100
    print("Accuracy: {:.2f}%".format(accuracy * 100))
    cv2.destroyAllWindows()



