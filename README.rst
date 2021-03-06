--------------------------------------
Dragon/CoCO emulator written in Python
--------------------------------------

DragonPy is a Open source (GPL v3 or later) emulator for the 30 years old homecomputer ``Dragon 32`` and ``Tandy TRS-80 Color Computer`` (CoCo)...

The `MC6809 <https://github.com/6809/MC6809>`_ project is used to emulate the 6809 CPU.

+--------------------------------------+----------------------------------------------------+
| |Build Status on travis-ci.org|      | `travis-ci.org/jedie/DragonPy`_                    |
+--------------------------------------+----------------------------------------------------+
| |Coverage Status on coveralls.io|    | `coveralls.io/r/jedie/DragonPy`_                   |
+--------------------------------------+----------------------------------------------------+
| |Requirements Status on requires.io| | `requires.io/github/jedie/DragonPy/requirements/`_ |
+--------------------------------------+----------------------------------------------------+

.. |Build Status on travis-ci.org| image:: https://travis-ci.org/jedie/DragonPy.svg?branch=master
.. _travis-ci.org/jedie/DragonPy: https://travis-ci.org/jedie/DragonPy/
.. |Coverage Status on coveralls.io| image:: https://coveralls.io/repos/jedie/DragonPy/badge.svg
.. _coveralls.io/r/jedie/DragonPy: https://coveralls.io/r/jedie/DragonPy
.. |Requirements Status on requires.io| image:: https://requires.io/github/jedie/DragonPy/requirements.svg?branch=master
.. _requires.io/github/jedie/DragonPy/requirements/: https://requires.io/github/jedie/DragonPy/requirements/

Dragon 32 with CPython 3 under Linux:

|screenshot Dragon 32|

.. |screenshot Dragon 32| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/20150820_DragonPy_Dragon32_CPython3_Linux_01.png

Tandy TRS-80 Color Computer 2b with CPython 2 under Windows:

|screenshot CoCo under Windows|

.. |screenshot CoCo under Windows| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/20150820_DragonPy_CoCo2b_CPython2_Win_01.png

(Note: Python 2 support was removed)

DragonPy is written in Python.
It's platform independent and runs with Python and PyPy under Linux/Windows/OSX/...
It's tested with Python 3.x, PyPy

DragonPy will not be a second XRoar written in Python.
This project is primarily to lean and understand.

Future goals are:

* Implement a integrated development environment for BASIC programs

A full featured Dragon / CoCo emulator is `XRoar <http://www.6809.org.uk/dragon/xroar.shtml>`_.

Current state
=============

The Dragon 32 / 64 and CoCo ROMs works in Text mode.
Also the "single board computer" ROMs sbc09, Simple6809 and Multicomp6809 works well.

There is a rudimentary BASIC editor with save/load BASIC programm listings direct into RAM.

Looks like this:

|old screenshot BASIC Editor|
(older version of the editor)

.. |old screenshot BASIC Editor| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/20140820_DragonPy_BASIC_Editor_01.png

Vectrex
-------

The `Vectrex (Wikipedia) <https://en.wikipedia.org/wiki/Vectrex>`_ is a vector display-based video game console.
The Hardware are *only* the 6809 CPU, a 6522 Versatile Interface Adapter and the AY-3-8912 sound chip.

Current state is completely not usable. The 6522 is only a dummy implementation.
It makes only sense to display some trace lines, e.g.:

::

    .../DragonPy$ poetry run DragonPy --verbosity 0 --machine=Vectrex run --trace --max_ops=1

BASIC Editor
============

Use "BASIC editor / open" in the main menu to open the editor.

You can load/save ASCII .bas files from you local drive or just type a BASIC listing ;)
With "inject into DragonPy" you send the current listing from the Editor to the Emulator and with "load from DragonPy" back from emulator to editor.
Note: The is currently no "warning" that un-saved content will be "overwritten" and there is no "auto-backup" ;)

The "renumbering" tool can be found in the editor window under "tools"

You can also run the BASIC Editor without the Emulator:

::

    .../DragonPy$ make editor
    # or:
    .../DragonPy$ poetry run DragonPy editor

A rudimentary BASIC source code highlighting is available and looks like this:

