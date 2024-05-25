import os
import argparse

from generator.generator import entrypoint

parser = argparse.ArgumentParser(
    description="Generate synthetic training data with your input data by deliberate problem solving."
)
parser.add_argument(
    "--input-file",
    required=True,
    default="input_data.json",
    help="Input Data File Path",
)
parser.add_argument(
    "--output-file",
    required=True,
    default="results.json",
    help="Output File Path for Generated Content",
)
parser.add_argument(
    "--model",
    default="gpt-3.5-turbo",
    help="Model name (default: gpt-3.5-turbo)",
)
parser.add_argument(
    "--max-tokens",
    type=int,
    default=1024,
    help="Max tokens for generation (default: 1024)",
)
parser.add_argument(
    "--temperature",
    type=float,
    default=0.7,
    help="Temperature for generation (default: 0.7)",
)
args = parser.parse_args()

entrypoint(args.input_file, args.output_file, args.model, args.max_tokens, args.temperature)
