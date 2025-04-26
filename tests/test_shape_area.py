from shape_area.factory import shape_factory
import pytest
from decimal import Decimal


def test_circle_area():
    c = shape_factory(1)
    assert round(c.area(), 4) == round(Decimal("3.1416"), 4)


def test_invalid_circle():
    with pytest.raises(ValueError):
        shape_factory(-5)


def test_triangle_area():
    t = shape_factory(3, 4, 5)
    assert round(t.area(), 4) == round(Decimal("6.0"), 4)


def test_triangle_is_right_true():
    t = shape_factory(3, 4, 5)
    assert t.is_right() is True


def test_triangle_is_right_false():
    t = shape_factory(3, 4, 6)
    assert t.is_right() is False


def test_invalid_triangle():
    with pytest.raises(ValueError):
        shape_factory(1, 2, 10)


def test_triangle_different_types():
    t = shape_factory("3", 4, 5.0)
    assert round(t.area(), 4) == round(Decimal("6.0"), 4)


def test_triangle_sequence():
    t = shape_factory(("3", 4, 5.0))
    assert round(t.area(), 4) == round(Decimal("6.0"), 4)
