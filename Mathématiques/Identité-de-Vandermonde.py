# Vidéo explicative du triangle de Pascal, et de l'identité de Vandermonde.

from manim import * 

class Introduction(Scene):
    def construct(self):

        self.next_section("Introduction", skip_animations=False)
        
        # Regardons ce triangle. 
        triangle1 = Triangle().shift(UP)

        triangle21 = Triangle().next_to(triangle1.get_corner(DL), DOWN, buff=0)
        triangle22 = Triangle().next_to(triangle1.get_corner(DR), DOWN, buff=0)

        triangle31 = Triangle().next_to(triangle21.get_corner(DL), DOWN, buff=0)
        triangle32 = Triangle().next_to(triangle21.get_corner(DR), DOWN, buff=0)
        triangle33 = Triangle().next_to(triangle22.get_corner(DR), DOWN, buff=0)
      
        triangles = VGroup(triangle1, triangle21, triangle22, triangle31, triangle32, triangle33)

        self.play(Create(triangles))
        self.wait(0.5)

        point1 = Dot(triangle1.get_corner(UP))
        point2 = Dot(triangle21.get_corner(UP))
        point3 = Dot(triangle22.get_corner(UP))
        point4 = Dot(triangle31.get_corner(UP))
        point5 = Dot(triangle32.get_corner(UP))
        point6 = Dot(triangle33.get_corner(UP))
        point7 = Dot(triangle31.get_corner(DL))
        point8 = Dot(triangle31.get_corner(DR))
        point9 = Dot(triangle32.get_corner(DR))
        point10 = Dot(triangle33.get_corner(DR))

        points = VGroup(point1, point2, point3, point4, point5, point6, point7, point8, point9, point10)

        self.play(GrowFromCenter(point1),
                  GrowFromCenter(point2),
                  GrowFromCenter(point3),
                  GrowFromCenter(point4),
                  GrowFromCenter(point5),
                  GrowFromCenter(point6),
                  GrowFromCenter(point7),
                  GrowFromCenter(point8),
                  GrowFromCenter(point9),
                  GrowFromCenter(point10),)
        self.wait(2)

        self.play(Flash(points[0]))
        self.wait()
        self.play(points[0].animate.set_color(YELLOW_E), Flash(points[8]))
        self.wait()
        self.play(points[8].animate.set_color(YELLOW_E))
        self.wait(2)

        index1 = MathTex(r"1").shift(RIGHT * 3).set_color(YELLOW_E) 

        fleche1 = Arrow(start=point1.get_bottom(), end=point2.get_top(),
                         buff=0.05, color=RED_E, max_tip_length_to_length_ratio=0)
        fleche2 = Arrow(start=point2.get_bottom(), end=point5.get_top(),
                         buff=0.05, color=RED_E, max_tip_length_to_length_ratio=0)
        fleche3 = Arrow(start=point5.get_bottom(), end=point9.get_top(),
                         buff=0.05, color=RED_E, max_tip_length_to_length_ratio=0)
        
        fleches = VGroup(fleche1, fleche2, fleche3)
        self.play(Create(fleches), FadeIn(index1, shift=DOWN), rate_func=smooth)
        self.wait()

        index2 = MathTex(r"2").shift(RIGHT * 3).set_color(ORANGE)

        fleche1 = Arrow(start=point1.get_bottom(), end=point3.get_top(),
                            buff=0.05, color=RED_E, max_tip_length_to_length_ratio=0)
        fleche2 = Arrow(start=point3.get_bottom(), end=point5.get_top(),
                            buff=0.05, color=RED_E, max_tip_length_to_length_ratio=0)
        fleche3 = Arrow(start=point5.get_bottom(), end=point9.get_top(),
                            buff=0.05, color=RED_E, max_tip_length_to_length_ratio=0)
        
        fleches2 = VGroup(fleche1, fleche2, fleche3)

        self.play(Create(fleches2), FadeOut(index1, shift=DOWN),
                  fleches.animate.set_opacity(0.5),
                  FadeIn(index2, shift=DOWN), rate_func=smooth,)
        self.wait()

        index3 = MathTex(r"3").shift(RIGHT * 3).set_color(RED_E)

        fleche1 = Arrow(start=point1.get_bottom(), end=point3.get_top(),
                            buff=0.05, color=RED_E, max_tip_length_to_length_ratio=0)
        fleche2 = Arrow(start=point3.get_bottom(), end=point6.get_top(),
                            buff=0.05, color=RED_E, max_tip_length_to_length_ratio=0)
        fleche3 = Arrow(start=point6.get_bottom(), end=point9.get_top(),
                            buff=0.05, color=RED_E, max_tip_length_to_length_ratio=0)
        
        fleches3 = VGroup(fleche1, fleche2, fleche3)

        self.play(Create(fleches3), FadeOut(index2, shift=DOWN),
                  fleches2.animate.set_opacity(0.5),
                   FadeIn(index3, shift=DOWN), rate_func=smooth)
        self.wait()

        index4 = MathTex(r"3", r"?").scale(1.5).set_color(RED_E)

        self.play(FadeOut(fleches),FadeOut(fleches2), FadeOut(fleches3),
                   rate_func=smooth)
        
        self.play(triangles.animate.shift(LEFT * 3), points.animate.shift(LEFT * 3),
                 TransformMatchingTex(index3, index4), rate_func=smooth)
        self.wait()

        points2 = points.copy()
        self.play(points2.animate.shift(RIGHT * 6))
        self.wait()

        n1 = MathTex("1").move_to(point1.get_center())
        n2 = MathTex("1").move_to(point2.get_center())
        n3 = MathTex("1").move_to(point3.get_center())
        n4 = MathTex("1").move_to(point4.get_center())
        n5 = MathTex("2").move_to(point5.get_center())
        n6 = MathTex("1").move_to(point6.get_center())
        n7 = MathTex("1").move_to(point7.get_center())
        n8 = MathTex("3").move_to(point8.get_center())
        n9 = MathTex("3").move_to(point9.get_center())
        n10 = MathTex("1").move_to(point10.get_center())

        numbers = VGroup(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10).shift(RIGHT * 6)

        for i in range(len(numbers)):
            self.play(Transform(points2[i], numbers[i], run_time=0.3))

        self.wait()
        self.play(triangles.animate.shift(LEFT * 7), points.animate.shift(LEFT * 7),
                  FadeOut(points2, run_time=0.1),
                  FadeOut(index4, shift=DOWN), numbers.animate.shift(LEFT * 3))
        self.play(FadeOut(triangles), FadeOut(points))
        self.wait()

        plus_sign = MathTex(r"+").move_to((n4.get_center() - n5.get_center()) / 2).shift(DOWN)
        fleche1 = Arrow(start=n4.get_bottom(), end=n8.get_top(),
                        buff=0.5, color=YELLOW_E)
        fleche2 = Arrow(start=n5.get_bottom(), end=n8.get_top(),
                        buff=0.5, color=YELLOW_E)

        self.play(Create(fleche1), Create(fleche2), Write(plus_sign))
        self.wait()
        self.play(Uncreate(fleche1), Uncreate(fleche2), Unwrite(plus_sign))
        self.wait() 

        # Expliquer comment obtenir le coefficient binomial
        coef_binomial = MathTex(r"\binom{n}{k}").shift(LEFT * 3 + UP)
        coef_exemple = MathTex(r"\binom{2}{1}=").next_to(coef_binomial, LEFT, buff=0.4)
        self.play(Write(coef_exemple))
        self.play(Write(coef_binomial))
        self.wait(2)

        ligne0 = MathTex(r"n=0").next_to(n1, RIGHT, buff=1).shift(RIGHT * 3.5)
        ligne1 = MathTex(r"n=1").next_to(n3, RIGHT, buff=1).shift(RIGHT * 3)
        ligne2 = MathTex(r"n=2").next_to(n6, RIGHT, buff=1).shift(RIGHT * 2.5)
        ligne3 = MathTex(r"n=3").next_to(n10, RIGHT, buff=1).shift(RIGHT * 2)

        self.play(n4.animate.set_color(RED_E).scale(1.2), n5.animate.set_color(RED_E).scale(1.2),    
                  n6.animate.set_color(RED_E).scale(1.2), coef_binomial[0][1].animate.set_color(RED_E).scale(1.2),
                  FadeIn(ligne0, shift=RIGHT),
                  FadeIn(ligne1, shift=RIGHT),
                  FadeIn(ligne2, shift=RIGHT),
                  FadeIn(ligne3, shift=RIGHT),
                  rate_func=there_and_back, run_time=10)
        self.wait(2)

        self.play(n5.animate.set_color(ORANGE).scale(1.2),
                  coef_binomial[0][2].animate.set_color(ORANGE).scale(1.2),
                  rate_func=there_and_back, run_time=5)
        self.wait(2)

        answer = MathTex(r"2").move_to(coef_binomial.get_center())

        self.play(FadeOut(coef_binomial, shift=DOWN),
                  FadeIn(answer, shift=DOWN),
                    rate_func=smooth)
        self.wait(3)

        group = VGroup(answer, coef_exemple, numbers)

        self.play(FadeOut(group, shift=DOWN))
        self.wait()

        self.next_section("Exercice 4", skip_animations=False)
        equation = MathTex(r"\binom{n+1}{k+1}", r"=", r"\binom{n}{k}", r"+", r"\binom{n}{k+1}").scale(1.1)
        self.play(Write(equation))
        self.wait(2)

        separatrice = Line(start=UP * 3, end=DOWN * 3)
        self.play(FadeOut(equation, shift=DOWN), Create(separatrice))
        self.wait(2)

        p_bleues = Tex("On a n* personnes bleues").scale(0.6).to_edge(UP, buff=1).shift(LEFT * 4)
        indication = Tex("n = 10").scale(0.4).to_edge(DOWN, buff=1).shift(LEFT * 5)

        circle1 = Circle(radius=0.2, color=BLUE_E, fill_opacity=1).shift(RIGHT * 3 + UP * 2.5)
        circle2 = Circle(radius=0.2, color=BLUE_E, fill_opacity=1).shift(RIGHT * 4.5 + UP * 1.8)
        circle3 = Circle(radius=0.2, color=BLUE_E, fill_opacity=1).shift(RIGHT * 3.8 + UP * 1.5)
        circle4 = Circle(radius=0.2, color=BLUE_E, fill_opacity=1).shift(RIGHT * 5.2 + UP * 0)
        circle5 = Circle(radius=0.2, color=BLUE_E, fill_opacity=1).shift(RIGHT * 2.8 + DOWN * 0.7)
        circle6 = Circle(radius=0.2, color=BLUE_E, fill_opacity=1).shift(RIGHT * 4.0 + DOWN * 1.8)
        circle7 = Circle(radius=0.2, color=BLUE_E, fill_opacity=1).shift(RIGHT * 5.5 + DOWN * 2.3)
        circle8 = Circle(radius=0.2, color=BLUE_E, fill_opacity=1).shift(RIGHT * 3.2 + DOWN * 2.8)
        circle9 = Circle(radius=0.2, color=BLUE_E, fill_opacity=1).shift(RIGHT * 4.8 + DOWN * 0.8)
        circle10 = Circle(radius=0.2, color=BLUE_E, fill_opacity=1).shift(RIGHT * 6.0 + UP * 2.0)

        circles = VGroup(circle1, circle2, circle3, circle4, circle5,
                         circle6, circle7, circle8, circle9, circle10)

        self.play(Write(p_bleues), GrowFromCenter(circles), Write(indication))
        self.wait(2)

        p_rouges = Tex("On a une personne rouge").scale(0.6).next_to(p_bleues, DOWN, buff=0.5)
        circle_red = Circle(radius=0.2, color=RED_E, fill_opacity=1).shift(RIGHT * 3.5)
        self.play(Write(p_rouges), GrowFromCenter(circle_red))
        self.wait(2)

        equipe_k = Tex("Equipe de k* + 1 personnes").scale(0.6).next_to(p_rouges, DOWN, buff=0.5)
        indication_k = Tex("k = 4").scale(0.4).to_edge(DOWN, buff=1).shift(LEFT * 3)
        self.play(Write(equipe_k), Write(indication_k))
        self.wait(2)

        self.play(Circumscribe(circle_red, color=YELLOW_E, shape=Circle),
                  Circumscribe(circle1, color=YELLOW_E, shape=Circle),
                  Circumscribe(circle2, color=YELLOW_E, shape=Circle),
                  Circumscribe(circle3, color=YELLOW_E, shape=Circle),
                  Circumscribe(circle4, color=YELLOW_E, shape=Circle))
        
        self.play(Circumscribe(circle6, color=YELLOW_E, shape=Circle),
                  Circumscribe(circle8, color=YELLOW_E, shape=Circle),
                  Circumscribe(circle2, color=YELLOW_E, shape=Circle),
                  Circumscribe(circle4, color=YELLOW_E, shape=Circle),
                  Circumscribe(circle5, color=YELLOW_E, shape=Circle))
        
        self.play(Circumscribe(circle6, color=YELLOW_E, shape=Circle),
                  Circumscribe(circle8, color=YELLOW_E, shape=Circle),
                  Circumscribe(circle2, color=YELLOW_E, shape=Circle),
                  Circumscribe(circle4, color=YELLOW_E, shape=Circle),
                  Circumscribe(circle10, color=YELLOW_E, shape=Circle))
        self.wait(2)

        # Distinguer les deux cas: avec et sans la personne 
        
        equation1 = MathTex(r"\binom{n+1}{k+1}").next_to(equipe_k, DOWN, buff=0.5).shift(LEFT * 1).scale(0.6)
        self.play(Write(equation1))
        self.wait(2)

        surround = SurroundingRectangle(circle_red, color=YELLOW_E, buff=0.1)
        self.play(Create(surround))
        self.wait(2)

        equation2 = MathTex(r"= \binom{n}{k}").scale(0.6).next_to(equation1, RIGHT, buff=0.2)
        self.play(Write(equation2))
        self.wait(2)

        self.play(Uncreate(surround))
        cross = Cross(circle_red, color=RED_E).move_to(circle_red.get_center())
        self.play(Create(cross))
        self.wait(2)

        equation3 = MathTex(r"+ \binom{n}{k+1}").scale(0.6).next_to(equation2, RIGHT, buff=0.1)
        self.play(Write(equation3))
        self.wait(3)

        groupe = VGroup(equation1, equation2, equation3, p_bleues, p_rouges,
                        equipe_k, indication, indication_k, circles, circle_red, cross, separatrice)
        self.play(FadeOut(groupe, shift=DOWN), FadeIn(numbers, shift=DOWN))
        self.wait(2)

        plus_sign = MathTex(r"+").move_to((n4.get_center() - n5.get_center()) / 2).shift(DOWN)
        fleche1 = Arrow(start=n4.get_bottom(), end=n8.get_top(),
                        buff=0.5, color=YELLOW_E)
        fleche2 = Arrow(start=n5.get_bottom(), end=n8.get_top(),
                        buff=0.5, color=YELLOW_E)

        self.play(Create(fleche1), Create(fleche2), Write(plus_sign))
        self.wait()

        equation1 = MathTex(r"\binom{n}{k}").scale(0.5).move_to(n4.get_center())
        equation2 = MathTex(r"\binom{n}{k+1}").scale(0.5).move_to(n5.get_center())
        equation3 = MathTex(r"\binom{n+1}{k+1}").scale(0.5).move_to(n8.get_center())

        self.play(Transform(n4, equation1), Transform(n5, equation2))
        self.play(Transform(n8, equation3))
        self.wait(2)

        group = VGroup(numbers, equation1, equation2, equation3, fleche1, fleche2, plus_sign)
        self.play(FadeOut(group, shift=DOWN))
        self.wait(2)

        self.next_section("Exercice suivant", skip_animations=False)

        equation = MathTex(r"\binom{2n}{n} = \sum_{k=0}^{n} \binom{n}{k}^2").scale(1.1)
        self.play(Write(equation))
        self.wait(3)

        self.play(FadeOut(equation, shift=DOWN))
        self.wait()

        square1 = Square(side_length=1, color=BLUE_E, fill_opacity=1).shift(LEFT * 0.75 + UP * 2.5)
        square2 = Square(side_length=1, color=BLUE_E, fill_opacity=1).shift(LEFT * 0.75 + UP * 1.25)
        square3 = Square(side_length=1, color=BLUE_E, fill_opacity=1).shift(LEFT * 0.75)
        square4 = Square(side_length=1, color=BLUE_E, fill_opacity=1).shift(LEFT * 0.75 + DOWN * 1.25)
        square5 = Square(side_length=1, color=BLUE_E, fill_opacity=1).shift(LEFT * 0.75 + DOWN * 2.5)

        carre1 = Square(side_length=1, color=RED_E, fill_opacity=1).shift(RIGHT * 0.75 + UP * 2.5)
        carre2 = Square(side_length=1, color=RED_E, fill_opacity=1).shift(RIGHT * 0.75 + UP * 1.25)
        carre3 = Square(side_length=1, color=RED_E, fill_opacity=1).shift(RIGHT * 0.75)
        carre4 = Square(side_length=1, color=RED_E, fill_opacity=1).shift(RIGHT * 0.75 + DOWN * 1.25)
        carre5 = Square(side_length=1, color=RED_E, fill_opacity=1).shift(RIGHT * 0.75 + DOWN * 2.5)


        self.play(GrowFromCenter(square1), GrowFromCenter(square2), GrowFromCenter(square3),
                  GrowFromCenter(square4), GrowFromCenter(square5),
                  GrowFromCenter(carre1), GrowFromCenter(carre2), GrowFromCenter(carre3),
                    GrowFromCenter(carre4), GrowFromCenter(carre5))
        self.wait(2)

        equation1 = MathTex(r"\binom{2n}{n}").shift(UP * 2).to_edge(LEFT, buff=2)

        indication = Tex("On pose n = 5 pour cet exemple").scale(0.5).to_edge(DOWN, buff=1).shift(RIGHT * 4)
        self.play(Write(indication))
        self.wait(2)

        circle1 = Circle(radius=0.2, color=GOLD, fill_opacity=1).move_to(square1.get_center())
        circle2 = Circle(radius=0.2, color=GOLD, fill_opacity=1).move_to(carre2.get_center())
        circle3 = Circle(radius=0.2, color=GOLD, fill_opacity=1).move_to(carre3.get_center())
        circle4 = Circle(radius=0.2, color=GOLD, fill_opacity=1).move_to(square4.get_center())
        circle5 = Circle(radius=0.2, color=GOLD, fill_opacity=1).move_to(carre5.get_center())  

        self.play(GrowFromCenter(circle1), GrowFromCenter(circle2), GrowFromCenter(circle3),
                  GrowFromCenter(circle4), GrowFromCenter(circle5))
        self.wait(2)
        self.play(circle1.animate.move_to(square2.get_center()),
                    circle2.animate.move_to(carre4.get_center()),
                    circle3.animate.move_to(square3.get_center()),
                    circle4.animate.move_to(square5.get_center()),
                    circle5.animate.move_to(carre1.get_center()),)
        self.wait(2)
        self.play(circle1.animate.move_to(square1.get_center()),
                    circle2.animate.move_to(square2.get_center()),
                    circle3.animate.move_to(square3.get_center()),
                    circle4.animate.move_to(square4.get_center()),
                    circle5.animate.move_to(square5.get_center()),)
        self.wait(2)
        self.play(circle1.animate.move_to(carre1.get_center()),
                    circle2.animate.move_to(carre2.get_center()),
                    circle3.animate.move_to(carre3.get_center()),
                    circle4.animate.move_to(carre4.get_center()),
                    circle5.animate.move_to(carre5.get_center()),)
        self.wait(2)
        self.play(circle1.animate.move_to(square2.get_center()),
                    circle2.animate.move_to(carre4.get_center()),
                    circle3.animate.move_to(square3.get_center()),
                    circle4.animate.move_to(square5.get_center()),
                    circle5.animate.move_to(carre1.get_center()),
                    Write(equation1))
        self.wait(2)

        self.play(Create(separatrice),
                  circle1.animate.move_to(carre1.get_center()),
                    circle2.animate.move_to(carre2.get_center()),
                    circle3.animate.move_to(carre3.get_center()),
                    circle4.animate.move_to(carre4.get_center()),
                    circle5.animate.move_to(carre5.get_center()),
                  )
        self.wait(2)

        indicateur1 = Tex("0").set_color(BLUE_E)
        indicateur2 = Tex("5").set_color(RED_E)
        rectangle = Rectangle(width=2, height=1, color=GOLD)

        indicateur1.next_to(rectangle.get_edge_center(LEFT), RIGHT, buff=0.4)
        indicateur2.next_to(rectangle.get_edge_center(RIGHT), LEFT, buff=0.4)
        indicateurs = VGroup(indicateur1, indicateur2, rectangle)

        indicateurs.to_edge(RIGHT, buff=2).shift(UP * 3)
        self.play(Create(indicateurs), FadeOut(indication, shift=DOWN))
        self.wait(2)

        self.play(ScaleInPlace(square1, 1.2),
                  ScaleInPlace(square2, 1.2),
                  ScaleInPlace(square3, 1.2),
                  ScaleInPlace(square4, 1.2),
                  ScaleInPlace(square5, 1.2),
                  ScaleInPlace(indicateur1, 1.2),
                  rate_func=there_and_back)
        self.wait()
        self.play(ScaleInPlace(carre1, 1.2),
                  ScaleInPlace(carre2, 1.2),
                  ScaleInPlace(carre3, 1.2),
                  ScaleInPlace(carre4, 1.2),
                  ScaleInPlace(carre5, 1.2),
                  ScaleInPlace(indicateur2, 1.2),
                  rate_func=there_and_back)
        self.wait(3)

        eq1 = MathTex(r"\binom{5}{0}").next_to(
            rectangle.get_edge_center(DOWN), DOWN, buff=1).set_color(BLUE_A).scale(0.7)
        self.play(Write(eq1))
        self.wait(2)

        eq2 = MathTex(r"\binom{5}{0}", r"\times").next_to(
            rectangle.get_edge_center(DOWN), DOWN, buff=1).set_color(BLUE_A).scale(0.7)
        self.play(ScaleInPlace(separatrice, 1.2), rate_func=there_and_back)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(2)

        eq3 = MathTex(r"\binom{5}{0}", r"\times", r"\binom{5}{5}").next_to(
            rectangle.get_edge_center(DOWN), DOWN, buff=1).set_color(BLUE_A).scale(0.7)
        self.play(ScaleInPlace(circle1, 1.2),
                  ScaleInPlace(circle2, 1.2),
                  ScaleInPlace(circle3, 1.2),
                  ScaleInPlace(circle4, 1.2),
                  ScaleInPlace(circle5, 1.2),
                  rate_func=there_and_back)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(2)

        equation_indicatrice = MathTex(r"\binom{n}{k} = \binom{n}{n-k}").to_edge(
            LEFT, buff=1).scale(0.8)
        self.play(FadeIn(equation_indicatrice, shift=DOWN))
        self.wait(2)
        self.play(FadeOut(equation_indicatrice, shift=DOWN))
        self.wait(2)

        eq4 = MathTex(r"\binom{5}{0}", r"\times", r"\binom{5}{5-5}").next_to(
            rectangle.get_edge_center(DOWN), DOWN, buff=1).set_color(BLUE_A).scale(0.7)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(2)

        eq5 = MathTex(r"\binom{5}{0}", r"\times", r"\binom{5}{0}").next_to(
            rectangle.get_edge_center(DOWN), DOWN, buff=1).set_color(BLUE_A).scale(0.7)
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait(2) 

        eq6 = MathTex(r"\binom{5}{0}", r"^2").next_to(

            rectangle.get_edge_center(DOWN), DOWN, buff=1).set_color(BLUE_A).scale(0.7)
        self.play(TransformMatchingTex(eq5, eq6))
        self.wait(2)

        indicateur3 = MathTex("1").move_to(indicateur1.get_center()).set_color(BLUE_E)
        indicateur4 = MathTex("4").move_to(indicateur2.get_center()).set_color(RED_E)

        self.play(FadeOut(indicateur1, shift=DOWN), FadeIn(indicateur3, shift=DOWN),
                  FadeOut(indicateur2, shift=UP), FadeIn(indicateur4, shift=UP),
                  circle1.animate.move_to(square1.get_center()))
        self.wait()

        eq7 = MathTex(r"\binom{5}{0}", r"^2", r"+").next_to(
            rectangle.get_edge_center(DOWN), DOWN, buff=1).set_color(BLUE_A).scale(0.7).shift(LEFT * 0.5)
        self.play(TransformMatchingTex(eq6, eq7))
        self.wait(2)

        eq8 = MathTex(r"\binom{5}{1}", r"^2", r"+").next_to(eq7, RIGHT, buff=0.1).set_color(
            BLUE_B).scale(0.7)
        self.play(circle1.animate.move_to(square4.get_center()),
                  circle2.animate.move_to(carre1.get_center()))
        
        self.play(circle1.animate.move_to(square5.get_center()),
                  circle2.animate.move_to(carre2.get_center()),
                  circle3.animate.move_to(carre1.get_center()))
        
        self.play(circle1.animate.move_to(square1.get_center()),
                  circle4.animate.move_to(carre5.get_center()),
                  circle5.animate.move_to(carre4.get_center()))
        self.play(Write(eq8))
        self.wait(2)

        indicateur1 = MathTex("2").move_to(indicateur3.get_center()).set_color(BLUE_E)
        indicateur2 = MathTex("3").move_to(indicateur4.get_center()).set_color(RED_E)

        eq9 = MathTex(r"\binom{5}{2}", r"^2", r"+").next_to(eq7, DOWN, buff=0.3).set_color(
            BLUE_C).scale(0.7)
        
        self.play(circle2.animate.move_to(square2.get_center()),
                  FadeOut(indicateur3, shift=DOWN), FadeOut(indicateur4, shift=UP),
                  FadeIn(indicateur1, shift=DOWN), FadeIn(indicateur2, shift=UP))
        
        self.play(Write(eq9))
        self.wait(2)

        indicateur3 = MathTex("3").move_to(indicateur1.get_center()).set_color(BLUE_E)
        indicateur4 = MathTex("2").move_to(indicateur2.get_center()).set_color(RED_E)

        eq10 = MathTex(r"\binom{5}{3}", r"^2", r"+").next_to(eq8, DOWN, buff=0.3).set_color(
            BLUE_D).scale(0.7)
        
        self.play(circle3.animate.move_to(square3.get_center()),
                  FadeOut(indicateur1, shift=DOWN), FadeOut(indicateur2, shift=UP),
                  FadeIn(indicateur3, shift=DOWN), FadeIn(indicateur4, shift=UP))
        
        self.play(Write(eq10))
        self.wait()

        eq11 = MathTex(r"\binom{5}{4}", r"^2", r"+").next_to(eq9, DOWN, buff=0.3).set_color(
            BLUE_E).scale(0.7)
        
        indicateur1 = MathTex("4").move_to(indicateur3.get_center()).set_color(BLUE_E)
        indicateur2 = MathTex("1").move_to(indicateur4.get_center()).set_color(RED_E)
        
        self.play(circle4.animate.move_to(square4.get_center()),
                  FadeOut(indicateur3, shift=DOWN), FadeOut(indicateur4, shift=UP),
                  FadeIn(indicateur1, shift=DOWN), FadeIn(indicateur2, shift=UP))
        
        self.play(Write(eq11))
        self.wait(0.5)

        indicateur3 = MathTex("5").move_to(indicateur1.get_center()).set_color(BLUE_E)
        indicateur4 = MathTex("0").move_to(indicateur2.get_center()).set_color(RED_E)

        eq12 = MathTex(r"\binom{5}{5}", r"^2").next_to(eq10, DOWN, buff=0.3).set_color(
            BLUE_E).scale(0.7)
        
        self.play(circle5.animate.move_to(square5.get_center()),
                  FadeOut(indicateur1, shift=DOWN), FadeOut(indicateur2, shift=UP),
                  FadeIn(indicateur3, shift=DOWN), FadeIn(indicateur4, shift=UP))
        
        self.play(Write(eq12))
        self.wait(2)

        equation_final = MathTex(r"\sum_{k=0}^{n} \binom{n}{k}^2").move_to(eq8.get_center()).shift(LEFT + DOWN)
        groupe = VGroup(eq7, eq8, eq9, eq10, eq11, eq12)

        self.play(Transform(groupe, equation_final))
        self.wait()

        groupe1 = VGroup(indicateurs, separatrice,indicateur3, indicateur4,
                        square1, square2, square3, square4, square5,
                        carre1, carre2, carre3, carre4, carre5,
                        circle1, circle2, circle3, circle4, circle4, circle5)

        equal_sign = MathTex("=")

        self.play(FadeOut(groupe1), FadeOut(groupe, run_time=0.1),
                  equation_final.animate.move_to(ORIGIN).shift(RIGHT * 1.4 + UP * 0.1),
                  equation1.animate.move_to(ORIGIN).shift(LEFT),
                  Write(equal_sign))
        self.wait(2)

        self.play(FadeOut(equation_final, equation1, equal_sign, shift=DOWN))

        self.next_section("Credits")

        credits1 = Tex("Vidéo réalisée grâce à Manim:", color=WHITE).to_edge(UP, buff=1).scale(0.8)

        manimBanner = ManimBanner().scale(0.8).shift(DOWN * 0.5)

        self.play(Write(credits1), Create(manimBanner))
        self.wait(3)
        

        self.play(FadeOut(credits1, manimBanner))
