import sys;
import boto; 

print "\nPython Boto Code to List all Instances in AWS Account\n\n" 
print "\tUsage: python list_instances.py [all, running, stopped]" 

numb_of_args=len(sys.argv)

if numb_of_args <= 1: 
   print "\n\tThis script expects atleast 1 argument! See usage!" 
   exit(0)
else:
   print ""
 
if(sys.argv[1] == "all"):
  print "start instances"
else: 
  print "stop instances" 

