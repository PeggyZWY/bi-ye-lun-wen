import numpy as np
import csv
import codecs
import math

def processRawData(dataCsv):
    preStockId = 'xxx'
    nowStockId = 'xxx'
    preVol = 0
    nowVol = 0
    head = True
    prePrice = -1
    nowPrice = -1
    totalVol = 0

    ret = {}
    absLn = []
    dltVol = []
    infoCount = 0

    dataCsv.next()

    for info in dataCsv:
        nowStockId = info[0]
        nowPrice = float(info[2])
        nowVol = float(info[3])
     
        if head or nowStockId != preStockId:
            if head:
                preStockId = info[0]
                prePrice = float(info[2])
                preVol = float(info[3])
            if not head:
                # process dltvol
                for idx in range(len(dltVol)):
                    dltVol[idx] = dltVol[idx] - totalVol / infoCount
                # do OLS
                y = np.array(absLn)
                x = np.array(dltVol)
                A = np.vstack([x,np.ones(len(x))]).T
                m, c = np.linalg.lstsq(A, y)[0]
                kv = 1000000 * m
                # store data to ret with id and kv
                ret[preStockId] = kv
                # clean data
                preStockId = nowStockId
                preVol = nowVol
                prePrice = nowPrice
                absLn = []
                dltVol = []
                totalVol = 0
                infoCount = 0
            head = False
            continue

        if nowPrice - prePrice == 0:
            continue # eliminate this data
        # get useful data item
        absLn.append(math.log(abs(prePrice - nowPrice) / prePrice))
        dltVol.append(nowVol)
        totalVol += nowVol
        infoCount += 1

        # pass current data to prev data 
        preStockId = nowStockId
        preVol = nowVol
        prePrice = nowPrice
    
    # do the last OLS
    # process dltvol
    for v in dltVol:
        v = v - totalVol/infoCount
    # do OLS
    y = np.array(absLn)
    x = np.array(dltVol)
    A = np.vstack([x,np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y)[0]
    kv = 1000000 * m
    # store data to ret with id and kv
    ret[nowStockId] = kv

    return ret



if __name__ == '__main__':   
    dataDir = ['2010', '2011', '2012', '2013', '2014']
    for yr in dataDir:
        dataRaw = codecs.open(yr+'/TRD_Dalyr.csv', 'rb', 'utf-16')
        dataCsv = csv.reader(dataRaw, delimiter = '\t')
        res = processRawData(dataCsv)
        outfile = open(yr+'_kv.txt', 'w')
        for r in sorted(res.keys()):
            outfile.write(r + '\t' + str(res[r]) + '\n')
        dataRaw.close()
        outfile.close()