|screenshot BASIC Editor|

.. |screenshot BASIC Editor| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/20140826_DragonPy_BASIC_Editor_01.png

Special feature: The Line number that are used in GOTO, SOGUB etc. are extra marked on the left side.

------------
installation
------------

IMPORTANT: The **PyPi package** name is **DragonPyEmulator** and `not only "DragonPy" <https://github.com/jpanganiban/dragonpy/issues/3>`_!!!

::

    pip install DragonPyEmulator

from source
===========

::

    ~$ git clone https://github.com/jedie/DragonPy.git
    ~$ cd DragonPy/
    ~/DragonPy$ make
    help                 List all commands
    install-poetry       install or update poetry
    install              install DragonPy via poetry
    update               Update the dependencies as according to the pyproject.toml file
    lint                 Run code formatters and linter
    fix-code-style       Fix code formatting
    tox-listenvs         List all tox test environments
    tox                  Run pytest via tox with all environments
    tox-py36             Run pytest via tox with *python v3.6*
    tox-py37             Run pytest via tox with *python v3.7*
    tox-py38             Run pytest via tox with *python v3.8*
    pytest               Run pytest
    update-rst-readme    update README.rst from README.creole
    publish              Release new version to PyPi
    download-roms        Download/Test only ROM files
    profile              Profile the MC6809 emulation benchmark
    benchmark            Run MC6809 emulation benchmark
    editor               Run only the BASIC editor
    Vectrex              Run GUI with Vectrex emulation (not working, yet!)
    sbc09                Run GUI with sbc09 ROM emulation
    Multicomp6809        Run GUI with Multicomp6809 ROM emulation
    Simple6809           Run GUI with Simple6809 ROM emulation
    CoCo2b               Run GUI with CoCo 2b emulation
    Dragon32             Run GUI with Dragon 32 emulation
    Dragon64             Run GUI with Dragon 64 emulation
    run                  *Run the DragonPy Emulator GUI*
    
    ~/DragonPy$ make install-poetry
    ~/DragonPy$ make install
    ~/DragonPy$ make run
    
    # use the CLI:
    ~/DragonPy$ poetry run DragonPy --help
    ~/DragonPy$ poetry run DragonPy

install in virtualenv by foot:
==============================

e.g.:

::

    # Create virtualenv:
    .../$ python3 -Im venv DragonPy
    
    # activate created virtualenv:
    .../$ cd DragonPy
    .../DragonPy$ source bin/activate
    
    # update pip before install:
    (DragonPy) .../DragonPy$ pip install -U pip
    ...
    
    # Install DragonPy:
    (DragonPy) .../DragonPy$ pip install DragonPyEmulator
    Collecting DragonPyEmulator
    ...
    Installing collected packages: click, six, dragonlib, pygments, MC6809, DragonPyEmulator
    Successfully installed DragonPyEmulator-0.5.3 MC6809-0.5.0 click-6.7 dragonlib-0.1.7 pygments-2.2.0 six-1.11.0
    
    # start Emulator
    (DragonPy) .../DragonPy$ DragonPy

Windows
=======

There are several ways to install the project under windows.

The following is hopeful the easiest one:

* Install Python 3, e.g.: `https://www.python.org/downloads/ <https://www.python.org/downloads/>`_

* Download the ``DragonPy`` git snapshot from Github: `master.zip <https://github.com/jedie/DragonPy/archive/master.zip>`_

* Extract the Archive somewhere

* Maybe, adjust paths in ``boot_dragonpy.cmd``

* Run ``boot_dragonpy.cmd``

The default ``boot_dragonpy.cmd`` will install via ``Python Package Index`` (PyPi) into ``%APPDATA%\DragonPy_env``

start DragonPy
--------------

The is a simple "starter GUI", just call the cli without arguments:

``%APPDATA%\DragonPy_env\Scripts\DragonPy.exe``

It looks like this:

|starter GUI|

.. |starter GUI| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/20150821_DragonPy_starterGUI.png

----
ROMs
----

All needed ROM files, will be downloaded automatically.

The files will be downloaded from:

