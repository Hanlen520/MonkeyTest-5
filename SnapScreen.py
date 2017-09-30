# -*- coding:utf-8 -*-
import os
import sys
import time


def androidScreencap(Deviceid='', path=0):
    localTime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    remote_obj = '/sdcard/%s.png' % localTime

    if path:
        local_obj = path
    else:
        local_obj = sys.path[0]

    print(remote_obj, local_obj)
    if Deviceid:
        snap = 'adb -s {} shell screencap -p {}'.format(Deviceid, remote_obj)
        pullPic = 'adb -s {} pull {} {}'.format(Deviceid, remote_obj, local_obj)
        print("run command: ", pullPic)

        os.system(snap)
        os.system(pullPic)

        print('OK.')


if __name__ == '__main__':
    androidScreencap()
