# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0
#
# Originally extracted from Fedora Project
# Authors: The Fedora Project Contributors

%global srcname torch

%global pypi_version 2.10.0
%global miniz_version 3.0.2

# For -test subpackage
# suitable only for local testing
# Install and do something like
#   export LD_LIBRARY_PATH=/usr/lib64/python3.12/site-packages/torch/lib
#   /usr/lib64/python3.12/site-packages/torch/bin/test_api, test_lazy
%bcond test 0

%ifarch x86_64 riscv64
%bcond rocm 0
%endif

# For testing distributed+rccl etc.
# TODO: openmpi not included in openRuyi
%bcond mpi 0

# TODO: no flang on openRuyi, so we cannot enable clang
%global toolchain gcc
%global _lto_cflags %nil

# Disable dwz with rocm because memory can be exhausted
%if %{with rocm}
%define _find_debuginfo_dwz_opts %{nil}
%endif

# Pytorch third-party buildrequires
#
# These system_xxx is kept for debug with some reasons:
#
# 1. some package that is not included in openRuyi.
# 2. some package on openRuyi lack some required component.
# 3. the corresponding version is mismatched with openRuyi.
%bcond system_flatbuffers 0
# Pytorch hardcode httplib to third_party/cpp-httplib
%bcond system_httplib 0
# TODO: kineto not included in openruyi
%bcond system_kineto 0
# TODO: on openRuyi, onnx lack of check_model symbol
%bcond system_onnx 0
# TODO: opentelemetry not included in openRuyi
%bcond system_opentelemetry 0
# TODO: tensorpipe not included in openRuyi
%bcond system_tensorpipe 0

Name:           python-%{srcname}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        PyTorch AI/ML framework
# See license.txt for license details
License:        BSD-3-Clause AND BSD-2-Clause AND 0BSD AND Apache-2.0 AND MIT AND BSL-1.0 AND GPL-3.0-or-later AND Zlib
URL:            https://pytorch.org/
VCS:            git:https://github.com/pytorch/pytorch.git
#!RemoteAsset:  sha256:8019957be2cbdb08dae8d22ad43a51fa4a6f7bf491dbe385ac4c4a77e1b23001
Source0:        https://github.com/pytorch/pytorch/archive/refs/tags/v%{version}.tar.gz
%if %{without system_flatbuffers}
%global flatbuffers_version 24.12.23
#!RemoteAsset:  sha256:7e2ef35f1af9e2aa0c6a7d0a09298c2cb86caf3d4f58c0658b306256e5bcab10
Source1:        https://github.com/google/flatbuffers/archive/refs/tags/v%{flatbuffers_version}.tar.gz
%endif
%if %{without system_tensorpipe}
# Developement on tensorpipe has stopped, repo made read only July 1, 2023, this is the last commit
%global tp_commit 52791a2fd214b2a9dc5759d36725909c1daa7f2e
%global tp_scommit 52791a2
#!RemoteAsset:  sha256:7ff0b84c0623f3360ec7c34b8c4fe02e7f9a87f8fa559c303f9574e44be0bc56
Source2:       https://github.com/pytorch/tensorpipe/archive/%{tp_commit}/tensorpipe-%{tp_scommit}.tar.gz
# The old libuv tensorpipe uses
#!RemoteAsset:  sha256:6cfeb5f4bab271462b4a2cc77d4ecec847fdbdc26b72019c27ae21509e6f94fa
Source3:       https://github.com/libuv/libuv/archive/refs/tags/v1.41.0.tar.gz
# Developement afaik on libnop has stopped, this is the last commit
%global nop_commit 910b55815be16109f04f4180e9adee14fb4ce281
%global nop_scommit 910b558
#!RemoteAsset:  sha256:ec3604671f8ea11aed9588825f9098057ebfef7a8908e97459835150eea9f63a
Source4:       https://github.com/google/libnop/archive/%{nop_commit}/libnop-%{nop_scommit}.tar.gz
%endif
%if %{without opentelemetry}
%global ot_ver 1.14.2
#!RemoteAsset:  sha256:c7e7801c9f6228751cdb9dd4724d0f04777ed53f524c8828e73bf4c9f894e0bd
Source5:       https://github.com/open-telemetry/opentelemetry-cpp/archive/refs/tags/v%{ot_ver}.tar.gz
%endif
%if %{without system_httplib}
%global hl_commit 89c932f313c6437c38f2982869beacc89c2f2246
%global hl_scommit 89c932f
#!RemoteAsset:  sha256:22ec970b3ecb60ef43293379a5cdc94b5fcdc34a888ebce2a3f6413c67262ab7
Source6:       https://github.com/yhirose/cpp-httplib/archive/%{hl_commit}/cpp-httplib-%{hl_scommit}.tar.gz
%endif
%if %{without system_kineto}
%global ki_commit 31f85df8fbd89c188f14ef10f1ec65379786b943
%global ki_scommit 31f85df
#!RemoteAsset:  sha256:c0edae39511cf3d91d66d6b383254ba3b3bee1af024a567566cfe39cbc84e674
Source7:       https://github.com/pytorch/kineto/archive/%{ki_commit}/kineto-%{ki_scommit}.tar.gz
%endif
%if %{without system_onnx}
%global onnx_ver 1.18.0
#!RemoteAsset:  sha256:b466af96fd8d9f485d1bb14f9bbdd2dfb8421bc5544583f014088fb941a1d21e
Source8:       https://github.com/onnx/onnx/archive/refs/tags/v%{onnx_ver}.tar.gz
%endif

