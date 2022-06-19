# Conjecture

A pythonic assertion library.

## 🛠 Installing

### Poetry

```
poetry add conjecture
```

### pip

```
pip install conjecture
```

## 🎓 Usage


### Basic

A basic assertion.

```pycon
>>> import conjecture
>>> assert 5 == conjecture.has(lambda v: v < 10)
>>> assert 5 == conjecture.has(lambda v: v > 10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

### Built-in conjectures

#### General

Matching none.

```pycon
>>> import conjecture
>>> assert None == conjecture.none()
```

Matching anything.

```pycon
>>> import conjecture
>>> assert None == conjecture.anything()
>>> assert 123 == conjecture.anything()
>>> assert "abc" == conjecture.anything()
```

#### Object

Matching instances of a class.

```pycon
>>> import conjecture
>>> assert 123 == conjecture.instance_of(int)
>>> assert "abc" == conjecture.instance_of((str, bytes))
```

Matching values.

```pycon
>>> import conjecture
>>> assert 123 == conjecture.equal_to(123)
>>> assert "abc" == conjecture.equal_to("abc")
```

#### Rich ordering

Matching lesser values.

```pycon
>>> import conjecture
>>> assert 5 == conjecture.greater_than(1)
>>> assert 5 == conjecture.greater_than_or_equal_to(1)
```

Matching greater values.

```pycon
>>> import conjecture
>>> assert 1 == conjecture.less_than(5)
>>> assert 1 == conjecture.less_than_or_equal_to(5)
```

#### Size

Matching empty collections.

```pycon
>>> import conjecture
>>> assert list() == conjecture.empty()
>>> assert set() == conjecture.empty()
>>> assert tuple() == conjecture.empty()
>>> assert dict() == conjecture.empty()
```

Matching length of collections.

```pycon
>>> import conjecture
>>> assert [1, 2, 3, 4, 5] == conjecture.length_of(5)
>>> assert [1, 2, 3] == conjecture.length_of(conjecture.less_than(5))
```

#### String

Matching string prefixes.

```pycon
>>> import conjecture
>>> assert "foo bar baz" == conjecture.prefixed_with("foo")
>>> assert b"foo bar baz" == conjecture.prefixed_with(b"foo")
```

Matching string suffixes.

```pycon
>>> import conjecture
>>> assert "foo bar baz" == conjecture.suffixed_with("baz")
>>> assert b"foo bar baz" == conjecture.suffixed_with(b"baz")
```

### Combined conjectures

Matching all conditions.

```pycon
>>> import conjecture
>>> assert 5 == conjecture.has(lambda v: v <= 5) & conjecture.has(lambda v: v => 5)
>>> assert 6 == conjecture.has(lambda v: v <= 5) & conjecture.has(lambda v: v => 5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>> assert 5 == conjecture.all_of(
...     conjecture.has(lambda v: v <= 5),
...     conjecture.has(lambda v: v => 5)
... )
>>> assert 6 == conjecture.all_of(
...     conjecture.has(lambda v: v <= 5),
...     conjecture.has(lambda v: v => 5)
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

Matching any conditions.

```pycon
>>> import conjecture
>>> assert 0 == conjecture.has(lambda v: v == 5) | conjecture.has(lambda v: v == 0)
>>> assert 5 == conjecture.has(lambda v: v == 5) | conjecture.has(lambda v: v == 0)
>>> assert 6 == conjecture.has(lambda v: v == 5) | conjecture.has(lambda v: v == 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>> assert 5 == conjecture.any_of(
...     conjecture.has(lambda v: v == 5),
...     conjecture.has(lambda v: v == 0)
... )
>>> assert 6 == conjecture.any_of(
...     conjecture.has(lambda v: v == 5),
...     conjecture.has(lambda v: v == 0)
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

### Negation

A negative assertion.

```pycon
>>> import conjecture
>>> assert 5 != conjecture.has(lambda v: v == 10)
>>> assert 5 == ~conjecture.has(lambda v: v == 10)
>>> assert 10 == ~conjecture.has(lambda v: v == 10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

## ⚖️ Licence

This project is licensed under the [MIT licence](http://dan.mit-license.org/).

All documentation and images are licenced under the 
[Creative Commons Attribution-ShareAlike 4.0 International License][cc_by_sa].

[cc_by_sa]: https://creativecommons.org/licenses/by-sa/4.0/

## 📝 Meta

This project uses [Semantic Versioning](http://semver.org/).
