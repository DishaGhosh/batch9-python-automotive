capital = {'USA':'waashington DC',
           'India':'new delhi',
           'china': 'beijing',
           'russia': 'moscow'}


print(capital['russia'])
print(capital.get('germany'))
print(capital.keys())
print(capital.values())
print(capital.items())

cap = capital.update({'germany': 'beijing'})
print(cap)
c = capital.update({'USA':'las vegas'})
print(c)
capital.pop('china')
capital.clear()

for key,value in capital.items():
    print(key,value)