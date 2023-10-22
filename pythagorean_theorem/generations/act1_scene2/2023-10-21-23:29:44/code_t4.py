from manim import *

class HistoricalBackground(Scene):
    def construct(self):
        # Create elements
        greece = ImageMobject("/actual/path/to/ancient_greece.jpg").scale(0.5)
        pythagoras = ImageMobject("/actual/path/to/pythagoras.jpg").scale(0.2)
        students = ImageMobject("/actual/path/to/students.jpg").scale(0.2)
        theorem_text = Text("This theorem has been a cornerstone of geometry for over two millennia.")

        # Position elements
        pythagoras.to_edge(LEFT)
        students.next_to(pythagoras, RIGHT, buff=0.5)
        theorem_text.to_edge(DOWN)

        # Animate elements
        self.play(FadeIn(greece))
        self.play(FadeInFrom(pythagoras, direction=LEFT), FadeInFrom(students, direction=RIGHT))
        self.play(Write(theorem_text))
        self.wait(2)

        # Cleanup
        self.play(FadeOut(greece), FadeOut(pythagoras), FadeOut(students), FadeOut(theorem_text))