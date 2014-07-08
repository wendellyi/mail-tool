#! /bin/sh

attach=$1

if [ 1 -ne $# ]; then
    echo "please input attach"
    exit
fi

python mail-tool.py -f wendellyih@yeah.net -p ywj880620 -a $attach -t wendellyih@yeah.net
