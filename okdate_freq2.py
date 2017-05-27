import collections

dates = open("all_messages.txt",'r').read()
calculations = collections.Counter(dates.split('\n'))

with open ('all_messages_sum.txt', 'w') as fp:
    for p in calculations.items():
        fp.write("%s,%s\n" % p)
