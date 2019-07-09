import argparse

from rasa.cli.arguments.default_arguments import add_model_param, add_sender_id_param
from rasa.cli.arguments.run import add_server_arguments
from rasa.core.channels.channel import UserMessage


def set_shell_arguments(parser: argparse.ArgumentParser):
    add_model_param(parser)
    add_sender_id_param(parser, UserMessage.DEFAULT_SENDER_ID)
    add_server_arguments(parser)


def set_shell_nlu_arguments(parser: argparse.ArgumentParser):
    add_model_param(parser)
