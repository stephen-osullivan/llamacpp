from huggingface_hub import hf_hub_download
hf_hub_download(
    repo_id="NousResearch/Meta-Llama-3-8B-Instruct-GGUF",
    local_dir="models",
    local_dir_use_symlinks=False,
    filename = "Meta-Llama-3-8B-Instruct-Q5_K_M.gguf")