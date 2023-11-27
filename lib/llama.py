from transformers import AutoTokenizer, AutoModelForCausalLM, TextIteratorStreamer
import torch
from threading import Thread

# based on https://huggingface.co/spaces/huggingface-projects/llama-2-7b-chat/blob/main/app.py

MODEL_ID = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
tokenizer.use_default_system_prompt = False
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
)

def generate(system_content, user_content, temp_value=1, max_tokens_value=256, top_p_value=1):
    conversation = []
    conversation.append({"role": "system", "content": system_content})
    conversation.append({"role": "user", "content": user_content})

    input_ids = tokenizer.apply_chat_template(conversation, return_tensors="pt")

    # streamer = TextIteratorStreamer(tokenizer, timeout=30.0, skip_prompt=True, skip_special_tokens=True)
    # generate_kwargs = dict(
    #     {"input_ids": input_ids},
    #     streamer=streamer,
    #     max_new_tokens=1024,
    #     do_sample=True,
    #     top_p=0.9,
    #     top_k=50,
    #     temperature=0.6,
    #     num_beams=1,
    #     repetition_penalty=1.2,
    # )
    # t = Thread(target=model.generate, kwargs=generate_kwargs)
    # t.start()

    # print("start streamining")
    # outputs = []
    # for text in streamer:
    #     outputs.append(text)
    #     print("".join(outputs))
    # print("end streamining")

    # output_str = "".join(outputs)

    outputs = model.generate(
        input_ids,
        max_new_tokens=int(max_tokens_value),
    )
    output_str = tokenizer.decode(outputs[0])

    print("user_content: ", user_content)
    print("response: ", output_str)
    print("end response")

    return output_str
