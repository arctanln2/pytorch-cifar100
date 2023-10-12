export CUDA_VISIBLE_DEVICES=4,5
export CUDA_MPS_PIPE_DIRECTORY=/tmp/nvidia-mps-10
export CUDA_MPS_LOG_DIRECTORY=/tmp/nvidia-log-10
nvidia-cuda-mps-control -d

# CUDA_VISIBLE_DEVICES=4,5
# python train.py -net vgg16 -gpu