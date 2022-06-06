#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import platform
import os

# Detect OS and run file accordingly
System = platform.system()
if System == "Windows":
    import Windows.pylemanager as pylemanager
    main = pylemanager.main
    main()
elif System == "Linux":
    import Linux.pylemanager as pylemanager
    main = pylemanager.main
    main()
elif System == "Darwin":
    import Darwin.pylemanager as pylemanager
    main = pylemanager.main
    main()
else:
    print("Unsupported OS")
    exit()
