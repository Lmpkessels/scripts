# scripts

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![Issues](https://img.shields.io/github/issues/Lmpkessels/scripts)

Contains scripts for the linux OS for automation and a greater workflow.

## Installation

```bash
# Make sure python3 is installed
$ sudo apt-get update
$ sudo apt-get install python3.6
```

```bash
# Clone https using HTTPS
git clone https://github.com/Lmpkessels/scripts.git
```

```bash
# Clone scripts using SSH
git clone git@github.com:Lmpkessels/scripts.git
```

## Execution

- For local execution from /home/user-name/scripts

```bash
# Move into directory
cd scripts.py
```

```bash
# Execute script
python3 script_name.py
```

- For global execution

```bash
# Create directory for executables
mkdir ~/bin/
```

```bash
# Move in to directory
cd ~/bin/
```

```bash
# Copy scripts into directory
cp script.py .
```

```bash
# Make script executable
chmod +x script.py
```

```bash
# Edit ~/.bash_profile
nano ~/.bash_profile
```

```bash
# Add the following line to ~/.bash_profile
export PATH="$PATH:$HOME/bin"
```

```bash
# Refresh ~/bash_profile
source ~/.bash_profile
```

```bash
# Run the script globally
script.py
```
