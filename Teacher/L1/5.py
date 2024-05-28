map = {ord('з'): 'z', ord('ю'): 'u'}

translated = 'привітзю'.translate(map)

print(translated) # zu