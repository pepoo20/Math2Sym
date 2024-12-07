# Math2Sym: A System for Solving Elementary Problems via Large Language Models and Symbolic Solvers

This repository contains the official implementation of the paper "Math2Sym: A System for Solving Elementary Problems via Large Language Models and Symbolic Solvers".

## Overview

Math2Sym is a novel system that combines Large Language Models (LLMs) with symbolic solvers to tackle elementary mathematical problems. Our approach achieves state-of-the-art performance across various mathematical problem-solving benchmarks.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Experiments](#experiments)
- [Data](#data)
- [Citation](#citation)

## Installation

```bash
git clone https://github.com/pepoo20/Math2Sym.git
cd Math2Sym
pip install -q -r requirements.txt
```

## Usage

### Pretraining
bash
```
cd LLama_Factory
CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage pt \
    --do_train True \
    --model_name_or_path meta-llama/Meta-Llama-3-8B-Instruct \
    --finetuning_type lora \
    --template empty \
    --dataset_dir data \
    --dataset Pretrain_Basic \
    --cutoff_len 1024 \
    --learning_rate 5e-05 \
    --num_train_epochs 1.0 \
    --max_samples 1000000 \
    --preprocessing_num_workers 16 \
    --per_device_train_batch_size 2 \
    --gradient_accumulation_steps 8 \
    --lr_scheduler_type cosine \
    --max_grad_norm 1.0 \
    --logging_steps 10 \
    --save_steps 1000 \
    --save_total_limit 3 \
    --warmup_steps 500 \
    --optim adamw_8bit \
    --packing True \
    --overwrite_output_dir \
    --output_dir saves/LLama_Symbol_pretrain/ \
    --bf16 True \
    --lora_rank 16 \
    --lora_alpha 16 \
    --lora_dropout 0 \
    --lora_target q_proj,v_proj \
    --val_size 0.02 \
    --evaluation_strategy steps \
    --eval_steps 1000 \
    --per_device_eval_batch_size 2 \
    --load_best_model_at_end True \
    --report_to none \
    --plot_loss True 
```

### Fine-tuning
```bash
cd LLama_Factory
CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage sft \
    --do_train True \
    --model_name_or_path meta-llama/Meta-Llama-3-8B-Instruct \
    --finetuning_type lora \
    --template WordProblemMath \
    --dataset_dir data \
    --dataset Basic_SFT \
    --cutoff_len 1024 \
    --learning_rate 5e-05 \
    --num_train_epochs 2.0 \
    --max_samples 1000000 \
    --preprocessing_num_workers 16 \
    --per_device_train_batch_size 2 \
    --gradient_accumulation_steps 8 \
    --lr_scheduler_type cosine \
    --max_grad_norm 1.0 \
    --logging_steps 10 \
    --save_steps 250 \
    --save_total_limit 2 \
    --warmup_steps 500 \
    --optim adamw_8bit \
    --packing True \
    --overwrite_output_dir \
    --output_dir saves/LLama3.1_Symbol_SFT/ \
    --bf16 True \
    --lora_rank 16 \
    --lora_alpha 16 \
    --lora_dropout 0 \
    --lora_target q_proj,v_proj \
    --val_size 0.02 \
    --evaluation_strategy steps \
    --eval_steps 250 \
    --per_device_eval_batch_size 2 \
    --load_best_model_at_end True \
    --report_to none \
    --plot_loss True 
```


## Benchmark

| Model                                                     | Zero-shot-CoT | Few Shot PaL | Few Shot + Solver | Fine-tuned basic | Fine-tuned advanced |
| --------------------------------------------------------- | ------------- | ------------- | ----------------- | ----------------- | -------------------- |
| [Mistral 7B](https://huggingface.co/deepseek-ai)           | 69            | 113           | 155               | 183               | **210**              |
| [Mistral 8x7B](https://huggingface.co/tiiuae)              | 135           | 145           | 154               | Nan               | Nan                  |
| [Orca 7B](https://huggingface.co/microsoft)                | 25            | 78            | 76                | 133               | **171**              |
| [Qwen 7B](https://huggingface.co/qwen-ai)                  | 116           | 126           | 139               | 170               | **207**              |
| [WizardMath 7B](https://huggingface.co/wizardmath)         | 133           | 135           | 140               | 183               | **217**              |
| [Llama3.1 8B](https://huggingface.co/facebook/llama)       | 156           | 140           | 168               | 197               | **211**              |
| [Qwen 0.5B](https://huggingface.co/qwen-ai)                | 15            | 22            | 7                 | **168**           | 132                  |
| [Qwen 1.8B](https://huggingface.co/qwen-ai)                | 24            | 76            | 52                | **153**           | 136                  |
| [Gemma 2B](https://huggingface.co/gemma-ai)                | 10            | 20            | 39                | 133               | **135**              |
| GPT-neo 350M | 0             | 70            | 36                | **130**           | 120                  |
| [GPT 3.5](https://huggingface.co/openai/gpt-3.5-turbo)     | 172           | 171           | **179**           | Nan               | Nan                  |
| [gpt-4o mini](https://huggingface.co/openai/gpt-4)         | **217**       | 182           | 182               | Nan               | Nan                  |

_Max score: 231_

## Evaluation

### Inference
```bash
cd LLama_Factory
CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage sft \
    --model_name_or_path saves/LLama8b/SFT \
    --finetuning_type full \
    --fp16 True \
    --template  WordProblemMath \
    --dataset_dir data \
    --dataset MathTest \
    --cutoff_len 1024 \
    --max_samples 100000 \
    --per_device_eval_batch_size 2 \
    --predict_with_generate True \
    --max_new_tokens 512 \
    --top_p 0.7 \
    --temperature 0.2 \
    --output_dir solver/evaluate/data/ \
    --do_predict True
```

### Evaluation
```bash
python -m solver.evaluate.evaluation solver/evaluate/data/Wizard.jsonl solver/evaluate/data/test.jsonl

```

## Data

We provide access to our training and evaluation datasets:

| Dataset | Size | Description | Link |
| ------- | ---- | ----------- | ---- |
| Pretrain_Basic | >1M | Pretraining dataset | [Download](https://huggingface.co/datasets/MathSymbol/EMSF) |
| WordProblems_SFT | 150K | Fine-tuning dataset | [Download](https://huggingface.co/datasets/MathSymbol/EMSF) |
| Advance | 79K | Advanced problems dataset | [Download](https://huggingface.co/datasets/MathSymbol/EMSF) |

## Citation

If you find this work useful, please cite our paper:

```bibtex
@inproceedings{
    nguyen2024mathsym,
    title={Math2Sym: A System for Solving Elementary Problems via Large Language Models and Symbolic Solvers},
    author={Minh Phu Nguyen and Minh Phuong Pham and Man Ngo and Kha Tuan Minh},
    booktitle={The 4th Workshop on Mathematical Reasoning and AI at NeurIPS'24},
    year={2024},
    url={https://openreview.net/forum?id=eQrkAPcGRF}
}
```

## License

<!-- [Add your license information here] -->