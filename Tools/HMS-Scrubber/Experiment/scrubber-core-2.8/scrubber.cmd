@echo off

set SCRUBBER_HOME=.

rem Set up the classpath
call %SCRUBBER_HOME%\setup-classpath.cmd

rem Now run the ETL (with args)
@java  %JVM_ARGS% -Dlog4j.configuration=file:conf/log4j.properties -classpath %SCRUBBER_CP% org.spin.loader.scrubber.impl.batch.DefaultBatchRunner %1 %2 %3

pause