import tensorflow as tf
from config import DATA_DIR
import os
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import numpy as np

validation_data = training_data = None


# Load the training data
def load_training_data():
    global training_data
    training_data = tf.keras.preprocessing.image_dataset_from_directory(
        os.path.join(DATA_DIR, "Train"),
        labels="inferred",
        label_mode="categorical",
        image_size=(35, 35),
        color_mode="rgb",
        batch_size=32,
        shuffle=True,
    )


def load_validation_data():
    global validation_data
    df = pd.read_csv(os.path.join(DATA_DIR, "Test.csv"))

    print("Loading validation data...")

    images = [cv2.imread(os.path.join(DATA_DIR, df["Path"][i])) for i in range(20)]
    images = [cv2.resize(image, (35, 35)) for image in images]
    images = np.array(images, dtype=np.uint8)
    labels = tf.keras.utils.to_categorical(df["ClassId"][:20], num_classes=43)

    validation_data = tf.data.Dataset.from_tensor_slices((images, labels)).batch(32)


def visualize_data():
    global training_data
    for image_batch, labels_batch in training_data.take(1):
        plt.figure(figsize=(10, 10))
        plt.suptitle("Training Data Samples", fontsize=16)
        for i in range(9):
            ax = plt.subplot(3, 3, i + 1)

            plt.imshow(image_batch[i].numpy().astype("uint8"))
            plt.title(f"Label: {labels_batch[i].numpy().argmax()}")
            plt.axis("off")
        plt.show()

    global validation_data
    for image_batch, labels_batch in validation_data.take(1):
        plt.figure(figsize=(10, 10))
        plt.suptitle("Validation Data Samples", fontsize=16)
        for i in range(9):
            ax = plt.subplot(3, 3, i + 1)
            plt.imshow(image_batch[i].numpy().astype("uint8"))
            plt.title(f"Label: {labels_batch[i].numpy().argmax()}")
            plt.axis("off")
        plt.show()


def train_model():
    # # Define the model
    model = tf.keras.Sequential(
        [
            tf.keras.Input(shape=(35, 35, 3)),
            tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(43, activation="softmax"),  # 43 classes for GTSRB
        ]
    )

    print(model.summary())

    model.compile(
        optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
    )

    # Train the model
    model.fit(
        training_data,
        validation_data=validation_data,
        epochs=10,  # Adjust the number of epochs as needed
        callbacks=[
            tf.keras.callbacks.ModelCheckpoint(
                filepath="model_checkpoint.h5",
                save_best_only=True,
                monitor="val_accuracy",
            )
        ],
    )


def evaluate_model(model):
    global validation_data
    # Evaluate the model on the validation data
    loss, accuracy = model.evaluate(validation_data)

    print(f"Validation Loss: {loss}")
    print(f"Validation Accuracy: {accuracy}")

    if accuracy >= 0.95:
        print("Model accuracy is above 95%. Saving the model.")
        model.save("gtsrb_model.h5")
    else:
        print("Model accuracy is below 95%. Not saving the model.")


if __name__ == "__main__":
    load_training_data()
    load_validation_data()

    visualize_data()
    train_model()
    evaluate_model()
