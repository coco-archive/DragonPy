#!/usr/bin/env python
# encoding:utf-8

"""
    loggin utilities
    ~~~~~~~~~~~~~~~~

    :created: 2014 by Jens Diemer - www.jensdiemer.de
    :copyleft: 2014 by the DragonPy team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from __future__ import absolute_import, division, print_function
from dragonlib.utils import six
xrange = six.moves.xrange

import logging
import sys

log = logging.getLogger(__name__)


# log.critical("Log handlers: %s", repr(log.handlers))
# if len(log.handlers) > 1:  # FIXME: tro avoid doublicated output
#     log.handlers = (log.handlers[0],)
#     log.critical("Fixed Log handlers: %s", repr(log.handlers))


def setup_logging(log, level, handler=None, log_formatter=None):
    """
    levels:
         1 - hardcode DEBUG ;)
        10 - DEBUG
        20 - INFO
        30 - WARNING
        40 - ERROR
        50 - CRITICAL/FATAL
        99 - nearly off
       100 - complete off
    """
    root_logger = logging.getLogger()

    if level == 100:
        root_logger.disabled = True
        return

    root_logger.setLevel(level=level)

    if log_formatter is None:
        log_formatter = "[%(processName)s %(threadName)s] %(message)s"
    formatter = logging.Formatter(log_formatter)

    if handler is None:
        handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    if hasattr(handler, "baseFilename"):
        sys.stderr.write("Log to file: %s (%s)\n" % (
            handler.baseFilename, repr(handler))
        )
    else:
        sys.stderr.write("Log to handler: %s\n" % repr(handler))
    root_logger.handlers = (handler,)


def disable_logging(log):
    """
    e.g.: for run all unittests.
    btw. logging can be activated again with e.g.: setup_logging()
    """
    log.log(99, "Disable all logging output.")
    root_logger = logging.getLogger()
    root_logger.setLevel(level=100)
    root_logger.disabled = True
    root_logger.handlers = ()


def log_memory_dump(memory, start, end, mem_info, level=99):
    log.log(level, "Memory dump from $%04x to $%04x:", start, end)

    for addr in xrange(start, end + 1):
        value = memory[addr]
        if isinstance(value, int):
            msg = "$%04x: $%02x (dez: %i)" % (addr, value, value)
        else:
            msg = "$%04x: %s (is type: %s)" % (addr, repr(value), type(value))
        msg = "%-25s| %s" % (
            msg, mem_info.get_shortest(addr)
        )
        log.log(level, "\t%s", msg)


def pformat_hex_list(hex_list):
    return " ".join(["$%x" % v for v in hex_list])

def pformat_byte_hex_list(hex_list):
    return " ".join(["$%02x" % v for v in hex_list])

def pformat_word_hex_list(hex_list):
    return " ".join(["$%02x" % v for v in hex_list])

def log_hexlist(byte_list, group=8, start=0x0000, level=99):
    def _log(level, addr, line):
        msg = pformat_byte_hex_list(line)
        msg = "%04x - %s" % (addr, msg)
        log.log(level, msg)

    pos = 0
    addr = start
    line = []
    for value in byte_list:
        pos += 1
        line.append(value)
        if pos >= group:
            _log(level, addr, line)
            addr += pos
            pos = 0
            line = []
    _log(level, addr, line)


def pformat_program_dump(ram_content):
    msg = pformat_byte_hex_list(ram_content)
    msg = msg.replace("$00 ", "\n$00\n")
    return msg


def log_program_dump(ram_content, level=99):
    msg = "BASIC program dump:\n"
    msg += pformat_program_dump(ram_content)
    log.log(level, msg)



#------------------------------------------------------------------------------


def test_run():
    import os
    import subprocess
    cmd_args = [
        sys.executable,
        os.path.join("..", "DragonPy_CLI.py"),
#         "-h"
#         "--log_list",
        "--verbosity", "50",
        "--log", "DragonPy.cpu6809,50;dragonpy.Dragon32.MC6821_PIA,40",

#         "--verbosity", " 1", # hardcode DEBUG ;)
#         "--verbosity", "10", # DEBUG
#         "--verbosity", "20", # INFO
#         "--verbosity", "30", # WARNING
#         "--verbosity", "40", # ERROR
#         "--verbosity", "50", # CRITICAL/FATAL
#         "--verbosity", "99", # nearly all off
        "--machine", "Dragon32", "run",
#        "--machine", "Vectrex", "run",
#        "--max_ops", "1",
#        "--trace",
    ]
    print("Startup CLI with: %s" % " ".join(cmd_args[1:]))
    subprocess.Popen(cmd_args, cwd="..").wait()

if __name__ == "__main__":
    dump = (0x1e, 0x07, 0x00, 0x0a, 0xa0, 0x00, 0x1e, 0x1a, 0x00, 0x14, 0x80, 0x20, 0x49, 0x20, 0xcb, 0x20, 0x30, 0x20, 0xbc, 0x20, 0x32, 0x35, 0x35, 0x3a, 0x00, 0x1e, 0x2d, 0x00, 0x1e, 0x93, 0x20, 0x31, 0x30, 0x32, 0x34, 0xc3, 0x28, 0x49, 0xc5, 0x32, 0x29, 0x2c, 0x49, 0x00, 0x1e, 0x35, 0x00, 0x28, 0x8b, 0x20, 0x49, 0x00, 0x1e, 0x4e, 0x00, 0x32, 0x49, 0x24, 0x20, 0xcb, 0x20, 0xff, 0x9a, 0x3a, 0x85, 0x20, 0x49, 0x24, 0xcb, 0x22, 0x22, 0x20, 0xbf, 0x20, 0x35, 0x30, 0x00, 0x00, 0x00)
    log_hexlist(dump)
#    log_hexlist(dump, group=4)
#    log_hexlist(dump, group=5)

    test_run()
