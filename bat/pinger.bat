@echo off
chcp 65001
title pinger
mode 60,20
color a

set /p IP=Enter IP=
color 3
:top
PING -n 1 %IP% | FIND "TTL="
title ::SEARCHING FOR MILFS %IP&
IF ERRORLEVEL 1 (echo [MILF ERROR] %IP%)
color 3
ping -t 2 0 10 127.0.0.1 >nul
GoTo top
