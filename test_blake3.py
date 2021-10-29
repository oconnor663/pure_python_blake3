import json
from os import path

from blake3 import Hasher


def test_vectors() -> None:

    with open(path.join(path.dirname(__file__), "test_vectors.json")) as f:
        vectors = json.load(f)

    key = vectors["key"].encode("ascii")
    context_string = vectors["context_string"]

    for case in vectors["cases"]:
        input_len = case["input_len"]
        print(f"input_len: {input_len}")
        input_bytes = bytes(i % 251 for i in range(input_len))

        # regular hash
        expected = bytes.fromhex(case["hash"])
        hasher = Hasher()
        hasher.update(input_bytes)
        assert expected == hasher.finalize(len(expected))

        # keyed hash
        expected = bytes.fromhex(case["keyed_hash"])
        hasher = Hasher.new_keyed(key)
        hasher.update(input_bytes)
        assert expected == hasher.finalize(len(expected))

        # key derivation
        expected = bytes.fromhex(case["derive_key"])
        hasher = Hasher.new_derive_key(context_string)
        hasher.update(input_bytes)
        assert expected == hasher.finalize(len(expected))
