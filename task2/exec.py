import glog as logging
import argparse
import subprocess
import platform

def check(host, MTU, os):
    if os == 'darwin':
        cmd = ['ping', '-D', '-s', str(MTU), str(host), '-c', '1', '-W', '3000']
    else:
        cmd = ['ping', '-M', 'do', '-s', str(MTU), str(host), '-c', '1', '-W', '3']
    res = subprocess.run(cmd, universal_newlines=True)
    return res.returncode == 0

parser = argparse.ArgumentParser()
parser.add_argument(
    '--host',
    required=True,
    help='host for which the minimal MTU is searched for'
)
parser.add_argument(
    '--loglevel',
    default='WARN',
    help='glog loglevel. Possible options: INFO WARN. Useless options: CRITICAL FATAL ERROR NOTSET WARNING DEBUG'
)

args = parser.parse_args()
host = args.host
loglevel = args.loglevel
logging.setLevel(loglevel)
current_os = platform.system().lower()

left, right = 0, 1502 - 28
while right - left > 1:
    mid = (left + right) // 2
    if check(host, mid, current_os):
        logging.info('MTU {} is ok'.format(mid))
        left = mid
    else:
        logging.info(f'MTU {mid} bad')
        right = mid

print('min MTU for {} is {}'.format(host, left))
