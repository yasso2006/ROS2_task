#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import random
from sensor_msgs.msg import RelativeHumidity

class humidity_node(Node):
    def __init__(self):
        super().__init__('humidity_node')
        self.publisher_ = self.create_publisher(RelativeHumidity, '/humidity', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        

    def timer_callback(self):
        msg = RelativeHumidity()
        msg._relative_humidity = float(random.randint(20, 100))
        self.publisher_.publish(msg)
        self.get_logger().info(f'Humidity: {int(msg.relative_humidity)}%')
        
        
def main():
    rclpy.init()
    node = humidity_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
    