# python-script-example

Small example on how to use python to replace bash scripts
These two scripts delete all images that were created (not downloaded) more than 2 weeks ago.
They are functionally similar, except that one was written in bash, and the other in python3.

To run them, first, ensure the script is executable (for UNIX machines), with:
```shell
chmod +x delete-old-images.*
```

And then simply execute the file
```shell
./delete-old-images.py # or ./delete-old-images.sh
```

These scripts were tested in bash 5.2.2, python 3.10.7, and docker 20.10.16.

//TODO
For more information, visit unicoeding.com/blog/ 



