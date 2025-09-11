
#!/usr/bin/env python3

import random
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Temperature

class temperature_node(Node):
    def __init__(self):
        super().__init__('temperature_node')
        self.publisher_ = self.create_publisher(Temperature, '/temperature', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):

        msg = Temperature()
        msg.temperature = float(random.randint(15, 40))
        msg.variance = 0.5  
        self.publisher_.publish(msg)
        self.get_logger().info(f'Temperature : {msg.temperature} °C')
                
        
        
def main():
    rclpy.init()
    node = temperature_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()