BuildRequires:  cmake
BuildRequires:  concurrentqueue-devel
# Although eigen3 enabled on openruyi, it cannot be detected during conf
# TODO: Fix this
BuildRequires:  eigen3
BuildRequires:  foxi-devel
BuildRequires:  libomp-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(libcpuinfo)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(openblas64)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pocketfft-devel
BuildRequires:  pthreadpool-devel
BuildRequires:  fp16-devel
BuildRequires:  fxdiv-devel
BuildRequires:  psimd-devel
BuildRequires:  sleef-devel
BuildRequires:  xnnpack-devel = 0+git20260211.312eb7e
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(filelock)
# TODO: enable on openRuyi
# BuildRequires:  python3dist(fsspec)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sympy)
# TODO: enable on openRuyi
# BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(typing-extensions)

%if %{with system_httplib}
BuildRequires:  cpp-httplib-devel
%endif

%if "%{toolchain}" == "gcc"
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
%endif
%if "%{toolchain}" == "clang"
BuildRequires:  clang
BuildRequires:  flang
%endif

%if %{with system_onnx}
BuildRequires:  onnx-devel
%endif

%if %{with mpi}
BuildRequires:  openmpi-devel
%endif

%if %{with system_flatbuffers}
BuildRequires:  pkgconfig(flatbuffers)
%endif

%if %{with rocm}
BuildRequires:  hipblas-devel
BuildRequires:  hipblaslt-devel
BuildRequires:  hipcub-devel
BuildRequires:  hipfft-devel
BuildRequires:  hiprand-devel
BuildRequires:  hipsparse-devel
BuildRequires:  hipsparselt-devel
BuildRequires:  hipsolver-devel
BuildRequires:  magma-devel
BuildRequires:  miopen-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocrand-devel
BuildRequires:  rocfft-devel
BuildRequires:  rccl-devel
BuildRequires:  rocprim-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-core-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocsolver-devel
BuildRequires:  rocm-smi-devel
BuildRequires:  rocthrust-devel
BuildRequires:  roctracer-devel
%endif

Requires:       python3dist(dill)
Requires:       python3dist(pyyaml)
%if %{with rocm}
Requires:       amdsmi
%endif

# As convention
Provides:       pytorch = %{version}-%{release}
Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PyTorch is a Python package that provides two high-level features:

 * Tensor computation (like NumPy) with strong GPU acceleration
 * Deep neural networks built on a tape-based autograd system

