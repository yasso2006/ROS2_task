import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import select
import tty
import termios

class turtles(Node):
    def _init_(self):
        super()._init_('turtles')
        
        self.turtle1_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.turtle2_publisher = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)
        
        self.turtle1_twist = Twist()
        self.turtle2_twist = Twist()
        
        self.get_logger().info("Use Arrow keys for turtle1, WASD for turtle2")
        self.get_logger().info("Press any key to move, release to stop")

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
            return key
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return None

    def run(self):
        self.settings = termios.tcgetattr(sys.stdin)
        
        while rclpy.ok():
            key = self.get_key()
            
            if key == 'q':
                break
            
            self.turtle1_twist = Twist()
            self.turtle2_twist = Twist()
        
            if key == 'w':
                self.turtle2_twist.linear.x = 2.0
            elif key == 's':
                self.turtle2_twist.linear.x = -2.0
            elif key == 'a':
                self.turtle2_twist.angular.z = 2.0
            elif key == 'd':
                self.turtle2_twist.angular.z = -2.0
            
            
            elif key == '\x1b':  
                arrow_key = sys.stdin.read(2)
                if arrow_key == '[A':   
                    self.turtle1_twist.linear.x = 2.0
                elif arrow_key == '[B': 
                    self.turtle1_twist.linear.x = -2.0
                elif arrow_key == '[D':  
                    self.turtle1_twist.angular.z = 2.0
                elif arrow_key == '[C':  
                    self.turtle1_twist.angular.z = -2.0
            
            self.turtle1_publisher.publish(self.turtle1_twist)
            self.turtle2_publisher.publish(self.turtle2_twist)

def main():
    rclpy.init()
    node = turtles()
    node.run()
    node.destroy_node()
    rclpy.shutdown()
