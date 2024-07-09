import pytest
import pytest_dev.source.shapes as shapes


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def other_rectangle():
    return shapes.Rectangle(5, 6)
