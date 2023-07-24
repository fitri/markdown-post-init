## Installation
1. Clone the repository to local working dir.
```
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