You can reuse your favorite Python packages such as NumPy, SciPy,
and Cython to extend PyTorch when needed.

%prep
%autosetup -p1 -n pytorch-%{version}

# GitHub release tarballs identify the version as an alpha, so replace that
echo "%{pypi_version}" > version.txt

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%if %{without system_flatbuffers}
tar xf %{SOURCE1}
rm -rf third_party/flatbuffers/*
cp -r flatbuffers-%{flatbuffers_version}/* third_party/flatbuffers/
%endif

%if %{without system_tensorpipe}
tar xf %{SOURCE2}
rm -rf third_party/tensorpipe/*
cp -r tensorpipe-*/* third_party/tensorpipe/
tar xf %{SOURCE3}
rm -rf third_party/tensorpipe/third_party/libuv/*
cp -r libuv-*/* third_party/tensorpipe/third_party/libuv/
tar xf %{SOURCE4}
rm -rf third_party/tensorpipe/third_party/libnop/*
cp -r libnop-*/* third_party/tensorpipe/third_party/libnop/

# gcc 15 include cstdint
sed -i '/#include <tensorpipe.*/a#include <cstdint>' third_party/tensorpipe/tensorpipe/common/allocator.h
sed -i '/#include <tensorpipe.*/a#include <cstdint>' third_party/tensorpipe/tensorpipe/common/memory.h
%endif

%if %{without system_opentelemetry}
tar xf %{SOURCE5}
rm -rf third_party/opentelemetry-cpp/*
cp -r opentelemetry-cpp-*/* third_party/opentelemetry-cpp/
%endif

%if %{without system_httplib}
tar xf %{SOURCE6}
rm -rf third_party/cpp-httplib/*
cp -r cpp-httplib-*/* third_party/cpp-httplib/
%endif

%if %{without system_kineto}
tar xf %{SOURCE7}
rm -rf third_party/kineto/*
cp -r kineto-*/* third_party/kineto/
%endif

%if %{without system_onnx}
tar xf %{SOURCE8}
rm -rf third_party/onnx/*
cp -r onnx-*/* third_party/onnx/
%endif

# Adjust for amd gpu targets currently supported
# sed -i -e 's@"gfx1100", "gfx1101", "gfx1200", "gfx1201", "gfx908",@"gfx1100", "gfx1101", "gfx1200", "gfx1201", "gfx1151",@' aten/src/ATen/native/cuda/Blas.cpp
sed -i -e 's@"gfx1100", "gfx1101", "gfx1200", "gfx1201", "gfx908",@"gfx1100", "gfx1101",@' aten/src/ATen/native/cuda/Blas.cpp

# Need to pip this
sed -i -e '/fsspec/d' setup.py

# Use system sympy
sed -i -e 's@sympy==1.13.1@sympy>=1.13.1@' setup.py

# A new dependency
# Connected to USE_FLASH_ATTENTION, since this is off, do not need it
sed -i -e '/aotriton.cmake/d' cmake/Dependencies.cmake
# Compress hip
sed -i -e 's@HIP_CLANG_FLAGS -fno-gpu-rdc@HIP_CLANG_FLAGS -fno-gpu-rdc --offload-compress@' cmake/Dependencies.cmake
# Silence noisy warning
sed -i -e 's@HIP_CLANG_FLAGS -fno-gpu-rdc@HIP_CLANG_FLAGS -fno-gpu-rdc -Wno-pass-failed@' cmake/Dependencies.cmake
sed -i -e 's@HIP_CLANG_FLAGS -fno-gpu-rdc@HIP_CLANG_FLAGS -fno-gpu-rdc -Wno-unused-command-line-argument@' cmake/Dependencies.cmake
sed -i -e 's@HIP_CLANG_FLAGS -fno-gpu-rdc@HIP_CLANG_FLAGS -fno-gpu-rdc -Wno-unused-result@' cmake/Dependencies.cmake
sed -i -e 's@HIP_CLANG_FLAGS -fno-gpu-rdc@HIP_CLANG_FLAGS -fno-gpu-rdc -Wno-deprecated-declarations@' cmake/Dependencies.cmake
# Use parallel jobs
sed -i -e 's@HIP_CLANG_FLAGS -fno-gpu-rdc@HIP_CLANG_FLAGS -fno-gpu-rdc -parallel-jobs=4@' cmake/Dependencies.cmake
# Need to link with librocm_smi64
sed -i -e 's@hiprtc::hiprtc@hiprtc::hiprtc rocm_smi64@' cmake/Dependencies.cmake

