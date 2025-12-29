from manim import *


class PutnamProblem1(Scene):
    def construct(self):
        
        announce = Text("Problem 1:").scale(0.8)
        announce.shift(UP)
        
        problem = MathTex(r"\text{Prove that }", r"\sqrt{2}+\sqrt{3}+\sqrt{5}", 
                          r"\text{ is irrational.}")

        # Display the problem on the screen
        self.play(Write(announce), Write(problem))   

        # Wait for a moment to let the viewer see the problem
        self.wait(2)

        number = MathTex(r"\text{Let }", "x", ":", "=", r"\sqrt{2}+\sqrt{3}+\sqrt{5}")
        number.to_edge(UP)

        self.play(TransformMatchingTex(problem, number), FadeOut(announce))
        self.wait(1)

        # Notice:

        warning_sign = Circle().scale(0.5)
        warning_sign.set_fill(opacity=0, color=WHITE)
        warning_sign.set_stroke(WHITE, width=6)

        exclamation = Text("!", color=WHITE).move_to(warning_sign.get_center())
        group = VGroup(warning_sign, exclamation).scale(0.7)

        careful = Paragraph("""
                       Be careful, 
                       prooving each term irrational is not enough, 
                       irrationality is not closed under addition!
                       """, 
                       alignment="center",
                       line_spacing=1.2).scale(0.6)
        
        careful.shift(DOWN)
        group.next_to(careful, UP)

        self.play(Write(careful), DrawBorderThenFill(group))
        self.wait(3)
        self.play(FadeOut(careful), FadeOut(group))

        supposition = MathTex(r"\text{Suppose } x \text{ is rational.}")
        self.play(Write(supposition))

        updated_number = MathTex(r"x", "=", r"\sqrt{2}+\sqrt{3}+\sqrt{5}", r"\in", r"\mathbb{Q}")
        updated_number.to_edge(UP)

        self.play(TransformMatchingTex(number, updated_number), FadeOut(supposition))
        self.wait(1)


        # Start solving the problem
        ###

        step1_guide = Tex("Rearrange: ").shift(UP + LEFT*5).scale(0.8)
        self.play(Write(step1_guide))

        step1 = MathTex(r"x", "-", r"\sqrt{5}", "=", r"\sqrt{2}", "+",  r"\sqrt{3}")
        self.play(Write(step1))
        self.wait(2)

        step2_guide = Tex("Square both sides: ").shift(UP + LEFT*4.5).scale(0.8)
        self.play(Transform(step1_guide, step2_guide))

        # Adding squares
        step2 = MathTex("(", "x", "-", r"\sqrt{5}", ")^2", "=", 
                        "(", r"\sqrt{2}", "+",  r"\sqrt{3}", ")^2")

        # Identité remarquable
        step2_1 = MathTex("x", "^2", "-", "2", "x", r"\sqrt{5}", "+", "5", "=", 
                        "2", "+", "3", "+", "2", r"\sqrt{6}")

        # Simplify
        step2_2 = MathTex("x", "^2", "+", "5", "-", "2", "-", "3", "=", 
                        "2", r"\sqrt{6}", "+", "2", "x", r"\sqrt{5}")
        
        # Rearrange
        step2_3 = MathTex("x", "^2", "=", 
                        "2", "\sqrt{6}", "+", "2", "x", "\sqrt{5}")
        
        steps2 = [step1, step2, step2_1, step2_2, step2_3]

        def play_steps(step_list, wait_time=2):
            for i in range(len(step_list) - 1):
                self.play(TransformMatchingTex(step_list[i], step_list[i+1],
                                                transform_mismatches=True))
                self.wait(wait_time)    

        play_steps(steps2)


        # Needs fixing here
        step3_guide = Tex("Square both sides again: ").shift(UP + LEFT*4.5).scale(0.8)
        self.play(Transform(step1_guide, step3_guide))

        step3 = MathTex("(", "x", "^2", ")^2", "=", "(",
                        "2", r"\sqrt{6}", "+", "2", "x", r"\sqrt{5}", ")", "^2")
        
        step3_1 = MathTex("x", "^4", "=", 
                        "24", "+", "8", "x", r"\sqrt{30}", "+", "20", "x", "^2")
        
        steps3 = [step2_3, step3, step3_1]
        play_steps(steps3)

        self.wait(2)

        # Add deduction:
        deduction = MathTex(r"\text{If } x \in \mathbb{Q},", r"\text{ then }", 
                            r"x^4 \in \mathbb{Q}.").scale(0.8).set_fill(
                                opacity=1, color=YELLOW)
        deduction.next_to(step3_1, DOWN, buff=1)

        self.play(Write(deduction), FadeOut(step1_guide))
        self.wait(2)

        math_deduction = MathTex("x", "^4", "=", 
                        "24", "+", "8", "x", r"\sqrt{30}", "+", "20", "x", "^2",
                        r"\in", r"\mathbb{Q}")
        
        math_deduction.next_to(updated_number, DOWN)

        self.play(TransformMatchingTex(step3_1, math_deduction))
        self.play(FadeOut(deduction))
        self.wait(2)

        deduction2 = MathTex("24", "+", "8", "x",
                        r"\sqrt{30}", "+", "20", "x", "^2",
                        r"\in", r"\mathbb{Q}").next_to(updated_number, DOWN)
        
        self.play(TransformMatchingTex(math_deduction, deduction2))
        self.wait(2)

        deduction = MathTex(r"\text{However, }", "24 + 20 x^2", r"\in", r"\mathbb{Q},",
                            r"\text{thus }", "8 x \sqrt{30}",
                            r"\in", r"\mathbb{Q}.").scale(0.8).set_fill(
                                opacity=1, color=YELLOW)
        
        self.play(Write(deduction))
        self.wait(2)

        deduction3 = MathTex("8", "x", r"\sqrt{30}", r"\in", r"\mathbb{Q}")
        deduction3.next_to(updated_number, DOWN)

        self.play(TransformMatchingTex(deduction2, deduction3), FadeOut(deduction))
        self.wait(2)

        deduction = MathTex(r"\text{Since }", "8", "x", r"\in", r"\mathbb{Q},",
                            r"\text{ we must have }",
                            r"\sqrt{30}", r"\in", r"\mathbb{Q}.").scale(0.8).set_fill(
                                opacity=1, color=YELLOW)
        
        self.play(Write(deduction))
        self.wait(2)

        deduction4 = MathTex(r"\sqrt{30}", r"\in", r"\mathbb{Q}").next_to(updated_number, DOWN)
        self.play(TransformMatchingTex(deduction3, deduction4), FadeOut(deduction))
        self.wait(2)

        # Proving that sqrt(30) is irrational
        contradiction1 = MathTex(r"\text{Since } \sqrt{30} \text{ is rational,}",
                                 ).scale(0.8)
        
        contradiction1_1 = MathTex(r"\text{ there exist coprime integers, }" , 
                                 r"n, m \in \mathbb{N}",).scale(0.8)
        
        contradiction1_2 = MathTex(r"\text{ such that }",
                                 r"\sqrt{30}",  "=", r"\frac{n}{m}.").scale(0.8)
        
        contradiction1_1.next_to(contradiction1, DOWN)
        contradiction1_2.next_to(contradiction1_1, DOWN)
        
        self.play(Write(contradiction1),
                Write(contradiction1_1), 
                Write(contradiction1_2))
        
        self.wait(3)
        
        contradiction2 = MathTex(r"\sqrt{30}", "=", r"\frac{n}{m}").scale(0.8)
        
        self.play(TransformMatchingTex(contradiction1_2, contradiction2),
                FadeOut(contradiction1),
                FadeOut(contradiction1_1))
        self.wait(2)
        
        squared_contradiction = MathTex("30", "=", r"\frac{n^2}{m^2}").scale(0.8)
        
        contradiction3 = MathTex("30", "m^2", "=", "n^2").scale(0.8)
        
        contradiction4 = MathTex("2", r"\times", "15", "m^2", "=", "n^2").scale(0.8)
        
        contradictions = [contradiction2,
                          squared_contradiction, contradiction3,
                          contradiction4]
        
        play_steps(contradictions)
        
        # Color the two in red
        
        contradiction4_1 = MathTex("2", r"\times", "15", "m^2", "=", "n^2").scale(0.8)
        contradiction4_1[0][0].set_color(RED)
        
        self.play(TransformMatchingTex(contradiction4, contradiction4_1))
        
        contradiction5 = MathTex(r"\text{Thus, } n^2 \text{ is even}").scale(0.8).shift(DOWN)
        
        self.play(Write(contradiction5))
        self.wait(2)
        
        contradiction6 = MathTex(r"\text{So, } n \text{ is even}").scale(0.8).shift(DOWN)
        self.play(Transform(contradiction5, contradiction6))
        self.wait(2)
        
        contradiction7 = MathTex(r"\text{Hence, there exists } k \in \mathbb{N},",
                                 r"\text{ such that } n = 2k.").scale(0.8).shift(DOWN)
        self.play(Transform(contradiction6, contradiction7), FadeOut(contradiction5))
        self.wait(2)
        
        # Replace n by 2k in the equation
        contradiction8 = MathTex("2", r"\times", "15", "m^2", "=", "(", "2", "k",
                                 ")", "^2").scale(0.8)
        self.play(TransformMatchingTex(contradiction4_1, contradiction8,
                                                transform_mismatches=True))
        self.wait(2)
        
        contradiction9 = MathTex("2", r"\times", "15", "m^2", "=", "4", "k", "^2").scale(0.8)
        self.play(TransformMatchingTex(contradiction8, contradiction9), FadeOut(contradiction6))
        self.wait(2)    
        
        contradiction10 = MathTex("15", "m^2", "=", "2", "k", "^2").scale(0.8)
       
        self.play(TransformMatchingTex(contradiction9, contradiction10))
        self.wait(2)
        
        last_contradiction = MathTex(r"\text{Thus, }", "m", "^2",
                                     r"\text{ is even.}").scale(0.8).shift(DOWN)
        
        self.play(Write(last_contradiction))
        self.wait(2)
        
        last_contradiction2 = MathTex(r"\text{So }", "m",
                                      r"\text{ is even.}").scale(0.8).shift(DOWN)
        self.play(TransformMatchingTex(last_contradiction, last_contradiction2),
                  FadeOut(contradiction10))
        self.wait(2)
        
        final_contradiction = MathTex(r"\begin{cases} 2 \mid n \\ 2 \mid m \end{cases}",
                                    r"\Longrightarrow",
                                    r"\gcd(n,m) \ge 2").scale(0.8)
        
        deduction_final = MathTex(r"\text{Thus we deduce that: }",).scale(0.8)
        deduction_final.next_to(final_contradiction, UP)
        
        self.play(Write(final_contradiction), Write(deduction_final), FadeOut(last_contradiction2))
        self.wait(3)
        
        super_final = MathTex(r"\gcd(n,m)", r"\ge 2").scale(0.8)
        super_final.shift(UP * 2.5 + RIGHT * 4)
        
        
        self.play(TransformMatchingTex(final_contradiction, super_final),
                    FadeOut(deduction_final))
        
        # Play reverse animation to show the contradiction
        self.wait(2)
        self.next_section("Contradiction")

        # Proving that sqrt(30) is irrational
        contradiction1 = MathTex(r"\text{Since } \sqrt{30} \text{ is rational,}",
                                 ).scale(0.8)
        
        contradiction1_1 = MathTex(r"\text{there exists }", "coprime", r"\text{ integers, }",
                                 r"n, m \in \mathbb{N}",).scale(0.8)
        
        contradiction1_2 = MathTex(r"\text{ such that }",
                                 r"\sqrt{30}",  "=", r"\frac{n}{m}.").scale(0.8)
        
        contradiction1_1.next_to(contradiction1, DOWN)
        contradiction1_2.next_to(contradiction1_1, DOWN)
        
        self.play(Write(contradiction1),
                Write(contradiction1_1), 
                Write(contradiction1_2))
        
        self.wait(3)

        contradiction2 = contradiction1_1

        contradiction2[1].set_color(RED)

        self.play(TransformMatchingTex(contradiction1_1, contradiction2))
        self.wait(2)

        conclusion = MathTex("coprime", r"\Longrightarrow", r"\gcd(n,m) = 1").scale(0.8)
        self.play(TransformMatchingTex(contradiction2, conclusion),
                    FadeOut(contradiction1), FadeOut(contradiction1_2))
        self.wait(3)

        self.play(super_final.animate.next_to(conclusion, DOWN))
        self.wait(2)

        super_final_2 = MathTex(r"\gcd(n,m)", "= 1", r"\ge 2").scale(0.8).next_to(conclusion, DOWN)
        self.play(TransformMatchingTex(super_final, super_final_2), FadeOut(conclusion))

        self.wait(2)

        final_statement = MathTex(r"\text{This is a contradiction!}").scale(0.8)
        self.play(Write(final_statement))

        self.wait(3)

        finale = MathTex(r"x", "=", r"\sqrt{2}+\sqrt{3}+\sqrt{5}", r"\notin", r"\mathbb{Q}")

        self.play(FadeOut(final_statement), FadeOut(super_final_2),
                  FadeOut(deduction4), TransformMatchingTex(updated_number, finale))
        
        self.wait(2)





        


        
        
        
        
        
        
        
        
