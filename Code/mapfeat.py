# -*- coding: utf-8 -*-
#!/usr/bin/python
# 将数据转换为LibSVM格式

def loadfmap( fname ):
    fmap = {}
    nmap = {}

    for l in open( fname ):

        arr = l.split()
        if arr[0].find('.') != -1:
            idx = int( arr[0].strip('.') )
            assert idx not in fmap
            fmap[ idx ] = {}
            ftype = arr[1].strip(':')
            content = arr[2]
        else:

            content = arr[0]
        for it in content.split(','):
            if it.strip() == '':
                continue

            k , v = it.split('=')
            fmap[ idx ][ v ] = len(nmap)
            nmap[ len(nmap) ] = ftype+'='+k
    return fmap, nmap



# start here
fmap, nmap = loadfmap( '../Data/feature_map.txt' )

# 14年数据转换
fo = open( '../Data/Alldata2014.txt', 'w' )
for l in open( '../Data/2014data.raw' ):

    arr = l.split(',')
    if arr[0] == '0':
        fo.write('1')
    else:
        assert arr[0] == '1'
        fo.write('0')
    for i in range( 1,len(arr) ):
        fo.write( ' %d:1' % fmap[i][arr[i].strip()] )
    fo.write('\n')

fo.close()

# 16年数据转换
fo = open( '../Data/Alldata2016.txt', 'w' )
for l in open( '../Data/2016data.raw' ):

    arr = l.split(',')
    if arr[0] == '0':
        fo.write('1')
    else:
        assert arr[0] == '1'
        fo.write('0')
    for i in range( 1,len(arr) ):
        fo.write( ' %d:1' % fmap[i][arr[i].strip()] )
    fo.write('\n')

fo.close()
