# agent_beacon.generator.generator.py


import os
import json
from typing import List, Dict, Any
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from templates.thought_templates import (
    template_step1,
    template_step2,
    template_step3,
    template_step4,
    template_step5,
)

import logging

logging.basicConfig(level=logging.INFO)


class ChainGenerator:
    """Chain step adding class to generate language model chains for processing input data."""

    def __init__(
        self,
        max_tokens: int = 1024,
        model: str = "gpt-3.5-turbo",
        temperature: float = 0,
    ) -> None:
        """
        Initialize the ChainGenerator.

        Args:
            max_tokens (int, optional): Maximum tokens per response. Defaults to 1024.
            model (str, optional): Model to use. Defaults to "gpt-3.5-turbo".
            temperature (float, optional): Sampling temperature. Defaults to 0.
        """
        self.max_tokens = max_tokens
        self.model = model
        self.temperature = temperature
        self.templates = [
            template_step1,
            template_step2,
            template_step3,
            template_step4,
            template_step5,
        ]
        self.output_keys = [
            "solutions",
            "review",
            "thought_process",
            "sorted_solutions",
            "data_out",
        ]

    def create_llm_chain(self, template: str, output_key: str) -> LLMChain:
        """
        Initialize an LLMChain.

        Args:
            template (str): Template for the prompt.
            output_key (str): Key for the output.

        Returns:
            LLMChain: Generated LLMChain.
        """
        return LLMChain(
            llm=ChatOpenAI(
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                model=self.model,
            ),
            prompt=PromptTemplate(input_variables=["input"], template=template),
            output_key=output_key,
        )

    def create_all_chains(self) -> List[LLMChain]:
        """
        Create all LLMChains.

        Returns:
            List[LLMChain]: List of generated LLMChains.
        """
        return [
            self.create_llm_chain(template, output_key)
            for template, output_key in zip(self.templates, self.output_keys)
        ]


def create_sequential_chain(all_chains: List[LLMChain]) -> SequentialChain:
    """
    Create a SequentialChain.

    Args:
        all_chains (List[LLMChain]): List of LLMChains.

    Returns:
        SequentialChain: Generated SequentialChain.
    """
    return SequentialChain(
        chains=all_chains,
        input_variables=[
            "input",
            "perfect_consideration",
            "number",
            "perspective",
            "example",
        ],
        output_variables=[
            "solutions",
            "review",
            "thought_process",
            "sorted_solutions",
            "data_out",
        ],
        verbose=True,
    )


def process_input_data(
    chain: SequentialChain, input_data: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Process input data using the SequentialChain.

    Args:
        chain (SequentialChain): SequentialChain for processing data.
        input_data (List[Dict[str, Any]]): Input data to be processed.

    Returns:
        List[Dict[str, Any]]: Processed output data.
    """
    all_outputs: List[Dict[str, Any]] = []
    for data in input_data:
        try:
            output_data = chain(data)
            all_outputs.append(output_data)
        except Exception as e:
            logging.error(f"Error processing data: {data} - {e}")
    return all_outputs


def append_to_json_file(file_path: str, data: List[Dict[str, Any]]) -> None:
    """
    Append data to a JSON file.

    Args:
        file_path (str): Path to the JSON file.
        data (List[Dict[str, Any]]): Input data to append.
    """
    try:
        if os.path.isfile(file_path):
            with open(file_path, "r") as json_file:
                existing_data = json.load(json_file)
                if isinstance(existing_data, list):
                    existing_data.extend(data)
                else:
                    existing_data = [existing_data] + data
        else:
            existing_data = data

        with open(file_path, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)

        logging.info(f"Results of input data appended to {file_path}.")
    except Exception as e:
        logging.error(f"Error appending data to file: {file_path} - {e}")


def load_input_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Load input data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[Dict[str, Any]]: Loaded input data.
    """
    try:
        with open(file_path, "r") as json_file:
            input_data = json.load(json_file)
            if not isinstance(input_data, list):
                raise ValueError("Input data should be a list of dictionaries.")
            return input_data
    except Exception as e:
        logging.error(f"Error loading input data from file: {file_path} - {e}")
        return []


def entrypoint(
    input_data_file,
    output_file,
    model="gpt-3.5-turbo",
    max_tokens=1024,
    temperature=0.7,
) -> None:
    """
    Main entry point for processing input data.

    Args:
        input_data_file: Path to the input data file.
        output_file: Path to the output file.
        model (str, optional): Model to use. Defaults to "gpt-3.5-turbo".
        max_tokens (int, optional): Maximum tokens per response. Defaults to 1024.
        temperature (float, optional): Sampling temperature. Defaults to 0.7.
    """
    input_data = load_input_data(input_data_file)
    if not input_data:
        logging.error("No valid input data found. Exiting.")
        return

    chain_creator = ChainGenerator(
        max_tokens=max_tokens, model=model, temperature=temperature
    )
    all_chains = chain_creator.create_all_chains()
    overall_chain = create_sequential_chain(all_chains)
    all_outputs = process_input_data(overall_chain, input_data)
    append_to_json_file(output_file, all_outputs)
