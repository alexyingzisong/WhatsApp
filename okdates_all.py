def is_int(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def starts_with_date(t):
	if(is_int(t[0]) and is_int(t[1]) and (t[2] is "/")) or (is_int(t[0]) and (t[1] is "/")):
		return True

chat_log = open("_chat.txt","r")
all_messages = open("all_messages.txt","w")

for line in chat_log:
		if starts_with_date(str(line)):
			all_messages.write(line.split(',', 1)[0]+"\n")

chat_log.close()
all_messages.close()

