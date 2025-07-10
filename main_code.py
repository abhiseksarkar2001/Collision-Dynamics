import pygame
import sys
import random
import math
from collections import defaultdict

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600  # Default container size
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)
BALL_COLOR = (255, 255, 255)
WALL_COLOR = (100, 100, 100)
BALL_RADIUS = 10
BALL_MASS = 1

# Physics parameters
ELASTICITY = 1.0  # Perfectly elastic collisions
FRICTION = 0.0     # No friction

class Ball:
    def __init__(self, x, y, vx, vy, radius=BALL_RADIUS, mass=BALL_MASS, color=BALL_COLOR):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.mass = mass
        self.color = color
        self.collisions = 0
    
    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
    
    def check_wall_collision(self, width, height):
        # Left and right walls
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.vx = -self.vx * ELASTICITY
            return True
        elif self.x + self.radius >= width:
            self.x = width - self.radius
            self.vx = -self.vx * ELASTICITY
            return True
        
        # Top and bottom walls
        if self.y - self.radius <= 0:
            self.y = self.radius
            self.vy = -self.vy * ELASTICITY
            return True
        elif self.y + self.radius >= height:
            self.y = height - self.radius
            self.vy = -self.vy * ELASTICITY
            return True
        
        return False
    
    def check_ball_collision(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance < self.radius + other.radius:
            # Calculate collision parameters
            RVA = math.atan2(self.vy - other.vy, self.vx - other.vx)
            RPA = math.atan2(dy, dx)
            
            # Simplified collision for equal-radius balls
            if self.radius == other.radius:
                # Use angle between centers for equal-radius balls
                IA = RPA
            else:
                # Original formula for different radii
                d = distance
                IP = d * math.sin(RPA - RVA) / abs(other.radius - self.radius)
                IA = math.asin(IP)
            
            # Calculate velocity changes
            denominator = (1 + math.tan(RVA + IA)**2) * (1 + other.mass - self.mass)
            if denominator == 0:
                denominator = 0.0001  # Prevent division by zero
                
            dv = -2 * ((other.vx - self.vx) + (other.vy - self.vy) * math.tan(RVA + IA)) / denominator
            
            # Update velocities
            self.vx = self.vx - (other.mass - self.mass) * dv
            self.vy = self.vy - math.tan(RVA + IA) * (other.mass - self.mass) * dv
            
            other.vx = other.vx + dv
            other.vy = other.vy + math.tan(RVA + IA) * dv
            
            # Separate balls to prevent sticking
            overlap = (self.radius + other.radius) - distance
            angle = math.atan2(dy, dx)
            self.x -= overlap * math.cos(angle) / 2
            self.y -= overlap * math.sin(angle) / 2
            other.x += overlap * math.cos(angle) / 2
            other.y += overlap * math.sin(angle) / 2
            
            return True
        
        return False
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

def create_balls(num_balls, width, height, velocity_range):
    balls = []
    for _ in range(num_balls):
        # Random position ensuring balls don't overlap initially
        while True:
            x = random.randint(BALL_RADIUS, width - BALL_RADIUS)
            y = random.randint(BALL_RADIUS, height - BALL_RADIUS)
            
            # Check for overlap with existing balls
            overlap = False
            for ball in balls:
                dx = x - ball.x
                dy = y - ball.y
                if math.sqrt(dx**2 + dy**2) < 2 * BALL_RADIUS:
                    overlap = True
                    break
            
            if not overlap:
                break
        
        # Random velocity within specified range
        vx = random.uniform(velocity_range[0], velocity_range[1]) * random.choice([-1, 1])
        vy = random.uniform(velocity_range[0], velocity_range[1]) * random.choice([-1, 1])
        
        balls.append(Ball(x, y, vx, vy))
    
    return balls

def run_simulation(num_balls=10, width=600, height=600, velocity_range=(-5, 5), duration=86400):
    # Set up display
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bouncing Balls Simulation")
    clock = pygame.time.Clock()
    
    # Create balls
    balls = create_balls(num_balls, width, height, velocity_range)
    
    # Statistics
    wall_collisions = 0
    ball_collisions = 0
    velocity_histogram = defaultdict(int)
    
    # Main loop
    running = True
    iteration = 0
    
    while running and iteration < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill(BACKGROUND_COLOR)
        
        # Draw walls
        pygame.draw.rect(screen, WALL_COLOR, (0, 0, width, height), 2)
        
        # Update and draw balls
        for i, ball in enumerate(balls):
            ball.move(1)  # dt = 1 iteration
            
            # Check wall collisions
            if ball.check_wall_collision(width, height):
                wall_collisions += 1
            
            # Check ball collisions
            for other in balls[i+1:]:
                if ball.check_ball_collision(other):
                    ball_collisions += 1
            
            ball.draw(screen)
        
        # Update velocity histogram (sample every 100 iterations)
        if iteration % 100 == 0:
            for ball in balls:
                speed = math.sqrt(ball.vx**2 + ball.vy**2)
                bin = int(speed * 2)  # Bin size of 0.5
                velocity_histogram[bin] += 1
        
        pygame.display.flip()
        clock.tick(FPS)
        iteration += 1
    
    pygame.quit()
    
    # Calculate average collisions per run
    avg_wall = wall_collisions / 5 if duration == 86400 else wall_collisions
    avg_ball = ball_collisions / 5 if duration == 86400 else ball_collisions
    
    return {
        "wall_collisions": avg_wall,
        "ball_collisions": avg_ball,
        "total_collisions": avg_wall + avg_ball,
        "velocity_histogram": velocity_histogram
    }

def plot_velocity_distribution(histogram):
    import matplotlib.pyplot as plt
    
    bins = sorted(histogram.keys())
    counts = [histogram[bin] for bin in bins]
    
    plt.bar(bins, counts, width=0.5)
    plt.xlabel("Velocity (pixels/iteration)")
    plt.ylabel("Number of balls")
    plt.title("Velocity Distribution of Balls")
    plt.show()

# Example usage for Experiment 1 (container shape variation)
if __name__ == "__main__":
    # Experiment 1: Container shape variation
    print("Running Experiment 1: Container shape variation")
    
    # Square container (600x600)
    results1 = run_simulation(width=600, height=600)
    print("600x600 container:", results1)
    
    # Rectangular container (900x400)
    results2 = run_simulation(width=900, height=400)
    print("900x400 container:", results2)
    
    # Narrow container (1200x300)
    results3 = run_simulation(width=1200, height=300)
    print("1200x300 container:", results3)
    
    # Plot velocity distribution
    plot_velocity_distribution(results1["velocity_histogram"])