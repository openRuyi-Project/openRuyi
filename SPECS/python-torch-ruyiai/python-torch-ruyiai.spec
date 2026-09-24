# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname torch

%global commit 6d667e1e03a30da647baea22b06ad3564019d002
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# Upstream's version.txt reads 2.15.0a0.
%global pypi_version 2.15.0a0+git%{shortcommit}

# third_party components this configuration compiles from source.
%global gloo_commit 74cc005ae13f69c11d8a41e50b42025b6730e796
%global flatbuffers_commit a2cd1ea3b6d3fee220106b5fed3f7ce8da9eb757
%global httplib_commit 62d899feac3cf9215a55f2b43da250fdd98d2156
%global kineto_commit 84e5ca9e8dc1a27abd174f1305bd8e0e400239ea
%global tensorpipe_commit 2b4cd91092d335a697416b2a3cb398283246849d
# TensorPipe's own submodules; it is built with the bundled libuv, and libnop
# is a header-only dependency.
%global libuv_commit 5152db2cbfeb5582e9c27c5ea1dba2cd9e10759b
%global libnop_commit 910b55815be16109f04f4180e9adee14fb4ce281
%global miniz_version 3.0.2

# The wheel build backend, carried as a source: pyproject.toml needs
# scikit-build-core 1.0 or newer, openRuyi still ships 0.12.x, and
# python-pyvex pins an upper bound against that version.
%global skbc_version 1.0.3
# Where the prep stage unpacks it; the requirements generator and the wheel
# build both import the backend from there.
%global skbc_dir %{_builddir}/scikit-build-core-%{skbc_version}

%global toolchain clang

%global _lto_cflags %nil

Name:           python-%{srcname}-ruyiai
Version:        2.15.0~a0+git20260921.%{shortcommit}
Release:        %autorelease
Summary:        PyTorch AI/ML framework with the RuyiAI RISC-V patches
# From pyproject.toml, which lists the licenses of the bundled components.
License:        Apache-2.0 AND (Apache-2.0 WITH LLVM-exception) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND MIT
URL:            https://github.com/RuyiAI-Stack/pytorch
VCS:            git:https://github.com/RuyiAI-Stack/pytorch.git
#!RemoteAsset:  sha256:d3800727e04c47ab43df1cdc48abaf499ad1930acc47221fd7d8e78792e6f05a
Source0:        https://github.com/RuyiAI-Stack/pytorch/archive/%{commit}/pytorch-%{commit}.tar.gz
#!RemoteAsset:  sha256:1d7260c64008e5ad430a01f63dfd94a3e04ea663f2694a3834f3877b4da66833
Source1:        https://github.com/pytorch/gloo/archive/%{gloo_commit}/gloo-%{gloo_commit}.tar.gz
#!RemoteAsset:  sha256:02db3e64fc74127f119ad2770068534e5b7b4731f6f79a5e8a30b2221ca4d744
Source2:        https://github.com/google/flatbuffers/archive/%{flatbuffers_commit}/flatbuffers-%{flatbuffers_commit}.tar.gz
#!RemoteAsset:  sha256:ee6cc9382bcee9392cc8f0e3b7ae79636b677264c2fd7ad9e5f8657302630073
Source3:        https://github.com/yhirose/cpp-httplib/archive/%{httplib_commit}/cpp-httplib-%{httplib_commit}.tar.gz
#!RemoteAsset:  sha256:77e2b6b7cbef6190b192aa71694f0833ed360824d2e5a6701fbd7d83eed9769f
Source4:        https://github.com/pytorch/kineto/archive/%{kineto_commit}/kineto-%{kineto_commit}.tar.gz
#!RemoteAsset:  sha256:0e85ca56bfe25ed7b3026d2784f716eb10ed1328ade346e3a252814752c57eeb
Source5:        https://github.com/pytorch/tensorpipe/archive/%{tensorpipe_commit}/tensorpipe-%{tensorpipe_commit}.tar.gz
#!RemoteAsset:  sha256:eeb2cdd529d0de964dccb479afb37427cdf001288786c51babe12c79c9cc8eac
Source6:        https://github.com/libuv/libuv/archive/%{libuv_commit}/libuv-%{libuv_commit}.tar.gz
#!RemoteAsset:  sha256:ec3604671f8ea11aed9588825f9098057ebfef7a8908e97459835150eea9f63a
Source7:        https://github.com/google/libnop/archive/%{libnop_commit}/libnop-%{libnop_commit}.tar.gz
#!RemoteAsset:  sha256:a4d7a05978ee37975c37743510c8991e2debce7ef83afb0a07c0c576fd4f16e8
Source8:        https://files.pythonhosted.org/packages/source/s/scikit_build_core/scikit_build_core-%{skbc_version}.tar.gz
# Functional smoke test for the just-built torch, run by the check stage.
Source9:        pytorch-smoke-test.py
BuildSystem:    pyproject

