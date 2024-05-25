<p align="center">
    <img src="./assets/original-31669f20cced100c1e16a68a6974b8b4.jpg" width="500"/>
</p>
<h1 align="center">SynthToT</h1>
<h3 align="center">Generate a synthetic dataset for your data through deliberate problem-solving</h3>
<h6 align="center"><a href="https://discord.gg/5TesGau62q">Join Mathematics & AI Institute Discord!</a></h6>

<hr>

## Table of Content

- [Introduction](#introduction)
- [Features](#features)
- [Enterprise Grid](#enterprise-grid)
- [Usage](#usage)
  - [Initial setup](#initial-setup)
  - [Preparing Input Data List](#preparing-input-data-list)
  - [Using Tool](#using-tool)
  - [Creating releases](#creating-releases)
- [Projects using this template](#projects-using-this-template)
- [FAQ](#faq)
- [Contributing](#contributing)


## Introduction

SynthToT is an simple AI agent system powered by [Langchain](https://www.langchain.com/). SynthToT agent developed by [Mathematics and AI Institute.](https://www.matyz.org/en/) It is specifically designed to facilitate the automated generation of synthetic datasets, which are crucial for the training of large language models. SynthToT Agent utilize the renowned [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) et al. Shunyu Yao, Dian Yu. Tree-of-Thoughts prompting strategy, *"which generalizes over the popular Chain of Thought approach to prompting language models, and enables exploration over coherent units of text (thoughts) that serve as intermediate steps toward problem solving. ToT allows LMs to perform deliberate decision making by considering multiple different reasoning paths and self-evaluating choices to decide the next course of action, as well as looking ahead or backtracking when necessary to make global choices."*

<hr>

> ### About Mathematics & AI Institute
> At the Math and AI Institute, our mission is to bring state-of-the-art research at the intersection of AI and mathematics. We specialize in generative AI technologies, leveraging their potential to empower industries with innovative projects. Generative AI, a cutting-edge field, enables the creation of diverse content, including text, images, and videos, while adapting seamlessly to new data. While we acknowledge the potential risks associated with the rapid evolution of Generative AI, our team is dedicated to ensuring the safety and interpretability of these tools. Our core areas of focus include AI Safety, Industry Integration, Fundamental Research, and Tailored AI Training for various sectors. 

> For more information about us, please check out website at [matyz.org/en](https://matyz.org/en)

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

## Enterprise Grid

At Mathematics and AI Institute, we're proud to offer the enterprise edition of SynthToT, tailored specifically for enterprise users. SynthToT Enterprise Edition provides advanced features designed to deliver a streamlined, scalable, and production-grade system synthetic data generation agent for your organization's needs. With SynthToT Enterprise, you can meet the demands of large-scale data products and enable a complex synthetic dataset generation system for safety-critical applications.

- Autotransformers: Integrate autotransformers for automated data transformation, enabling efficient and seamless preprocessing of input data for synthetic dataset generation.

- User Interface (UI): Access SynthToT Enterprise Edition through an intuitive user interface, providing a user-friendly experience for configuring settings, monitoring processes, and accessing generated datasets.

- Scalability: Scale SynthToT Enterprise Edition effortlessly to accommodate growing datasets and increased computational demands, ensuring seamless performance under heavy workloads.

- Integration Capabilities: Integrate SynthToT Enterprise Edition seamlessly with existing event-driven data processing systems, and MLOps pipelines for enhanced interoperability and continous data flow.

- Automated Quality Assurance: Utilize automated quality assurance mechanisms to ensure the accuracy, consistency, and reliability of generated synthetic datasets, reducing manual intervention and error rates.

- Plugable Thought Templates: Customize the synthetic data generation process by plugging in thought templates, allowing users to define and utilize their own templates tailored to specific use cases and domains.

### Get Started with SynthToT Enterprise Edition

To get started with SynthToT Enterprise Edition, [contact our team](mailto:info@matyz.org) for a demo or trial.

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

### Creating releases

Creating new GitHub and PyPI releases is easy. The GitHub Actions workflow that comes with this repository will handle all of that for you. All you need to do is follow the instructions in [RELEASE_PROCESS.md](./RELEASE_PROCESS.md).

## Projects using this template

Here is an incomplete list of some projects that started off with this template:

- [ai2-tango](https://github.com/allenai/tango)
- [cached-path](https://github.com/allenai/cached_path)
- [beaker-py](https://github.com/allenai/beaker-py)
- [gantry](https://github.com/allenai/beaker-gantry)
- [ip-bot](https://github.com/abe-101/ip-bot)

☝️ *Want your work featured here? Just open a pull request that adds the link.*

## FAQ

#### Should I use this template even if I don't want to publish my package?

Absolutely! If you don't want to publish your package, just delete the `docs/` directory and the `release` job in [`.github/workflows/main.yml`](https://github.com/dtunai/SynthToT/blob/main/.github/workflows/main.yml).

## Contributing

If you find a bug, please open a bug report. If you have an idea for an improvement or new feature :rocket:, please open a [feature request](https://github.com/dtunai/SynthToT/issues/new?assignees=&labels=Feature+request&template=feature_request.md&title=).
