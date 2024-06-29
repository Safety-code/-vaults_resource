import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display the square of a number", type=int)
args = parser.parse_args()
print(args.square**2)


# #adding optional arguemnt #short options

parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")


#combining positional and optional argument
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display the square of a given number")
parser.add_argument("-v","--verbosity", help="increase output verbosity", action="count", choices=[0,1, 2])
args = parser.parse_args()
answer = args.square**2

if args.verbosity == 2:
    print(f"the square of {args.square} is equal to {answer}")
elif args.verbosity == 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)

#add action=count
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
#parser.add_argument("square", type=int, help="display the square of a given number")
parser.add_argument("-v","--verbosity", action="count", default=0, help="increase output verbosity",)
args = parser.parse_args()
#answer = args.square**2
answer = args.x**args.y

if args.verbosity >= 2:   #bug fix"==" to >="
    #print(f"the square of {args.x} to the power {args.y} is equals to {answer}")
    print(f"Running '{__file__}'")
if args.verbosity >= 1:
    #print(f"{args.x}^{args.y} == {answer}")
    print(f"{args.x}^{args.y} == ", end="")
print(answer)


#adding mutually exclusive group

#combining positional and optional argument
parser = argparse.ArgumentParser("Calculate X raise to the power Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="exponent")
args = parser.parse_args()
answer = args.x ** args.y 

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} is equal to {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")