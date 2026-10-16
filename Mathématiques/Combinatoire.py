# Introduction à la combinatoire,
# Vidéo qui explique les bases de la combinatoire ainsi que le binôme de Newton.

from manim import *

class Introduction(Scene):
    
    def construct(self):
        ### Introduire ce qui va être fait dans les 4 prochaines vidéos:
        self.next_section("Introduction")

        # Qu'est ce que la combinatoire?
        titre = Tex("La combinatoire").scale(1.2)
        sous_ligne = Underline(titre)

        self.play(Write(titre), Create(sous_ligne))
        self.wait(2)

        description = Tex("Étude des configurations de collections finies d'objets.").scale(0.5)
        
        groupe_titre = VGroup(titre, sous_ligne)
        self.play(groupe_titre.animate.to_edge(UP).scale(0.7))

        description.next_to(groupe_titre, DOWN)
        self.play(Write(description))
        self.wait(2)

        # Montrer des carrés qui changent de place:
        liste_carres = []

        # Liste des couleurs:
        colors = [RED_E, GREEN_E, BLUE_E, YELLOW_E]

        # point de réference: 
        ref = Point().shift(LEFT * 3.5)

        for i in range(4):
            carre = Square(1).set_opacity(1)
            carre.set_color(colors[i])

            carre.next_to(ref).shift(RIGHT * i * 2)

            liste_carres.append(carre)

        groupe_carre = VGroup(*liste_carres)
        self.play(DrawBorderThenFill(groupe_carre))
        self.wait(1)

        ## Changer de configurations pour montrer l'exemple:
        self.play(groupe_carre[0].animate.shift(RIGHT * 4),
                  groupe_carre[1].animate.shift(LEFT * 2),
                  groupe_carre[2].animate.shift(LEFT * 2),
                  rate_func=smooth)
        
        self.wait(0.8)
        
        self.play(groupe_carre[3].animate.shift(LEFT * 4),
                  groupe_carre[0].animate.shift(RIGHT * 2),
                  groupe_carre[2].animate.shift(RIGHT * 2),
                  rate_func=smooth)
        
        self.wait(0.8)
        
        self.play(groupe_carre[3].animate.shift(LEFT * 2),
                  groupe_carre[1].animate.shift(RIGHT * 2),
                  groupe_carre[2].animate.shift(RIGHT * 2),
                  groupe_carre[0].animate.shift(LEFT * 2),
                  rate_func=smooth)
        
        self.wait(0.8)

        # Montrer le nombre de combinaison possible:
        brace = Brace(groupe_carre)
        texte_brace = brace.get_tex("4! = 24").scale(0.8)

        self.play(GrowFromCenter(brace), Write(texte_brace))
        self.wait(3)

        # Tout effacer:
        self.play(FadeOut(groupe_titre,
                          description,
                          groupe_carre,
                          brace,
                          texte_brace))
        
        self.wait(2)

        ### Montrer sur quoi va porter ce cours:
        self.next_section("Chapitres")

        # L'idée ici est la suivante:
        # Lister les chapitres à gauche
        # Pour chaque chapitre, montrer une image qui l'illustre à droite.

        # Temps d'attente entre deux chapitres:
        attente = 2

        ## Chapitre 1
        chapitre1 = Tex("· Union et intersection d'ensemble").to_edge(LEFT, buff=0.5)
        chapitre1.shift(UP * 2).scale(0.8)

        # Venn diagram: 
        cercle1 = Circle(radius=1, color=GREEN_E).set_opacity(0.8)
        cercle2 = Circle(radius=1, color=BLUE_E).set_opacity(0.8).shift(RIGHT * 0.8)

        intersection = Intersection(cercle1, cercle2, color=YELLOW_E, fill_opacity=0.8)
        groupe_venn = VGroup(cercle1, cercle2, intersection).to_edge(RIGHT, buff=2)

        difference = Difference(cercle1, cercle2, color=RED_E, fill_opacity=0.8)
        union = Union(cercle1, cercle2, color=ORANGE, fill_opacity=0.8)


        self.play(FadeIn(chapitre1))
        self.wait(3)

        # Montrer les exemples
        self.play(FadeIn(groupe_venn, shift=DOWN))
        self.wait()
        self.play(FadeOut(groupe_venn, shift=DOWN),  FadeIn(union, shift=DOWN))
        self.wait()
        self.play(FadeOut(union, shift=DOWN), FadeIn(difference, shift=DOWN))
        self.wait()
        self.play(FadeOut(difference, shift=DOWN))
        self.wait(attente)

        ## Chapitre 2
        chapitre2 = Tex("· Cardinal d'un ensemble fini").next_to(chapitre1, DOWN, buff=0.5).scale(0.8)

        
        ensemble = Tex("A = (•, •, •)").scale(0.6)
        ensemble.to_edge(RIGHT, buff=2)

        brace = Brace(ensemble)
        texte_brace = brace.get_tex("|A| = 3").scale(0.6)


        self.play(FadeIn(chapitre2),
                  chapitre1.animate.scale(0.6).set_color(GRAY_B))
        self.wait(3)
        self.play(FadeIn(ensemble, shift=DOWN))
        self.play(GrowFromCenter(brace), Write(texte_brace))
        self.wait()
        self.play(FadeOut(brace, texte_brace, ensemble, shift=DOWN))
        self.wait(attente)

        ## Chapitre 3
        chapitre3 = Tex("· Coefficients binomiaux").next_to(chapitre2, DOWN, buff=0.5).scale(0.8)

        # Triangle de pascal:
        ligne1 = Tex("1")
        ligne2 = Tex("1 1").next_to(ligne1, DOWN, buff=0.5)
        ligne3 = Tex("1 2 1").next_to(ligne2, DOWN, buff=0.5)

        triangle_de_pascal = VGroup(ligne1, ligne2, ligne3)
        triangle_de_pascal.to_edge(RIGHT, buff=3).shift(UP)

        # Binome de Newton:
        binome = MathTex(r"(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^kb^{n-k}").scale(0.6)
        binome.to_edge(RIGHT, buff=2)

        # Coefficient binomiaux
        coef = MathTex(r"\binom{n}{k}=\frac{n!}{k!(n-k)!}").scale(0.6)
        coef.to_edge(RIGHT, buff=2)

        self.play(FadeIn(chapitre3),
                  chapitre2.animate.scale(0.6).set_color(GRAY_B))
        self.wait(3)
        self.play(FadeIn(coef, shift=DOWN))
        self.wait()
        self.play(FadeIn(triangle_de_pascal, shift=DOWN),
                  FadeOut(coef, shift=DOWN))
        self.wait()
        self.play(FadeIn(binome, shift=DOWN),
                  FadeOut(triangle_de_pascal, shift=DOWN))
        self.wait()
        self.play(FadeOut(binome, shift=DOWN))
        self.wait(attente)

        ## Chapitre 4
        chapitre4 = Tex("· Applications entre 2 ensembles").next_to(chapitre3, DOWN, buff=0.5).scale(0.8)

        # Application injective

        elipse1 = Ellipse(width=2, height=4, color=RED_E, fill_opacity=0.8)
        
        ## Points à l'interieur des ensembles:
        points = []
        for i in range(-2, 3):
            point = Dot(color=BLACK)
            point.move_to(elipse1.get_center())
            point.shift(UP * i * 0.75)
            points.append(*point)

        points1 = VGroup(*points)
        points1.z_index = 1

        elipse2 = elipse1.copy()
        elipse2.set_color(BLUE_E)

        points2 = points1.copy()
        points2.z_index = 1

        elipse2.shift(RIGHT*4)
        points2.shift(RIGHT*4)

        application_injective = VGroup(points1, points2, elipse1, elipse2)

        # Ajouter des fleches pour representer l'application:
        fleche1 = Arrow(start=points1[4].get_center(),
                        end=points2[4].get_center(),
                        color=WHITE,
                        max_tip_length_to_length_ratio=0.1,
                        stroke_width=2)
        
        fleche2 = Arrow(start=points1[3].get_center(),
                        end=points2[2].get_center(),
                        color=WHITE,
                        max_tip_length_to_length_ratio=0.1,
                        stroke_width=2)
        
        fleche3 = Arrow(start=points1[2].get_center(),
                        end=points2[3].get_center(),
                        color=WHITE,
                        max_tip_length_to_length_ratio=0.1,
                        stroke_width=2)
        
        fleche4 = Arrow(start=points1[1].get_center(),
                        end=points2[1].get_center(),
                        color=WHITE,
                        max_tip_length_to_length_ratio=0.1,
                        stroke_width=2)
        
        fleche5 = Arrow(start=points1[0].get_center(),
                        end=points2[1].get_center(),
                        color=WHITE,
                        max_tip_length_to_length_ratio=0.1,
                        stroke_width=2)
                        
        
        application_injective.add(fleche1,
                                  fleche2,
                                  fleche3,
                                  fleche4,
                                  fleche5)


        application_injective.scale(0.4)
        application_injective.to_edge(RIGHT, buff=2.5)

        # Application surjective

        elipse3 = Ellipse(width=2, height=4, color=GREEN_E, fill_opacity=0.8)
        
        ## Points à l'interieur des ensembles:
        points = []
        for i in range(-2, 3):
            point = Dot(color=BLACK)
            point.move_to(elipse3.get_center())
            point.shift(UP * i * 0.75)
            points.append(*point)

        points3 = VGroup(*points)
        points3.z_index = 1

        elipse4 = elipse3.copy()
        elipse4.set_color(BLUE_E)

        points4 = points3.copy()
        points4.z_index = 1

        elipse4.shift(RIGHT*4)
        points4.shift(RIGHT*4)

        application_surjective = VGroup(points3, points4, elipse3, elipse4)

        # Ajouter des fleches pour representer l'application:
        fleche6 = Arrow(start=points3[4].get_center(),
                        end=points4[4].get_center(),
                        color=WHITE,
                        max_tip_length_to_length_ratio=0.1,
                        stroke_width=2)
        
        fleche7 = Arrow(start=points3[2].get_center(),
                        end=points4[3].get_center(),
                        color=WHITE,
                        max_tip_length_to_length_ratio=0.1,
                        stroke_width=2)
        
        fleche8 = Arrow(start=points3[3].get_center(),
                        end=points4[2].get_center(),
                        color=WHITE,
                        max_tip_length_to_length_ratio=0.1,
                        stroke_width=2)
        
        fleche9 = Arrow(start=points3[0].get_center(),
                        end=points4[1].get_center(),
                        color=WHITE,
                        max_tip_length_to_length_ratio=0.1,
                        stroke_width=2)
        
        fleche10 = Arrow(start=points3[1].get_center(),
                        end=points4[0].get_center(),
                        color=WHITE,
                        max_tip_length_to_length_ratio=0.1,
                        stroke_width=2)
        
        
        application_surjective.add(fleche10,
                                  fleche6,
                                  fleche7,
                                  fleche8,
                                  fleche9)


        application_surjective.scale(0.4)
        application_surjective.to_edge(RIGHT, buff=2.5)

        # Animation:

        self.play(FadeIn(chapitre4),
                  chapitre3.animate.scale(0.6).set_color(GRAY_B))
        self.wait(3)
        self.play(FadeIn(application_injective, shift=DOWN))
        self.wait()
        self.play(FadeOut(application_injective, shift=DOWN),
                  FadeIn(application_surjective, shift=DOWN))
        self.wait()
        self.play(FadeOut(application_surjective, shift=DOWN))
        self.wait(attente)

        self.play(FadeOut(chapitre1,
                          chapitre2,
                          chapitre3,
                          chapitre4))

        # Conclusion
        self.next_section("Outro")

        conclusion2 = Tex("Vidéo réalisée grâce à ").shift(UP * 2).scale(0.7)  

        banner = ManimBanner().scale(0.5)
        banner.next_to(conclusion2, DOWN, buff=0.5)

        label = Tex("Manim*", color=WHITE).scale(0.4).next_to(banner, DOWN, buff=0.3)

        self.play(Write(conclusion2))
        self.play(FadeIn(banner), Write(label))
        self.wait(3)

        self.play(FadeOut(conclusion2,
                          banner, label))  
        self.wait(1)


        

        
