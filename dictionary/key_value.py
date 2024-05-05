counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for ke in counts:
    print(counts[ke]) # 1 42 100
    if counts[ke] > 10:
        print(ke, counts[ke]) # annie 43 
                              # jan 100