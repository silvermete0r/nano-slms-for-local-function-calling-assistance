# Fast Nano SLMs (Fine-Tuning & Optimization)

**Main Goal:** Optimizing Inference and Memory Efficiency for Function-calling tasks (fine-tuning) in private/resource-constrained environments.

**Current SOTA Model:** [FunctionGemma 270M by Google DeepMind](https://deepmind.google/models/gemma/functiongemma/) is an open model specialized for function calling at the edge.

## Setup (free)

*All experiments were conducted using freely available and accessible resources, ensuring that experiments will be reproducable without any extra-costs.*

* Hardware: `NVIDIA Tesla T4 (VRAM 16GB)`
* Environment: `Google Colab / Kaggle Notebooks`

## Dataset

[Salesforce/xlam-function-calling-60k dataset](https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k) - 60,000 data collected by APIGen, an automated data generation pipeline designed to produce verifiable high-quality datasets for function-calling applications. 

### Data Splitting

*The dataset was downsampled to 50% to mitigate `out-of-memory issues` and accelerate training and evaluation experiments.*

Data Splitting Notebook: [notebooks/Data_Splitting_Nano_SLMs_Function_Calling_Salesforce.ipynb](notebooks/Data_Splitting_Nano_SLMs_Function_Calling_Salesforce.ipynb)

| Set | Samples |
| ---  | ---     |
| Test | 1,500 (5%) | 
| Validation | 1,500 (5%) | 
| SFT Train | 10,000 (~33%) |
| GRPO Train | 17,000 (~57%) |
| **Total** | 30,000 |

## Nano Function Calling Master SLMs Zoo

Lightweight function-calling models fine-tuned using `LoRA SFT (full-precision) + GRPO (Group Relative Policy Optimization -> deterministic/verifiable rewards)` based on the `Salesforce/xlam-function-calling-60k dataset`

| No. | Base model | Huggingface Link | 
| --- | --- | --- |
| 1 | [Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) | https://huggingface.co/silvermete0r/qwen2.5-nano-function-master | 
| 2 | [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) | *release will be soon..* | 
| 3 | [Qwen/Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B) | *release will be soon..* | 
| 4 | [HuggingFaceTB/SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct) | *release will be soon..* | 
| 5 | [HuggingFaceTB/SmolLM2-135M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct) | *release will be soon..* | 
| 6 | [h2oai/h2o-danube3-500m-chat](https://huggingface.co/h2oai/h2o-danube3-500m-chat) | *release will be soon..* | 
| 7 | [apple/OpenELM-270M-Instruct](https://huggingface.co/apple/OpenELM-270M-Instruct) | *release will be soon..* | 
| 8 | [apple/OpenELM-450M-Instruct](https://huggingface.co/apple/OpenELM-450M-Instruct) | *release will be soon..* | 
| 9 | [google/gemma-3-270m-it](https://huggingface.co/google/gemma-3-270m-it) | *release will be soon..*  |
| 10 | [google/functiongemma-270m-it](https://huggingface.co/google/functiongemma-270m-it) | *release will be soon..*  |


## Experimentations

1. No-Code Fine-tuning web platform for gemma-270m: https://huggingface.co/spaces/google/functiongemma-tuning-lab