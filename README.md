# 5G_game
Conway's game of life for 5G lab

## Setup

**Step 1**: Clone the repository: 
```
git clone https://github.com/AleksandraOD/5G_game
```

**Step 2**: Dependencies to download 
```
pip3 install matplotlib numpy
```
**Step 3**: Run the file
```
python3 life_animation.py
```
To view the created animation, check the project directory for `life.gif` and open the file


## Features

For a list of all possible arguments, check the help docs:


```
python3 life_animation.py --help
```

## Examples
![Infinite]()
```
python3 life_animation.py --field-size "50,10" --n-generations 150 --cmap "Greens"
```

By default, animations save automatically once generated (with filename: `life.gif`) .

### MovieWriter Errors
Different versions of `matplotlib` handle animation creation differently. If you're getting an *MovieWriter imagemagick unavailable* error, try:
```
pip3 install --upgrade matplotlib
```
