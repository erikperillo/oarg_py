import sys
import re


res = list(sys.argv[1:])

for k,i in enumerate(res):
    _i = re.sub(r'(?<!\\),',',,',i)
    res[k] = re.sub(r'\\,',',',_i)

res = " " + ",".join(res)
for delim in [",,,"]:
    while res.find(delim) >= 0:
        res = res.replace(delim,",,")

print res

res = res.replace(" -",",-").split(",-")
print
print res

remaining = []
for __cand in res:
    _cand = __cand.split(",,")
    cand = _cand[0]
    _remaining = _cand[1:]
    cands = cand.split(",")

    if ("-" + cands[0]) in sys.argv:
        opt = cands[0]
        args = cands[1:]
        print "\topt:",opt
        print "\targs:",args
    else:
        _remaining = [_cand[0]] + _remaining

    remaining += _remaining

    print "\tremaining:",remaining
exit()

from oarg import *

ti = Oarg(int,"-i --int-val",-2,"Integer value",2)
tf = Oarg(float,"-f --float-val",3.1415,"Float value",1)
ts = Oarg(str,"-----s str -string-val:::::::::::","default","String value",4)
tb = Oarg(bool,"-b --bool-val",False,"Boolean value")
hlp = Oarg(bool,"-h --help",False,"This help message")

if parse() != 0:
     print "ERROR: unknown args:",Oarg.invalid_options
     print "Use --help for info"
     exit()

if hlp.getVal():
     describeArgs("Valid options:")
     exit()

print "ti.getVal() =",ti.getVal(),ti.getTupleVal()
print "tf.getVal() =",tf.getVal(),tf.getTupleVal()
print "ts.getVal() =",ts.getVal(),ts.getTupleVal()
print "tb.getVal() =",tb.getVal(),tb.getTupleVal()
