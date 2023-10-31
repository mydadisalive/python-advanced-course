import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description='A script that does something.')

# Add command-line arguments
parser.add_argument('--input', type=str, help='Input file')
parser.add_argument('--output', type=str, help='Output file')

# Parse the command-line arguments
args = parser.parse_args()

# Access the arguments
input_file = args.input
output_file = args.output