+----------------+------------------------------------------------------------------------------------------------------------------+
| Dragon 32 + 64 | `http://archive.worldofdragon.org/archive/index.php?dir=Software/Dragon/Dragon%20Data%20Ltd/Dragon%20Firmware/`_ |
+----------------+------------------------------------------------------------------------------------------------------------------+
| CoCo 2b        | `http://www.roust-it.dk/coco/roms/`_                                                                             |
+----------------+------------------------------------------------------------------------------------------------------------------+
| Multicomp      | `http://searle.x10host.com/Multicomp/index.html`_                                                                |
+----------------+------------------------------------------------------------------------------------------------------------------+
| Simple6809     | `http://searle.x10host.com/6809/Simple6809.html`_                                                                |
+----------------+------------------------------------------------------------------------------------------------------------------+

.. _http://archive.worldofdragon.org/archive/index.php?dir=Software/Dragon/Dragon%20Data%20Ltd/Dragon%20Firmware/: http://archive.worldofdragon.org/archive/index.php?dir=Software/Dragon/Dragon%20Data%20Ltd/Dragon%20Firmware/
.. _http://www.roust-it.dk/coco/roms/: http://www.roust-it.dk/coco/roms/
.. _http://searle.x10host.com/Multicomp/index.html: http://searle.x10host.com/Multicomp/index.html
.. _http://searle.x10host.com/6809/Simple6809.html: http://searle.x10host.com/6809/Simple6809.html

sbc09 and vectrex ROMs are included.

All ROM files and download will be checked by SHA1 value, before use.

---------
run tests
---------

You can run tests with PyPy, Python 2 and Python 3:

::

    ~/DragonPy$ make pytest
    # or:
    ~/DragonPy$ make tox
    # or:
    ~/DragonPy$ poetry run pytest

----------------
more screenshots
----------------

"sbc09" ROM in Tkinter window:

|screenshot sbc09|

.. |screenshot sbc09| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/DragonPy_sbc09_01.png

"Simple6809" ROM in Tkinter window:

|screenshot simple6809|

.. |screenshot simple6809| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/Simple6809_TK_04.PNG

Dragon Keyboard
===============

The keyboard mapping is stored into `dragonpy/Dragon32/keyboard_map.py <https://github.com/jedie/DragonPy/blob/master/dragonpy/Dragon32/keyboard_map.py>`_.

Some notes:

* "CLEAR" is mapped to "Home" / "Pos 1" key

* "BREAK" is mapped to "Escape" button

* "LEFT" is mapped to left cursor key and to normal backspace, too.

A "auto shift" mode is implemented. So normal lowercase letters would be automaticly converted to uppercase letters.

paste clipboard
---------------

It is possible to paste the content of the clipboard as user input in the machine.
Just copy (Ctrl-C) the follow content:

::

    10 CLS
    20 FOR I = 0 TO 255:
    30 POKE 1024+(I*2),I
    40 NEXT I
    50 I$ = INKEY$:IF I$="" THEN 50

Focus the DragonPy window and use Ctrl-V to paste the content.

Looks like:

|https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/20140805_DragonPy_Dragon32_Listing.png|

.. |https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/20140805_DragonPy_Dragon32_Listing.png| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/20140805_DragonPy_Dragon32_Listing.png

Then just **RUN** and then it looks like this:

|https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/20140805_DragonPy_Dragon32_CharMap.png|

.. |https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/20140805_DragonPy_Dragon32_CharMap.png| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/20140805_DragonPy_Dragon32_CharMap.png

DragonPy schematic
==================

::

    +------------------+                         +---------------------+
    |                  |                         |                     |
    | +-------------+  |                         |       6809 CPU      |
    | |             |  |                         |       +     ^       |
    | |     GUI     |  |                         |       |     |       |
    | |             |  | Display RAM callback    |    +--v-----+--+    |
    | |  .--------------------------------------------+   Memory  |    |
    | |  |          |  |                         |    +--+-----^--+    |
    | |  |          |  |                         |       |     |       |
    | |  |          |  |                         | +-----v-----+-----+ |
    | |  |          |  |                         | |    Periphery    | |
    | |  |          |  |     Keyboard queue      | |   MC6883 SAM    | |
    | |  |          +--------------------------------->MC6821 PIA    | |
    | |  |          |  |                         | |                 | |
    | +--+-----^----+  |                         | |                 | |
    |    |     |       |                         | +-----------------+ |
    |    |     |       |                         |                     |
    | +--v-----+----+  |                         |                     |
    | |             |  |                         |                     |
    | |   Display   |  |                         |                     |
    | |             |  |                         |                     |
    | +-------------+  |                         |                     |
    +------------------+                         +---------------------+

