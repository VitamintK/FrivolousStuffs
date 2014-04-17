rows = []
with open('FINAL EVENTS DECEMBER STATUS for kevin - Sheet1.csv') as yolo:
    for line in yolo:
        rows.append((line.strip()+',').split(','))

for i in range(0,len(rows[0])):
    eventlist = ['{0} ({1})'.format(row[0],row[2]) for row in rows if row[i]=='1']
    print '{0}: {1}'.format(rows[0][i],', '.join(eventlist))
