from manim import *

# The introduction scene:
class Introduction(Scene):
    def construct(self):

        def Parthenon():
            parthenon = VGroup()

            base = Rectangle(height=0.2, width=2, color=YELLOW_A)

            # Extend the base: 
            base_line = Line(start=base.get_corner(DL) + LEFT * 0.1,
                             end=base.get_corner(DR) + RIGHT * 0.1,
                             color=YELLOW_A)
            
            parthenon.add(base, base_line)

            lines_num = 5

            # Add vertical lines:
            for i in range(lines_num + 1):
                # Partition width:
                partition = (i / lines_num) * 2

                down_point = base.get_corner(UL) + RIGHT * partition
                
                up_point = down_point + UP 

                parthenon.add(Line(start=down_point, end=up_point, color=YELLOW_A))

            # Add the ceiling:
            ceiling = Rectangle(height=0.2, width=2.1, color=YELLOW_A).shift(UP + UP * 0.2)

            triangle = Triangle(color=YELLOW_A)
            triangle.scale_to_fit_height(0.2)
           
            triangle.next_to(ceiling, UP)

            parthenon.add(ceiling, triangle)
            
            return parthenon

        parthenon = Parthenon()
        self.play(Create(parthenon))

        self.wait(2)