BuildOption(prep):  -n pytorch-%{commit}
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
# scikit-build-core runtime dependencies; the backend is carried as a source
# rather than a repository build requirement, so its own dependencies are
# declared here.  It looks for CMake and Ninja on PATH instead of pulling their
# PyPI wheels, which is why this spec requires the tools and not
# python3dist(cmake) or python3dist(ninja).
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pathspec)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sympy)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(urllib3)

Requires:       libomp
Requires:       python3dist(dill)
Requires:       python3dist(pyyaml)

Provides:       python-%{srcname}-ruyiai = %{version}-%{release}
Provides:       python3-%{srcname}-ruyiai = %{version}-%{release}
Provides:       python3-%{srcname}-ruyiai%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}-ruyiai
# This package installs the torch module, so it cannot coexist with either
# flavor of the upstream-source package.
Conflicts:      python-%{srcname}
Conflicts:      python-%{srcname}-rocm

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(concurrentqueue)

%description devel
Headers and CMake metadata for building C++ extensions against the matching
%{name} runtime.

%patchlist
# In pytorch-smoke-test.py, torch.dot()/torch.vdot() on complex tensors return 0
# because ATen's BLAS ABI probe misdetects OpenBLAS's cblas_*dot*_sub interface
# force the CBLAS complex-dot path
# There is similar solution in downstream:
# https://github.com/conda-forge/pytorch-cpu-feedstock/issues/180
# https://github.com/conda-forge/pytorch-cpu-feedstock/blob/main/recipe/patches/0004-Use-BLAS_USE_CBLAS_DOT-for-OpenBLAS-builds.patch
2001-force-cblas-complex-dot-for-openblas.patch
# Build against the system fmt instead of the vendored third_party/fmt.
2003-use-system-fmt.patch
# Link c10's public Semaphore.h against the packaged concurrentqueue target and
# let the exported CMake SDK rediscover it.  Rebased from the openRuyi 2.13
# patch: the ROCm-only rocm_smi64 hunk is dropped, this spec is CPU-only.
2005-use-system-cmake-dependencies.patch
# Make the submodule sanity check in cmake/PreBuildSteps.cmake follow the
# USE_ flags, so it accepts a third_party tree that only carries the
# components this build compiles.  The prep stage additionally deletes
# .gitmodules, which is what selects that fallback list over the full list of
# 37 submodule paths.
2006-skip-unused-submodule-prebuild-checks.patch
# Gate the RVV depthwise-convolution kernels on the vector extension rather
# than on the intrinsic API version, which is defined even for the rva20
# baseline.
2011-gate-rvv-kernel-on-vector-target.patch
# Take scikit-build-core out of build-system.requires, pin the schema floor
# directly, and drop the license-files pattern that the pruned third_party
# tree cannot satisfy.  This is the successor to the sibling spec's 2004, which
# kept the backend from pulling its own build dependencies.
2012-vendor-scikit-build-core.patch

%description
PyTorch is a Python package that provides two high-level features:

 * Tensor computation (like NumPy) with strong GPU acceleration
 * Deep neural networks built on a tape-based autograd system

You can reuse your favorite Python packages such as NumPy, SciPy,
and Cython to extend PyTorch when needed.

This build follows the RuyiAI-Stack riscv branch rather than an upstream
release.  On top of upstream main the branch carries the RISC-V test fixes
and the autograd ABI compatibility overloads that its maintainers need, so
RISC-V users get the tree the fork's own CI validates.  It is a CPU-only
build and cannot be installed alongside python-%{srcname}.

%prep -a
# The snapshot ships third_party as empty submodule directories plus the few
# components upstream tracks in-tree.  Prune it down to what this
# configuration compiles and unpack the pinned archives in place, which
# reproduces the third_party contents of the upstream release asset that
# SPECS/python-torch builds from.
rm -f .gitmodules

