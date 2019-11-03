import base58

# addr.txt contains addresses from two transactions:
# https://btc.com/ceb1a7fb57ef8b75ac59b56dd859d5cb3ab5c31168aa55eb3819cd5ddbd3d806
# https://btc.com/9173744691ac25f3cd94f35d4fc0e0a2b9d1ab17b4fe562acc07660552f95518
rawData = b''
f = open('addr.txt')
line = f.readline()
while line:
	addr = base58.b58decode_check(line)
	rawData += addr[1:]
	line = f.readline()

imgData = b''

lines = rawData.split(b'\r\n')[1:]
for line in lines:
	# if line.count == 0:
	# 	break
	if line.find(b'=yend') != -1:
		break
#	http://www.yenc.org/yEnc-draft-1.txt
#    Inner encoding loop
#    -------------------
# So the 'inner loop encoding' is:
# * Fetch the character
# * Add 42
# * Check for NULL, TAB(ascii 9), LF(ascii 10), CR (ascii 13) and '='
# * If one of the critical chars encounters then write '=' as escape
#   character to the output stream followed by the critical+64.
# (NULL -> =@,   TAB --> =I,  LF --> =J,  CR --> =M,  '=' --> =}
	#for c in line.replace(b'=@', b'\x00').replace(b'=I', b'\x09').replace(b'=J', b'\x0a').replace(b'=M', b'\x0d').replace(b'=}', b'='):
	escape = False
	for c in line:
		if c == ord('='):
			escape = True
			continue
		if escape:
			c = c - 64
			escape = False
		imgData += bytes([(256+c-42)%256])

file = open('bitcoin.raw', 'wb')
file.write(rawData)
file.close()

file = open('bitcoin.jpg', 'wb')
file.write(imgData)
file.close()
