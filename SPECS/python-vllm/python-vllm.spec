# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global flavor @BUILD_FLAVOR@%{nil}

%global srcname vllm

%global onednn_ver 3.10

%global llvm_maj_ver 22

%if "%{flavor}" == "rocm"
%bcond rocm 1
%else
%bcond rocm 0
%endif

%if %{with rocm}
%global toolchain clang
%endif

%if %{with rocm}
Name:           python-%{srcname}-rocm
%else
Name:           python-%{srcname}
%endif
Version:        0.27.1
Release:        %autorelease
Summary:        A high-throughput and memory-efficient inference and serving engine for LLMs
License:        Apache-2.0
URL:            https://github.com/vllm-project/vllm
#!RemoteAsset:  sha256:eec2d54d137ac1e59cb4c39226dfee1943eefc8f4788f5821d7300d6acbdb646
Source0:        https://files.pythonhosted.org/packages/source/v/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:ba5834a1fdbb6d1c1b1c065dfd789438e7aa42c03fc52d92c02af85d78d1c75c
Source1:        https://github.com/uxlfoundation/oneDNN/archive/refs/tags/v%{onednn_ver}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(jinja2)
BuildRequires:  libomp
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  python3dist(numpy)

%if %{with rocm}
BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  clang%{llvm_maj_ver}-tools-extra
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hipblas)
BuildRequires:  cmake(hipblaslt)
BuildRequires:  cmake(hipcub)
BuildRequires:  cmake(hipfft)
BuildRequires:  cmake(hiprand)
BuildRequires:  cmake(hipsparse)
BuildRequires:  cmake(hipsparselt)
BuildRequires:  cmake(hipsolver)
BuildRequires:  cmake(miopen)
BuildRequires:  cmake(rocblas)
BuildRequires:  cmake(rocrand)
BuildRequires:  cmake(rocfft)
BuildRequires:  cmake(rccl)
BuildRequires:  cmake(rocprim)
BuildRequires:  cmake(rocsolver)
BuildRequires:  cmake(rocthrust)
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(rocm-core)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(rocm_smi)
BuildRequires:  compiler-rt(major) = %{llvm_maj_ver}
BuildRequires:  hipcc
BuildRequires:  libstdc++-devel
BuildRequires:  lld(major) = %{llvm_maj_ver}
BuildRequires:  llvm(major) = %{llvm_maj_ver}
BuildRequires:  python-torch-rocm-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-device-libs
BuildRequires:  rocm-llvm-macros
BuildRequires:  rocminfo
BuildRequires:  roctracer-devel
%else
BuildRequires:  cmake(sleef)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(numa)
BuildRequires:  python-torch-devel
%endif

Requires:       ninja
Requires:       python3dist(uvloop)
%if %{with rocm}
Requires:       python-torch-rocm
Requires:       python3dist(triton)
Requires:       amdsmi
%else
Requires:       python3dist(torch)
%endif

%if %{with rocm}
Provides:       vllm-rocm = %{version}-%{release}
Conflicts:      python-%{srcname}
%else
Provides:       python-%{srcname} = %{version}-%{release}
Provides:       vllm = %{version}-%{release}
Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}
Conflicts:      python-%{srcname}-rocm
%endif

%patchlist
# https://github.com/vllm-project/vllm/pull/51099
1000-riscv-fp32vec-copy-ctors-non-explicit.patch
%if %{with rocm}
# https://github.com/vllm-project/vllm/pull/45916
1001-ROCm-split-KV-paged-decode.patch
%endif
2001-Adjust-dependencies-for-openRuyi.patch
# Allow single-process execution when PyTorch lacks the Gloo backend
2002-CPU-single-process-fake-distributed-backend.patch
%if %{with rocm}
# Define roc::hipsparselt before importing Torch's CMake targets
2003-ROCm-hipsparselt-ordering.patch
# Build cumem_allocator with ROCm HIP
2004-cumem_allocator-define-USE_ROCM-for-CXX-target.patch
# triton_kernels is an optional feature which git-clones code via network
2005-Skip-triton_kernels-bundling-via-env.patch
%else
# Adjust CPU backend for openRuyi's OpenMP path
2006-CPU-backend-OpenMP-path.patch
%endif

%description
vLLM is a fast and easy-to-use library for LLM inference and serving, featuring
PagedAttention for efficient management of attention key/value memory,
continuous batching of incoming requests, and an OpenAI-compatible API server.

%prep -a
%if %{without rocm}
# OneDNN is used for CPU backend
tar -xzf %{SOURCE1}
%endif

%generate_buildrequires
%if %{with rocm}
export VLLM_VERSION_OVERRIDE=%{version}+rocm
export VLLM_TARGET_DEVICE=rocm
%else
export VLLM_VERSION_OVERRIDE=%{version}+cpu
export VLLM_TARGET_DEVICE=cpu
%endif
%pyproject_buildrequires -R

%build -p
%if %{with rocm}
export VLLM_VERSION_OVERRIDE=%{version}+rocm
export VLLM_TARGET_DEVICE=rocm
export PYTORCH_ROCM_ARCH=%{rocm_gpu_list_default}
export ROCM_HOME=%{_prefix}
export PATH=%{rocmllvm_bindir}:$PATH
export HIP_CLANG_PATH=%{rocmllvm_bindir}
# Do not bundle triton_kernels into vllm/third_party
export VLLM_SKIP_TRITON_KERNELS=1
export CMAKE_ARGS="-DCMAKE_HIP_FLAGS=--rocm-device-lib-path=$(%{rocmllvm_bindir}/clang -print-resource-dir)/amdgcn/bitcode"
%else
export VLLM_VERSION_OVERRIDE=%{version}+cpu
export VLLM_TARGET_DEVICE=cpu
export FETCHCONTENT_SOURCE_DIR_ONEDNN="$PWD/oneDNN-%{onednn_ver}"
# RISC-V CPU: cpu_extension.cmake auto-detects the RVV vector length from /proc/cpuinfo
# SG2044 has VLEN=128
%ifarch riscv64
export CMAKE_ARGS="-DVLLM_RVV_VLEN=128"
%endif
%endif
export CMAKE_BUILD_TYPE=Release

# Limit parallelism by available memory to avoid builder OOM.
mem_gb=$(awk '/MemTotal/ {print int($2/1024/1024)}' /proc/meminfo)
compile_jobs=$(nproc)
mem_jobs=$(( 1 + mem_gb / 3 ))
[ "$mem_jobs" -lt "$compile_jobs" ] && compile_jobs=$mem_jobs
[ "$compile_jobs" -lt 1 ] && compile_jobs=1
export MAX_JOBS=$compile_jobs

%check
# Not all runtime dependencies and backend setup are unavailable.
# vLLM have several backend and we only use two of them.

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/vllm

%changelog
%autochangelog
