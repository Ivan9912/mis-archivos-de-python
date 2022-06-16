@echo off
:menu
cls
title Geben Sie das Passwort ein:
color 03
echo.
echo.
echo.
echo.
echo.
echo.
set /p var=           SCRIBT:
if %var%==1595 goto :jojo
if not %var%==1595 goto :jojoj
:jojoj
cls
color 0c
echo.
echo.
echo.
echo.
echo                  ERRORERRORERROR  ERRORERROR       ERRORERROR            ERRORERROR      ERRORERROR
echo                  ERRORERRORERROR  ERROR   ERROR    ERROR   ERROR       ERROR    ERROR    ERROR   ERROR
echo                  ERROR            ERROR     ERROR  ERROR     ERROR   ERROR        ERROR  ERROR     ERROR
echo                  ERROR            ERROR     ERROR  ERROR     ERROR   ERROR        ERROR  ERROR     ERROR
echo                  ERRORERROR       ERROR   ERROR    ERROR   ERROR     ERROR        ERROR  ERROR   ERROR
echo                  ERRORERROR       ERRORERROR       ERRORERROR        ERROR        ERROR  ERRORERROR
echo                  ERROR            ERROR  ERROR     ERROR  ERROR      ERROR        ERROR  ERROR  ERROR
echo                  ERROR            ERROR   ERROR    ERROR   ERROR     ERROR        ERROR  ERROR   ERROR
echo                  ERRORERRORERROR  ERROR    ERROR   ERROR    ERROR      ERROR    ERROR    ERROR    ERROR
echo                  ERRORERRORERROR  ERROR     ERROR  ERROR     ERROR       ERRORERROR      ERROR     ERROR
echo.
echo.
echo.
set /p var= Volver (V) o Salir (S)
if %var%==v goto :menu
if %var%==s
exit
:jojo
cls
color 0a
start Ivan
echo.
echo.
echo.
echo.
echo                   .                 ........
echo                    ..              ..........
echo                     ..            ........  ..
echo                      ..          .......      .
echo                       ..        .......
echo                        ..      .......
echo                         ..    .......
echo                          ..  .......
echo                           .........
echo                            .......
set /p var=
exit
