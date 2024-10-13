## Table of Contents

- [Install](#install)
- [Benchmark](#benchmark)
- [Data](#data)

## Install
```bash
git clone https://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@github.com/pepoo20/Symbol-Math.git
cd Symbol-Math
ls
pip install -q .
```

## Reproduce

### Pretrain
```bash
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
    --plot_loss True 
```

### SFT
```bash
CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage sft \
    --do_train True \
    --model_name_or_path meta-llama/Meta-Llama-3-8B-Instruct \
    --finetuning_type lora \
    --template WordProblemMath \
    --dataset_dir data \
    --dataset WordProblems_SFT \
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
    --plot_loss True 
```


## Data

| Dataset | Size | Link |
| ------- | ---- | ---- |
| Pretrain_Basic | >1M  | [Download](https://huggingface.co/datasets/MathSymbol/EMSF)
| WordProblems_SFT | 150K | [Download](https://huggingface.co/datasets/MathSymbol/EMSF)
| Advance | 79K | [Download](https://huggingface.co/datasets/MathSymbol/EMSF) |



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

### Predict
```bash
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

### Evaluate
```bash
python -m solver.evaluate.evaluation solver/evaluate/data/Wizard.jsonl solver/evaluate/data/test.jsonl

```
<!-- 
## Requirement

| Mandatory    | Minimum | Recommend |
| ------------ | ------- | --------- |
| python       | 3.8     | 3.10      |
| torch        | 1.13.1  | 2.2.0     |
| transformers | 4.37.2  | 4.39.3    |
| datasets     | 2.14.3  | 2.18.0    |
| accelerate   | 0.27.2  | 0.28.0    |
| peft         | 0.9.0   | 0.10.0    |
| trl          | 0.8.1   | 0.8.1     |

| Optional     | Minimum | Recommend |
| ------------ | ------- | --------- |
| CUDA         | 11.6    | 12.2      |
| deepspeed    | 0.10.0  | 0.14.0    |
| bitsandbytes | 0.39.0  | 0.43.0    |
| flash-attn   | 2.3.0   | 2.5.6     | -->

