import os

# To get a specific variable
cuda_visible_devices = os.getenv('CUDA_VISIBLE_DEVICES')
print(f"CUDA_VISIBLE_DEVICES: {cuda_visible_devices}")

# To print all environment variables
for key, value in os.environ.items():
    print(f"{key}: {value}")
