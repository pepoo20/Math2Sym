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
pip install -q galore-torch wandb tiktoken datasets==2.17.1 flash-attn
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
    --flash_attn True \
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
    --report_to wandb \
    --overwrite_output_dir \
    --output_dir saves/LLaMA3-8B-Chat/lora/ \
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
Merge Lora with model
```bash
python src/merge_peft.py --base_model=meta-llama/Llama-2-7b-hf --peft_model=save/qlora-out --output_dir=qlora-merge
```
## Dat
### SFT
```bash
CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage sft \
    --do_train True \
    --model_name_or_path meta-llama/Meta-Llama-3-8B-Instruct \
    --finetuning_type lora \
    --template llama3_Math \
    --flash_attn True \
    --dataset_dir data \
    --dataset WordProblem_SFT_LLama \
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
    --report_to wandb \
    --overwrite_output_dir \
    --output_dir saves/LLaMA3-8B-Chat/lora_template/ \
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

<details>
For other models not llama3, change the `--template` to the corresponding template name.
Pretrain:  
- empty
SFT:  
- WordProblemMath

</details>

a
### Pretrain

| Dataset | Size | Description | Link |
| ------- | ---- | ----------- | ---- |
| Pretrain_Basic | 1M | Basic text data | [Download](https://huggingface.co/datasets/MathSymbol/SymbolBasic_1M_v1)

### SFT

| Dataset | Size | Description | Link |
| ------- | ---- | ----------- | ---- |
| WordProblems_SFT | 150K | Math word problems | [Download](https://huggingface.co/datasets/MathSymbol/Symbol_WordProblem)

## Benchmark

| Model                                                    | Trained                  | Zero shot    | 5 shot example  |
| -------------------------------------------------------- | --------------------------- | ----------------- | --------- |
| [Qwen1.5-0.5B](https://huggingface.co/baichuan-inc)         | 73/92                      |             |  |
| [Qwen1.5-1.8B](https://huggingface.co/bigscience)               | 61/92 |    | -         |
| [Gemma-2B](https://huggingface.co/bigscience)              | 55/92 |    | -         |
| [Llama3-8b](https://huggingface.co/THUDM)                 |                           |    |   |
| [Gemma-7b](https://huggingface.co/CohereForAI)          |                     | 0.29     | 0.15    |
| [Mistral-7b](https://huggingface.co/deepseek-ai)     |                   | 0.3     | 0.5  |
| [Mistral-8x7b](https://huggingface.co/tiiuae)                  |                  | 0.6   | 0.62    |
| [Gpt-3.5](https://huggingface.co/google)         |    |   0.75     | 0.87  

## Evaluation

### Predict
```bash
CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage sft \
    --model_name_or_path saves/LLama8b/SFT \
    --finetuning_type full \
    --fp16 True \
    --template  llama3_Math \
    --flash_attn True \
    --dataset_dir data \
    --dataset MathTest \
    --cutoff_len 1024 \
    --max_samples 100000 \
    --per_device_eval_batch_size 2 \
    --predict_with_generate True \
    --max_new_tokens 512 \
    --top_p 0.7 \
    --temperature 0.2 \
    --output_dir evals/LLama3-8b/ \
    --do_predict True
```

### Evaluate
```bash
python src/evaluation.py evals/LLama3-8b/generated_predictions.jsonl  data/Math_test.jsonl
```

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
| flash-attn   | 2.3.0   | 2.5.6     |

