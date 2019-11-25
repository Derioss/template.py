#!/user/bin/python3
import logging
import logging.handlers
import sys
import argparse
import os
############LOGGING#################################

def my_log(my_log, host, port, loglevel):

    LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

    my_log = logging.getLogger(my_log)
    my_log.setLevel(LEVELS[loglevel])
    logFormatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    sysloghandler = logging.handlers.SysLogHandler(address='/dev/log') # for syslog in /var/log/syslog
    sysloghandler.setFormatter(logFormatter)
    my_log.addHandler(sysloghandler)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    my_log.addHandler(consoleHandler)
    return my_log

###################VAR########################
syslog_host='localhost' # adresse du syslog
port=514 # port udp du syslog

####################MAIN#############################
def main(loglevel,my_log,dryrun):
    #logging 
    my_log = my_log('script.py',syslog_host,port,loglevel)    
    my_log.info('START PROGRAM')    
    if dryrun is True:
        my_log.info('DRYRUN ACTIVE')

      
    my_log.info('STOP PROGRAM')
##########################################################

if __name__ == "__main__":
    ## args options for log level
    parser = argparse.ArgumentParser()
    parser.add_argument("-l","--loglevel", action="store",dest="verbosity",default='info',
    help="options: debug info warning error critical, default=info")
    parser.add_argument("-d","--dryrun", action="store_true",help="active this option to performed dryrun")
    args = parser.parse_args()    
    loglevel=args.verbosity
    if args.dryrun:
        dryrun=args.dryrun
    else:
        dryrun=False
    #main
    main(loglevel,my_log,dryrun)