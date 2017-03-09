import boto.ec2; 
import sys; 

numb_of_args = len(sys.argv)

if numb_of_args <= 2: 
   print "Error... Need to pass REGION and TYPE & AMI"
   exit(0); 

ec2_conn = boto.ec2.connect_to_region(sys.argv[1])
ec2_conn.run_instances('ami-a58d0dc5', instance_type='t2.micro')


