import tensorflow as tf
from sklearn.model_selection import train_test_split
from text2vec import *

X_train, X_test, y_train, y_test = train_test_split(documents, y_encoded, test_size=0.33, random_state=42)

print(X_train)
print(y_train)

chatBotModel = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(100,)),
    tf.keras.layers.Dense(32),
    tf.keras.layers.Activation("relu"),
    tf.keras.layers.Dense(3),
    tf.keras.layers.Activation("softmax")
])

chatBotModel = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(100,)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

chatBotModel.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

X_train = np.array(X_train)
y_train = np.array(y_train)

#history = chatBotModel.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.25)
#loss, accuracy = chatBotModel.evaluate(X_test, y_test)

def predict_task(prompt):
    lb = ["play_chess", "chat", "query_selection"]
    x = np.array([get_sentence_embedding(prompt)])
    a = chatBotModel.predict(x)[0]
    mx = 0
    for i in range(3):
        if a[i]>a[mx]:
            mx = i
    return lb[mx]


