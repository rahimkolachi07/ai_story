from main import*
import gradio as gr
pipe=mod()
from PIL import Image

def mod1(prompt1):
    output = pipe(
        prompt=prompt1,
        negative_prompt="bad quality, worse quality, low resolution",
        num_frames=16,
        guidance_scale=2.0,
        num_inference_steps=6,
        generator=torch.Generator("cpu").manual_seed(0),
    )
    frames = output.frames[0]
    export_to_gif(frames, "animatelcm.gif")
    img = Image.open("animatelcm.gif")
    return img
app=gr.Interface(fn=mod1, inputs="text",outputs="image")
app.launch(share=True)

