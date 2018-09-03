import requests
import re

def humanFileSize(size):
    if(size >= 1<<40):
        size = size/(1<<40)
        return '%.2f' % size + ' TiB'
    if(size >= 1<<30):
        size = size/(1<<30)
        return '%.2f' % size + ' GiB'
    if(size >= 1<<20):
        size = size/(1<<20)
        return '%.2f' % size + ' MiB'
    if(size >= 1<<10):
        size = size/(1<<10)
        return '%.2f' % size + ' KiB'
    return '%.2f' % size + ' Bytes'

key = 'J92K8-ZTPH4-O0Y5V'
hash = 'e38c39f82b2650c0ec555c457e07595bb2ce7a02'
url = 'https://vm.umaxhosting.com'

payload = {'key':key,
        'hash':hash,
        'action':'info',
        'bw':'true'}
r = requests.post(url+'/api/client/command.php', data=payload, verify=False)
match = re.match(r'<bw>(\d*),(\d*),(\d*),(\d*)<\/bw>', r.text)

total = int(match.group(1))
used = int(match.group(2))
percent = used/total*100

print('  Data usage for this month: '+humanFileSize(used)+' of '+humanFileSize(total)+' used. ('+'%.3f' %percent+' %)')
