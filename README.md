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