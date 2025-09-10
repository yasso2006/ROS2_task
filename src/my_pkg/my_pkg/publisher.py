#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int16
import random

class publisher(Node):
    def __init__(self):
        super().__init__("publisher")
        self.get_logger().info("Started Publisher node!!")
        self.publisher_node = self.create_publisher(Int16, 'random_topic', 10)
        self.counter = 0
        self.create_timer(1,  self.rand_callback)

    def rand_callback(self):
        msg = Int16()
        msg.data = random.randint(0,100)
        self.publisher_node.publish(msg)

    # def timer_callback(self):
    #     self.get_logger().info(f"hello {self.counter}")
    #     self.counter += 1

def main():
    rclpy.init()
    node = publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
                

