# Une vidéo qui explique le principe d'inclusion exclusion. 

from manim import *

class Introduction(Scene):
    def construct(self):

        self.next_section("Notations", skip_animations=False)

        titre = Tex("Quelques notations").scale(1.2).to_edge(UP, buff=1)
        sous_ligne = Underline(titre)
        self.play(Write(titre), Create(sous_ligne))

        circle = Circle(radius=0.8, color=RED_E, fill_color=RED_D, fill_opacity=1).shift(LEFT * 4)

        square = Square(side_length=1.5, color=BLUE_E, fill_color=BLUE_D, fill_opacity=1)

        star = Star(outer_radius=0.8, color=GREEN_E, fill_color=GREEN_D, fill_opacity=1).shift(RIGHT * 4)

        self.play(DrawBorderThenFill(circle))
        self.wait()
        self.play(DrawBorderThenFill(square))
        self.wait()
        self.play(DrawBorderThenFill(star))
        self.wait()

        self.play(Indicate(circle, color=RED_E))
        self.play(FadeOut(square, star, shift=DOWN * 2),
                  circle.animate.move_to(ORIGIN))
        self.wait()

        circle_copy = circle.copy()

        label_A = Tex("A").move_to(circle.get_center())
        label_A.add_updater(lambda m : m.move_to(circle.get_center()))

        label_B = Tex("B").move_to(circle_copy.get_center())
        label_B.add_updater(lambda m : m.move_to(circle_copy.get_center()))

        self.add(circle_copy)
        self.play(circle_copy.animate.shift(RIGHT * 1).set_color(BLUE_E),
                  circle.animate.shift(LEFT))
        self.wait()

        self.play(Write(label_A), Write(label_B))
        self.wait()

        self.play(circle_copy.animate.shift(LEFT * 0.8))
        self.wait()

        notation = MathTex(r"A", r"\cup", r"B").shift(RIGHT * 4)
        self.play(Write(notation))
        self.wait()

        self.play(Circumscribe(VGroup(circle, circle_copy), Rectangle, time_width=4, fade_out=True, color=ORANGE),
                  ApplyWave(notation, time_width=2))
        self.wait()

        union = Union(circle, circle_copy, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5)
        union_indication = MathTex(r"A \cup B").move_to(union.get_center()).scale(0.5)
        union_indication.add_updater(lambda m : m.move_to(union.get_center()))

        self.play(GrowFromCenter(union))
        self.play(union.animate.to_edge(LEFT, buff=0.5).shift(UP).scale(0.5))
        self.play(Write(union_indication))
        self.wait()

        notation2 = MathTex(r"A", r"\cap", r"B").shift(RIGHT * 4)
        self.play(TransformMatchingTex(notation, notation2, fade_transform_mismatches=True))
        self.wait()

        intersection_1 = Intersection(circle, circle_copy, color=PURPLE_E, fill_color=PURPLE_D, fill_opacity=0.5)
        intersection_indication = MathTex(r"A \cap B").move_to(intersection_1.get_center()).scale(0.5)
        intersection_indication.add_updater(lambda m : m.next_to(intersection_1, direction=RIGHT, buff=0.5))

        self.play(Circumscribe(Intersection(circle, circle_copy), Rectangle, time_width=4, fade_out=True, color=ORANGE),
                  ApplyWave(notation2, time_width=2))
        self.wait()

        self.play(GrowFromCenter(intersection_1))
        self.play(intersection_1.animate.next_to(union, direction=DOWN, buff=0.5).shift(LEFT * 0.5).scale(0.6))
        self.play(Write(intersection_indication))
        self.wait()

        notation3 = MathTex(r"A", r"\backslash", r"B").shift(RIGHT * 4)
        self.play(TransformMatchingTex(notation2, notation3, fade_transform_mismatches=True))
        self.wait()

        prive = Difference(circle, circle_copy, color=YELLOW_E, fill_color=YELLOW_D, fill_opacity=0.5)
        prive_indication = MathTex(r"A \backslash B").move_to(prive.get_center()).scale(0.5)
        prive_indication.add_updater(lambda m : m.move_to(prive.get_center()))

        self.play(Circumscribe(Difference(circle, circle_copy), Rectangle, time_width=4, fade_out=True, color=ORANGE),
                  ApplyWave(notation3, time_width=2))
        self.wait()

        self.play(GrowFromCenter(prive))
        self.play(prive.animate.next_to(union, direction=DOWN, buff=0.6).shift(DOWN).scale(0.6))
        self.play(Write(prive_indication))
        self.wait(3)

        self.play(FadeOut(VGroup(circle, circle_copy, union, intersection_1, prive,
                              label_A, label_B, union_indication, intersection_indication, prive_indication,
                              notation3, sous_ligne, titre)))
        self.wait()

        self.next_section("Introduction", skip_animations=False)

        titre  = Tex("Principe d'inclusion-exclusion").scale(1.2)
        self.play(Write(titre))
        self.wait()

        self.play(FadeOut(titre))

        # Aucune variable dans l'écran.

        self.next_section("Exemple concret", skip_animations=False)

        carre1 = Square(side_length=2, color=RED_E, fill_opacity=1,
                        fill_color=RED_D).shift(LEFT * 2)
        carre2 = Square(side_length=2, color=BLUE_E, fill_opacity=1,
                        fill_color=BLUE_D).shift(RIGHT * 2)
        
        carre_A = Tex("A").move_to(carre1.get_center())
        carre_A.add_updater(lambda m : m.move_to(carre1.get_center()))

        carre_B = Tex("B").move_to(carre2.get_center())
        carre_B.add_updater(lambda m : m.move_to(carre2.get_center()))

        self.play(DrawBorderThenFill(carre1), DrawBorderThenFill(carre2))
        self.wait()
        self.play(Write(carre_A), Write(carre_B))
        self.wait()

        self.play(carre1.animate.shift(RIGHT),
                  carre2.animate.shift(LEFT))
        
        group = VGroup(carre1, carre2)
        self.play(Circumscribe(group, Rectangle, time_width=4, fade_out=True,
                               color=ORANGE))
        self.wait()

        aire_total = MathTex(r"\text{Aire}_{tot}")
        aire_total.to_edge(UP, buff=1).shift(LEFT)

        equation = MathTex(r"=", r"A", r"+", r"B")
        equation.next_to(aire_total, direction=RIGHT, buff=0.3)

        self.play(Write(aire_total))
        self.wait()
        self.play(Write(equation))
        self.wait()

        carre_A.remove_updater(lambda m : m.move_to(carre1.get_center()))

        self.play(carre1.animate.shift(RIGHT).scale(1.5),
                  carre2.animate.scale(0.5).shift(RIGHT * 2),
                  carre_B.animate.scale(0.4),
                  carre_A.animate.next_to(carre1.get_corner(DL),
                                                 direction=UR, buff=0.5))
        
        self.play(carre2.animate.next_to(carre1.get_corner(UR),
                                         direction=DL, buff=0))
        self.wait()
        self.play(Circumscribe(group, Rectangle, time_width=4, fade_out=True,
                               color=ORANGE))
        self.wait()
        
        equation2 = MathTex(r"\neq", r"A", r"+", r"B").next_to(aire_total, direction=RIGHT, buff=0.3)
        self.play(TransformMatchingTex(equation, equation2, fade_transform_mismatches=True))
        self.wait()

        equation3 = MathTex(r"=", r"A").next_to(aire_total, direction=RIGHT, buff=0.3)
        self.play(TransformMatchingTex(equation2, equation3, fade_transform_mismatches=True))
        self.wait()

        self.play(carre2.animate.shift(RIGHT * 0.5))
        self.wait()

        equation4 = MathTex(r"=", r"A", r"+", r"\frac{1}{2}B").next_to(aire_total, direction=RIGHT, buff=0.3)
        self.play(TransformMatchingTex(equation3, equation4, fade_transform_mismatches=True))
        self.wait(3)
        
        equation5 = MathTex(r"=", r"A", r"+", r"B", r"-", r"C").next_to(aire_total, direction=RIGHT, buff=0.3)
        self.play(TransformMatchingTex(equation4, equation5, fade_transform_mismatches=True))
        self.wait()

        group1 = VGroup(carre1, carre2, equation5, aire_total, carre_A, carre_B)
        self.play(FadeOut(group1, shift=DOWN))

        self.next_section("Venn diagrams", skip_animations=False)

        cercle1 = Circle(radius=1.2, color=RED_E, 
                        fill_color=RED_D, fill_opacity=0).shift(LEFT * 2)
        a = Tex("A")
        a.add_updater(lambda m: m.next_to(cercle1, direction=DOWN, buff=0.6))
        
        cercle2 = Circle(radius=1.2, color=BLUE_E,
                         fill_color=BLUE_D, fill_opacity=0).shift(RIGHT * 2)
        b = Tex("B")
        b.add_updater(lambda m : m.next_to(cercle2, direction=DOWN, buff=0.6))

        self.play(DrawBorderThenFill(cercle1), DrawBorderThenFill(cercle2))
        self.play(Write(a), Write(b))
        self.wait()

        self.play(cercle1.animate.shift(RIGHT * 1.2),
                  cercle2.animate.shift(LEFT * 1.2))
        self.wait()

        intersection = Intersection(cercle1, cercle2)
        intersection.set_fill(ORANGE)
        intersection.set_opacity(0)

        self.add(intersection)

        self.play(cercle1.animate.set_opacity(1),
                  cercle2.animate.set_opacity(1),
                  intersection.animate.set_opacity(1))
        
        carre_indice1 = Square(side_length=0.2, fill_color=RED_D, color=RED_D,
                               fill_opacity=1)
        indice1 = MathTex(r"A \backslash B").scale(0.5).next_to(carre_indice1, direction=RIGHT, buff=0.4)

        carre_indice2 = Square(side_length=0.2, fill_color=ORANGE, color=ORANGE,
                               fill_opacity=1).next_to(carre_indice1, direction=DOWN, buff=0.5)
        indice2 = MathTex(r"A \cap B").scale(0.5).next_to(carre_indice2, direction=RIGHT, buff=0.4)

        carre_indice3 = Square(side_length=0.2, fill_color=BLUE_D, color=BLUE_D,
                               fill_opacity=1).next_to(carre_indice2, direction=DOWN, buff=0.5)
        indice3 = MathTex(r"B \backslash A").scale(0.5).next_to(carre_indice3, direction=RIGHT, buff=0.4)

        indication_group = VGroup(carre_indice1, indice1,
                                  carre_indice2, indice2,
                                  carre_indice3, indice3)
        
        indication_group.to_edge(LEFT, buff=0.5)
        self.play(DrawBorderThenFill(carre_indice1),
                  DrawBorderThenFill(carre_indice2),
                  DrawBorderThenFill(carre_indice3),
                  Write(indice1),
                  Write(indice2),
                  Write(indice3))
        self.wait()

        equation = MathTex(r"P(A \cup B)", r"\equiv", r"\text{Aire}_{tot}").to_edge(UP, buff=1)

        self.play(Circumscribe(VGroup(cercle1, cercle2), Rectangle, time_width=4, fade_out=True,
                               color=ORANGE))
        self.wait()
        self.play(Write(equation))
        self.wait()

        equation2 = MathTex(r"P(A \cup B)", r"=", r"P(A)", r"+", r"P(B)").to_edge(UP, buff=1)
        self.play(TransformMatchingTex(equation, equation2, fade_transform_mismatches=True))
        self.wait()

        self.play(Indicate(equation2[2], color=RED_D),
                    Indicate(cercle1, color=RED_E), run_time=2)
        self.wait(2)

        cercle2.z_index = -1

        self.play(Indicate(equation2[4], color=BLUE_D),
                    Indicate(cercle2, color=BLUE_E), run_time=2)
        self.wait(2)

        fois_deux = MathTex(r"\times 2").move_to(intersection.get_center()).scale(0.7)
        self.play(Indicate(intersection, color=ORANGE),
                Write(fois_deux, rate_func=there_and_back), run_time=2)

        equation3 = MathTex(r"P(A \cup B)", r"=", r"P(A)", r"+", r"P(B)", r"-", r"P(A \cap B)").to_edge(UP, buff=1)
        self.play(TransformMatchingTex(equation2, equation3, fade_transform_mismatches=True))
        self.wait(3)

        A_copie = Difference(cercle1, intersection, color=RED_E, fill_color=RED_D, fill_opacity=1)
        B_copie = Difference(cercle2, intersection, color=BLUE_E, fill_color=BLUE_D, fill_opacity=1)
        inter_copie = intersection.copy()

        self.add(A_copie, B_copie, inter_copie)
        self.play(A_copie.animate.shift(LEFT * 2.5 + UP * 1).scale(0.5),
                  B_copie.animate.shift(RIGHT * 2.5 + UP * 1).scale(0.5),
                    inter_copie.animate.shift(UP * 1.5).scale(0.5))
        
        self.play(ApplyWave(VGroup(A_copie, B_copie, inter_copie), time_width=2))
        self.play(FadeOut(A_copie, B_copie, inter_copie, shift=DOWN))
        self.wait(2)

        self.play(FadeOut(cercle1, cercle2, intersection, equation3, indication_group, a, b))
        self.wait(2)

        self.next_section("Généralisation", skip_animations=False)

        formule = MathTex(r"\left| \bigcup_{i=1}^k A_i \right|",
                          r"=", r"\sum_{j=1}^k (-1)^{j-1}",
                          r"\sum_{1 \leq i_1 < \dotsb < i_j \leq k} \left| A_{i_{1}} \cap A_{i_{2}} \cap \dotsb \cap A_{i_{j}} \right|",)
        
        self.play(Write(formule))
        self.wait(3)

        self.play(FadeOut(formule))

        c1 = Circle(radius=0.8, color=RED_E, fill_color=RED_D, fill_opacity=0.5).shift(LEFT * 0.4 + UP * 0.4)
        c2 = Circle(radius=0.8, color=BLUE_E, fill_color=BLUE_D, fill_opacity=0.5).shift(RIGHT * 0.4 + UP * 0.4)
        c3 = Circle(radius=0.8, color=GREEN_E, fill_color=GREEN_D, fill_opacity=0.5).shift(DOWN * 0.4)

        labA = Tex("A").next_to(c1, direction=LEFT, buff=0.3)
        labB = Tex("B").next_to(c2, direction=RIGHT, buff=0.3)
        labC = Tex("C").next_to(c3, direction=DOWN, buff=0.3)


        self.play(DrawBorderThenFill(c1), DrawBorderThenFill(c2), DrawBorderThenFill(c3),
                  Write(labA), Write(labB), Write(labC), rate_function=smooth)

        self.wait(2)

        labA.add_updater(lambda m : m.next_to(c1, direction=LEFT, buff=0.3))
        labB.add_updater(lambda m : m.next_to(c2, direction=RIGHT, buff=0.3))
        labC.add_updater(lambda m : m.next_to(c3, direction=DOWN, buff=0.3))


        formulae1 = MathTex(r"|", r"A", r"\cup", r"B", r"\cup", r"C", r"|").to_edge(UP, buff=0.4).scale(0.8)

        self.play(VGroup(c1, c2, c3).animate.shift(LEFT * 4))
        self.wait()

        labA_copie = labA.copy()
        labB_copie = labB.copy()
        labC_copie = labC.copy()

        self.play(TransformMatchingTex(VGroup(labA_copie, labB_copie, labC_copie), 
                                      formulae1, fade_transform_mismatches=True))
        self.wait(2)

        labA_copie2 = labA.copy()
        labB_copie2 = labB.copy()
        labC_copie2 = labC.copy()

        c1_copie = c1.copy()
        c2_copie = c2.copy()
        c3_copie = c3.copy()

        forumulae2 = MathTex(r"|", r"A", r"\cup", r"B", r"\cup", r"C", r"|",
                             r"=", r"|", r"A", r"|").to_edge(UP, buff=0.4).scale(0.8)
                             
        self.play(Indicate(c1, color=RED_E), run_time=2)
        
        self.play(c1_copie.animate.shift(RIGHT * 7),
                  TransformMatchingTex(VGroup(formulae1, labA_copie2), 
                                      forumulae2, fade_transform_mismatches=True),
                                      run_time=2)
        self.wait(2)

        forumulae3 = MathTex(r"|", r"A", r"\cup", r"B", r"\cup", r"C", r"|",
                             r"=", r"|", r"A", r"|", r"+", r"|", r"B", r"|" ).to_edge(UP, buff=0.4).scale(0.8)
                             
        self.play(Indicate(c2, color=BLUE_E), run_time=2)
        
        self.play(c2_copie.animate.shift(RIGHT * 9),
                  TransformMatchingTex(VGroup(forumulae2, labB_copie2), 
                                      forumulae3, fade_transform_mismatches=True),
                                      run_time=2)
        self.wait(2)

        forumulae4 = MathTex(r"|", r"A", r"\cup", r"B", r"\cup", r"C", r"|",
                             r"=", r"|", r"A", r"|", r"+", r"|", r"B", r"|",
                             r"+", r"|", r"C", r"|").to_edge(UP, buff=0.4).scale(0.8)
                             
        self.play(Indicate(c3, color=GREEN_E), run_time=2)
        
        self.play(c3_copie.animate.shift(RIGHT * 8 + DOWN),
                  TransformMatchingTex(VGroup(forumulae3, labC_copie2), 
                                      forumulae4, fade_transform_mismatches=True),
                                      run_time=2)
        self.wait(2)

        AinterB = Intersection(c1, c2, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5)
        BinterC = Intersection(c2, c3, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5)
        AinterC = Intersection(c1, c3, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5)

        labAinterB = MathTex(r"A \cap B").next_to(AinterB, direction=UP, buff=0.3).scale(0.5)
        labBinterC = MathTex(r"B \cap C").next_to(BinterC, direction=RIGHT, buff=0.3).scale(0.5)
        labAinterC = MathTex(r"A \cap C").next_to(AinterC, direction=LEFT, buff=0.3).scale(0.5)

        self.play(GrowFromCenter(AinterB), run_time=0.5)
        self.play(Indicate(AinterB, color=ORANGE),
                  Write(labAinterB), run_time=2)
        
        formula5 = MathTex(r"|", r"A", r"\cup", r"B", r"\cup", r"C", r"|",
                             r"&=", r"|", r"A", r"|", r"+", r"|", r"B", r"|",
                             r"+", r"|", r"C", r"|", r"\\",
                             r"&-", r"|", r"A \cap B", r"|").to_edge(UP, buff=0.4).scale(0.8)
        
        self.play(TransformMatchingTex(VGroup(forumulae4, labAinterB), 
                                      formula5, fade_transform_mismatches=True),
                                      AinterB.animate.shift(RIGHT * 7), run_time=2)
        
        differenceA = Difference(c1_copie,  AinterB, color=RED_E, fill_color=RED_D, fill_opacity=0.5)

        self.play(Transform(VGroup(c1_copie, AinterB), differenceA))
        self.wait(2)

        self.play(GrowFromCenter(BinterC), run_time=0.5)
        self.play(Indicate(BinterC, color=ORANGE),
                  Write(labBinterC), run_time=2)
        
        formula6 = MathTex(r"|", r"A", r"\cup", r"B", r"\cup", r"C", r"|",
                             r"&=", r"|", r"A", r"|", r"+", r"|", r"B", r"|",
                             r"+", r"|", r"C", r"|", r"\\",
                             r"&-", r"|", r"A \cap B", r"|",
                             r"-", r"|", r"B \cap C", r"|").to_edge(UP, buff=0.4).scale(0.8)
        
        self.play(TransformMatchingTex(VGroup(formula5, labBinterC), 
                                      formula6, fade_transform_mismatches=True),
                                      BinterC.animate.shift(RIGHT * 9), run_time=2)
        
        differenceB = Difference(c2_copie,  BinterC, color=BLUE_E, fill_color=BLUE_D, fill_opacity=0.5)

        self.play(Transform(VGroup(c2_copie, BinterC), differenceB))
        self.wait(2)

        self.play(GrowFromCenter(AinterC), run_time=0.5)
        self.play(Indicate(AinterC, color=ORANGE),
                  Write(labAinterC), run_time=2)
        
        formula7 = MathTex(r"|", r"A", r"\cup", r"B", r"\cup", r"C", r"|",
                             r"&=", r"|", r"A", r"|", r"+", r"|", r"B", r"|",
                             r"+", r"|", r"C", r"|", r"\\",
                             r"&-", r"|", r"A \cap B", r"|",
                             r"-", r"|", r"B \cap C", r"|",
                             r"-", r"|", r"A \cap C", r"|").to_edge(UP, buff=0.4).scale(0.8)
        
        self.play(TransformMatchingTex(VGroup(formula6, labAinterC), 
                                      formula7, fade_transform_mismatches=True),
                                      AinterC.animate.shift(RIGHT * 8 + DOWN), run_time=2)
        
        differenceC = Difference(c3_copie,  AinterC, color=GREEN_E, fill_color=GREEN_D, fill_opacity=0.5)

        self.play(Transform(VGroup(c3_copie, AinterC), differenceC))
        self.wait(2)

        self.play(c1_copie.animate.shift(RIGHT),
                  c2_copie.animate.shift(LEFT),
                  c3_copie.animate.shift(UP))
        self.wait(2)

        intersection_finale = Intersection(c1, c2, c3, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5)
        lab_intersection_finale = MathTex(r"A \cap B \cap C").next_to(intersection_finale, direction=UP, buff=1).scale(0.5)

        formula8 = MathTex(r"|", r"A", r"\cup", r"B", r"\cup", r"C", r"|",
                             r"&=", r"|", r"A", r"|", r"+", r"|", r"B", r"|",
                             r"+", r"|", r"C", r"|", r"\\",
                             r"&-", r"|", r"A \cap B", r"|",
                             r"-", r"|", r"B \cap C", r"|",
                             r"-", r"|", r"A \cap C", r"|", r"\\",
                             r"&+", r"|", r"A \cap B \cap C", r"|").to_edge(UP, buff=0.4).scale(0.8)

        self.play(GrowFromCenter(intersection_finale), run_time=0.5)
        self.play(Indicate(intersection_finale, color=ORANGE),
                  Write(lab_intersection_finale), run_time=2)
        self.play(TransformMatchingTex(VGroup(formula7, lab_intersection_finale),
                                      formula8, fade_transform_mismatches=True),
                                    intersection_finale.animate.shift(RIGHT * 8), run_time=2)
        self.wait(3)

        self.play(FadeOut(VGroup(AinterB, BinterC, AinterC, c1_copie, c2_copie, c3_copie,
                              labA, labB, labC, intersection_finale,
                              formula8, c1, c2, c3)))
        self.wait(2)

        self.next_section("Credits")

        credits1 = Tex("Vidéo réalisée grâce à Manim:", color=WHITE).to_edge(UP, buff=1).scale(0.8)

        manimBanner = ManimBanner().scale(0.8).shift(DOWN * 0.5)

        self.play(Write(credits1), Create(manimBanner))
        self.wait(3)
        

        self.play(FadeOut(credits1, manimBanner))
