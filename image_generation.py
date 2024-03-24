import torch
from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained(
    "cagliostrolab/animagine-xl-3.1", 
    torch_dtype=torch.float16, 
    use_safetensors=True, 
)
pipe.to('cuda')

prompt = "1girl, souryuu asuka langley, neon genesis evangelion, solo, upper body, v, smile, looking at viewer, outdoors, night"
negative_prompt = "nsfw, lowres, (bad), text, error, fewer, extra, missing, worst quality, jpeg artifacts, low quality, watermark, unfinished, displeasing, oldest, early, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract]"

image = pipe(
    prompt, 
    negative_prompt=negative_prompt,
    width=832,
    height=1216, 
    guidance_scale=7,
    num_inference_steps=28
).images[0]

image.save("./asuka_test.png")
