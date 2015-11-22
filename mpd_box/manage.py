#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    
    from mpd_box.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
