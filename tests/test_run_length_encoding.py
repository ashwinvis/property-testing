from proptests.run_length_encoding import encode, decode


def test_with_example():
    sample = "aksjdnkansdan"
    output = decode(encode(sample))

    assert sample == output
