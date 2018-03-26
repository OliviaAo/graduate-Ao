#!/bin/sh

SCRUBBER_HOME=`dirname $0`

#
#Set up the classpath

source $SCRUBBER_HOME/setup-classpath.sh
 
#
#Now run the ETL (with args)

java $JVM_ARGS  -Dlog4j.configuration=file:conf/log4j.properties -cp $SCRUBBER_CP org.spin.loader.scrubber.impl.batch.DefaultBatchRunner "$@"
