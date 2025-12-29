# A geometric proof of the irrationality of sqrt(2) by Tennenbaum

from manim import *

class Main(Scene):
    def construct(self):

        ### Introduction Scene ###  
        self.next_section("Introduction")

        # Assume sqrt(2) is rational: sqrt(2) = a/b
        text = MathTex(r"\text{Show that }", r"\sqrt{2}", r"\text{ is irrational}")
        self.play(Write(text))
        self.wait(2)

        placeholder = MathTex(r"\text{Assume that }", r"\sqrt{2}", r"\in", r"\mathbb{Q}")

        self.play(TransformMatchingTex(text,
            placeholder)) # Writing that sqrt(2) is rational
        self.wait(2)
        
        # Use the definition of rationality:
        assumption1 = MathTex(r"\text{By definition, there exist coprime integers }",
                            r"a, b", r"\text{ with }", r"b \neq 0")
        
        assumption2 = MathTex(r"\text{ such that }",
                            r"\sqrt{2}", "=", r"\frac{a}{b}")

        assumption1[1].set_color(YELLOW)
        assumption1.scale(0.8).next_to(placeholder, DOWN)

        assumption2.scale(0.8).next_to(assumption1, DOWN)

        self.play(Write(assumption1))
        self.play(Write(assumption2), run_time=2)
        self.wait(4)


        # Add main title:
        title = MathTex(r"\sqrt{2}", "=", r"\frac{a}{b}", r"\in", r"\mathbb{Q}")
        title[0].set_color(BLUE)
        title.to_edge(UP)

        # Fade out previous assumptions before writing coprime note
        self.play(FadeOut(assumption1), FadeOut(assumption2),
                  TransformMatchingTex(placeholder, title))
        
        # Beware that a and b are coprime
        coprime = MathTex(r"\textit{Note that }", r"a", r"\textit{ and }", r"b", r"\textit{ are coprime}")
        coprime2 = MathTex(r"\textit{(i.e., they have no common divisors other than 1)}")
        coprime[1].set_color(YELLOW)
        coprime[3].set_color(YELLOW)
        coprime.scale(0.8)
        coprime2.scale(0.6).next_to(coprime, DOWN)

        self.play(Write(coprime))
        self.play(Write(coprime2), run_time=2)
        self.wait(3)

        self.play(FadeOut(coprime), FadeOut(coprime2))

        ### Finished introduction scene, the only remaining variable is title###
        self.next_section()

        ### Main Proof Scene ###
        introduction = MathTex(r"\textit{Using the assumption we just made, we can show that: }",
                               r"a", r"^2", "=", r"2", r"b", r"^2")
        introduction.scale(0.8)
        self.play(Write(introduction))
        self.wait(3)

        # Keep the deduced on the corner
        ps = MathTex(r"a", r"^2", "=", r"2", r"b", r"^2")
        ps.scale(0.8)
        ps.set_color(YELLOW)
        ps.shift(UP*2.5 + RIGHT*4)
        self.play(TransformMatchingTex(introduction, ps), rate_func = smooth, run_time=2)
        self.wait(2)

        # Create squares to represent a^2 and 2b^2
        ### Plan
        # Create the two squares: one of side a (blue), one of side b (green)
        # Put them side by side with side label and area labels
        # Write that the area of the blue square is equal to twice the area of the green square
        # When writing, refer to the squares and the equation
        #  
        # ###

        # Squares
        a_square = Square(side_length=3, color=BLUE, fill_opacity=0.5).shift(LEFT*2.5)
        b_square1 = Square(side_length=1.5, color=GREEN, fill_opacity=0.5).shift(RIGHT*2.5)

        # Length indicators
        a_indicator1 = MathTex(r"a").next_to(a_square, DOWN).scale(0.6)
        a_indicator2 = MathTex(r"a").next_to(a_square, LEFT).scale(0.6)

        b_indicator1 = MathTex(r"b").next_to(b_square1, DOWN).scale(0.6)
        b_indicator2 = MathTex(r"b").next_to(b_square1, RIGHT).scale(0.6)
        a_group = VGroup(a_indicator1, a_indicator2)
        b_group = VGroup(b_indicator1, b_indicator2)

        self.play(DrawBorderThenFill(a_square),
                  DrawBorderThenFill(b_square1), run_time=3)
        self.play(Write(a_group), Write(b_group), run_time=2)
        self.wait(2)

        # Area labels
        a_area = MathTex(r"a", r"^2").move_to(a_square.get_center()).scale(0.8)
        b_area = MathTex(r"b", r"^2").move_to(b_square1.get_center()).scale(0.8)

        b_area.add_updater(lambda m: m.move_to(b_square1.get_center()))

        self.play(Write(a_area), Indicate(ps[0:2], color=BLUE), run_time=2)
        self.play(Write(b_area), Indicate(ps[4:6], color=GREEN), run_time=2)
        self.wait(2)

        b_square2 = b_square1.copy()
        self.play(FadeOut(a_group), FadeOut(b_group), Create(b_square2))

        self.play(b_square2.animate.shift(UP),
                  b_square1.animate.shift(DOWN),
                run_time=2)
        
        self.wait(1)

        # Show that the areas are equal
        equal_sign = MathTex(r"=").scale(1.5)
        self.play(Write(equal_sign),
                  Wiggle(ps),
                   run_time=2)

        self.wait(2)

        self.play(FadeOut(equal_sign, shift = UP * 2), FadeOut(a_area), FadeOut(b_area))
        b_area.remove_updater(lambda m: m.move_to(b_square1.get_center()))

        # The middle squares:
        middle_big_square = Square(side_length=3.5, color=BLUE, fill_opacity=0.5)
        middle_small_square1 = Square(side_length=2, color=GREEN, fill_opacity=0.5)
        middle_small_square2 = middle_small_square1.copy()

        middle_small_square1.align_to(middle_big_square.get_corner(UL), UL)
        middle_small_square2.align_to(middle_big_square.get_corner(DR), DR)

        self.play(TransformMatchingShapes(a_square, middle_big_square),
                  TransformMatchingShapes(b_square2, middle_small_square1),
                  TransformMatchingShapes(b_square1, middle_small_square2),
                  run_time=2)
        self.wait(2)

        self.next_section("Conclusion")
        # The remaining variables are:
        # title: sqrt(2) = a/b in Q
        # ps: a^2 = 2 b^2
        # middle_big_square, middle_small_square1, middle_small_square2

        # Highlight the overlapping areas
        small_overlap = Square(side_length=0.5, color=RED, fill_opacity=0.7)
        small_overlap.move_to(middle_big_square.get_center())

        big_overlap1 = Square(side_length=1.5, color=YELLOW, fill_opacity=0.7)
        big_overlap2 = big_overlap1.copy()

        big_overlap1.align_to(middle_big_square.get_corner(DL), DL)
        big_overlap2.align_to(middle_big_square.get_corner(UR), UR)

        self.play(FadeIn(small_overlap), 
                  FadeIn(big_overlap1), FadeIn(big_overlap2),
                    run_time=2)
        self.wait(2)

        self.play(FadeOut(middle_big_square),
                  FadeOut(middle_small_square1),
                FadeOut(middle_small_square2),
                small_overlap.animate.shift(LEFT * 2),
                big_overlap1.animate.shift(RIGHT * 3),
                big_overlap2.animate.shift(RIGHT),
                FadeIn(equal_sign.move_to(ORIGIN)),
                Wiggle(ps),
                run_time=2)
        self.wait(2)

        absurd = MathTex(r"\text{Absurd!}").set_color(RED)
        absurd.next_to(equal_sign, UP)
        self.play(Write(absurd), FadeOut(ps, shift=DOWN), run_time=2)
        self.wait(4)

        conclusion = MathTex(r"\sqrt{2}", r"\notin", r"\mathbb{Q}")
        conclusion[0].set_color(BLUE)
        
        self.play(FadeOut(small_overlap, shift=LEFT),
                  FadeOut(big_overlap1, shift=RIGHT),
                FadeOut(big_overlap2, shift=RIGHT),
                FadeOut(equal_sign, shift=DOWN * 2),
                FadeOut(absurd, shift=DOWN * 2),
                TransformMatchingTex(title, conclusion),
                run_time=2)


        




        



        