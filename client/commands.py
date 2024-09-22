""" Contains command logic for the command-line client. """

import logging
import socket
from time import time

from weighting.generator import AlphaNumGenerator


logger = logging.getLogger(__name__)


def generate(args):
    logger.info("Initialize the Generator...")
    generator = AlphaNumGenerator()
    
    ctime = time()
    logger.info(f"Generating the file {args.output} with {args.lines} random strings.")
    generator.save(output=args.output, lines=args.lines)
    ctime = round(time() - ctime, 2)
    logger.info(f"The file was generated in {ctime} seconds.")


def process(args):
    host, port = args.server_addr.split(':')
    port = int(port)
    
    fd = open(args.chains, 'rb')
    output = open(args.output, 'wt')
    logger.info("Processing the input file...")
    start = time()
    while True:
        chain = fd.readline().strip()
        if not chain:
            break
        # connect to server and send the string
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.send(chain)
            resp = s.recv(2048).decode()
            print(resp, file=output)
    process_time = round(time() - start, 2)
    logger.info(f"Input file processed in {process_time} seconds.")
