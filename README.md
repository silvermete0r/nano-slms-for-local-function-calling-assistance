# Fast Nano SLMs (Fine-Tuning & Optimization)

**Main task:** optimizing inference and memory efficiency for function-calling tasks (fine-tuning) in private/resource-constrained environments.

# Experiments 

| No. | Base model | Description | Technique | Huggingface Link | Training Notebook |
| --- | --- | --- | --- | --- | --- |
| 1 | [Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) | A lightweight function-calling model fine-tuned from `Qwen/Qwen2.5-0.5B-Instruct` on the `Salesforce/xlam-function-calling-60k dataset`. | Method: `LoRA (r=16, alpha=32)` + Target modules: `q_proj, v_proj, k_proj, o_proj` | https://huggingface.co/silvermete0r/qwen2.5-nano-function-master | [notebook](notebooks/SLM_Qwen2_5_0_5B_Fine_Tuning_for_Function_Calling_Tasks.ipynb) | 