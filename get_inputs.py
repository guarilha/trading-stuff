from bcb import sgs

cdi = sgs.get({'CDI': 4389}, last=1).values.tolist()[0][0]
ipca = sgs.get({'IPCA': 13522}, last=1).values.tolist()[0][0]
print('CDI: ' + str(cdi) + '%')
print('IPCA: ' + str(ipca) + '%')
