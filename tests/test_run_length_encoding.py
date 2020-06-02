from hypothesis import given
import hypothesis.strategies as st

from proptests.run_length_encoding import encode, decode


def test_with_example():
    sample = "aksjdnkansdan"
    output = decode(encode(sample))

    assert sample == output


@given(st.text())
def test_with_property(sample):
    output = decode(encode(sample))

    assert sample == output
