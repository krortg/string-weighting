## String Weighting

### Requirements

A version of Python 3.11 or higher is required

### Usage

The project contains a command line client and the `weighting` package that contains the generation logic and the server, both packages are executable

To start a server instance run:

```bash
$ python -m weighting <server_addr> <server_port>
```

To see the client commands use

```bash
$ python -m client -h
```

It is possible to execute two commands:

- `generate`: Generates a file with a set of random text strings
  
    ```bash
    $ python -m client generate -l 2000 
    ```

- `process`: Sends the strings from the file passed as a parameter to the specified server and records the responses in an output file

    ```bash
    $ python -m client process localhost:8080 ./chains.txt 
    ```

For each command can be typed the `-h` for more info.