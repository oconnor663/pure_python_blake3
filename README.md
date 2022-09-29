# Pure Python BLAKE3 [![Actions Status](https://github.com/oconnor663/pure_python_blake3/workflows/tests/badge.svg)](https://github.com/oconnor663/pure_python_blake3/actions)

This project is a pure Python implementations of the BLAKE3 cryptographic hash
function. It's intended for educational and testing use only. It's too slow for
production use, and it hasn't been audited. If you're writing production Python
code, see the [`blake3`](https://pypi.org/project/blake3/) module, which
provides bindings for the high-performance Rust implementation.

This a direct port of the [Rust reference
implementation](https://github.com/BLAKE3-team/BLAKE3/blob/master/reference_impl/reference_impl.rs).
It supports all the features of BLAKE3, including keyed hashing, key
derivation, and extendable output. Python 3.8 or later is required.

## Examples

```python
import pure_blake3

# regular hashing
hasher1 = pure_blake3.Hasher()
hasher1.update(b"foobarbaz")
output1 = hasher1.finalize()

# regular hashing in multiple steps
hasher2 = pure_blake3.Hasher()
hasher2.update(b"foo")
hasher2.update(b"bar")
hasher2.update(b"baz")
output2 = hasher2.finalize()
assert output2 == output1

# extendable output
hasher3 = pure_blake3.Hasher()
hasher3.update(b"foobarbaz")
output3 = hasher3.finalize(100)
assert output3[:32] == output2

# keyed hashing
import secrets
random_key = secrets.token_bytes(32)
message = b"a message to authenticate"
keyed_hasher = pure_blake3.Hasher.new_keyed(random_key)
keyed_hasher.update(message)
mac = keyed_hasher.finalize()

# key derivation
context_string = "pure_blake3 2021-10-29 18:37:44 example context"
key_material = b"usually at least 32 random bytes, not a password"
kdf = pure_blake3.Hasher.new_derive_key(context_string)
kdf.update(key_material)
derived_key = kdf.finalize()
```