performance
===========

The current implementation is not really optimized.

With CPython there is round about 490.000 CPU cycles/sec. in console version.
This is half as fast as the real Hardware.

With PyPy round about 6.900.000 - 8.000.000 CPU cycles/sec.
In other words with PyPy it's 8 times faster as the real Hardware.

e.g. The Dragon 32 6809 machine with a 14.31818 MHz crystal runs with:
0,895MHz (14,31818Mhz/16=0,895MHz) in other words: 895.000 CPU-cycles/sec.

-----
TODO:
-----

#. implement more Dragon 32 periphery

missing 6809 unittests after coverage run:

* MUL

* BVS

----------
PyDragon32
----------

Some Python/BASIC tools/scripts around Dragon32/64 / CoCo homecomputer.

All script are copyleft 2013-2020 by Jens Diemer and license unter GNU GPL v3 or above, see LICENSE for more details.

Python scripts:
===============

* PyDC - Convert dragon 32 Cassetts WAV files into plain text:

    * `https://github.com/jedie/DragonPy/tree/master/PyDC <https://github.com/jedie/DragonPy/tree/master/PyDC>`_

* Filter Xroar traces:

    * `https://github.com/jedie/DragonPy/tree/master/misc <https://github.com/jedie/DragonPy/tree/master/misc>`_

BASIC programms:
================

* Simple memory HEX viewer:

    * `https://github.com/jedie/DragonPy/tree/master/BASIC/HexViewer <https://github.com/jedie/DragonPy/tree/master/BASIC/HexViewer>`_

* Test CC Registers:

    * `https://github.com/jedie/DragonPy/tree/master/BASIC/TestCC_Registers <https://github.com/jedie/DragonPy/tree/master/BASIC/TestCC_Registers>`_

Input/Output Tests
------------------

`/BASIC/InputOutput/keyboard.bas <https://github.com/jedie/DragonPy/tree/master/BASIC/InputOutput/keyboard.bas>`_
Display memory Locations $0152 - $0159 (Keyboard matrix state table)

Example screenshow with the "Y" key is pressed down. You see that this is saved in $0153:

|KeyBoard Screenshot 01|

.. |KeyBoard Screenshot 01| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/keyboard01.png

Example with "U" is hold down:

|KeyBoard Screenshot 02|

.. |KeyBoard Screenshot 02| image:: https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/DragonPy/keyboard02.png

-----
Links
-----

* Grant Searle's Multicomp FPGA project:

    * Homepage: `http://searle.x10host.com/Multicomp/ <http://searle.x10host.com/Multicomp/>`_

    * own `dragonpy/Multicomp6809/README <https://github.com/jedie/DragonPy/tree/master/dragonpy/Multicomp6809#readme>`_

* Lennart Benschop 6809 Single Board Computer:

    * Homepage: `http://lennartb.home.xs4all.nl/m6809.html <http://lennartb.home.xs4all.nl/m6809.html>`_

    * own `dragonpy/sbc09/README <https://github.com/jedie/DragonPy/tree/master/dragonpy/sbc09#readme>`_

* Grant Searle's Simple 6809 design:

    * Homepage: `http://searle.x10host.com/6809/Simple6809.html`_

    * own `dragonpy/Simple6809/README <https://github.com/jedie/DragonPy/tree/master/dragonpy/Simple6809#readme>`_

Some links:

* `http://www.burgins.com/m6809.html <http://www.burgins.com/m6809.html>`_

* `http://www.maddes.net/m6809pm/ <http://www.maddes.net/m6809pm/>`_ - Programming Manual for the 6809 microprocessor from Motorola Inc. (now Freescale)

