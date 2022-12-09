import argparse
import subprocess
import platform
import time

def check(host, MTU, os_type):
    if os_type == 'darwin':
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

args = parser.parse_args()
host = args.host
os_type = platform.system().lower()

left, right = 0, 1502 - 28
while right - left > 1:
    mid = (left + right) // 2
    if check(host, mid, os_type):
        print('MTU {} is ok'.format(mid))
        left = mid
    else:
        print('MTU {} bad'.format(mid))
        right = mid
    time.sleep(0.3)

print('min MTU for {} is {}'.format(host, left))
