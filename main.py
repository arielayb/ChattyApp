from Module.MsgHandler import MsgHandler
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, help="echo the string you use here")
    parser.add_argument("-a", "--ipaddr", type=str, help="echo the string you use here")
    parser.add_argument("-u", "--user", type=str, help="echo the string you use here")
    parser.add_argument("-s", "--passwd", type=str, help="echo the string you use here")
    args = parser.parse_args()

    port = args.port
    ipaddr = args.ipaddr
    user = args.user
    passwd = args.passwd

    print("port?", args.port)
    amq = MsgHandler(port, ipaddr, user, passwd)
    amq.sendPacket("hello world!")
    amq.getPacket()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