# No third_party fmt, use system
sed -i -e 's@fmt::fmt-header-only@fmt@' CMakeLists.txt
sed -i -e 's@fmt::fmt-header-only@fmt@' aten/src/ATen/CMakeLists.txt
sed -i -e 's@list(APPEND ATen_HIP_INCLUDE $<TARGET_PROPERTY:fmt,INTERFACE_INCLUDE_DIRECTORIES>)@@' aten/src/ATen/CMakeLists.txt

sed -i -e 's@fmt::fmt-header-only@fmt@' third_party/kineto/libkineto/CMakeLists.txt
sed -i -e 's@fmt::fmt-header-only@fmt@' c10/CMakeLists.txt
sed -i -e 's@fmt::fmt-header-only@fmt@' torch/CMakeLists.txt
sed -i -e 's@fmt::fmt-header-only@fmt@' cmake/Dependencies.cmake
sed -i -e 's@fmt::fmt-header-only@fmt@' caffe2/CMakeLists.txt

sed -i -e 's@add_subdirectory(${PROJECT_SOURCE_DIR}/third_party/fmt)@#add_subdirectory(${PROJECT_SOURCE_DIR}/third_party/fmt)@' cmake/Dependencies.cmake
sed -i -e 's@set_target_properties(fmt-header-only PROPERTIES INTERFACE_COMPILE_FEATURES "")@#set_target_properties(fmt-header-only PROPERTIES INTERFACE_COMPILE_FEATURES "")@' cmake/Dependencies.cmake
sed -i -e 's@list(APPEND Caffe2_DEPENDENCY_LIBS fmt::fmt-header-only)@#list(APPEND Caffe2_DEPENDENCY_LIBS fmt::fmt-header-only)@' cmake/Dependencies.cmake

# No third_party FXdiv
sed -i -e 's@if(NOT TARGET fxdiv)@if(MSVC AND USE_XNNPACK)@' caffe2/CMakeLists.txt
sed -i -e 's@TARGET_LINK_LIBRARIES(torch_cpu PRIVATE fxdiv)@#TARGET_LINK_LIBRARIES(torch_cpu PRIVATE fxdiv)@' caffe2/CMakeLists.txt

# https://github.com/pytorch/pytorch/issues/149803
# Tries to checkout nccl
sed -i -e 's@    checkout_nccl()@    True@' tools/build_pytorch_libs.py

# Disable the use of check_submodule's in the setup.py, we are a tarball, not a git repo
sed -i -e 's@check_submodules()$@#check_submodules()@' setup.py

# Release comes fully loaded with third party src
# Remove what we can
#
# For 2.1 this is all but miniz-2.1.0
# Instead of building as a library, caffe2 reaches into
# the third_party dir to compile the file.
# mimiz is licensed MIT
# https://github.com/richgel999/miniz/blob/master/LICENSE
mv third_party/miniz-%{miniz_version} .
#
# setup.py depends on this script
mv third_party/build_bundled.py .

%if %{without system_flatbuffers}
# Need the just untarred flatbuffers/flatbuffers.h
mv third_party/flatbuffers .
%endif

%if %{without system_tensorpipe}
mv third_party/tensorpipe .
%endif

%if %{without system_opentelemetry}
mv third_party/opentelemetry-cpp .
%endif

%if %{without system_httplib}
mv third_party/cpp-httplib .
%endif

%if %{without system_kineto}
mv third_party/kineto .
%endif

%if %{without system_onnx}
mv third_party/onnx .
%endif

