PRE_SEQ_LEN=128
CHECKPOINT=adgen-chatglm-6b-pt-128-2e-2
STEP=10000

CUDA_VISIBLE_DEVICES=5 python3 main.py \
    --do_predict \
    --test_file RelationExtraction/processed_valid.json \
    --overwrite_cache \
    --prompt_column instruction \
    --response_column output \
    --model_name_or_path THUDM/chatglm-6b \
    --ptuning_checkpoint ./output/$CHECKPOINT/checkpoint-$STEP \
    --output_dir ./output/$CHECKPOINT \
    --overwrite_output_dir \
    --max_source_length 480 \
    --max_target_length 410 \
    --per_device_eval_batch_size 8 \
    --predict_with_generate \
    --pre_seq_len $PRE_SEQ_LEN \
    --quantization_bit 4
