#/bin/sh

printenv | awk '{print "export " $1}' > /usr/src/env.sh

/usr/sbin/cron -f