# synthtot.synthtot.py

import os
import argparse
import logging
from generator.generator import entrypoint
from templates.thought_templates import system_user_assistant, instruct


def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up argument parser
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
        default="output_data.json",
        help="Output File Path for Synthetic Generated Pairs",
    )
    parser.add_argument(
        "--prompt-template",
        required=True,
        default="system-user-assistant",
        help="Prompt Pairs Data Format",
    )
    parser.add_argument(
        "--model",
        default="gpt-4",
        help="Model name (default: gpt-4)",
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

    if args.prompt_template == "system-user-assistant":
        prompt_template = system_user_assistant
    else:
        prompt_template = instruct

    # Call the entry point function with the parsed arguments
    entrypoint(
        args.input_file,
        args.output_file,
        prompt_template,
        args.model,
        args.max_tokens,
        args.temperature,
    )


if __name__ == "__main__":
    main()
