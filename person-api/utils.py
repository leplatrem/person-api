import credstash
import logging
import os


def get_secret(secret_name, context):
    """Fetch secret from environment or credstash."""
    secret = os.getenv(secret_name.split('.')[1], None)

    if not secret:
        secret = credstash.getSecret(
            name=secret_name,
            context=context,
            region="us-west-2"
        )
    return secret


class StructuredLogger(object):
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.set_stream_logger()

    def set_stream_logger(self, format_string=None):
        """Stream logger class borrowed from https://github.com/threatresponse/aws_ir."""

        if not format_string:
            format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

        time_format = "%Y-%m-%dT%H:%M:%S"

        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(self.level)
        streamFormatter = logging.Formatter(format_string, time_format)
        streamHandler.setFormatter(streamFormatter)
        logger.addHandler(streamHandler)

    def get_logger(self):
        logging.getLogger(self.name).addHandler(logging.NullHandler())
