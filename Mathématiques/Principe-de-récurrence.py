# Vidéo expliquant le principe de récurrence à destination des étudiants en L1 physique.

from manim import *

class Recurrence(Scene):
    def construct(self):

        self.next_section("Introduction", skip_animations=False)
        titre = Tex("Le Principe de récurrence", color=WHITE).scale(1).to_edge(UP)
        self.play(Write(titre))

        # Le prince de récurrence est une propriété propre aux entiers.
        Entiers = NumberLine(x_range=[0, 10, 1],
                             length=10,
                             color=WHITE,
                             include_numbers=True,
                             include_ticks=True,
                             include_tip=True)
        
        self.play(Create(Entiers), run_time=3)
        self.wait(2)

        # Et donc nous ne pouvons pas l'appliquer aux réels.
        tick1 = Line(UP * 0.1, DOWN * 0.1, color=RED).move_to(Entiers.n2p(3.14))
        label1 = MathTex(r"\pi", color=RED).next_to(tick1, UP).scale(0.8)

        tick2 = Line(UP * 0.1, DOWN * 0.1, color=RED).move_to(Entiers.n2p(0.5))
        label2 = MathTex(r"0.5", color=RED).next_to(tick2, UP).scale(0.8)

        tick3 = Line(UP * 0.1, DOWN * 0.1, color=RED).move_to(Entiers.n2p(6.28))
        label3 = MathTex(r"\tau", color=RED).next_to(tick3, UP).scale(0.8)

        self.play(Create(tick1), Write(label1),
                  Create(tick2), Write(label2),
                  Create(tick3), Write(label3))
        self.wait(2)

        self.play(FadeOut(tick1, label1,
                          tick2, label2,
                          tick3, label3, shift=UP))
        self.wait(1)

        # Le rang initial:
        rang_initial = MathTex(r"n_0", color=YELLOW_E).scale(0.8).to_edge(UP)
        rang_initial.next_to(Entiers.get_tick(0), UP, buff=0.3)

        initialisation = Tex("Initialisation", color=YELLOW_E).scale(0.6)
        initialisation.shift(DOWN * 2 + LEFT * 2)

        self.play(Write(rang_initial), Write(initialisation))
        self.wait(2)

        self.play(rang_initial.animate.next_to(Entiers.get_tick(1), UP, buff=0.3))
        self.wait(2)

        self.play(rang_initial.animate.next_to(Entiers.get_tick(7), UP, buff=0.3))
        self.wait(2)

        self.play(rang_initial.animate.next_to(Entiers.get_tick(1), UP, buff=0.3))
        self.wait(2)

        # Les flèches qui montrent l'hérédité
        fleche = CurvedArrow(Entiers.get_tick(2).get_top() + UP * 0.2,
                            Entiers.get_tick(3).get_top() + UP * 0.2,
                            radius=-1,
                            tip_shape=StealthTip,
                            color=GREEN_E).scale(0.8)
        
        heredite = Tex("Hérédité", color=GREEN_E).scale(0.6)
        heredite.shift(DOWN * 2 + RIGHT * 2)

        self.play(Create(fleche), rang_initial.animate.shift(UP * 0.2), Write(heredite))
        self.wait(2)

        self.play(fleche.animate.shift(RIGHT))
        self.wait(1)

        self.play(fleche.animate.shift(RIGHT * 3))
        self.wait(1)

        self.play(fleche.animate.shift(LEFT * 6))
        self.wait(2)

        self.play(fleche.animate.shift(RIGHT * 1))
        self.wait(2)

        groupeFleches = VGroup(rang_initial, fleche, Entiers)

        for i in range(7):
            fleche_copie = fleche.copy()
            groupeFleches.add(fleche_copie)
            self.play(Create(fleche_copie), run_time=0.05)
            self.play(fleche_copie.animate.shift(RIGHT * (i)), run_time=0.2)

        self.wait(3)

        self.play(FadeOut(groupeFleches, shift=DOWN))
        self.wait(2)

        group = VGroup(warning_sign, exclamation).scale(0.7).to_edge(UP, buff=2)

        self.play(heredite.animate.shift(UP * 4 + RIGHT).scale(1.2),
                  initialisation.animate.shift(UP * 4 + LEFT).scale(1.2),
                  Create(group))
        
        self.wait(2)

        contre_initialisation = MathTex(r"P(n): \text{ } 2^n=n!").next_to(initialisation.get_center(), DOWN, buff=4)
        contre_heredite = MathTex(r"Q(n): \text{ } n = n+1").next_to(heredite.get_center(), DOWN, buff=4)

        self.play(Write(contre_initialisation), Write(contre_heredite))
        self.wait(2)

        self.play(FadeOut(contre_heredite, contre_initialisation, group, 
                          heredite, initialisation, titre,
                          shift=DOWN))
        self.wait(2)

        self.next_section("Suites définies par récurrence")

        titre2 = Tex("Suites définies par récurrence", color=WHITE).scale(1).to_edge(UP)
        self.play(Write(titre2))
        self.wait(2)

        suite = MathTex(r"x")
        self.play(Write(suite))
        self.wait(2)

        suite1 = MathTex(r"\sqrt{", r"x", r"}")
        self.play(TransformMatchingTex(suite, suite1))
        self.wait(2)

        suite2 = MathTex(r"\sqrt{", r"\sqrt{", r"x", r"}", r"}")
        self.play(TransformMatchingTex(suite1, suite2))
        self.wait(2)

        suite3 = MathTex(r"\sqrt{", r"\sqrt{", r"\sqrt{", r"\sqrt{", r"x", r"}", r"}", r"}", r"}")
        self.play(TransformMatchingTex(suite2, suite3))
        self.wait(2)

        self.play(FadeOut(suite3, shift=DOWN))
        self.wait(2)

        # Expliquer sur les séries récurrentes:align_to
        suite = MathTex(r"0.5")
        self.play(Write(suite))
        self.wait()


        suite1 = MathTex(r"(", r"0.5", r")")
        indice1 = MathTex(r"0").scale(0.4).next_to(suite1.get_corner(DR), RIGHT, buff=0.05).set_color(YELLOW)
        self.play(TransformMatchingTex(suite, suite1), Write(indice1))
        self.play(Flash(indice1))
        self.wait(2)

        suite2 = MathTex(r"(", r"0.5", r"^{2}", r")")
        indice2 = MathTex(r"1").scale(0.4).next_to(suite2.get_corner(DR), RIGHT, buff=0.05).set_color(YELLOW)
        self.play(TransformMatchingTex(suite1, suite2), ReplacementTransform(indice1, indice2))
        self.wait(2)

        suite3 = MathTex(r"(", r"0.5", r"^{2^2}", r")")
        indice3 = MathTex(r"2").scale(0.4).next_to(suite3.get_corner(DR), RIGHT, buff=0.05).set_color(YELLOW)
        self.play(TransformMatchingTex(suite2, suite3), ReplacementTransform(indice2, indice3))
        self.wait(2)

        suite4 = MathTex(r"(", r"0.5", r"^{2^{2^{2}}}", r")")
        indice4 = MathTex(r"3").scale(0.4).next_to(suite4.get_corner(DR), RIGHT, buff=0.05).set_color(YELLOW)
        self.play(TransformMatchingTex(suite3, suite4), ReplacementTransform(indice3, indice4))
        self.wait(2)

        suite5 = MathTex(r"(", r"0.5", r"^{2^{2^{2^{...}}}}", r")")
        indice5 = MathTex(r"i").scale(0.4).next_to(suite5.get_corner(DR), RIGHT, buff=0.05).set_color(YELLOW)
        self.play(TransformMatchingTex(suite4, suite5), ReplacementTransform(indice4, indice5))
        self.wait(2)
        
        self.play(FadeOut(suite5, indice5, shift=DOWN))

        intervalle = NumberLine(x_range=[0, 1, 0.1],
                                length=2,
                                color=WHITE,
                                include_numbers=False,
                                include_ticks=False,
                                )
        intervalle.to_edge(LEFT, buff=1).shift(UP * 1)
        
        selector = Triangle(color=YELLOW).scale(0.1).rotate(PI / 3)
        dn = DecimalNumber(0)
        x = MathTex("n_0").scale(0.7)

        suite = MathTex(r"u_n = \begin{cases} u_0 =  \\ u_{n+1} = f(u_n) \end{cases}").to_edge(LEFT, buff=1).shift(DOWN * 1)

        dn = dn.next_to(suite[0][6], RIGHT, buff=0.1)
        update_group = VGroup(selector, dn, x)

        def update_vgrp(vgrp):
            s,d,xv = vgrp
            s.next_to(intervalle.n2p(dn.get_value()),UP,buff=0.1)
            xv.next_to(selector,UP,buff=0.2)
 
        axes = Axes(
            x_range=[0, 1, 0.1],
            y_range=[0, 1, 0.1],
            x_length=4,
            y_length=4,
            tips=False,
            axis_config={"include_numbers": False}
        )

        plot_box = SurroundingRectangle(
            axes,
            buff=0.3,
            color=WHITE,
            stroke_width=2
        )

        plot_group = VGroup(plot_box, axes).to_edge(RIGHT, buff=1)

        def get_graph():
            a = dn.get_value()  # parameter coming from the decimal
            return axes.plot(
                lambda x: a * x * (1 - x),  # example function depending on a
                x_range=[0, 1],
                color=BLUE
            )

        graph = always_redraw(get_graph)

        update_group.add_updater(update_vgrp)
        ChangeDecimalToValue(dn, 0)

        self.play(FadeIn(intervalle,update_group, graph, plot_group), Write(suite))
        self.wait(2)

        self.play(
        ChangeDecimalToValue(dn, 0.76),
        run_time=4)
        self.wait(0.5)

        self.play(
        ChangeDecimalToValue(dn, 0.23),
        run_time=4)
        self.wait(0.5)

        self.play(
        ChangeDecimalToValue(dn, 0.5),
        run_time=4)
        self.wait(0.5)

        self.play(FadeOut(intervalle, selector, suite, update_group, titre2, plot_group, graph))

        self.next_section("Ce qu'on va couvrir")

        titre = Tex("Objectifs").to_edge(UP, buff=1)

        epsilon_delta = MathTex(r"\epsilon, \delta").shift(LEFT * 2)
        question_mark = Tex("?").shift(RIGHT * 2)

        self.play(Write(titre), Write(epsilon_delta), Write(question_mark))
        self.wait()

        croix = Cross(epsilon_delta, stroke_color=RED_E).move_to(epsilon_delta.get_center())
        self.play(Create(croix))
        self.wait()

        self.play(Flash(question_mark, color=YELLOW_E))
        self.wait()

        groupe = VGroup(epsilon_delta, question_mark, croix, titre)
        self.play(FadeOut(groupe))

        coef_binomiaux = MathTex(r"\binom{n}{k}").scale(1.2).shift(LEFT * 4)
        triangle_pascal = Triangle(color=BLUE_D).scale(1.2)
        formule = MathTex(r"\binom{2n}{n} &= \\ &\sum_{k=0}^{n} \binom{n}{k}^2").scale(0.9).shift(RIGHT * 4)

        self.play(Write(coef_binomiaux))
        self.wait(2)

        self.play(DrawBorderThenFill(triangle_pascal))
        self.wait(2)

        self.play(Write(formule))
        self.wait(2)

        self.play(FadeOut(coef_binomiaux, triangle_pascal, formule))
        self.wait(2)

        formule2 = MathTex(r"\left| \bigcup_{i=1}^k A_i \right|",
                          r"&= \\", r"\sum_{j=1}^k (-1)^{j-1}",
                          r"\sum_{1 \leq i_1 < \dotsb < i_j \leq k} &\left| A_{i_{1}} \cap A_{i_{2}} \cap \dotsb \cap A_{i_{j}} \right|",)
        
        formule2.scale(0.6).shift(RIGHT * 2)

        c1 = Circle(radius=0.8, color=RED_E, fill_color=RED_D, fill_opacity=0.5).shift(LEFT * 0.4 + UP * 0.4)
        c2 = Circle(radius=0.8, color=BLUE_E, fill_color=BLUE_D, fill_opacity=0.5).shift(RIGHT * 0.4 + UP * 0.4)
        c3 = Circle(radius=0.8, color=GREEN_E, fill_color=GREEN_D, fill_opacity=0.5).shift(DOWN * 0.4)

        venn = VGroup(c1, c2, c3).shift(LEFT * 4)

        self.play(DrawBorderThenFill(venn))
        self.wait(2)

        self.play(Write(formule2))
        self.wait(2)

        self.play(FadeOut(venn, formule2))
        self.wait()

        self.next_section("Credits")

        credits1 = Tex("Vidéo réalisée grâce à Manim:", color=WHITE).to_edge(UP, buff=1).scale(0.8)

        manimBanner = ManimBanner().scale(0.8).shift(DOWN * 0.5)

        self.play(Write(credits1), Create(manimBanner))
        self.wait(3)
        

        self.play(FadeOut(credits1, manimBanner))
