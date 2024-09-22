import argparse
import logging

from client.commands import (
    generate,
    process,
)

# Config the logs for client
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] :: %(message)s",
)


# Provides a simple comand-line client for manage generation and file processing
def main():
    parser = argparse.ArgumentParser(
        prog="CLI Client",
        description="Generate string file and submit chains for processing to server.",
    )
    subcommands = parser.add_subparsers(
        title="Commands",
        description="Valid commands for command-line client.",
    )
    
    # Subcommands Parser
    # `generate` command parser
    generator_parser = subcommands.add_parser(
        "generate",
        help="Generate a chain.txt file with a set of random text strings.",
    )
    
    generator_parser.add_argument(
        "-l",
        "--lines",
        type=int,
        default=10**6,
        help="The number of lines in the generated file.",
    )
    generator_parser.add_argument(
        "-o",
        "--output",
        help="The output file where string will be stored",
        default="./chains.txt",
    )
    generator_parser.set_defaults(func=generate)
    
    # `process` command parser
    process_parser = subcommands.add_parser(
        "process",
        help="Process the input file sending the string into it to server, store the responses into output file.",
    )
    
    process_parser.add_argument(
        "server_addr",
        help="The weighting server address."   
    )
    process_parser.add_argument(
        "chains",
        help="The file to process by the server",
    )
    process_parser.add_argument(
        "-o",
        "--output",
        default="./weights.txt",
        help="The output file with the server responses.",
    )
    process_parser.set_defaults(func=process)

    # parse arguments
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
