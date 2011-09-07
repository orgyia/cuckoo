#!/usr/bin/python
# Cuckoo Sandbox - Automated Malware Analysis
# Copyright (C) 2010-2011  Claudio "nex" Guarnieri (nex@cuckoobox.org)
# http://www.cuckoobox.org
#
# This file is part of Cuckoo.
#
# Cuckoo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Cuckoo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.

from cuckoo.colors import *

def logo():
    print cyan("                     _                  ")
    print cyan("    ____ _   _  ____| |  _ ___   ___    ")
    print cyan("   / ___) | | |/ ___) |_/ ) _ \\ / _ \\ ")
    print cyan("  ( (___| |_| ( (___|  _ ( |_| | |_| |  ")
    print cyan("   \\____)____/ \\____)_| \_)___/ \\___/") + " v0.2"
    print
    print " www.cuckoobox.org                                "
    print " Copyright (C) 2010-2011                          "
    print " by " + bold("Claudio") + " \"nex\" " + bold("Guarnieri")
    print
    
