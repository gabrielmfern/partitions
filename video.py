from extension import *

BACKGROUD_COLOR = '#0f1517'
ACCENT_COLOR = '#96d0e5'
SECONDARY_COLOR = '#e5ab96'
TERTIARY_COLOR = '#ffffff'

class Thumbnail(Scene):
    def set_background(self):
        self.background = FullScreenRectangle()
        self.background.set_fill(BACKGROUD_COLOR, 1)

    def construct(self):
        self.set_background()

        self.partitions_2_10 = VGroup(
            Tex('9+1'),
            Tex('8+2'),
            Tex('7+3'),
            Tex('6+4'),
            Tex('5+5'),
            Tex('4+6'),
            Tex('3+7'),
            Tex('2+8'),
            Tex('1+9')
        )
        for tex in self.partitions_2_10:
            tex.scale(1.2)
        self.partitions_2_10.set_color(ACCENT_COLOR)
        align(self.partitions_2_10, DOWN + RIGHT)
        self.partitions_2_10.move_to(ORIGIN)
        self.add(self.partitions_2_10)

class Presentation(Scene):
    def set_background(self):
        self.background = FullScreenRectangle()
        self.background.set_fill(BACKGROUD_COLOR, 1)

    def construct(self):
        self.set_background()

        self.partitions_2_10 = VGroup(
            Tex('9+1'),
            Tex('8+2'),
            Tex('7+3'),
            Tex('6+4'),
            Tex('5+5'),
            Tex('4+6'),
            Tex('3+7'),
            Tex('2+8'),
            Tex('1+9')
        )
        self.partitions_2_10.set_color(ACCENT_COLOR)
        align(self.partitions_2_10, DOWN)
        self.partitions_2_10.move_to(ORIGIN)
        self.play(Write(self.partitions_2_10), run_time=2.5)

        self.wait(3)

        self.in_common_brace = always_redraw(Brace, self.partitions_2_10, RIGHT)
        always(self.in_common_brace.set_color, TERTIARY_COLOR)
        self.sum_results = Tex('10').set_color(ACCENT_COLOR).scale(3)
        always(self.sum_results.next_to, self.in_common_brace, RIGHT)

        self.play(GrowFromCenter(self.in_common_brace), FadeIn(self.sum_results), run_time=2)

        self.wait(3)

        self.play(
            Indicate(self.partitions_2_10.submobjects[0]),
            Indicate(self.partitions_2_10.submobjects[8])
        )
        
        self.wait()

        self.play(
            Indicate(self.partitions_2_10.submobjects[1]),
            Indicate(self.partitions_2_10.submobjects[7])
        )

        self.play(
            Indicate(self.partitions_2_10.submobjects[2]),
            Indicate(self.partitions_2_10.submobjects[6])
        )

        self.play(
            Indicate(self.partitions_2_10.submobjects[3]),
            Indicate(self.partitions_2_10.submobjects[5])
        )

        self.wait(1.5)

        self.partitions_2_10_no_redundancy = VGroup(
            Tex('9+1'),
            Tex('8+2'),
            Tex('7+3'),
            Tex('6+4'),
            Tex('5+5'),
        )
        self.partitions_2_10_no_redundancy.set_color(ACCENT_COLOR)
        align(self.partitions_2_10_no_redundancy, DOWN)
        self.partitions_2_10_no_redundancy.move_to(ORIGIN)
        self.play(Transform(self.partitions_2_10, self.partitions_2_10_no_redundancy), run_time=1.5)

        self.wait(2)
        
        self.play(self.partitions_2_10.animate.to_edge(DOWN))

        self.wait()

        self.title = Text('Particões de 10 em 2 números').scale(2).set_color(TERTIARY_COLOR)
        self.title.to_edge(UP)
        self.play(Write(self.title))

        self.wait()

        self.title_2 = Text('Formas de escrever 10 com 2 números').set_color(TERTIARY_COLOR).scale(1.5)
        self.title_2.to_edge(UP)
        self.play(Transform(self.title, self.title_2))

        self.wait()

        self.title_3 = Text('Formas de juntar 2 números para formar 10').set_color(TERTIARY_COLOR).scale(1.4)
        self.title_3.to_edge(UP)
        self.play(Transform(self.title, self.title_3))

        self.wait(4)

        self.title_4 = Tex('p').set_color(ACCENT_COLOR).scale(3)
        self.title_4.to_edge(UP)
        self.play(Transform(self.title, self.title_4))

        self.wait(2)

        self.title_5 = Tex('p_2').set_color(ACCENT_COLOR).scale(3)
        self.title_5.to_edge(UP)

        self.play(Transform(self.title, self.title_5))

        self.wait(2)

        self.title_6 = Tex('p_2(10)').set_color(ACCENT_COLOR).scale(3)
        self.title_6.to_edge(UP)

        self.play(Transform(self.title, self.title_6))

        self.wait(2)

        self.title_7 = Tex('p_2(10)', '=5').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
            '=5': TERTIARY_COLOR
        })
        self.title_7.scale(3).to_edge(UP)

        self.play(Transform(self.title, self.title_7))

        self.wait()

