#! /bin/sh

attach=$1
subject=$2

if [ 2 -ne $# ]; then
    echo "please correct parameter"
    exit
fi

python mail-tool.py -f wendellyih@yeah.net -p ywj880620 -a $attach -t wendellyih@yeah.net -s "$subject"