# The build compiles miniz sources straight out of third_party.
mv third_party/miniz-%{miniz_version} .
rm -rf third_party/*
mv miniz-%{miniz_version} third_party

mkdir -p third_party/gloo third_party/flatbuffers third_party/cpp-httplib
mkdir -p third_party/kineto third_party/tensorpipe
tar -xf %{_sourcedir}/gloo-%{gloo_commit}.tar.gz -C third_party/gloo --strip-components=1
tar -xf %{_sourcedir}/flatbuffers-%{flatbuffers_commit}.tar.gz -C third_party/flatbuffers --strip-components=1
tar -xf %{_sourcedir}/cpp-httplib-%{httplib_commit}.tar.gz -C third_party/cpp-httplib --strip-components=1
tar -xf %{_sourcedir}/kineto-%{kineto_commit}.tar.gz -C third_party/kineto --strip-components=1
tar -xf %{_sourcedir}/tensorpipe-%{tensorpipe_commit}.tar.gz -C third_party/tensorpipe --strip-components=1

# TensorPipe builds the bundled libuv (PyTorch forces TP_BUILD_LIBUV on) and
# includes libnop headers; neither is a system package in openRuyi.
mkdir -p third_party/tensorpipe/third_party/libuv
mkdir -p third_party/tensorpipe/third_party/libnop
tar -xf %{_sourcedir}/libuv-%{libuv_commit}.tar.gz -C third_party/tensorpipe/third_party/libuv --strip-components=1
tar -xf %{_sourcedir}/libnop-%{libnop_commit}.tar.gz -C third_party/tensorpipe/third_party/libnop --strip-components=1

# Fake out pocketfft, and system header will be used
mkdir third_party/pocketfft
cp %{_includedir}/pocketfft_hdronly.h third_party/pocketfft/

# Use the system valgrind headers
mkdir third_party/valgrind-headers
cp %{_includedir}/valgrind/* third_party/valgrind-headers/

# Unpack the build backend outside the source tree.  It has to be importable
# while the build requirements are generated as well, which happens after this
# stage, so both stages point PYTHONPATH at the unpacked "src" directory.
rm -rf %{skbc_dir}
mkdir -p %{skbc_dir}
tar -xf %{_sourcedir}/scikit_build_core-%{skbc_version}.tar.gz -C %{skbc_dir} --strip-components=1

%generate_buildrequires
# We build from a git snapshot instead of a PyPI version
export PYTORCH_BUILD_VERSION=%{pypi_version}
export PYTORCH_BUILD_NUMBER=1
# The generator imports the build backend and calls its wheel requirements
# hook, so the backend unpacked by the prep stage has to be importable here.
export PYTHONPATH="%{skbc_dir}/src${PYTHONPATH:+:$PYTHONPATH}"
# Too much extra packages for PyTorch, use '-R' to skip them
%pyproject_buildrequires -R

%build -p
# The wheel is built with the backend from Source8: the pyproject_wheel macro
# passes --no-build-isolation to pip, so pip imports the backend from
# PYTHONPATH instead of installing one.
export PYTHONPATH="%{skbc_dir}/src${PYTHONPATH:+:$PYTHONPATH}"
# These knobs stay environment variables instead of becoming BuildOption
# arguments.  PyTorch forwards USE_/BUILD_/CMAKE_ names from the environment
# into CMake cache variables (cmake/EnvVarForwarding.cmake), and four of them
# are read from the environment alone, where a build-backend config setting
# could not reach them: PYTORCH_BUILD_VERSION feeds the version metadata
# provider, MAX_JOBS is aliased by the scikit-build env table in
# pyproject.toml, LDFLAGS goes to CMake's linker detection, and
# PYTORCH_BLAS_USE_CBLAS_DOT is read through $ENV{} by
# 2001-force-cblas-complex-dot-for-openblas.patch.
export PYTORCH_BUILD_VERSION=%{pypi_version}
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
# TensorPipe builds the bundled libuv; PyTorch sets this in its own CMake code
# and the variable is not forwarded from the environment.
export TP_BUILD_LIBUV=ON

export LDFLAGS="-fuse-ld=lld %{build_ldflags}"
export CMAKE_LIBRARY_PATH=%{_libdir}
export CMAKE_PREFIX_PATH="%{_prefix}:%{_libdir}/cmake:%{python3_sitearch}"

# See 2001-force-cblas-complex-dot-for-openblas.patch
export PYTORCH_BLAS_USE_CBLAS_DOT=ON

%install -a
# Development SDK files belong to -devel, not the main package.
sed -i '\#%{python3_sitearch}/torch/include/#d;\#%{python3_sitearch}/torch/share/cmake/#d' \
    %{pyproject_files}

%check -a
# Default check only verifies that the built modules import.  Additionally run
# a small functional smoke against the just-built tree: real matmul, autograd,
# a training step, and a complex dot/vdot guard.
# The fork's own test suite is not run here: test/run_test.py blocklists most
# of it on riscv64 and the remaining failures are tracked in the fork's issues
# 33 and 34.
PYTHONPATH="%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}" \
PYTHONDONTWRITEBYTECODE=1 \
%{__python3} -sP %{SOURCE9}

%files -f %{pyproject_files}
%doc README.md NOTICE
%{_bindir}/torchfrtrace
%{_bindir}/torchrun

%files devel
%{python3_sitearch}/torch/include/
%{python3_sitearch}/torch/share/cmake/

%changelog
%autochangelog
