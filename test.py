import sys
import re
import oarg

from oarg import *

ti = Oarg(int,"-i --int-val",-2,"Integer value",2)
tf = Oarg(float,"-f --float-val",3.1415,"Float value",1)
ts = Oarg(str,"-----s str -string-val:::::::::::","default","String value",4)
tb = Oarg(bool,"-b --bool-val",False,"Boolean value")
hlp = Oarg(bool,"-h --help",False,"This help message")

parse()

if hlp.val:
     describeArgs("Valid options:")
     exit()

print "ti.val =",ti.val,ti.vals
print "tf.val =",tf.val,tf.vals
print "ts.val =",ts.val,ts.vals
print "tb.val =",tb.val,tb.vals