* `http://www.6809.org.uk/dragon/hardware.shtml <http://www.6809.org.uk/dragon/hardware.shtml>`_

* `http://dragondata.worldofdragon.org/Publications/inside-dragon.htm <http://dragondata.worldofdragon.org/Publications/inside-dragon.htm>`_

* `http://koti.mbnet.fi/~atjs/mc6809/ <http://koti.mbnet.fi/~atjs/mc6809/>`_ - 6809 Emulation Page

Source codes:

* `https://github.com/naughton/mc6809/blob/master/mc6809.ts <https://github.com/naughton/mc6809/blob/master/mc6809.ts>`_

* `https://github.com/maly/6809js/blob/master/6809.js <https://github.com/maly/6809js/blob/master/6809.js>`_

* `http://mamedev.org/source/src/mess/drivers/dragon.c.html <http://mamedev.org/source/src/mess/drivers/dragon.c.html>`_

* `http://mamedev.org/source/src/mess/machine/dragon.c.html <http://mamedev.org/source/src/mess/machine/dragon.c.html>`_

* `http://mamedev.org/source/src/emu/cpu/m6809/m6809.c.html <http://mamedev.org/source/src/emu/cpu/m6809/m6809.c.html>`_

* `https://github.com/kjetilhoem/hatchling-32/blob/master/hatchling-32/src/no/k/m6809/InstructionSet.scala <https://github.com/kjetilhoem/hatchling-32/blob/master/hatchling-32/src/no/k/m6809/InstructionSet.scala>`_

Dragon 32 resources:

* Forum: `http://archive.worldofdragon.org/phpBB3/index.php <http://archive.worldofdragon.org/phpBB3/index.php>`_

* Wiki: `http://archive.worldofdragon.org/index.php?title=Main_Page <http://archive.worldofdragon.org/index.php?title=Main_Page>`_

-------
Credits
-------

Some code based on:

**ApplePy**

