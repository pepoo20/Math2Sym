# Example usage:
# python merge_peft.py --base_model=meta-llama/Llama-2-7b-hf --peft_model=./qlora-out --output_dir=alpaca-qlora

from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_model", type=str)
    parser.add_argument("--peft_model", type=str)
    parser.add_argument("--output_dir", type=str)

    return parser.parse_args()

def main():
    args = get_args()

    print(f"[1/4] Loading base model: {args.base_model}")
    base_model = AutoModelForCausalLM.from_pretrained(
        args.base_model,
        return_dict=True,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    tokenizer = AutoTokenizer.from_pretrained(args.base_model)

    print(f"[2/4] Loading adapter: {args.peft_model}")
    model = PeftModel.from_pretrained(base_model, args.peft_model, device_map="auto")
    
    print("[3/4] Merge base model and adapter")
    model = model.merge_and_unload()
    
    print(f"[4/4] Saving model and tokenizer in {args.output_dir}")
    model.save_pretrained(f"{args.output_dir}")
    tokenizer.save_pretrained(f"{args.output_dir}")

if __name__ == "__main__" :
    main()