import fileinput

#cmd: Python3 binaryToJpeg.py file.txt
contents = ''.join(fileinput.input()) 
bits = ''.join(contents.split())  
 
data = bytes(
    int(bits[i:i+8], 2)
    for i in range(0, len(bits), 8)
)

with open("recovered.jpg", "wb") as f:
    f.write(data)