# Facial Emotion Recognition

Facial emotion recognition was part of my master thesis.

System was developed in Google Colab.


## Installation

Clone the repo onto your local machine

```bash
$ git clone https://github.com/lukamaric996/Facial-Emotion-Recognition.git
```

Access `Facial-Emotion-Recognition` directory

```bash
$ cd Facial-Emotion-Recognition
```

Create new environment named `fer`

```bash
$ conda create -n fer python=3.8
```

```bash
$ pip install -r requirements.txt
```
You might also try ```$ conda install -r requirements.txt``` if pip installation conflicts are giving you trouble.


## Use

Activate the environment

```bash
$ conda activate fer
```

Run the gui python script inside ```openCV_gui directory```

```bash
$ cd openCV_gui
$ python openCVapp.py
```

Deactivate the environment after use 

```bash
$ conda deactivate
```

## Remove from your local machine

Remove the environment and its dependencies

```bash
$ conda remove -n fer --all
```

## Requirements

Library dependencies are listed in [requirements.txt](https://github.com/lukamaric996/Facial-Emotion-Recognition/requirements.txt).

## License

[MIT](https://github.com/lukamaric996/Facial-Emotion-Recognition/LICENSE)
