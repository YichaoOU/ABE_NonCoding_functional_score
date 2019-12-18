
import pandas as pd
import os
import sys
"""

get gRNA A bed file

"""


df = pd.read_csv("gRNA.all.bed",sep="\t",header=None)
length=1
def row_apply(x):
	chr = x[0]
	gRNA_start = x[1]
	gRNA_end = x[2]
	gRNA = x[3]
	value = x[4]
	strand = x[5]
	output_list = []
	count = -1
	for i in gRNA:
		count += 1
		if i == "A":
			start = count
		else:
			continue
		
		if strand == "-":
			edit_end = gRNA_end-start
			edit_start = gRNA_end-(start+length)
			edit_gRNA_seq = gRNA[start:(start+length)]
		if strand == "+":
			edit_start = gRNA_start+start
			edit_end = gRNA_start+start+length
			edit_gRNA_seq = gRNA[start:(start+length)]
		# output_list.append([chr,edit_start,edit_end,"%s_%s_%s_%s_%s"%(chr,gRNA_start,edit_start,gRNA,strand),value,strand])
		output_list.append([chr,edit_start,edit_end,gRNA,count,strand])
	return output_list		

my_list = df.apply(row_apply,axis=1).tolist()
out_list = []
for x in my_list:
	if x == []:
		continue
	out_list+=x
df = pd.DataFrame(out_list)
print (df.head())
print (df.shape)
df[6] = df[0]+df[1].astype(str)+df[2].astype(str)
# df = df.drop_duplicates(6)
print (df.shape)
df[[0,1,2,3,4,5]].to_csv("gRNA_all_A.bed",sep="\t",header=False,index=False)