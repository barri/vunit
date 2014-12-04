# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014, Lars Asplund lars.anders.asplund@gmail.com

# Make vunit python module importable
from os.path import join, dirname, basename
import sys
path_to_vunit = join(dirname(__file__), '..', '..')
sys.path.append(path_to_vunit)
#  -------

from vunit import VUnit

ui = VUnit.from_argv()

src_path = join(dirname(__file__), "src")

uart_lib = ui.add_library("uart_lib")
uart_lib.add_source_files(join(src_path, "*.vhd"))

tb_uart_lib = ui.add_library("tb_uart_lib")
tb_uart_lib.add_source_files(join(src_path, "test", "*.vhd"))

ui.main()
