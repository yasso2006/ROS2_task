#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import random
from sensor_msgs.msg import FluidPressure

class pressure_node(Node):
    def __init__(self):
        super().__init__('pressure_node')
        self.publisher_ = self.create_publisher(FluidPressure, '/pressure', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        

    def timer_callback(self):
        msg = FluidPressure()
        msg.fluid_pressure = float(random.randint(900, 1100))
        self.publisher_.publish(msg)
        self.get_logger().info(f'Pressure: "{int(msg.fluid_pressure)}hPa"')
        
        
def main():
    rclpy.init()
    node = pressure_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
    