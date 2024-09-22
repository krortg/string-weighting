import argparse

from weighting.server import WeightingServer


def main():
    parser = argparse.ArgumentParser(
        prog="Weight Module Server",
        description="Provides a tcp server for the weighting package."
    )
    
    parser.add_argument(
        "address",
        type=str,
        help="The server address",
    )
    parser.add_argument(
        "port",
        type=int,
        help="The server port",
    )
    
    args = parser.parse_args()
    with WeightingServer((args.address, args.port)) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.logger.info("Server stopped via <Ctrl-c>")


if __name__ == "__main__":
    main()