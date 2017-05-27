#import collections

me = "Alex:"
her = "xy:"

alex_date = open("alex_date.txt","w")
xy_date = open("xy_date.txt","w")

chat_log = open("_chat.txt","r")

for line in chat_log:
	if (me in line):
		alex_date.write(line.split(',', 1)[0]+"\n")
	elif (her in line):
		xy_date.write(line.split(',', 1)[0]+"\n")

chat_log.close()
alex_date.close()
xy_date.close()

