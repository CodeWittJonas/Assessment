import task_2 as Task_2


Task_2.dognames_count()
sample_dict = {'Adam': 1}

name_1 = 'Adam'
name_2 = 'Berta'

name_list = [name_1, name_2]

for name in name_list:
    if name in sample_dict:
        continue
    else:
        sample_dict.update({name: len(sample_dict)+1})

print(sample_dict)
