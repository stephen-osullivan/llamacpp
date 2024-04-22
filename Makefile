install:
	pip install --upgrade pip &&\
		CMAKE_ARGS="-DLLAMA_CUDA=on" FORCE_CMAKE=1 pip install --verbose 'llama-cpp-python[server]' &&\
		pip install -r requirements.txt

endpoint:
	python3 -m llama_cpp.server --model models/Meta-Llama-3-8B-Instruct-Q5_K_M.gguf --host 0.0.0.0 --port 8000\
		--n_gpu_layers=30 chat_format chatml

docker_run_remote_image: 
	docker run --rm -it --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -p 8000:8000\
		 -v /home/sos00/projects/llamacpp/models:/models -e MODEL=/models/Meta-Llama-3-8B-Instruct-Q5_K_M.gguf ghcr.io/abetlen/llama-cpp-python:latest

docker build_local_image:
	docker build -t cuda_simple .
docker_run_local_image: 
	docker run --rm -it --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -p 8000:8000\
		 -v /home/sos00/projects/llamacpp/models:/models -e MODEL=/models/Meta-Llama-3-8B-Instruct-Q5_K_M.gguf -t cuda_simple