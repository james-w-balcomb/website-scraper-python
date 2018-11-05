import argparse
import configparser
import logging

import ats_utilities.ats_file_system
import ats_utilities.ats_utilities
import constants


def parse_commandline_arguments(sys_argv):

    # logger = logging.getLogger(__name__)
    logger = logging.getLogger('default_logger')

    logger.info("Parsing Command-Line Arguments...")

    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument(
        "-c",
        "--configuration_file",
        action = "store",
        dest = "configuration_file",
        default = False,
        help = "The path and name for the INI-style configuration file."
               " [Default: ./csv_to_mysql.ini]"
    )
    argument_parser.add_argument(
        "-d",
        "--directory",
        action = "store",
        dest = "csv_directory",
        default = False,
        help = "The root directory from which to begin processing CSV files."
               " [Default: ./CSV/"
    )

    vars_parse_args = vars(argument_parser.parse_args())

    commandline_arguments_config = dict()
    commandline_arguments_config["csv"] = dict()
    commandline_arguments_config["mysql"] = dict()

    if vars_parse_args["csv_directory"]:
        commandline_arguments_config["csv"]["csv_directory"] = vars_parse_args["csv_directory"]

    return commandline_arguments_config


def parse_configuration_file(configuration_file_path_name):

    # logger = logging.getLogger(__name__)
    logger = logging.getLogger('default_logger')

    # TODO(JamesBalcomb): add option for Configuration File Format

    useable_file = ats_utilities.ats_file_system.is_file_useable(configuration_file_path_name)

    # TODO(JamesBalcomb): make this raise an error if the file is unuseable
    if not useable_file:
        logger.error("Configuration File is not useable!!")

    config_parser = configparser.ConfigParser()
    config_parser.read(configuration_file_path_name)

    # TODO(JamesBalcomb): add if is_integer then int()
    # TODO(JamesBalcomb): add if is_float then float()
    configuration_file_config = dict()
    for section in config_parser.sections():
        configuration_file_config[section] = {}
        for key_name, key_value in config_parser.items(section):
            configuration_file_config[section][key_name] = key_value

    return configuration_file_config


def get_configuration(sys_argv):

    # logger = logging.getLogger(__name__)
    logger = logging.getLogger('default_logger')

    # ###################### #
    # Command-Line Arguments #
    # ###################### #

    # logger.info("Parsing Command-Line Arguments...")

    commandline_arguments_config = parse_commandline_arguments(sys_argv)

    # ###################### #
    # INI Configuration File #
    # ###################### #

    logger.info("Parsing Configuration File...")

    if "configuration_file" in commandline_arguments_config\
            and commandline_arguments_config["configuration_file"]:
        configuration_file = commandline_arguments_config["configuration_file"]
    else:
        configuration_file = constants.DEFAULT_CONFIGURATION_FILE

    configuration_file_config = parse_configuration_file(configuration_file)

    # ########################### #
    # Merge Configuration Options #
    # ########################### #

    configuration = ats_utilities.ats_utilities.merge_dictionaries(
        configuration_file_config,
        commandline_arguments_config
    )

    return configuration
