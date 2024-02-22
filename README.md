# CREPL

`CREPL` is REPL (read–eval–print loop) program written in Python for C.

![CREPL](https://raw.githubusercontent.com/surajkareppagol/Project-Assets/main/CREPL/CREPL.png)

## How It Works ?

The program has three has three containers for three sections, that is,

- `file_global` for global statements such as `macros`, `global variables` etc.
- `file_functions` for all the function statements
- `file_local` for all local statements

The content from these three lists is written to a temporary `C` file, and it is compiled and executed, the result it displayed, if there are any errors, errors will be displayed.

If there is an error, the lists will revert back to previous code.

## 🌟 What's New ?

- Restructured the program
- Added support for multi-line statements
- Added support for nested statements
- Used Regex to distinguish local and global statements
- Add `show` and `global:` or `g:` keyword

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

- `show` or `show()`
  View current content of template file.

- `g:` or `global:`
  Add global statements, use `g: #include <stdlib.h>` or `global: #define MAX 100`

## Demo

![CREPL](https://raw.githubusercontent.com/surajkareppagol/Project-Assets/main/CREPL/CREPL.gif)

## What Next ?

- Refactor code
- Add support to format code with correct spacing
