import tensorflow.keras.callbacks
from tensorflow.keras.layers import Conv1D, Dense, Dropout, Flatten, Input, MaxPooling1D
from tensorflow.keras.models import Model


class CharCNN(Model):
    def __init__(self, num_labels):
        super(CharCNN, self).__init__()

        self.conv_1x = Conv1D(128, 6, activation="relu", padding="valid")
        self.max_pool_1x = MaxPooling1D(4)
        self.dropout_1x = Dropout(0.5)
        self.conv_2x = Conv1D(256, 6, activation="relu", padding="valid")
        self.max_pool_2x = MaxPooling1D(4)
        self.dropout_2x = Dropout(0.5)
        self.conv_3x = Conv1D(512, 6, activation="relu", padding="valid")
        self.max_pool_3x = MaxPooling1D(4)
        self.dropout_3x = Dropout(0.5)

        self.flatten = Flatten()
        self.dense = Dense(128, activation="relu")
        self.preds = Dense(
            num_labels, activation="softmax", name="char_cnn_predictions"
        )

    def call(self, inputs: Input):
        x = self.conv_1x(inputs)
        x = self.max_pool_1x(x)
        x = self.dropout_1x(x)
        x = self.conv_2x(x)
        x = self.max_pool_2x(x)
        x = self.dropout_2x(x)
        x = self.conv_3x(x)
        x = self.max_pool_3x(x)
        x = self.dropout_3x(x)
        x = self.flatten(x)
        x = self.dense(x)

        return self.preds(x)
