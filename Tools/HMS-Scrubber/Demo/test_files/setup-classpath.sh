#!/bin/sh

#
#Set up our classpath with our library dependencies...
for jar in `ls $SCRUBBER_HOME/lib/*.jar`;
do
    SCRUBBER_CP=$jar:$SCRUBBER_CP
done

#
#and the Scrubber Lib


# JAVA VM params
JVM_ARGS="-Xms256m -Xmx256m"