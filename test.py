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