%if %{without system_protobuf}
mv third_party/protobuf .
%endif

# Remove everything
rm -rf third_party/*
# Put stuff back
mv build_bundled.py third_party
mv miniz-%{miniz_version} third_party

%if %{without system_flatbuffers}
mv flatbuffers third_party
%endif

%if %{without system_tensorpipe}
mv tensorpipe third_party
%endif

%if %{without system_opentelemetry}
mv opentelemetry-cpp third_party
%endif

%if %{without system_httplib}
mv cpp-httplib third_party
%endif

%if %{without system_kineto}
mv kineto third_party
%endif

%if %{without system_onnx}
mv onnx third_party
%endif

%if %{without system_protobuf}
mv protobuf third_party
%endif

# Fake out pocketfft, and system header will be used
mkdir third_party/pocketfft
cp /usr/include/pocketfft_hdronly.h third_party/pocketfft/

# Use the system valgrind headers
mkdir third_party/valgrind-headers
cp %{_includedir}/valgrind/* third_party/valgrind-headers

# Fix installing to /usr/lib64
sed -i -e 's@DESTINATION ${PYTHON_LIB_REL_PATH}@DESTINATION ${CMAKE_INSTALL_PREFIX}/${PYTHON_LIB_REL_PATH}@' caffe2/CMakeLists.txt

# reenable foxi linking
sed -i -e 's@list(APPEND Caffe2_DEPENDENCY_LIBS foxi_loader)@#list(APPEND Caffe2_DEPENDENCY_LIBS foxi_loader)@' cmake/Dependencies.cmake

%if %{without system_tensorpipe}
# cmake version changed
sed -i -e 's@cmake_minimum_required(VERSION 3.4)@cmake_minimum_required(VERSION 3.5)@' third_party/tensorpipe/third_party/libuv/CMakeLists.txt
sed -i -e 's@cmake_minimum_required(VERSION 3.4)@cmake_minimum_required(VERSION 3.5)@' libuv*/CMakeLists.txt
%endif

%if %{without system_opentelemetry}
sed -i -e 's@cmake_minimum_required(VERSION 3.1)@cmake_minimum_required(VERSION 3.5)@' third_party/opentelemetry-cpp/CMakeLists.txt
%endif

%if %{with rocm}
# hipify
./tools/amd_build/build_amd.py
# installs to /usr/include
sed -i -e 's@rocm-core/rocm_version.h@rocm_version.h@' aten/src/ATen/hip/tunable/TunableGemm.h
# https://github.com/pytorch/pytorch/issues/149805
sed -i -e 's@rocm-core/rocm_version.h@rocm_version.h@' cmake/public/LoadHIP.cmake
# installs to /usr/include
sed -i -e 's@rocm-core/rocm_version.h@rocm_version.h@' aten/src/ATen/hip/tunable/Tunable.cpp
sed -i -e 's@rocm-core/rocm_version.h@rocm_version.h@' aten/src/ATen/cuda/tunable/Tunable.cpp
# use any hip, correct CMAKE_MODULE_PATH
sed -i -e 's@lib/cmake/hip@lib64/cmake/hip@' cmake/public/LoadHIP.cmake
sed -i -e 's@HIP 1.0@HIP MODULE@'            cmake/public/LoadHIP.cmake
# silence an assert
# sed -i -e '/qvalue = std::clamp(qvalue, qmin, qmax);/d' aten/src/ATen/native/cuda/IndexKernel.cu
%endif

# moodycamel include path needs adjusting to use the system's
sed -i -e 's@${PROJECT_SOURCE_DIR}/third_party/concurrentqueue@/usr/include/concurrentqueue@' cmake/Dependencies.cmake

%build
# Control the number of jobs
# The build can fail if too many threads exceed the physical memory
# Run at least one thread, more if CPU & memory resources are available.
COMPILE_JOBS=`nproc`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
# Take into account memmory usage per core, do not thrash real memory
# Build may consumes more than 2GB per core
BUILD_MEM=3
MEM_KB=0
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
COMPILE_JOBS_MEM=`eval "expr 1 + ${MEM_GB} / ${BUILD_MEM}"`
if [ "$COMPILE_JOBS_MEM" -lt "$COMPILE_JOBS" ]; then
    COMPILE_JOBS=$COMPILE_JOBS_MEM
