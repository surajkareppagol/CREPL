# CREPL

`CREPL` is REPL (read–eval–print loop) program written in Python for C.

![CREPL](https://raw.githubusercontent.com/surajkareppagol/Project-Assets/main/CREPL/CREPL.png)

## How It Works ?

There is a pre-written C template, and new lines of code from the terminal gets injected into this template, and it is immediately executed, the output or errors are passed to display.

## C Template

```c
#include <stdio.h>

int main(){

  return 0;
}
```

## Usage

```bash
git clone https://github.com/surajkareppagol/CREPL
cd CREPL
```

Activate virtual environment,

```bash
python3 -m venv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
python3 src/main.py
```

To deactivate virtual environment,

```bash
deactivate
```

## Keywords

- `exit` or `exit()`
  Exit the CREPL by resetting the template.

- `clear` or `clear()`
  Clear the screen.

- `reset` or `reset()`
  Reset the template.

## Demo

![CREPL](https://raw.githubusercontent.com/surajkareppagol/Project-Assets/main/CREPL/CREPL.gif)

## What Next ?

- Use C like `getch()` to get multi-line inputs
- Correctly handle all errors
