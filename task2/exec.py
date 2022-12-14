import argparse
import subprocess
import platform
import time

def check(host, MTU, count, os_type):
    if os_type == 'darwin':
        cmd = ['ping', '-D', '-s', str(MTU), str(host), '-c', str(count), '-W', '3000']
    else:
        cmd = ['ping', '-M', 'do', '-s', str(MTU), str(host), '-c', str(count), '-W', '3']
    res = subprocess.run(cmd, universal_newlines=True)
    return res.returncode

parser = argparse.ArgumentParser()
parser.add_argument(
    '--host',
    required=True,
    help='host for which the minimal MTU is searched for'
)
parser.add_argument(
    '--count',
    required=False,
    help='ping per time',
    default=1,
)

args = parser.parse_args()
host = args.host
os_type = platform.system().lower()
count = args.count

left, right = 64 - 28, 1519 - 28
while right - left > 1:
    mid = (left + right) // 2
    ret_code = check(host, mid, count, os_type)
    if ret_code == 0:
        print('MTU {} is ok'.format(28 + mid))
        left = mid
    elif ret_code == 1:
        print('MTU {} is bad'.format(28 + mid))
        right = mid
    else:
        print('failed')
        exit(1)
    time.sleep(0.3)

print('MTU for {} is {}'.format(host, left + 28))
