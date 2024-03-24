from main import*
pipe=mod()
from PIL import Image


output = pipe(
    prompt="flaying car above the water",
    negative_prompt="bad quality, worse quality, low resolution",
    num_frames=16,
    guidance_scale=2.0,
    num_inference_steps=6,
    generator=torch.Generator("cpu").manual_seed(0),
)
frames = output.frames[0]
export_to_gif(frames, "animatelcm.gif")
