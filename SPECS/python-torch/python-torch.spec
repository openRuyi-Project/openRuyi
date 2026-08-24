# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0
#
# Originally extracted from Fedora Project
# Authors: The Fedora Project Contributors

%global srcname torch

# PyTorch upstream use clang as default toolchain
%global toolchain clang

%global miniz_version 3.0.2

%bcond test 1

# The default flavor builds a CPU-only torch
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "rocm"
%bcond rocm 1
%else
%bcond rocm 0
%endif

# For testing distributed+rccl etc.
# TODO: openmpi not included in openRuyi
%bcond mpi 0

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
# TODO: tensorpipe not included in openRuyi
%bcond system_tensorpipe 0

%if %{with rocm}
Name:           python-%{srcname}-rocm
%else
Name:           python-%{srcname}
%endif
Version:        2.13.0
Release:        %autorelease
Summary:        PyTorch AI/ML framework
# From pyproject.toml
License:        Apache-2.0 AND (Apache-2.0 WITH LLVM-exception) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND MIT
URL:            https://pytorch.org/
VCS:            git:https://github.com/pytorch/pytorch.git
# The PyPI package is wheels-only(binary package)
# The GitHub tag archive excludes submodules
# The official release asset includes the third_party C++ sources needed for a distro source build
#!RemoteAsset:  sha256:66614a19060f69cfd63cd0295f65a1241bd15df2fa65c60ae51066c11c2ce812
Source0:        https://github.com/pytorch/pytorch/releases/download/v%{version}/pytorch-v%{version}.tar.gz
# Functional smoke test for the just-built torch, run by the check phase.
Source1:        pytorch-smoke-test.py
BuildSystem:    pyproject

BuildOption(prep):  -n pytorch-v%{version}
# packages: torch, torchgen, functorch, torchrun
BuildOption(install):  -l '*torch*'
# torch.lib.lib*: C++ shared libs
# torchgen.static_runtime.gen_static_runtime_ops: imports non-opensource Meta-internal libfb;
# torch.utils.tensorboard*: needs tensorboard, not yet packaged in openRuyi.
BuildOption(check):  -e 'torch.lib.lib*'
BuildOption(check):  -e 'torchgen.static_runtime.gen_static_runtime_ops'
BuildOption(check):  -e 'torch.utils.tensorboard*'

BuildRequires:  clang
BuildRequires:  clang-tools-extra
BuildRequires:  cmake
BuildRequires:  cmake(concurrentqueue)
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(LLVM)
BuildRequires:  cmake(ONNX)
BuildRequires:  cmake(onnxruntime)
BuildRequires:  cmake(sleef)
BuildRequires:  cmake(zlib)
BuildRequires:  compiler-rt
BuildRequires:  cpuinfo
BuildRequires:  eigen3
BuildRequires:  foxi-devel
BuildRequires:  fp16-devel
BuildRequires:  fxdiv-devel
BuildRequires:  libomp-devel
BuildRequires:  libstdc++-devel
BuildRequires:  lld
BuildRequires:  ninja
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(openblas64)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pocketfft-devel
BuildRequires:  pthreadpool-devel
BuildRequires:  psimd-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(fsspec)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sympy)
BuildRequires:  python3dist(typing-extensions)

%if %{with system_httplib}
BuildRequires:  cmake(httplib)
%endif

%if %{with mpi}
BuildRequires:  openmpi-devel
%endif

%if %{with test}
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
# urllib3 is needed by torch.distributed.elastic.rendezvous.etcd_rendezvous_backend
BuildRequires:  python3dist(urllib3)
%endif

%if %{with system_flatbuffers}
BuildRequires:  pkgconfig(flatbuffers)
%endif

%if %{with rocm}
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(amd_smi)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hipblas)
BuildRequires:  cmake(hipblaslt)
BuildRequires:  cmake(hipcub)
BuildRequires:  cmake(hipfft)
BuildRequires:  cmake(hiprand)
BuildRequires:  cmake(hipsparse)
BuildRequires:  cmake(hipsparselt)
BuildRequires:  cmake(hipsolver)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(miopen)
BuildRequires:  cmake(rccl)
BuildRequires:  cmake(rocblas)
BuildRequires:  cmake(rocfft)
BuildRequires:  cmake(rocm-core)
BuildRequires:  cmake(rocm_smi)
BuildRequires:  cmake(rocprim)
BuildRequires:  cmake(rocrand)
BuildRequires:  cmake(rocsolver)
BuildRequires:  cmake(rocthrust)
BuildRequires:  pkgconfig(magma)
BuildRequires:  rocm-cmake
BuildRequires:  rocm-llvm-macros
BuildRequires:  roctracer-devel
%endif

