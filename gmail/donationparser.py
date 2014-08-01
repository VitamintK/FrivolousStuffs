import BeautifulSoup

with open('Gmail - Fwd  Notification of Donation Received.htm','r') as f:
    donationfile = f.read()

donationsoup = BeautifulSoup.BeautifulSoup(donationfile)
#print donationsoup.prettify()
donationemails = donationfile.split('This email confirms that')
for donationemail in donationemails[1:]:
    try:
        eaddress = donationemail.split('mailto:')[1].split('"')[0]
        amount,rest = donationemail.split('">$')[1].split(' USD')[:2]
        name = rest.split('<td width="55%">')[4].split('</td>')[0]
        print amount
        print eaddress
        print name
        try:
            address = [BeautifulSoup.BeautifulSoup(line.replace('&nbsp;',' ')).prettify() for line in rest.split('Address')[1].split('<td width="55%">')[1].split('</td>')[0].split('<br>')]
            print address
        except:
            pass
        #who needs regex
    except Exception as e:
        raise e
