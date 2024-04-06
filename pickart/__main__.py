from pathlib import Path

from argparse import ArgumentParser

from pickart.converter import convert_to_pickart
from pickart.converter import convert_to_png

parser = ArgumentParser()

parser.add_argument("-i", default="input", help="Input folder(default 'input')")
parser.add_argument(
    "-o",
    default="output",
    help="Output folder(default 'output'). If folder does not exist it will be created.",
)
parser.add_argument(
    "-m",
    choices=("to_pickart", "to_png"),
    default="to_pickart",
    help="Convertion mode(default 'to_pickart'). Note: mode 'to_pickart' converts only .png images.",
)

args = parser.parse_args()


def main():
    input_dir: Path = Path(args.i)
    output_dir: Path = Path(args.o)

    if not input_dir.is_dir():
        print(f"'{input_dir}' folder does not exist.")
        return

    if args.m == "to_pickart":
        for filename in input_dir.glob("*.png"):
            print(f"Converting '{filename}' to pickart")
            convert_to_pickart(filename, output_dir)
    elif args.m == "to_png":
        for filename in input_dir.glob("*.pickart"):
            print(f"Converting '{filename}' to png")
            convert_to_png(filename, output_dir)


main()
