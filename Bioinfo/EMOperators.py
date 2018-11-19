#!/usr/bin/env python3


class EMOperators(object):

    @staticmethod
    def overlap(s1, s2):
        """
           x and y are overlapping if they share
           at least one part in common
        """

        overlap = False
        for x_part in x:
            for y_part in y:
                if (x_part.start, x_part.end) == /
                   (y_part.start, y_part.end):
                       overlap = True
                       break
        return overlap

    @staticmethod
    def disjoint(x, y):
        """
           x and y are disjoint if they share
           no parts in common
        """

        return not EM.overlap(x, y)

    @staticmethod
    def binary_product(s1, s2):
        """todo"""

        pass

    @staticmethod
    def difference(s1, s2):
        """todo"""

        pass

    @staticmethod
    def binary_sum(s1, s2):
        """todo"""

        pass

