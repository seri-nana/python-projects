import random
import math

def estimate_pi(num_points):
    """
    Estimates the value of Pi using the Monte Carlo method.

    Args:
        num_points: The total number of random points to generate.

    Returns:
        The estimated value of Pi.
    """
    points_inside_circle = 0
    total_points = num_points

    for _ in range(total_points):
        # Generate random x and y coordinates between 0 and 1
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # Calculate the distance from the origin (0, 0)
        distance = math.sqrt(x**2 + y**2)

        # Check if the point is inside the quarter circle (radius 1)
        if distance < 1:
            points_inside_circle += 1

    # The ratio of points inside the circle to total points is 
    # equal to the ratio of the areas (pi*r^2 / 4*r^2 = pi/4).
    # Since r=1, the area of the quarter circle is pi/4.
    # Therefore, Pi can be estimated as 4 * (points_inside_circle / total_points)
    pi_estimate = 4 * (points_inside_circle / total_points)
    return pi_estimate

# --- Example Usage ---
if __name__ == "__main__":
    iterations = 1000000  # More iterations provide a more accurate estimate
    pi = estimate_pi(iterations)
    print(f"Number of iterations: {iterations}")
    print(f"Estimated value of Pi: {pi}")
    print(f"Actual value of Pi (math.pi): {math.pi}")
    print(f"Difference: {abs(math.pi - pi)}")

