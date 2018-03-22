@echo off


@set JVM_ARGS=-Xmx512m -Xms128m
@set SCRUBBER_CP=.
@set LIB_DIR=%SCRUBBER_HOME%\lib


for /F %%G in ('dir /b %LIB_DIR%') do (call :append %%G)



GOTO :eof


@REM appending must be done in procedure call otherwise it won't append.  Windows=dumb
:append
            @set SCRUBBER_CP=%SCRUBBER_CP%;%LIB_DIR%\%1
            GOTO :eof
            
            
            


            