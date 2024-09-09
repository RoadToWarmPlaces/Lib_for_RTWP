# Created by nikoro256 on 2024-09-09
# Copyright (c) 2024 RTWP

from functools import cmp_to_key


class AngleSort:
    def __init__(self, xs: list[int], ys: list[int], mid_x: int, mid_y: int):
        self.xs = xs
        self.ys = ys
        self.mid_x = mid_x
        self.mid_y = mid_y
        self.angle_sort()

    def get(self, i):
        """
        i番目のx座標、y座標を求める。
        """
        return self.xs[self.order[i]], self.ys[self.order[i]]

    def comp_angle(self, a: tuple[int, int], b: tuple[int, int]):
        # aとbを比較する関数
        if a[1] * b[1] < 0:
            if a[1] > 0:
                return -1
            else:
                return 1
        elif a[1] == 0:
            if a[0] >= 0:
                return -1
            else:
                if b[1] < 0:
                    return -1
                else:
                    return 1
        elif b[1] == 0:
            if b[0] >= 0:
                return 1
            else:
                if a[1] < 0:
                    return 1
                else:
                    return -1
        comp = a[0] * b[1] - a[1] * b[0]
        if comp < 0:
            return 1
        elif comp == 0:
            return 0
        else:
            return -1

    def solve_triangle_area(self, x1, y1, x2, y2, x3, y3):
        """
        3角形の面積を求める。
        整数値
        """
        return abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) // 2

    def solve_all_triangle_areas(self):
        """
        i,i+1,中心を結んだ三角形をそれぞれのiについて調べる。

        order : angle_sortの結果
        xs : xのlist
        ys : yのlist
        mid_x : 中心のx座標
        mid_y : 中心のy座標
        """
        areas = []
        for i in range(len(self.order)):
            areas.append(
                self.solve_triangle_area(
                    self.mid_x,
                    self.mid_y,
                    self.xs[self.order[i]],
                    self.ys[self.order[i]],
                    self.xs[self.order[(i + 1) % len(self.order)]],
                    self.ys[self.order[(i + 1) % len(self.order)]],
                )
            )
        return areas

    def solve_mid_triangle_area(self, i, j):
        """
        中心点と他の２点から面積を求める。
        """
        area = 0
        area += self.solve_triangle_area(
            self.mid_x,
            self.mid_y,
            self.xs[self.order[i]],
            self.ys[self.order[i]],
            self.xs[self.order[j]],
            self.ys[self.order[j]],
        )
        return area

    def angle_sort(self):
        """
        偏角ソートをする。

        xs : xのlist
        ys : yのlist
        mid_x : 中心のx座標
        mid_y : 中心のy座標
        """
        assert len(self.xs) == len(self.ys)
        angles = [i for i in range(len(self.xs))]
        self.order = sorted(
            angles,
            key=cmp_to_key(
                lambda a, b: self.comp_angle(
                    (self.xs[a] - self.mid_x, self.ys[a] - self.mid_y),
                    (self.xs[b] - self.mid_x, self.ys[b] - self.mid_y),
                )
            ),
        )
        return self.order


def solve_rotation(x1, y1, x2, y2, x3, y3):
    ## x1,y1を基軸にしてx2,y2,x3,y3の回転を求める。
    tmp = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    if tmp < 0:
        return False
    else:
        return True
