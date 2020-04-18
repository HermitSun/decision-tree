# map string to number
# age = {
#     'young': 0,
#     'pre': 1,
#     'presbyopic': 2
# }
# prescript = {
#     'myope': 0,
#     'hyper': 1
# }
# astigmatic = {
#     'no': 0,
#     'yes': 1
# }
# tearRate = {
#     'reduced': 0,
#     'normal': 1
# }
# glass_type = {
#     'hard': 0,
#     'soft': 1,
#     'no lenses': 2
# }

# export variables
dataset = []
labels = ['age', 'prescript', 'astigmatic', 'tearRate']

# read and convert
file = open('./lenses.txt')
src = file.read().splitlines()
for line in src:
    split = line.split('\t')
    dataset.append([
        split[0],
        split[1],
        split[2],
        split[3],
        split[4]  # glass type
    ])
file.close()
