import socketserver
import logging
import logging.config

logging.config.fileConfig("weighting/logging.conf")


class WeightingRequestHandler(socketserver.BaseRequestHandler):
    """
    Handler for input requests, assumes that the request (socket)
    contains a text string to process its weight.
    """
    
    logger = logging.getLogger(__name__)
    
    def handle(self):
        self.chain = self.request.recv(2048).decode()
        self.logger.info(f"Processing incoming chain '{self.chain}' from {self.client_address}.")
        
        weight = self.server.weigh(self.chain)
        self.request.send(f"The weight for '{self.chain}' is {weight}".encode())
        self.logger.info(f"Weighting process for '{self.chain}' ended.")


class WeightingServer(socketserver.ThreadingTCPServer):
    """ Extends `socketserver.ThreadingTCPServer` to include weight function definition and log messages. """

    allow_reuse_address = True
    
    def __init__(self, server_address, request_handler_class=WeightingRequestHandler):
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Starting the weighting calculator server at {server_address}")
        super().__init__(server_address, request_handler_class)
    
    def server_activate(self):
        super().server_activate()
        self.logger.info(f"Listing to requests on address {self.server_address}")

    def serve_forever(self, poll_interval=0.5):
        self.logger.info("Waiting for incoming requests")
        return super().serve_forever(poll_interval)

    def weigh(self, chain):
        lookup_a = 0
        weight = 0
        spaces = 0
        for char in chain:
            # Look for double `a` rule
            lookup_a = lookup_a + 1 if char in "aA" else 0
            if lookup_a == 2:
                self.logger.info(f"Double 'a' rule detected >> '{chain}'.")
                return 1000
            
            # Update weight and spaces count
            weight += 1.5 * char.isalpha() + 2 * char.isnumeric()
            spaces += char.isspace()
        return round(weight / spaces, 2)
