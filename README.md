![bitcoin logo](https://github.com/bsnjoy/bitcoin_logo_decode/blob/master/bitcoin.jpg)  
Bitcoin logo bitcoin.jpg stored in two transactions:
https://btc.com/ceb1a7fb57ef8b75ac59b56dd859d5cb3ab5c31168aa55eb3819cd5ddbd3d806
https://btc.com/9173744691ac25f3cd94f35d4fc0e0a2b9d1ab17b4fe562acc07660552f95518

logo stored in [yenc format](http://www.yenc.org/yEnc-draft-1.txt) by encoding hex values into addresses

for example first address 16c3ddpaDs9ajhDqhzY7oSPrdHvhR227tP after base58 decoding contains value:  
**=ybegin line=128 siz**

You can check it with:  
**echo "16c3ddpaDs9ajhDqhzY7oSPrdHvhR227tP" | python3 base58.py -d**

**addr.txt** - contain all of the addresses from two above transactions  
**bitcoin.raw** - raw data after base58 decoding of addresses and removing first byte and last 4 digits used for crc.  
**bitcoin.jpg** - decoded image  
**c** - main programm which generates bitcoin.jpg and bitcoin.raw from addr.txt  
**base58.py** - program for base58 encoding from https://github.com/keis/base58/blob/master/base58.py  

Run with python3:  
**python3 main.py**
