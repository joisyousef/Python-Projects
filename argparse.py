import argparse

parser = argparse.ArgumentParser(description="Example Python CLI")

parser.add_argument("hacker_name",help="enter the hacker name",type=str)
parser.add_argument("hacker_power",help="enter the hacker power",type=int)

parser.add_argument("-bh","--blackhat",default=False,action="store_true")
parser.add_argument("-wh","--whitehat",default=True,action="store_true")

parser.add_argument("-ht","--hackertype",choices=["whitehat","blackhat","greyhat"])

args = parser.parse_args()
print(args)