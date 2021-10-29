import json
from os import path
import secrets
import subprocess
import sys

from blake3 import Hasher

HERE = path.dirname(__file__)


def test_vectors() -> None:

    with open(path.join(HERE, "test_vectors.json")) as f:
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


def test_execute() -> None:
    input_bytes = secrets.token_bytes(100_000)

    hasher = Hasher()
    hasher.update(input_bytes)
    expected = hasher.finalize(32).hex().encode("ascii")

    blake3_py = path.join(HERE, "blake3.py")
    result = subprocess.run(
        [sys.executable, blake3_py],
        capture_output=True,
        check=True,
        input=input_bytes,
    )
    assert result.stdout.strip() == expected
    assert result.stderr == b""
