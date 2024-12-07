# Dataset Information

The dataset configuration is defined in `dataset_info.json`. Currently, we support the following math-related datasets:

## Available Datasets

### 1. MathTest
json
"MathTest": {
  "file_name": "Math_test.jsonl",
  "columns": {
    "prompt": "Question"
  }
}
```

### 2. Pretrain_Basic
```json
"Pretrain_Basic": {
  "hf_hub_url": "MathSymbol/EMSF",
  "subset": "pretrain",
  "columns": {
    "prompt": "response"
  }
}
```

### 3. Basic_SFT and Advance_SFT
```json
{
  "hf_hub_url": "MathSymbol/EMSF",
  "subset": "[basic|advanced]",
  "columns": {
    "prompt": "question",
    "response": "answer"
  }
}
```

## Dataset Format Details

### For Training Datasets (Basic_SFT and Advance_SFT)
The datasets should follow this format:
```json
[
  {
    "question": "math question here",
    "answer": "solution here"
  }
]
```

### For Pretraining Dataset (Pretrain_Basic)
Only the `prompt` column will be used for training.

### For Testing Dataset (MathTest)
The dataset should be in JSONL format with questions in the specified format:
```json
{
  "Question": "math question here"
}
```

## Usage
You can use these datasets by specifying `--dataset [dataset_name]` where dataset_name can be:
- MathTest
- Pretrain_Basic
- Basic_SFT
- Advance_SFT

All datasets are sourced from the MathSymbol/EMSF repository on Hugging Face hub, except for MathTest which is a local file.
```