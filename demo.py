import json

def get_trainingDataset(json_file):
	if not json_file:
		json_file = './tester_.json'


	with open(json_file, 'r') as f:
		array = json.load(f)

	trainData = []
	for txt in array:
	#	print(txt)
		txtContent = txt['content']
		inx = 0
		if '\t' in txtContent:
			if txtContent.index('\t') < 10:
				inx = txtContent.index('\t') + 1
			content = txtContent[inx:]
			content = content.replace('\t', ' ')

		else:
			content = txtContent

		annot = txt['annotation']
		annotlist=[]
		for an in annot:
			if(len(an['label'])> 1):print('WARNING: Multiple Labels-', an['label'])
			dic = an['points'][0]
			start = dic['start']
			end = dic['end']+1
			ent_ = txtContent[start:end]
			start = start - inx
			end = end - inx
			ent = content[start:end]
			#print('>1>',inx, ent_+'||'+ txtContent)
			#print('>2>',inx, an['label'][0], '||' , ent + '||' + content)
			annotlist.append((start, end,an['label'][0]))
		trainData.append((content,{"entities":annotlist}))
	return trainData

if __name__ == '__main__':
	json_file = './tester.json'
	trainData = get_trainingDataset(json_file)
	for txt in trainData:
		print(txt)


