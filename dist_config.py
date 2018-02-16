# -*- coding: utf-8 -*-

# Cython version to cythonize the code.
CYTHON_VERSION = '0.27.3'

# Key-value of sdist build settings.
# See descriptions of WHEEL_LINUX_CONFIGS for details.
# Note that cuDNN and NCCL must be available for sdist.
SDIST_CONFIG = {
    'image': 'kmaehashi/cuda-manylinux1:9.0-cudnn7-devel',
    'nccl': {
        'type': 'v2-tar',
        'files': [
            'nccl_2.1.4-1+cuda9.0_x86_64.txz',
        ],
    },
    'verify_image': 'nvidia/cuda:9.0-cudnn7-devel-{system}',
    'verify_systems': ['ubuntu16.04'],
}

# Key-value of CUDA version and its corresponding build settings.
# Keys of the build settings are as follows:
# - `name`: a package name
# - `image`: a name of the base docker image name used for build
# - `libs`: a list of shared libraries to be bundled in wheel
# - `nccl`: an assets of NCCL library distribution
# - `verify_image`: a name of the base docker image name used for verify
# - `verify_systems`: a list of systems to verify on; expaneded as {system} in
#                     `verify_image`.
WHEEL_LINUX_CONFIGS = {
    '7.0': {
        # Note: NCCL is not available in CUDA 7.0.
        'name': 'cupy-cuda70',
        'image': 'kmaehashi/cuda-manylinux1:7.0-cudnn4-devel',
        'libs': [
            '/usr/local/cuda/lib64/libcudnn.so.4',  # cuDNN v4
        ],
        'nccl': None,
        'verify_image': 'nvidia/cuda:7.0-devel-{system}',
        #'verify_systems': ['ubuntu14.04', 'centos7'],
        'verify_systems': ['ubuntu14.04'],
    },
    '7.5': {
        'name': 'cupy-cuda75',
        'image': 'kmaehashi/cuda-manylinux1:7.5-cudnn6-devel',
        'libs': [
            '/usr/local/cuda/lib64/libcudnn.so.6',  # cuDNN v6
            '/usr/local/cuda/lib64/libnccl.so.1',  # NCCL v1
        ],
        'nccl': {
            'type': 'v1-deb',
            'files': [
                'libnccl1_1.2.3-1.cuda7.5_amd64.deb',
                'libnccl-dev_1.2.3-1.cuda7.5_amd64.deb',
            ],
        },
        'verify_image': 'nvidia/cuda:7.5-devel-{system}',
        #'verify_systems': ['ubuntu14.04', 'centos7', 'centos6'],
        'verify_systems': ['centos7'],
    },
    '8.0': {
        'name': 'cupy-cuda80',
        'image': 'kmaehashi/cuda-manylinux1:8.0-cudnn7-devel',
        'libs': [
            '/usr/local/cuda/lib64/libcudnn.so.7',  # cuDNN v7
            '/usr/local/cuda/lib64/libnccl.so.2',  # NCCL v2
        ],
        'nccl': {
            'type': 'v2-tar',
            'files': [
                'nccl_2.1.4-1+cuda8.0_x86_64.txz',
            ],
        },
        'verify_image': 'nvidia/cuda:8.0-devel-{system}',
        #'verify_systems': ['ubuntu16.04', 'ubuntu14.04', 'centos7', 'centos6'],
        'verify_systems': ['ubuntu14.04'],
    },
    '9.0': {
        'name': 'cupy-cuda90',
        'image': 'kmaehashi/cuda-manylinux1:9.0-cudnn7-devel',
        'libs': [
            '/usr/local/cuda/lib64/libcudnn.so.7',  # cuDNN v7
            '/usr/local/cuda/lib64/libnccl.so.2',  # NCCL v2
        ],
        'nccl': {
            'type': 'v2-tar',
            'files': [
                'nccl_2.1.4-1+cuda9.0_x86_64.txz',
            ],
        },
        'verify_image': 'nvidia/cuda:9.0-devel-{system}',
        #'verify_systems': ['ubuntu16.04', 'centos7', 'centos6'],
        'verify_systems': ['ubuntu16.04'],
    },
}

# Key-value of python version (used in pyenv) to use for build and its
# corresponding configurations.
# Keys of the configuration are as follows:
# - `python_tag`: a CPython implementation tag
# - `linux_abi_tag`: a CPython ABI tag for Linux
# - `requires`: a list of required packages; this is needed as some older
#               NumPy does not support newer Python.
WHEEL_PYTHON_VERSIONS = {
    '2.7.6': {
        'python_tag': 'cp27',
        'linux_abi_tag': 'cp27mu',
        'requires': ['numpy<1.10'],
    },
    '3.4.7': {
        'python_tag': 'cp34',
        'linux_abi_tag': 'cp34m',
        'requires': ['numpy<1.10'],
    },
    '3.5.1': {
        'python_tag': 'cp35',
        'linux_abi_tag': 'cp35m',
        'requires': ['numpy<1.10'],
    },
    '3.6.0': {
        'python_tag': 'cp36',
        'linux_abi_tag': 'cp36m',
        # Use NumPy 1.11.3 for Python 3.6.
        'requires': ['numpy<1.12'],
    },
}

# Python versions available for verification.
VERIFY_PYTHON_VERSIONS = sorted(list(WHEEL_PYTHON_VERSIONS.keys()))

# Sorted list of all possible python versions used in build process.
PYTHON_VERSIONS = sorted(set(
    list(WHEEL_PYTHON_VERSIONS.keys()) +
    VERIFY_PYTHON_VERSIONS
    ))
