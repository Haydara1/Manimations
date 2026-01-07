# Problem 2 from Chapter 1 of the Putnam and beyond book
# Show that no set nine consecutive integers can be partitioned into two sets
# with the product of the elements of the first set equal to
# the product of the elements of the second set.

from manim import *
import random as rd
import numpy as np

class Problem2(Scene):
    def construct(self):
        # Introduction text
        self.next_section("Problem Statement", skip_animations=True)

        title = Text("Problem 2").scale(0.8)
        self.play(Write(title), run_time=2)
        self.wait(2)

        problem_statement = Tex(
            r"Show that no set of nine consecutive integers can be partitioned into two sets "
            r"with the product of the elements of the first set equal to "
            r"the product of the elements of the second set.",
        ).scale(0.7)

        self.play(title.animate.to_edge(UP), run_time=2)
        self.play(Write(problem_statement),run_time=10)
        self.wait(3)
        self.play(FadeOut(problem_statement), FadeOut(title))

        # Solution  
        # No variables on the screen
        self.next_section("Solution")

        assumption = Tex("Assume such set exists.").scale(0.7)
        self.play(Write(assumption), run_time=2)
        self.wait(2)

        big_set = Ellipse(height=4.0, width=2.0, color=ORANGE)
        text_group = VGroup().move_to(big_set.get_center())
        

        for i in range(9):
            integer = MathTex(f"n_{{{i}}}").scale(0.6)
            integer.align_to(big_set.get_top(), DOWN)

            if i > 0:
                integer.shift(DOWN + DOWN  *  np.ceil(i / 2) / 2 + RIGHT * ((-1) ** i) / 2)

                if i % 2 == 0:
                    integer.shift(DOWN * 0.25)
            else:
                integer.shift(DOWN + DOWN  *  i / 2)

            text_group.add(integer)

        instruction = Tex("Let's create such a set").scale(0.7)
        instruction.next_to(big_set.get_bottom(), DOWN)

        self.play(DrawBorderThenFill(big_set),
                   FadeOut(assumption),
                   Write(instruction))
        self.play(Write(text_group))
        self.wait(3)

        # Add the small circles
        small_left_set = Ellipse(height=3.0, color=YELLOW).shift(LEFT * 3)
        small_right_set = Ellipse(height=3.0, color=YELLOW).shift(RIGHT * 3)

        copy = big_set.copy()
        self.add(copy)

        # Create the elements group
        elements_group = VGroup()

        for i in range(9):
            element = MathTex(f"n_{{{i}}}").scale(0.5)
            elements_group.add(element)

        # A function to assign the elements randomly to the two sets.
        def assignIntegersToSets(chance):

            set1_num = 0
            
            for element in elements_group:
                which_set = rd.random() # decide randomly on the position of the set

                if(which_set <= chance): # Put in the set on the left
                    which_set += 1
                    element.move_to(small_left_set.get_center())
                    element.shift(UP * rd.uniform(-1, 1) + RIGHT * rd.uniform(-0.7, 0.7))

                else: # Put in the set on the right
                    element.move_to(small_right_set.get_center())
                    element.shift(UP * rd.uniform(-1, 1) + RIGHT * rd.uniform(-0.7, 0.7))

            
            self.play(FadeIn(elements_group))
            

        # Assign the elements to the two sets


        # Transform the set to two subsets
        self.play(Transform(big_set, small_left_set),
                  Transform(copy, small_right_set), 
                  FadeOut(text_group),
                  FadeOut(instruction),
                  run_time = 2)
        
        caution = Tex("The problem doesn't specify if we have to partition the sets evenly!").scale(0.5)
        caution.shift(DOWN * 3)

        self.play(Write(caution))
        assignIntegersToSets(0.5)

        for i in range(3):
            self.wait(0.1)
            self.play(FadeOut(elements_group))
            assignIntegersToSets(rd.random())

        self.wait(2)
        self.play(FadeOut(caution),
                  FadeOut(elements_group),
                  FadeOut(big_set),
                  FadeOut(copy))
        
        self.wait(2)

        




        