class Partition2DivisionComparison(Scene):
    def set_background(self):
        self.background = FullScreenRectangle()
        self.background.set_fill(BACKGROUD_COLOR, 1)

    def construct(self):
        self.set_background()

        self.partitions_2_10 = VGroup(
            Tex('9+1'),
            Tex('8+2'),
            Tex('7+3'),
            Tex('6+4'),
            Tex('5+5')
        )
        self.partitions_2_10.set_color(ACCENT_COLOR)
        align(self.partitions_2_10, DOWN)
        self.partitions_2_10.to_edge(DOWN)

        self.in_common_brace = always_redraw(Brace, self.partitions_2_10, RIGHT)
        always(self.in_common_brace.set_color, TERTIARY_COLOR)
        self.sum_results = Tex('10').set_color(ACCENT_COLOR).scale(3)
        always(self.sum_results.next_to, self.in_common_brace, RIGHT)

        self.title = Tex('p_2(10)', '=5').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
            '=5': TERTIARY_COLOR
        })
        self.title.scale(3).to_edge(UP)

        self.add(self.partitions_2_10, self.title, self.in_common_brace, self.sum_results)

        self.wait(2)

        self.play(FadeOut(self.title), FadeOut(self.partitions_2_10), FadeOut(self.in_common_brace), FadeOut(self.sum_results))

        self.wait(2)

        self.partitions_2 = VGroup(
                VGroup(
                    Tex('p_2(1)', '=0').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=0': TERTIARY_COLOR
                    }),
                    Tex('p_2(2)', '=1').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=1': TERTIARY_COLOR
                    }),
                    Tex('p_2(3)', '=1').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=1': TERTIARY_COLOR
                    }),
                    Tex('p_2(4)', '=2').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=2': TERTIARY_COLOR
                    }),
                    Tex('p_2(5)', '=2').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=2': TERTIARY_COLOR
                    }),
                    Tex('p_2(6)', '=3').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=3': TERTIARY_COLOR
                    }),
                    Tex('p_2(7)', '=3').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=3': TERTIARY_COLOR
                    }),
                    Tex('p_2(8)', '=4').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=4': TERTIARY_COLOR
                    }),
                    Tex('p_2(9)', '=4').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=4': TERTIARY_COLOR
                    }),
                    Tex('p_2(10)', '=5').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=5': TERTIARY_COLOR
                    }),
                ),
                VGroup(
                    Tex('p_2(11)', '=5').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=5': TERTIARY_COLOR
                    }),
                    Tex('p_2(12)', '=6').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=6': TERTIARY_COLOR
                    }),
                    Tex('p_2(13)', '=6').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=6': TERTIARY_COLOR
                    }),
                    Tex('p_2(14)', '=7').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=7': TERTIARY_COLOR
                    }),
                    Tex('p_2(15)', '=7').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=7': TERTIARY_COLOR
                    }),
                    Tex('p_2(16)', '=8').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=8': TERTIARY_COLOR
                    }),
                    Tex('p_2(17)', '=8').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=8': TERTIARY_COLOR
                    }),
                    Tex('p_2(18)', '=9').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=9': TERTIARY_COLOR
                    }),
                    Tex('p_2(19)', '=9').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=9': TERTIARY_COLOR
                    }),
                    Tex('p_2(20)', '=10').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=10': TERTIARY_COLOR
                    }),
                ),
                VGroup(
                    Tex('p_2(21)', '=10').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=10': TERTIARY_COLOR
                    }),
                    Tex('p_2(22)', '=11').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=11': TERTIARY_COLOR
                    }),
                    Tex('p_2(23)', '=11').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=11': TERTIARY_COLOR
                    }),
                    Tex('p_2(24)', '=12').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=12': TERTIARY_COLOR
                    }),
                    Tex('p_2(25)', '=12').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=12': TERTIARY_COLOR
                    }),
                    Tex('p_2(26)', '=13').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=13': TERTIARY_COLOR
                    }),
                    Tex('p_2(27)', '=13').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=13': TERTIARY_COLOR
                    }),
                    Tex('p_2(28)', '=14').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=14': TERTIARY_COLOR
                    }),
                    Tex('p_2(29)', '=14').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=14': TERTIARY_COLOR
                    }),
                    Tex('p_2(30)', '=15').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=15': TERTIARY_COLOR
                    }),
                ),
                VGroup(
                    Tex('p_2(31)', '=15').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=15': TERTIARY_COLOR
                    }),
                    Tex('p_2(32)', '=16').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=16': TERTIARY_COLOR
                    }),
                    Tex('p_2(33)', '=16').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=16': TERTIARY_COLOR
                    }),
                    Tex('p_2(34)', '=17').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=17': TERTIARY_COLOR
                    }),
                    Tex('p_2(35)', '=17').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=17': TERTIARY_COLOR
                    }),
                    Tex('p_2(36)', '=18').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=18': TERTIARY_COLOR
                    }),
                    Tex('p_2(37)', '=18').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=18': TERTIARY_COLOR
                    }),
                    Tex('p_2(38)', '=19').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=19': TERTIARY_COLOR
                    }),
                    Tex('p_2(39)', '=19').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=19': TERTIARY_COLOR
                    }),
                    Tex('p_2(40)', '=20').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=20': TERTIARY_COLOR
                    }),
                ),
                VGroup(
                    Tex('p_2(41)', '=20').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=20': TERTIARY_COLOR
                    }),
                    Tex('p_2(42)', '=21').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=21': TERTIARY_COLOR
                    }),
                    Tex('p_2(43)', '=21').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=21': TERTIARY_COLOR
                    }),
                    Tex('p_2(44)', '=22').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=22': TERTIARY_COLOR
                    }),
                    Tex('p_2(45)', '=22').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=22': TERTIARY_COLOR
                    }),
                    Tex('p_2(46)', '=23').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=23': TERTIARY_COLOR
                    }),
                    Tex('p_2(47)', '=23').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=23': TERTIARY_COLOR
                    }),
                    Tex('p_2(48)', '=24').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=24': TERTIARY_COLOR
                    }),
                    Tex('p_2(49)', '=24').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=24': TERTIARY_COLOR
                    }),
                    Tex('p_2(50)', '=25').set_color(ACCENT_COLOR).set_color_by_tex_to_color_map({
                        '=25': TERTIARY_COLOR
                    }),
                )
        )
        
        for col in self.partitions_2:
            align(col, DOWN)
        align(self.partitions_2)
        self.partitions_2.move_to(ORIGIN)

        self.play(FadeIn(self.partitions_2), run_time=2)

        self.wait(3)

        self.play(
            Indicate(
                last(
                    last(self.partitions_2.submobjects).submobjects
                )
            ),
        )

        self.play(
            Indicate(
                last(
                    self.partitions_2.submobjects[
                        len(self.partitions_2.submobjects) - 2
                    ].submobjects
                )
            ),
        )

        self.play(
            Indicate(
                last(
                    self.partitions_2.submobjects[
                        len(self.partitions_2.submobjects) - 3
                    ].submobjects
                )
            ),
        )

        self.play(
            Indicate(
                last(
                    self.partitions_2.submobjects[
                        len(self.partitions_2.submobjects) - 4
                    ].submobjects
                )
            ),
        )

        self.play(
            Indicate(
                last(
                    self.partitions_2.submobjects[
                        len(self.partitions_2.submobjects) - 5
                    ].submobjects
                )
            ),
        )

        self.wait()

        partition_2_11 = self.partitions_2.submobjects[1].submobjects[0]
        self.play(*(FadeOut(partition) for partition in all_except(self.partitions_2.submobjects[1].submobjects, 0)), *(FadeOut(group) for group in all_except(self.partitions_2.submobjects, 1)))

        temp_partition_2_11 = partition_2_11.copy()
        temp_partition_2_11.scale(2).move_to(ORIGIN)
        self.play(Transform(partition_2_11, temp_partition_2_11))

        self.wait(2)

        self.frac = Tex(r'\frac{11}{2}', '=5', '.5').set_color(TERTIARY_COLOR).scale(2)

        self.play(partition_2_11.animate.shift(UP * 3), Write(self.frac))

        self.wait()

        self.play(Indicate(VGroup(self.frac.get_part_by_tex('=5'), self.frac.get_part_by_tex('.5'))), Indicate(partition_2_11.get_part_by_tex('=5')))

        self.wait(2)

        self.play(Indicate(self.frac.get_part_by_tex('.5')))

        floor_frac = Tex(r'\left\lfloor\frac{11}{2}\right\rfloor', '=5').set_color(TERTIARY_COLOR).scale(2)

        self.play(Transform(self.frac, floor_frac), run_time=2)

        self.wait(2)

        temp_floor_frac = Tex(r'\left\lfloor5.5\right\rfloor=5').set_color(TERTIARY_COLOR).scale(2)

        self.play(Transform(self.frac, floor_frac), run_time=2)

        self.wait(2)

        temp_floor_frac = Tex(r'\left\lfloor6.23091\right\rfloor=6').set_color(TERTIARY_COLOR).scale(2)
        
        self.play(Transform(self.frac, temp_floor_frac), run_time=2)

        self.wait(2)

        temp_floor_frac = Tex(r'\left\lfloor3.1415926\right\rfloor=3').set_color(TERTIARY_COLOR).scale(2)
        
        self.play(Transform(self.frac, temp_floor_frac), run_time=2)

        self.wait(2)

        temp_partition_2_11 = Tex('p_2(11)', r'=\left\lfloor\frac{11}{2}\right\rfloor', '=5').set_color(TERTIARY_COLOR).set_color_by_tex_to_color_map({
            'p_2(11)': ACCENT_COLOR
        })
        temp_partition_2_11.scale(2)

        self.wait(2)
        
        partition_2_11 = VGroup(partition_2_11, self.frac)
        self.play(Transform(partition_2_11, temp_partition_2_11), run_time=2)

        self.wait(3)

        temp_partition_2_11 = Tex(r'p_2(\text{número})', r'=\left\lfloor\frac{\text{número}}{2}\right\rfloor').set_color(TERTIARY_COLOR).set_color_by_tex_to_color_map({
            r'p_2(\text{número})': ACCENT_COLOR
        })
        temp_partition_2_11.scale(2)

        self.play(Transform(partition_2_11, temp_partition_2_11), run_time=2)

        self.wait(2)

        self.partition_example = Tex('p_2(31)'  , r'=\left\lfloor\frac{31}{2}\right\rfloor', '=15').set_color(TERTIARY_COLOR).set_color_by_tex_to_color_map({
            'p_2(31)': ACCENT_COLOR
        })
        self.partition_example.scale(2)
        self.partition_example.shift(DOWN * 3)

        temp_group = VGroup(self.partition_example, partition_2_11.copy())
        temp_group.move_to(ORIGIN)
        self.play(Transform(partition_2_11, temp_group), run_time=3)

        self.wait(4)

        self.partition_problem = Tex(r'p_3(\text{número})'  , r'=', r'\text{???}').set_color(TERTIARY_COLOR).set_color_by_tex_to_color_map({
            r'p_3(\text{número})': ACCENT_COLOR,
            r'\text{???}': SECONDARY_COLOR
        })
        self.partition_problem.scale(2)

        self.play(Transform(partition_2_11, self.partition_problem), run_time=2)

        self.wait()
