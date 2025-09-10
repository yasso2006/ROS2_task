#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int16

class subscriber(Node):
    def __init__(self):
        super().__init__("subscriber")
        self.get_logger().info("Started Subscriber node!!")
        self.subscriber = self.create_subscription(Int16, 'random_topic', self.listener_callback, 10)


    def listener_callback(self, msg):
        if msg.data%2:
            odd_even = "odd"
        else:
            odd_even = "even"
        self.get_logger().info(f"random: {msg.data}, {odd_even}")

    # def timer_callback(self):
    #     self.get_logger().info(f"hello {self.counter}")
    #     self.counter += 1

def main():
    rclpy.init()
    node = subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
                

