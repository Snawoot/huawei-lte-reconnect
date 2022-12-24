#!/usr/bin/env python3
"""
Example code on how to reconnect dialup:
python3 reconnect_dialup.py http://admin:PASSWORD@192.168.8.1/
"""
import time
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from huawei_lte_api.Connection import Connection
from huawei_lte_api.Client import Client
from huawei_lte_api.enums.client import ResponseEnum

def main():
    def check_nonnegative_float(value):
        fvalue = float(value)
        if fvalue <= 0:
            raise argparse.ArgumentTypeError(
                "%s is an invalid non-negative float value" % value)
        return fvalue
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('url', type=str,
        help='device URL. Example: http://admin:PASSWORD@192.168.8.1/')
    parser.add_argument('-u', '--username', type=str, help='username for login')
    parser.add_argument('-p', '--password', type=str, help='password for login')
    parser.add_argument('-d', '--delay', type=check_nonnegative_float, default=120,
        help='delay between turning off and on')
    args = parser.parse_args()
    
    with Connection(args.url, username=args.username, password=args.password) as connection:
        client = Client(connection)
        print('Disabling dialup...')
        if client.dial_up.set_mobile_dataswitch(0) == ResponseEnum.OK.value:
            print('OK')
        else:
            print('Error')
        print('Sleeping for %.2f seconds...' % (args.delay,))
        time.sleep(args.delay)
        print('Enabling dialup...')
        if client.dial_up.set_mobile_dataswitch(1) == ResponseEnum.OK.value:
            print('OK')
        else:
            print('Error')

if __name__ == '__main__':
    main()
