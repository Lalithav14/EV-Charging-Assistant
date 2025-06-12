import rclpy
from rclpy.node import Node
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from std_msgs.msg import String

class HealthNode(Node):
    def __init__(self):
        super().__init__('health_node')
        self.publisher_ = self.create_publisher(String, 'vehicle_health_status', 10)
        self.timer = self.create_timer(10.0, self.check_health)
        self.model = self.build_model()
        self.dataset = self.load_dataset()

    def build_model(self):
        model = Sequential()
        model.add(LSTM(32, input_shape=(10, 3), return_sequences=False))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def load_dataset(self):
        df = pd.read_csv('https://raw.githubusercontent.com/datablist/sample-csv-files/main/files/people/people-100.csv')
        X = np.random.rand(100, 10, 3)  # Simulated features: temperature, battery, vibration
        y = np.random.randint(0, 2, 100)
        self.model.fit(X, y, epochs=5, verbose=0)
        return X

    def check_health(self):
        X_test = np.random.rand(1, 10, 3)
        y_pred = self.model.predict(X_test)[0][0]
        status = "GOOD" if y_pred > 0.5 else "ATTENTION NEEDED"
        msg = String()
        msg.data = f"Vehicle Health: {status}"
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = HealthNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
