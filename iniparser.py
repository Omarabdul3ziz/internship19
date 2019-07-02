sample = """

    [general]
    appname = configparser
    version = 0.1

    [author]
    name = xmonader
    email = notxmonader@gmail.com

"""

samplelines = sample.splitlines()

while "" in samplelines : 
    samplelines.remove("")

samplelines2 = []
for i in samplelines:
    j = i.replace(' ','')
    samplelines2.append(j)

section = ""
kv = []
configData = {}
for i in  samplelines2:
    if i[0] == '[':
        if section == '':
            section = i[1:-1]
            continue
        else :
            new_dict = {}
            for j in kv:
                new_dict.update({j.split("=")[0]: j.split("=")[1]})
            
            configData[section] = new_dict
            section = i[1:-1]
            kv =[]
    else :
        kv.append(i)

new_dict = {}
for j in kv:
    new_dict.update({j.split("=")[0]: j.split("=")[1]})

configData[section] = new_dict

#print (configData)
print (configData['general'])
print (configData['general']['appname'])


