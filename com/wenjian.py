fp = open('filename.txt')
fw = open("out.txt", "w")
for line in fp:
    if not line.startswith("111"):
        fw.write(line)

fp.close()
fw.close()