An Apple ][ emulator in Python

* Author: James Tauber

* `https://github.com/jtauber/applepy <https://github.com/jtauber/applepy>`_

* License: MIT

**XRoar**
A really cool Dragon / CoCo emulator

* Author: Ciaran Anscomb

* `http://www.6809.org.uk/xroar/ <http://www.6809.org.uk/xroar/>`_

* License: GNU GPL v2

included Python modules:
========================

**python-pager**
Page output and find dimensions of console.

* Author: Anatoly Techtonik

* License: Public Domain

* Homepage: `https://bitbucket.org/techtonik/python-pager/ <https://bitbucket.org/techtonik/python-pager/>`_

* Stored here: `/dragonpy/utils/pager.py <https://github.com/jedie/DragonPy/blob/master/dragonpy/utils/pager.py>`_

**srecutils.py**
Motorola S-Record utilities

* Author: Gabriel Tremblay

* License: GNU GPL v2

* Homepage: `https://github.com/gabtremblay/pysrec <https://github.com/gabtremblay/pysrec>`_

* Stored here: `/dragonpy/utils/srecord_utils.py <https://github.com/jedie/DragonPy/blob/master/dragonpy/utils/srecord_utils.py>`_

requirements
============

**dragonlib**
Dragon/CoCO Python Library

* Author: Jens Diemer

* `https://pypi.org/project/DragonLib/ <https://pypi.org/project/DragonLib/>`_

* `https://github.com/6809/dragonlib <https://github.com/6809/dragonlib>`_

* License: GNU GPL v3

**MC6809**
Implementation of the MC6809 CPU in Python

* Author: Jens Diemer

* `https://pypi.org/project/MC6809 <https://pypi.org/project/MC6809>`_

* `https://github.com/6809/MC6809 <https://github.com/6809/MC6809>`_

* License: GNU GPL v3

**pygments**
generic syntax highlighter

* Author: Georg Brandl

* `https://pypi.org/project/Pygments <https://pypi.org/project/Pygments>`_

* `http://pygments.org/ <http://pygments.org/>`_

* License: BSD License

-------
History
-------

* `*dev* <https://github.com/jedie/DragonPy/compare/v0.7.0...master>`_:

    * tbc

* `01.10.2020 - v0.7.0 <https://github.com/jedie/DragonPy/compare/v0.6.0...v0.7.0>`_:

    * Modernize project testing, CI pipeline, usw poetry etc.

    * Many Code updates

    * Remove Python v2 fallback code parts

    * Update ROM Download Links

    * Bugfix "--max_ops" cli options

* `19.06.2018 - v0.6.0 <https://github.com/jedie/DragonPy/compare/v0.5.3...v0.6.0>`_:

    * Update to new MC6809 API

    * reimplementing Simple6809, contributed by `Claudemir Todo Bom <https://github.com/ctodobom>`_

    * TODO: Fix speedlimit

    * Fix ``No module named 'nose'`` on normal PyPi installation

* `24.08.2015 - v0.5.3 <https://github.com/jedie/DragonPy/compare/v0.5.2...v0.5.3>`_:

    * Bugfix for "freeze" after "speed limit" was activated

* `20.08.2015 - v0.5.2 <https://github.com/jedie/DragonPy/compare/v0.5.1...v0.5.2>`_:

    * Add run 'MC6809 benchmark' button to 'starter GUI'

    * bugfix 'file not found' in 'starter GUI'

    * change the GUI a little bit

* `19.08.2015 - v0.5.1 <https://github.com/jedie/DragonPy/compare/v0.5.0...v0.5.1>`_:

    * Add a "starter GUI"

    * Add work-a-round for tkinter usage with virtualenv under windows, see: `virtualenv issues #93 <https://github.com/pypa/virtualenv/issues/93>`_

    * bugfix e.g.: keyboard input in "sbc09" emulation

    * use nose to run unittests

* `18.08.2015 - v0.5.0 <https://github.com/jedie/DragonPy/compare/v0.4.0...v0.5.0>`_:

    * ROM files will be downloaded on-the-fly (``.sh`` scripts are removed. So it's easier to use under Windows)

* `26.05.2015 - v0.4.0 <https://github.com/jedie/DragonPy/compare/v0.3.2...v0.4.0>`_:

    * The MC6809 code is out sourced to: `https://github.com/6809/MC6809`_

* `15.12.2014 - v0.3.2 <https://github.com/jedie/DragonPy/compare/v0.3.1...v0.3.2>`_:

    * Use `Pygments <http://pygments.org/>`_ syntax highlighter in BASIC editor

* `08.10.2014 - v0.3.1 <https://github.com/jedie/DragonPy/compare/v0.3.0...v0.3.1>`_:

    * Release as v0.3.1

    * 30.09.2014 - Enhance the BASIC editor

    * 29.09.2014 - Merge `PyDragon32 <https://github.com/jedie/PyDragon32>`_ project

* `25.09.2014 - v0.3.0 <https://github.com/jedie/DragonPy/compare/v0.2.0...v0.3.0>`_:

    * `Change Display Queue to a simple Callback <https://github.com/jedie/DragonPy/commit/f396551df730b509498d1b884cdda8f7075737c4>`_

    * Reimplement `Multicomp 6809 <https://github.com/jedie/DragonPy/commit/f3bfbdb2ae9906d8e051436173225c3fa8de1373>`_ and `SBC09 <https://github.com/jedie/DragonPy/commit/61c26911379d2b7ea6d07a8b479ab14c5d5a7154>`_

    * Many code refactoring and cleanup

* `14.09.2014 - v0.2.0 <https://github.com/jedie/DragonPy/compare/v0.1.0...v0.2.0>`_:

    * Add a speedlimit, config dialog and IRQ: `Forum post 11780 <http://archive.worldofdragon.org/phpBB3/viewtopic.php?f=5&t=4308&p=11780#p11780>`_

* `05.09.2014 - v0.1.0 <https://github.com/jedie/DragonPy/compare/8fe24e5...v0.1.0>`_:

    * Implement pause/resume, hard-/soft-reset 6809 in GUI and improve a little the GUI/Editor stuff

    * see also: `Forum post 11719 <http://archive.worldofdragon.org/phpBB3/viewtopic.php?f=5&t=4308&p=11719#p11719>`_.

* 27.08.2014 - Run CoCo with Extended Color Basic v1.1, bugfix transfer BASIC Listing with `8fe24e5...697d39e <https://github.com/jedie/DragonPy/compare/8fe24e5...697d39e>`_ see: `Forum post 11696 <http://archive.worldofdragon.org/phpBB3/viewtopic.php?f=5&t=4308&start=90#p11696>`_.

* 20.08.2014 - rudimenary BASIC IDE works with `7e0f16630...ce12148 <https://github.com/jedie/DragonPy/compare/7e0f16630...ce12148>`_, see also: `Forum post 11645 <http://archive.worldofdragon.org/phpBB3/viewtopic.php?f=8&t=4439#p11645>`_.

* 05.08.2014 - Start to support CoCo, too with `0df724b <https://github.com/jedie/DragonPy/commit/0df724b3ee9d87088b524c3623040a41e9772eb4>`_, see also: `Forum post 11573 <http://archive.worldofdragon.org/phpBB3/viewtopic.php?f=5&t=4308&start=80#p11573>`_.

* 04.08.2014 - Use the origin Pixel-Font with Tkinter GUI, see: `Forum post 4909 <http://archive.worldofdragon.org/phpBB3/viewtopic.php?f=5&t=4909>`_ and `Forum post 11570 <http://archive.worldofdragon.org/phpBB3/viewtopic.php?f=5&t=4308&start=80#p11570>`_.

* 27.07.2014 - Copyrigth info from Dragon 64 ROM is alive with `543275b <https://github.com/jedie/DragonPy/commit/543275b1b90824b64b67dcd003cc5ab54296fc15>`_, see: `Forum post 11524 <http://archive.worldofdragon.org/phpBB3/viewtopic.php?f=5&t=4308&start=80#p11524>`_.

* 29.06.2014 - First "HELLO WORLD" works, see: `Forum post 11283 <http://archive.worldofdragon.org/phpBB3/viewtopic.php?f=5&t=4308&start=70#p11283>`_.

* 27.10.2013 - "sbc09" ROM works wuite well almist, see: `Forum post 9752 <http://archive.worldofdragon.org/phpBB3/viewtopic.php?f=5&t=4308&start=60#p9752>`_.

* 16.10.2013 - See copyright info from "Simple6809" ROM with `25a97b6 <https://github.com/jedie/DragonPy/tree/25a97b66d8567ba7c3a5b646e4a807b816a0e376>`_ see also: `Forum post 9654 <http://archive.worldofdragon.org/phpBB3/viewtopic.php?f=5&t=4308&start=50#p9654>`_.

* 10.09.2013 - Start to implement the 6809 CPU with `591d2ed <https://github.com/jedie/DragonPy/commit/591d2ed2b6f1a5f913c14e56e1e37f5870510b0d>`_

* 28.08.2013 - Fork "Apple ][ Emulator" written in Python: `https://github.com/jtauber/applepy`_ to `https://github.com/jedie/DragonPy <https://github.com/jedie/DragonPy>`_

------
Links:
------

+--------+-----------------------------------------------+
| Forum  | `http://forum.pylucid.org/`_                  |
+--------+-----------------------------------------------+
| IRC    | `#pylucid on freenode.net`_                   |
+--------+-----------------------------------------------+
| Jabber | pylucid@conference.jabber.org                 |
+--------+-----------------------------------------------+
| PyPi   | `https://pypi.org/project/DragonPyEmulator/`_ |
+--------+-----------------------------------------------+
| Github | `https://github.com/jedie/DragonPy`_          |
+--------+-----------------------------------------------+

.. _http://forum.pylucid.org/: http://forum.pylucid.org/
.. _#pylucid on freenode.net: http://www.pylucid.org/permalink/304/irc-channel
.. _https://pypi.org/project/DragonPyEmulator/: https://pypi.org/project/DragonPyEmulator/

--------
donation
--------

* Send `Bitcoins <http://www.bitcoin.org/>`_ to `1823RZ5Md1Q2X5aSXRC5LRPcYdveCiVX6F <https://blockexplorer.com/address/1823RZ5Md1Q2X5aSXRC5LRPcYdveCiVX6F>`_

------------

``Note: this file is generated from README.creole 2020-10-01 13:19:41 with "python-creole"``