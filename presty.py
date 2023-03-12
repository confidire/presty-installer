#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import shutil


def main():
    sys.argv.remove(sys.argv[0])
    args=' '.join(sys.argv)
    if args=="version":
        print("v1.0.0")
        sys.exit()
    if  not isinstance(shutil.which("composer"),str):
        print("未部署Composer运行环境，已退出程序")
        sys.exit()
    if  not isinstance(shutil.which("php"),str):
        print("未部署PHP运行环境，已退出程序")
        sys.exit()
    if args=="install":
        print("正在下载框架及依赖库...")
        status=os.system("composer create-project upstair/presty=1.x-dev")
        if status != 0:
                print("\033[0;37;41m发生未知错误，已退出程序\033[0m")
                sys.exit()
        else:
                print("\033[0;37;42m下载成功！\033[0m")
                sys.exit()
    if args=="update":
        print("正在更新框架及依赖库...")
        status=os.system("composer update")
        if status != 0:
                print("\033[0;37;41m发生未知错误，已退出程序\033[0m")
                sys.exit()
        else:
                print("\033[0;37;42m更新成功！\033[0m")
                sys.exit()
    if not os.path.exists('presty'):
        opinion=input("\033[0;37;41m检测到没有安装框架，是否需要安装？[y/n]\033[0m ")
        if opinion=="y":
            status=os.system("composer create-project upstair/presty=1.x-dev")
            if status != 0:
                print("\033[0;37;41m发生未知错误，已退出程序\033[0m")
                sys.exit()
            os.chdir(os.getcwd() + "\\presty")
            print("\033[0;37;42m下载成功！\033[0m")
        elif opinion== "n":
            print("\033[0;37;43m已退出程序\033[0m")
            sys.exit()
        else:
            print("\033[0;37;41m回复无效，已退出程序\033[0m")
            sys.exit()
    os.system("php presty "+args)


if __name__ == "__main__":
    main()