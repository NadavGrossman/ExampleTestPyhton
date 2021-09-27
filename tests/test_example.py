import pytest
from fixtures.fixture_1 import some_array

@pytest.mark.asyncio
async def test_example(some_array):
    assert [1] == some_array


if __name__ == "__main__":
    test_example()