fi
export MAX_JOBS=$COMPILE_JOBS

# For verbose cmake output
# export VERBOSE=ON
# For verbose linking
# export CMAKE_SHARED_LINKER_FLAGS=-Wl,--verbose

# Manually set this hardening flag
export CMAKE_EXE_LINKER_FLAGS=-pie
export BUILD_CUSTOM_PROTOBUF=OFF
export BUILD_NVFUSER=OFF
export BUILD_SHARED_LIBS=ON
export BUILD_TEST=OFF
export CMAKE_BUILD_TYPE=RelWithDebInfo
export CMAKE_FIND_PACKAGE_PREFER_CONFIG=ON
export CAFFE2_LINK_LOCAL_PROTOBUF=OFF
export INTERN_BUILD_MOBILE=OFF
export USE_DISTRIBUTED=OFF
export USE_CUDA=OFF
export USE_FAKELOWP=OFF
export USE_FBGEMM=OFF
export USE_FLASH_ATTENTION=OFF
export USE_GLOO=OFF
export USE_ITT=OFF
export USE_KINETO=OFF
export USE_KLEIDIAI=OFF
export USE_LITE_INTERPRETER_PROFILER=OFF
export USE_LITE_PROTO=OFF
export USE_MAGMA=OFF
export USE_MEM_EFF_ATTENTION=OFF
export USE_MKLDNN=OFF
export USE_MPI=OFF
export USE_NCCL=OFF
export USE_NNPACK=OFF
export USE_NUMPY=ON
export USE_OPENMP=ON
export USE_PYTORCH_QNNPACK=OFF
export USE_ROCM=OFF
export USE_SYSTEM_SLEEF=ON
export USE_SYSTEM_EIGEN_INSTALL=ON
%if %{with system_onnx}
export USE_SYSTEM_ONNX=ON
%endif
export USE_SYSTEM_PYBIND11=ON
export USE_SYSTEM_LIBS=OFF
export USE_SYSTEM_NCCL=OFF
export USE_XNNPACK=OFF
export USE_XPU=OFF
export USE_SYSTEM_PTHREADPOOL=ON
export USE_SYSTEM_CPUINFO=ON
export USE_SYSTEM_FP16=ON
export USE_SYSTEM_FXDIV=ON
export USE_SYSTEM_PSIMD=ON
export USE_SYSTEM_XNNPACK=OFF
export USE_DISTRIBUTED=ON
export USE_TENSORPIPE=ON
%if %{without system_tensorpipe}
export TP_BUILD_LIBUV=OFF
%endif

%if %{with mpi}
export USE_MPI=ON
%endif

%if %{with rocm}
export USE_ROCM=ON
export USE_ROCM_CK_SDPA=OFF
export USE_ROCM_CK_GEMM=OFF
export USE_FBGEMM_GENAI=OFF

export USE_MAGMA=ON
export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`

# pytorch uses clang, not hipcc
export HIP_CLANG_PATH=%{rocmllvm_bindir}
export PYTORCH_ROCM_ARCH=%{rocm_gpu_list_default}
%endif

%pyproject_wheel

%install
%if %{with rocm}
export USE_ROCM=ON
export USE_ROCM_CK=OFF
export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`

# pytorch uses clang, not hipcc
export HIP_CLANG_PATH=%{rocmllvm_bindir}
export PYTORCH_ROCM_ARCH=%{rocm_gpu_list_default}
%endif

%pyproject_install
%pyproject_save_files '*torch*'

%check
# Not working yet

%files
%doc README.md
%license LICENSE
%{_bindir}/torchrun
%{python3_sitearch}/%{srcname}*
%{python3_sitearch}/functorch

%changelog
%autochangelog
