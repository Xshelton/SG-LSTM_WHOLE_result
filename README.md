# SG-LSTM_WHOLE_result
## How to run it .
### first one of the most important file should be downloaded first:
- link：https://pan.baidu.com/s/1XImsWAx5CIa2CvEty6oBKw 
- password:16aa
### without LSTM_score19487522.npy no scores would be coming out 

then put the LSTM_score19487522.npy into the same folder of other files.

### ** 1-topN read.py** 
- by changing the I_wanna_top=100# from 100 into N, you can achieve top N pairs for SG-LSTM-WHOLE
- because it has to search 14,000,000pairs, so please be patient in waiting the procedure.

### ** 2 score for one pair.py**
-- by changing the mirna='hsa-miR-6794-5p'	/ gene='GNL2' pair name ,you can get the score of this pair.

top ten predicted by it for your reference:

	1&GNL2&	hsa-miR-4769-3p&	41.50028992\\
	2&GNL2&	hsa-miR-6794-5p&	41.22437286\\
	3&GNL2&	hsa-miR-1283&	41.06597137\\
	4&GNL2&	hsa-miR-98-3p	&40.94686508\\
	5&GNL2	&hsa-miR-656-3p&	40.8991127\\
	6&GNL2&	hsa-miR-7109-5p&	40.72394562\\
	7&GNL2&	hsa-miR-520a-5p&	40.49018097\\
	8&GNL2&	hsa-miR-2113&	40.43338013\\
	9&SULT2B1&	hsa-miR-7152-5p&	40.04142761\\
	10&ADRM1&	hsa-miR-2114-3p&	39.85257721\\
