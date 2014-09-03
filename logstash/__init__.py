
from logstash.formatter import LogstashFormatterVersion0, LogstashFormatterVersion1

from logstash.handler_tcp import TCPLogstashHandler
from logstash.handler_udp import UDPLogstashHandler, LogstashHandler

def swift_setup(conf, name, log_to_console, log_route, fmt, logger,
                adapted_logger):
    log_server = open("/etc/swift/log_server.conf").read()
    ip, port = log_server.split("|")
    my_handler = UDPLogstashHandler(ip, int(port), version=1)
    logger.addHandler(my_handler)
