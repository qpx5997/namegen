# namegen
This is a Python module that can be used to generate random names. You can import it by using the following code:

```
import namegen
```

## Functions

`namegen` has two basic functions: `randname` and `randname_customizable`.

### `randname()`

To use `randname()`, use the following syntax:

```
namegen.randname(length, capitalize=True)
```
Do note that these arguments are optional. If `length` is left out, `length` will be set to a random number between 3 and 7. The `capitalize` argument capitalizes the first letter if it is `True`.

The `randname()` function generates a completely random name. It returns a randomly generated sequence of consonants and vowels. Do note that the names produced by this function may be unpronounceable.

#### Example usage

```
print(namegen.randname(4, capitalize=True))
```

### `randname_customizable()`

To use `randname_customizable()`, use the following syntax:

```
namegen.randname_customizable(template, capitalize=True)
```

The argument `template` expects a string of letters. The only two letters allowed are `c` and `v`, `c` represents consonants and `v` represents vowels.

`randname_customizable()` is a version of `randname()` with a customizable template. Unlike `randname()` which has a randomly generated template, `randname_customizable()` expects the user to input their own template. This is one example of a template:

```
cvccvc
```

This will make `randname_customizable()` output a word that has a consonant as its first phoneme, a vowel as its second, two consonants as its third and fourth, a vowel as its fifth and a consonant as its sixth.

#### Example usage

```
print(namegen.randname_customizable("vcvccv", capitalize=False))
```

The following are some possible outputs of the code:

```
ashokli
eekosgoo
afamchi
okeesnoo
```

## Phonemes

These are all the possible phonemes that can be outputted. Do note that the `length` argument does not define the length of the word; it defines the number of phonemes in the word.

### Consonants

b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z, sh, ph, ch, th

### Vowels

a, e, ee, i, o, oo, u, y
