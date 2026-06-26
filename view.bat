:: Used for automatically opening .FMIF files when clicked. Must be in same directory as FMIF.py and FMIFView.py
@echo off
title FMIFView
FMIFView.py %1
exit /b