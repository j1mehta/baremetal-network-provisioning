import telnetlib
import time

def connect_to_switch(device_ip,port,device_username,device_password,timeout):
#  print "Connecting the device : " + device_ip
  tn = telnetlib.Telnet(device_ip,port=port,timeout=timeout)
  tn.write("\n")
  index,match,data = tn.expect(["Press <Enter> twice",'Press any key to continue','~#',"Username: "],20)
  time.sleep(1)
 # print ("data = %s , index = %s" ) % (data,index)
  if ( index == 0 or index == -1) :
    tn.write("\r")
    tn.write("\n")
    tn.write("\r")
    tn.write("\n")
    index,match,data = tn.expect(["login:",'~#'],20)
  #  print ("data = %s , index = %s" ) % (data,index)
    if (index == 0) :
      tn.write(device_username+"\n")
      index, match, data = tn.expect(['~#',"Password: "],20)
   #   print ("data = %s , index = %s " ) % (data,index)
      tn.write(device_password + "\n")
      tn.read_until('~#',6)
    else :
      tn.write("\n")
  elif (index == 3) :
    tn.write(device_username+"\n")
    index, match, data = tn.expect(['~#',"Password: "],6)
    #print ("data = %s , index = %s" ) % (data,index)
    tn.write(device_password + "\n")
    tn.read_until('~#',6)
  time.sleep(1)
  tn.write("\n")
  output = tn.read_until('~#',6)
#  print output
  if (tn) :
    print "Connected to device "
  return tn

def run_cmd_op(tn,command):
  tn.read_until('~#',2)
#  print "Executing command : " + command
  tn.write(command+"\n")
  data = tn.read_until('~#',2)
#  print data
  return data

