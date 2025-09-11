#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Temperature, FluidPressure, RelativeHumidity
import datetime

class monitor_node(Node):
    def __init__(self):
        super().__init__('monitor_node')

        self.temp_sub = self.create_subscription(Temperature,'/temperature',self.temperature_callback,10)
        self.humi_sub = self.create_subscription(RelativeHumidity,'/humidity',self.humidity_callback,10)
        self.press_sub = self.create_subscription(FluidPressure,'/pressure',self.pressure_callback,10)
        
        self.current_temp = None
        self.current_humi = None    
        self.current_press = None

    def temperature_callback(self, msg):
        self.current_temp = msg.temperature
        self.log_current_readings()
       

    def humidity_callback(self, msg):
        self.current_humi = msg.relative_humidity
        self.log_current_readings()
       

    def pressure_callback(self, msg):
        self.current_press = msg.fluid_pressure
        self.log_current_readings()
       

    def log_current_readings(self):
        self.get_logger().info(f"Temp: {int(self.current_temp)} °C, Humidity: {self.current_humi} %, Pressure: {self.current_press} hpa")

def main():
    rclpy.init()
    node = monitor_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()