Requires:       libomp
Requires:       python3dist(dill)
Requires:       python3dist(pyyaml)
%if %{with rocm}
Requires:       amdsmi
%endif

%if %{with rocm}
Provides:       pytorch-rocm = %{version}-%{release}
Conflicts:      python-%{srcname}
%else
Provides:       python-%{srcname} = %{version}-%{release}
Provides:       pytorch = %{version}-%{release}
Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}
Conflicts:      python-%{srcname}-rocm
%endif

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(concurrentqueue)

%description devel
Headers and CMake metadata for building C++ and HIP extensions against the
matching %{name} runtime.

%if %{with test}
%package test
Summary:        Installed native test payload for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
Native test programs, helper libraries, and fixtures for post-install
validation of %{name}. This is not the complete upstream Python test suite.
%endif

%patchlist
# Clang fails on a -Wc2y-extensions diagnostic from benchmark's __COUNTER__ preprocessor check.
1000-benchmark-silence-c2y-counter-warning.patch
# Add gfx1100/gfx1101/gfx1151 to getHipblasltPreferredArchs()
# On gfx1100 rocBLAS fp16 GEMM has no Tensile solution for some shapes and fails with
# HIPBLAS_STATUS_INTERNAL_ERROR; default to hipBLASLt there
# https://github.com/pytorch/pytorch/commit/10a5f2ff7c90d8c84938b0e789ab2f4145f90b5d
1001-default-to-hipblaslt-on-gfx110x.patch
# In pytorch-smoke-test.py, torch.dot()/torch.vdot() on complex tensors return 0
# because ATen's BLAS ABI probe misdetects OpenBLAS's cblas_*dot*_sub interface
# force the CBLAS complex-dot path
# There is similar solution in downstream:
# https://github.com/conda-forge/pytorch-cpu-feedstock/issues/180
# https://github.com/conda-forge/pytorch-cpu-feedstock/blob/main/recipe/patches/0004-Use-BLAS_USE_CBLAS_DOT-for-OpenBLAS-builds.patch
2001-force-cblas-complex-dot-for-openblas.patch
2002-use-system-googletest.patch
2003-use-system-fmt.patch
2004-use-system-pyproject-build-dependencies.patch
2005-use-system-cmake-dependencies.patch
# Remove git submodule checks
2006-skip-unused-submodule-prebuild-checks.patch
# Workaround for system llvm22 AMDGPU codegen bug
# Should Drop this if llvm 23.1.0 enabled
2007-loss-hip-O0-workaround-llvm22-codegen.patch
# Adapt shared CUDA/HIP declarations to the ROCm 7.2 clang ABI.
2008-fix-rocm-compatibility.patch
# Skip try-run phase of cmake for bundled 'benchmark'
2009-skip-benchmark-try-run.patch
# Install the GLOO test
2010-install-cpu-gloo-test.patch

%description
PyTorch is a Python package that provides two high-level features:

 * Tensor computation (like NumPy) with strong GPU acceleration
 * Deep neural networks built on a tape-based autograd system

You can reuse your favorite Python packages such as NumPy, SciPy,
and Cython to extend PyTorch when needed.

%prep -a
# GitHub release tarballs identify the version as an alpha, so replace that
echo "%{version}" > version.txt

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Release comes fully loaded with third party src
# Remove what we can
#
# For 2.1 this is all but miniz-2.1.0
# Instead of building as a library, caffe2 reaches into
# the third_party dir to compile the file.
# mimiz is licensed MIT
# https://github.com/richgel999/miniz/blob/master/LICENSE
mv third_party/miniz-%{miniz_version} .
%if %{without system_flatbuffers}
# Need the just untarred flatbuffers/flatbuffers.h
mv third_party/flatbuffers .
%endif

%if %{without system_tensorpipe}
mv third_party/tensorpipe .
%endif

%if %{without system_httplib}
mv third_party/cpp-httplib .
%endif

%if %{without system_kineto}
mv third_party/kineto .
%endif

mv third_party/gloo .
%if %{with test}
mv third_party/benchmark .
%endif
mv third_party/mslk .

