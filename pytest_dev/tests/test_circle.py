import math

import pytest
import pytest_dev.source.shapes as shapes


class TestCircle:
    # def test_one(self):
    #     assert True

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius

        assert result == expected

    def test_not_same_area_rect(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()
