# shift
Alphanumeric shifting made easy.

## About
**shift** is a cli tool that makes it easier to perform alphanumeric char shifting.

The current version provides a set of functionalities such as:
* letter forward and backward
* number forward and backward
* forward and backward ignoring numbers
* forward and backward ignoring letters
* forward and backward with a range of numbers

## Installation
**shift** requires no third-party lib. You can grab the lastest version by clonning this repository:
```shell
git clone https://github.com/tommelo/shift
```

## Usage
```shell
python shift.py alpha <options>
```
The shift cli takes one positional argument(alpha) that represents an alphanumeric string:
```shell
python shift.py abc -p 2
```

See the options overview:

Short opt | Long opt | Default | Required | Description
--------- | -------- | ------- | -------- | -----------
-p        | --positions      | 1     | No | The number of positions to shift
-r        | --range          | None  | No | A limited range of numbers
N/A       | --backwards      | False | No | Performs a backward shift
N/A       | --ignore-numbers | False | No | Ignores every char that is a digit
N/A       | --ignore-letters | False | No | Ignores every char that is a letter
N/A       | --version        | N/A   | No | Shows the current version

### -p, --positions
The number of positions to be shifted. The default number is 1.
```shell
python shift.py abc123 -p 2

// result: cde345
```

### -r, --range
Performs number shifting in a limited range of numbers. Each number of the range must be specified with a space separator.
```shell
python shift.py abc123 -p 4 -r 1 2 3 4 5

// result: efg512
```

You can combine the shell range functionality to specify the --range argument:
```shell
python shift.py abc123 -p 13 -r {0..9}

// result: nop456
```

### --backwards
Performs a backward shift.
```shell
python shift.py abc -p 2 --backwards

// result: yza
```

### --ignore-numbers
Ignores every char that is a digit.
```shell
python shift.py abc123 --ignore-numbers

// result: bcd123
```

### --ignore-letters
Ignores every char that is a letter.
```shell
python shift.py abc123 --ignore-letters

// result: abc234
```

### --version
Shows the current version.
```shell
python shift.pt --version
```
## Piped Input
```shell
echo abc | python shift.py
```

## Piped Output
```shell
python shift.py abc -p 2 | cat
python shift.py abc -p 2 > shifted.txt
```

## License
This is an open-source software licensed under the [MIT license](https://opensource.org/licenses/MIT).
