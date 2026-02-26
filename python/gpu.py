import torch

# Check if CUDA (GPU support) is available
is_cuda = torch.cuda.is_available()

if is_cuda:
    device_name = torch.cuda.get_device_name(0)
    cuda_version = torch.version.cuda
    print(f"Status: GPU detected!")
    print(f"Device: {device_name}")
    print(f"CUDA Version: {cuda_version}")
else:
    print("Status: No GPU found. Running on CPU.")
