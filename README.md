# Python script example

Small example on how to use python to replace bash scripts as part of the blog post [Life is too short to learn Bash](https://unicoeding.com/blog/life-is-too-short-to-learn-bash/).

These scripts delete all images that were created (not downloaded) more than 2 weeks ago.
They are functionally similar, except that one was written in bash, and the others in python3.

To run the python script:
```shell
chmod +x delete-old-images.py
./delete-old-images.py 
```

To run the bash script:
```shell
./delete-old-images.sh
chmod +x delete-old-images.sh
```

To run the python program, first ensure the python dependencies are installed.
I recommend by doing it inside virtual environment:
```shell
python3 -m venv venv && source ./venv/bin/activate && pip install -r requirements.txt
```
Then run the program with
```shell
python delete-old-images-program.py
```

Tested in Bash 5.2.2, Python 3.10.7, and Docker 20.10.16.
