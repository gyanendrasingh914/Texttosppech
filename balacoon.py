import gradio as gr
from balacoon_tts import TTS
from huggingface_hub import hf_hub_download
addon_path = hf_hub_download(repo_id="balacoon/tts", filename = "en_us_cmuartic_jets_cpu.addon")


tts = TTS(addon_path)

def alpha(text):
    samples = tts.synthesize(text,tts.get_speakers()[9])
    # samples
    return gr.Audio(value = (tts.get_sampling_rate(),samples))


dem = gr.Interface(fn = alpha,inputs = 'text',outputs = 'audio')
dem.launch()