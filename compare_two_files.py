import argparse

parser=argparse.ArgumentParser(
    description="Enter two file names"
)
parser.add_argument("file1", help="First input file")
parser.add_argument("file2", help="Seond input file")

args = parser.parse_args()

with open(args.file1) as f1, open(args.file2) as f2:
    list_1=[line.rstrip("\n") for line in f1 ]
    list_2=[line.rstrip("\n") for line in f2 ]

set_1=(set(list_1))
set_2=(set(list_2))

common_data=set_1.intersection(set_2)

print(common_data)
