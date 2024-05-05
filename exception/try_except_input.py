temp = "5 degree"
cel = 0
try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('cannot convert')
print(cel)