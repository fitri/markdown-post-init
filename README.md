This a Python script to generate markdown file with metadata header from configuration file `.ini`.

**Features:**
- Basic metadata title and date
- Auto date setting
- Markdown file name from title
- Flexible custom configuration file
- Overwrite value from commandline

## Installation
1. Clone the repository to local working dir.
```bash
git clone git@github.com:fitri/markdown-post-init.git .
```

2. Copy out the `post-init.py` and also `config.ini` to content dir

## Usage
1. Edit configuration `config.ini` below the header `[metadata]` with custom markdown metadata key. Left empty if no default value to update on each posts.
2. Alias post-init.py as runable script
```bash
alias postinit="python $PWD/post-init.py"
```
3. Run the command `postinit` to create new markdown `.md` file

## Commandline
Printing out help and flags options
```bash
postinit --help
```

Overwrite default
```bash
postinit --date 2023-09-09
```