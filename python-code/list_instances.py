import boto.ec2; 
import sys; 

numb_of_args = len(sys.argv)

if numb_of_args <= 1: 
   print "Error... Need to pass region" 
   exit(0); 

ec2_conn = boto.ec2.connect_to_region(sys.argv[1])
reservations = ec2_conn.get_all_reservations(); 

print reservations 

inst_list = reservations[0].instances 

ins = inst_list[0]

print ins.instance_type
print ins.state 


