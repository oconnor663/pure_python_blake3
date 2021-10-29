# Pure Python BLAKE3 [![Actions Status](https://github.com/oconnor663/pure_python_blake3/workflows/tests/badge.svg)](https://github.com/oconnor663/pure_python_blake3/actions)

This project is a pure Python implementations of the BLAKE3 cryptographic hash
function. It's intended for educational and testing use only. It's too slow for
production use, and it hasn't been audited. If you're writing production Python
code, see the [`blake3`](https://pypi.org/project/blake3/) module, which
provides bindings for the high-performance Rust implementation.

This a direct port of the [Rust reference
implementation](https://github.com/BLAKE3-team/BLAKE3/blob/master/reference_impl/reference_impl.rs).
It supports all the features of BLAKE3, including keyed hashing, key
derivation, and extendable output.

## Examples

```python
import pure_blake3

hasher = pure_blake3.Hasher()
hasher.update(b"foobarbaz")
output1 = hasher.finalize()

hasher = pure_blake3.Hasher()
hasher.update(b"foo")
hasher.update(b"bar")
hasher.update(b"baz")
output2 = hasher.finalize()

assert output1 == output2
```
