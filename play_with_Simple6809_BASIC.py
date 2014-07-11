#!/usr/bin/env python
# encoding:utf-8

"""
    Simple6809 Play
    ~~~~~~~~~~~~~~~

    Just for devloper to play a little bit with the BASIC Interpreter.

    :created: 2014 by Jens Diemer - www.jensdiemer.de
    :copyleft: 2014 by the DragonPy team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""


import logging
import os

from dragonpy.tests.test_base import Test6809_BASIC_simple6809_Base



class Test_simple6809_BASIC(Test6809_BASIC_simple6809_Base):
    def __init__(self):
#        os.remove(self.TEMP_FILE);print "Delete CPU date file!"
        self.setUpClass()

    def hello_world(self):
        self.setUp() # restore CPU/Periphery state to a fresh startup.

        self.periphery.add_to_input_queue('PRINT "HELLO WORLD!"\r\n')
        op_call_count, cycles, output = self._run_until_OK()
        print op_call_count, cycles, output

    def play(self):
        self.setUp() # restore CPU/Periphery state to a fresh startup.

        self.periphery.add_to_input_queue('?5/3\r\n')
        op_call_count, cycles, output = self._run_until_OK(max_ops=100000)
        print op_call_count, cycles, output



if __name__ == '__main__':
    log = logging.getLogger("DragonPy")
    log.setLevel(
#        1
#        10 # DEBUG
#        20 # INFO
#        30 # WARNING
#        40 # ERROR
        50 # CRITICAL/FATAL
    )
    log.addHandler(logging.StreamHandler())


    c = Test_simple6809_BASIC()

    print "-"*79
    c.hello_world()
    print "-"*79
    c.play()
    print "-"*79

    print " --- END --- "