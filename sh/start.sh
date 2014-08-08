PID1=`ps aux | grep lighttpd_phone | grep -v grep | awk '{print $2}'`
PID2=`ps aux | grep scgimain.py | grep -v grep | awk '{print $2}'`
kill $PID1
kill $PID2
/usr/sbin/lighttpd -f /rd/angular-tps/config/lighttpd_phone.conf
./../server/scgimain.py 2> output.log &
