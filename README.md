# bi-ye-lun-wen  
  
##  说明  
### "01\_from3049to1086/" 文件夹  
数据从最开始的3049家公司不断地筛选、分析和清除，最后到达1086家。细分过程如下：  
1. 1427到1104是剔除了高管缺失的公司  
2. 1104到1087是剔除了没有连续5年都有KV值的公司。这其中包含了一个Python程序来处理KV值  
3. 1087到1086是剔除了600699这支股票，因为它在2010年缺年报  

### "02\_analysing1086/" 文件夹  
它包括四个文件夹：  
1. 01\_statistical\_description （描述性统计）  
2. 02\_collinearity\_analysis （相关性分析）  
3. 03\_linear\_regression\_analysis （线性回归分析）  
4. 04\_robust\_analysis （稳健性分析）  

### "03\_back\_test/" 文件夹  
这是策略回测的过程，包含了筛选数据和一个Python小程序。  
  
### "04_others/" 文件夹  
这是在写论文的其他部分（绪论，文献综述，研究设计等）时，为了作图和制表的数据及过程。