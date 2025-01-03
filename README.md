<h1 align="center">SynthToT</h1>
<h3 align="center">Generate synthetic dataset for your training dataset through deliberate problem-solving</h3>
<hr>

## Table of Content

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
  - [Initial setup](#initial-setup)
  - [Preparing Input Data List](#preparing-input-data-list)
  - [Using Tool](#using-tool)
  - [Creating releases](#creating-releases)
- [Projects using this template](#projects-using-this-template)
- [FAQ](#faq)
- [Contributing](#contributing)


## Introduction

SynthToT is an simple AI agent system powered by [Langchain](https://www.langchain.com/). It is specifically designed to facilitate the automated generation of synthetic datasets, which are crucial for the training of large language models. SynthToT Agent utilize the renowned [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) et al. Shunyu Yao, Dian Yu. Tree-of-Thoughts prompting strategy, *"which generalizes over the popular Chain of Thought approach to prompting language models, and enables exploration over coherent units of text (thoughts) that serve as intermediate steps toward problem solving. ToT allows LMs to perform deliberate decision making by considering multiple different reasoning paths and self-evaluating choices to decide the next course of action, as well as looking ahead or backtracking when necessary to make global choices."*

<hr>

By implementing this strategy, the SynthToT Agent offers a CLI interface for generating JSON dataset outputs using Tree-of-Thoughts (ToT) reasoning applied to the seed input content. This approach provides a distinctive foundation for creating datasets that are ideal for training state-of-the-art language models, adhering to the following JSON schema:

**Output JSON Schema**

```json
[
    {
        "input": "",
        "perfect_consideration": "",
        "number": 10,
        "perspective": "",
        "prompt_template": "",
        "solutions": "",
        "thought_process": "",
        "sorted_solutions": "",
        "data_out": ""
    }
    // N items of seed input list
]
```

**Input JSON Schema**
```json
[
    {
        "input": "",
        "perfect_consideration": "",
        "number": 10,
        "perspective": "",
    },
    // N items of seed input list
]
```

You can view example input_data and output_data from under the `examples` folder.

## Features

### Chaining

- **Initialization:** Customizable parameters such as maximum tokens per response, model type, and sampling temperature.

    - max_tokens: Limits the number of tokens generated per response.
    - model: Specifies the language model to use (default is "gpt-4").
    - temperature: Controls the randomness of the output (default is 0).

- **Template Management:** Utilizes a set of predefined Tree-of-Thoughts templates and corresponding output keys for structured data generation.

- **LLMChain:** Initializes an LLMChain with a specified prompt template and output key, using the selected language model and parameters.

- **Chain Assembly:** Generates a list of LLM chained instances based on the predefined templates and output keys.

## Usage

### Initial setup

**I. Create a new Conda or virtual environment with the Python version 3.10:**

```bash
conda create -n synthtotenv python=3.10.11
```

```bash
conda activate synthtotenv
```

or create virtual environment with venv.

**II. Clone the repository, go into folder, and install requirements:**

Clone from the remote:

```bash
git clone https://github.com/dtunai/SynthToT/
```

Switch to package folder:

```bash
cd SynthToT
```

Install requirements:

```bash
pip install -r setup-requirements.txt
```

Build the package:

```bash
pip install -e .
```

### Preparing Input Data List

Now, you're tasked with creating your input data list. This list will serve as the foundation for generating synthetic output and potential solutions using the Tree-of-Thoughts approach by agents chains. Please take a look at `examples` folder for input data examples.

### Using Tool

After creating your input list, now you can seed the list to the SynthToT via a simple CLI interface:

```bash
python synthtot/synthtot.py \
    --input-file <INPUT_FILE_PATH> \
    --output-file <OUTPUT_FILE_PATH> \
    --prompt-pairs-format <system-user-assistant || instruct>
    --model <OPENAI_MODEL_NAME> \
    --max-tokens <MAX_TOKEN_NUMBER> \
    --temperature <TEMPERATURE_FLOAT>
```

## Contributing

If you find a bug, please open a bug report. If you have an idea for an improvement or new feature :rocket:, please open a [feature request](https://github.com/dtunai/SynthToT/issues/new?assignees=&labels=Feature+request&template=feature_request.md&title=).
