# -*- coding: utf-8 -*-
#
# This file is part of the copydeps program.
# Copyright (C) 2019 Artur "suve" Iwicki
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License,
# either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program (LICENCE.txt). If not, see <https://www.gnu.org/licenses/>.
#

import subprocess


def run(program, args=None):
	if args is None:
		args = [program]
	else:
		args.insert(0, program)

	proc = subprocess.run(args=args, capture_output=True)

	status = proc.returncode
	stdout = proc.stdout.decode("utf-8").split("\n")
	stderr = proc.stderr.decode("utf-8").split("\n")

	return status, stdout, stderr
