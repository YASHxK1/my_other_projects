#!python -m pip install numpy tensorflow matplotlib seaborn scikit-learn gradio
#!python -m pip install tensorflow

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import gradio as gr

# Define paths
fake_dir = "D:\codes\ML\deepfake detector\Data\Fake"
real_dir = "D:\codes\ML\deepfake detector\Data\Real"

# Load images
def load_images_from_folder(folder, label):
    images = []
    labels = []
    for filename in os.listdir(folder):
        img = image.load_img(os.path.join(folder, filename), target_size=(128, 128))
        img = image.img_to_array(img)
        img = img / 255.0  # Normalize the image
        images.append(img)
        labels.append(label)
    return images, labels

# Load fake and real images
fake_images, fake_labels = load_images_from_folder(fake_dir, 0)
real_images, real_labels = load_images_from_folder(real_dir, 1)

# Combine the data
X = np.array(fake_images + real_images)
y = np.array(fake_labels + real_labels)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=2, validation_data=(X_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy:.2f}")

# Plot training history
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()

# Confusion Matrix
y_pred = model.predict(X_test)
y_pred = np.round(y_pred).astype(int)
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Classification Report
print(classification_report(y_test, y_pred))

# Function to predict if an image is fake or real
def predict_image(img):
    img = image.load_img(img, target_size=(128, 128))
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    if prediction < 0.5:
        return "Fake"
    else:
        return "Real"

model.save('D:\codes\ML\deepfake detector\MODELdeepfakedetector.h5')  # Saves the model in HDF5 format