# Remove everything
rm -rf third_party/*
# Put stuff back
mv miniz-%{miniz_version} third_party

%if %{without system_flatbuffers}
mv flatbuffers third_party
%endif

%if %{without system_tensorpipe}
mv tensorpipe third_party
%endif

%if %{without system_httplib}
mv cpp-httplib third_party
%endif

%if %{without system_kineto}
mv kineto third_party
%endif

mv mslk third_party

mv gloo third_party

%if %{with test}
# googletest is provided by the system gtest-devel (openRuyi package) instead
# of the vendored submodule -- see 2002-use-system-googletest.patch, which makes
# PyTorch's cmake call find_package(GTest) and alias the GTest:: targets to the
# bare names the test CMakeLists link against.
mv benchmark third_party

# Benchmark configuration is applied by patch 2009.
%endif

# Fake out pocketfft, and system header will be used
mkdir third_party/pocketfft
cp %{_includedir}/pocketfft_hdronly.h third_party/pocketfft/

# Use the system valgrind headers
mkdir third_party/valgrind-headers
cp %{_includedir}/valgrind/* third_party/valgrind-headers

%if %{with rocm}
./tools/amd_build/build_amd.py
%endif

%generate_buildrequires
# We use a git tarball instead of PyPI version
export PYTORCH_BUILD_VERSION=%{version}
export PYTORCH_BUILD_NUMBER=1
# Too much extra packages for PyTorch, use '-R' to skip them
%pyproject_buildrequires -R

%build -p
export PYTORCH_BUILD_VERSION=%{version}
export PYTORCH_BUILD_NUMBER=1
# Control the number of jobs
# The build can fail if too many threads exceed the physical memory
# Run at least one thread, more if CPU & memory resources are available.
COMPILE_JOBS=`nproc`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
# Take into account memory usage per core, do not thrash real memory
# TraceType/VariableType files can consume 4GB+ per compilation unit
# Use a more conservative estimate: 4GB per job for safety
BUILD_MEM=4
MEM_KB=0
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
COMPILE_JOBS_MEM=`eval "expr 1 + ${MEM_GB} / ${BUILD_MEM}"`
if [ "$COMPILE_JOBS_MEM" -lt "$COMPILE_JOBS" ]; then
    COMPILE_JOBS=$COMPILE_JOBS_MEM
fi
# Ensure at least 2 jobs to avoid single-threading the large files
if [ "$COMPILE_JOBS" -lt 2 ]; then
    COMPILE_JOBS=2
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
%if %{with test}
export BUILD_TEST=ON
%endif
# Use Release instead of RelWithDebInfo to reduce compile time and memory usage
export CMAKE_BUILD_TYPE=Release
export CMAKE_FIND_PACKAGE_PREFER_CONFIG=ON
export CAFFE2_LINK_LOCAL_PROTOBUF=OFF
export INTERN_BUILD_MOBILE=OFF
export USE_CUDA=OFF
export USE_FAKELOWP=OFF
export USE_FBGEMM=OFF
export USE_FLASH_ATTENTION=OFF
export USE_GLOO=ON
export USE_ITT=OFF
export USE_KINETO=OFF
export USE_KLEIDIAI=OFF
export USE_LITE_INTERPRETER_PROFILER=OFF
export USE_LITE_PROTO=OFF
export USE_MAGMA=OFF
export USE_MEM_EFF_ATTENTION=OFF
export USE_MKLDNN=OFF
export USE_MPI=OFF
export USE_MSLK=OFF
export USE_NCCL=OFF
export USE_NNPACK=OFF
export USE_NUMPY=ON
export USE_OPENMP=ON
export USE_PYTORCH_QNNPACK=OFF
export USE_ROCM=OFF
export USE_SYSTEM_SLEEF=ON
export USE_SYSTEM_EIGEN_INSTALL=ON
export USE_SYSTEM_ONNX=ON
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

# The system clang does not auto-detect the rocm-device-libs bitcode
# Without HIPFLAGS configure fails with "cannot find ROCm device library".
export HIPFLAGS="--rocm-device-lib-path=$(%{rocmllvm_bindir}/clang -print-resource-dir)/amdgcn/bitcode"

export CMAKE_NO_SYSTEM_FROM_IMPORTED=ON
%endif

export LDFLAGS="-fuse-ld=lld %{build_ldflags}"
export CMAKE_LIBRARY_PATH=%{_libdir}
export CMAKE_PREFIX_PATH="%{_prefix}:%{_libdir}/cmake:%{python3_sitearch}"

# See 2001-force-cblas-complex-dot-for-openblas.patch
export PYTORCH_BLAS_USE_CBLAS_DOT=ON

%install -p
%if %{with rocm}
export USE_ROCM=ON
export USE_ROCM_CK=OFF
export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`

# pytorch uses clang, not hipcc
export HIP_CLANG_PATH=%{rocmllvm_bindir}
export PYTORCH_ROCM_ARCH=%{rocm_gpu_list_default}
export HIPFLAGS="--rocm-device-lib-path=$(%{rocmllvm_bindir}/clang -print-resource-dir)/amdgcn/bitcode"
%endif

%install -a
%if %{with rocm}
# Gloo is for CPU backend
# During PyTorch ROCm building, Gloo tests link the uninstalled libc10d_hip_test.so
rm -f %{buildroot}%{python3_sitearch}/torch/bin/ProcessGroupGlooTest \
      %{buildroot}%{python3_sitearch}/torch/bin/ProcessGroupGlooAsyncTest
sed -i '\#/torch/bin/ProcessGroupGlooTest$#d;\#/torch/bin/ProcessGroupGlooAsyncTest$#d' %{pyproject_files}
%endif

# Development SDK files belong to -devel, not the main package.
sed -i '\#%{python3_sitearch}/torch/include/#d;\#%{python3_sitearch}/torch/share/cmake/#d' \
    %{pyproject_files}

%if %{with test}
# Test files belong to -test, not the main package
sed -i \
    -e '\#%{python3_sitearch}/torch/bin/\(FileStoreTest\|HashStoreTest\|ProcessGroupGlooAsyncTest\|ProcessGroupGlooTest\|TCPStoreTest\|test_aoti_abi_check\|test_api\|test_cpp_rpc\|test_dist_autograd\|test_jit\|test_lazy\|test_shim\)$#d' \
    -e '\#%{python3_sitearch}/torch/bin/\(script_module_v4\.ptl\|test_interpreter_async\.pt\)$#d' \
    -e '\#%{python3_sitearch}/torch/bin/upgrader_models#d' \
    -e '\#%{python3_sitearch}/torch/lib/\(libaoti_custom_ops\|libbackend_with_compiler\|libjitbackend_test\|libtorchbind_test\)\.so$#d' \
    -e '\#%{python3_sitearch}/torch/test/#d' \
    -e '\#%{python3_sitearch}/torch/test$#d' \
    %{pyproject_files}
%endif

%check -a
%if %{with test}
# Default %check only checks imports
# Additionally run a small functional smoke against the just-built tree:
# real matmul, autograd, a training step, and a complex dot/vdot guard
# Fedora/Debian/Arch do not run PyTorch's own test/*.py suite at build time either;
# A smoke is enough to catch base functionality
PYTHONPATH="%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}" \
PYTHONDONTWRITEBYTECODE=1 \
%{__python3} -sP %{SOURCE1}
%endif

%files -f %{pyproject_files}
%doc README.md NOTICE
%{_bindir}/torchrun

%files devel
%{python3_sitearch}/torch/include/
%{python3_sitearch}/torch/share/cmake/

%if %{with test}
%files test
%{python3_sitearch}/torch/bin/FileStoreTest
%{python3_sitearch}/torch/bin/HashStoreTest
%if %{without rocm}
%{python3_sitearch}/torch/bin/ProcessGroupGlooTest
%endif
%{python3_sitearch}/torch/bin/TCPStoreTest
%{python3_sitearch}/torch/bin/script_module_v4.ptl
%{python3_sitearch}/torch/bin/test_aoti_abi_check
%{python3_sitearch}/torch/bin/test_api
%{python3_sitearch}/torch/bin/test_cpp_rpc
%{python3_sitearch}/torch/bin/test_dist_autograd
%{python3_sitearch}/torch/bin/test_interpreter_async.pt
%{python3_sitearch}/torch/bin/test_jit
%{python3_sitearch}/torch/bin/test_lazy
%{python3_sitearch}/torch/bin/test_shim
%{python3_sitearch}/torch/bin/upgrader_models/
%{python3_sitearch}/torch/lib/libaoti_custom_ops.so
%{python3_sitearch}/torch/lib/libbackend_with_compiler.so
%{python3_sitearch}/torch/lib/libjitbackend_test.so
%{python3_sitearch}/torch/lib/libtorchbind_test.so
%{python3_sitearch}/torch/test/
%endif

%changelog
%autochangelog
