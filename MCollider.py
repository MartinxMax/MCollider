#!/usr/bin/python3
# @Мартин.
import sys,argparse,textwrap,hashlib

import requests
from loguru import logger
from multiprocessing.dummy import Pool as ThreadPool

Version = "@Мартин. MCollider_MD5 Tool V1.0.0"
Title='''
************************************************************************************
<免责声明>:本工具仅供学习实验使用,请勿用于非法用途,否则自行承担相应的法律责任
<Disclaimer>:This tool is onl y for learning and experiment. Do not use it for illegal purposes, or you will bear corresponding legal responsibilities
************************************************************************************'''
Logo=f'''
   ▄▄▄▄███▄▄▄▄         ▄████████       ▄██████▄        ▄█             ▄█             ▄█       ████████▄          ▄████████         ▄████████ 
 ▄██▀▀▀███▀▀▀██▄      ███    ███      ███    ███      ███            ███            ███       ███   ▀███        ███    ███        ███    ███ 
 ███   ███   ███      ███    █▀       ███    ███      ███            ███            ███▌      ███    ███        ███    █▀         ███    ███ 
 ███   ███   ███      ███             ███    ███      ███            ███            ███▌      ███    ███       ▄███▄▄▄           ▄███▄▄▄▄██▀ 
 ███   ███   ███      ███             ███    ███      ███            ███            ███▌      ███    ███      ▀▀███▀▀▀          ▀▀███▀▀▀▀▀   
 ███   ███   ███      ███    █▄       ███    ███      ███            ███            ███       ███    ███        ███    █▄       ▀███████████ 
 ███   ███   ███      ███    ███      ███    ███      ███▌    ▄      ███▌    ▄      ███       ███   ▄███        ███    ███        ███    ███ 
  ▀█   ███   █▀       ████████▀        ▀██████▀       █████▄▄██      █████▄▄██      █▀        ████████▀         ██████████        ███    ███ 
                                                      ▀              ▀                                                            ███    ███ 
                                                    Github==>https://github.com/MartinxMax    
                                                    {Version}  
'''



def Init_Loger():
    logger.remove()
    logger.add(
        sink=sys.stdout,
        format="<green>[{time:HH:mm:ss}]</green><level>[{level}]</level> -> <level>{message}</level>",
        level="INFO"
    )


class Main_Class():
    def __init__(self,args):
        self.MD5=args.MD5
        self.CODE_LIST = []

    def run(self):
        if self.MD5:
            logger.warning("Cracking containing MD5 values of:" + self.MD5)
            pool = ThreadPool()
            for i in range(100):
                self.CODE_LIST.append(str(10000000 * i) + ':' + str(10000000 * (i + 1)))
            logger.info("Cracking....")
            pool.map(self.Crack_MD5, self.CODE_LIST)
            pool.close()
            pool.join()

    def Get_MD5(self, note):
        return hashlib.md5(note.encode('utf-8')).hexdigest()

    def Crack_MD5(self, scope):
        start_num = int(scope.split(':')[0])
        end_num = int(scope.split(':')[-1])
        logger.info(f"[Runing] Decoding range {start_num}-{end_num} pure digits")
        for i in range(start_num, end_num):
            if self.MD5 in self.Get_MD5(str(i)):
                logger.warning(f"{i} is contained by MD5:{self.Get_MD5(str(i))}")
                break

def main():
    print(Logo,"\n",Title)
    Init_Loger()
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent('''
        Example:
            author-Github==>https://github.com/MartinxMax
        Basic usage:
            python3 {MPHP} -md5 xxxxxxxx # Support for fuzzy blasting
            '''.format(MPHP = sys.argv[0]
                )))
    parser.add_argument('-md5', '--MD5',default=None, help='MD5')
    args = parser.parse_args()
    Main_Class(args).run()


if __name__ == '__main__':
    main()