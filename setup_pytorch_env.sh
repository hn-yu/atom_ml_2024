#!/bin/bash

# 脚本：创建PyTorch环境并设置Jupyter kernel
# 包含：pytorch, ase, asap3, ipykernel
# CUDA版本：12.9

set -e  # 出错时退出

ENV_NAME="pytorch-env"
DISPLAY_NAME="PyTorch Environment (CUDA 12.9)"

echo "🚀 开始创建PyTorch环境..."

# 1. 创建虚拟环境
echo "📦 创建虚拟环境: $ENV_NAME"
uv venv $ENV_NAME --python 3.11

# 2. 激活环境
echo "🔄 激活虚拟环境..."
source $ENV_NAME/bin/activate

# 3. 安装PyTorch (CUDA 12.9)
echo "🔥 安装PyTorch with CUDA 12.9..."
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# 注意：PyTorch官方可能还没有专门的cu129版本，cu124应该与CUDA 12.9兼容
# 如果需要确切的版本，可以检查 https://pytorch.org/get-started/locally/

# 4. 安装ASE (Atomic Simulation Environment)
echo "⚛️  安装ASE..."
uv pip install ase

# 5. 安装ASAP3
echo "🔬 安装ASAP3..."
uv pip install asap3

# 6. 安装Jupyter相关包
echo "📓 安装Jupyter kernel支持..."
uv pip install ipykernel jupyter notebook

# 7. 注册为Jupyter kernel
echo "🔗 注册Jupyter kernel..."
python -m ipykernel install --user --name=$ENV_NAME --display-name="$DISPLAY_NAME"

# 8. 验证安装
echo "✅ 验证安装..."
echo "Python版本:"
python --version

echo "PyTorch版本:"
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}'); print(f'CUDA version: {torch.version.cuda if torch.cuda.is_available() else \"N/A\"}')"

echo "ASE版本:"
python -c "import ase; print(f'ASE: {ase.__version__}')"

echo "ASAP3版本:"
python -c "import asap3; print(f'ASAP3: {asap3.__version__}')"

echo "已安装的Jupyter kernels:"
jupyter kernelspec list

echo ""
echo "🎉 环境设置完成！"
echo "环境名称: $ENV_NAME"
echo "Kernel名称: $DISPLAY_NAME"
echo ""
echo "使用方法:"
echo "1. 激活环境: source $ENV_NAME/bin/activate"
echo "2. 启动Jupyter: jupyter notebook"
echo "3. 在notebook中选择 '$DISPLAY_NAME' kernel"
echo ""
echo "如需删除kernel: jupyter kernelspec uninstall $ENV_NAME"