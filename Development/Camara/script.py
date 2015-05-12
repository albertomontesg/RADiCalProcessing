
log = open('tmp/tmp.log', 'r')
lines = log.readlines()
ip = lines[-2].split(': ')[1].split('\n')[0]

template = open('template.html', 'r')
lh = template.readlines()
lh[6] = lh[6]%ip

index = open('index.html', 'w')
index.writelines(lh)

log.close()
template.close()
index.close()