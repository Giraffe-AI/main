from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right-angled triangle
        triangle = Polygon(np.array([0,0,0]), np.array([1,0,0]), np.array([0,1,0]))

        # Label the sides of the triangle
        labels = ["a", "b", "c"]
        sides = [Line(triangle.points[i-1], triangle.points[i]) for i in range(3)]
        for i, side in enumerate(sides):
            label = MathTex(labels[i]).next_to(side, UP)
            self.add(label)

        # Add the triangle to the scene
        self.add(triangle)

        # Add narration
        narration = Text("Welcome to another episode of 3blue1brown. Today, we're going to explore the Pythagorean theorem, a fundamental principle in geometry that you've probably heard of. It's about right-angled triangles, like the one you see here.")
        narration.to_edge(DOWN)
        self.play(Write(narration))

        # Wait for a while before moving on to the next scene
        self.wait(5)

        # Clear the scene
        self.clear()

# Render the scene
if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim -p -c #FFFFFF --video_dir ~/Videos/ {script_name} PythagoreanTheorem")