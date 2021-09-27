import pytest


@pytest.fixture
def some_array():
    return [1]


@pytest.mark.asyncio
async def test_example(some_array):
    assert [2] == some_array


if __name__ == "__main__":
    test_example()
