# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname triton

# Use the same RuyiAI LLVM commit as buddy-mlir so LLVM/MLIR versions match.
%global llvm_commit f346011a7ac59144fe085e0bc029cb24835f7a69
%global triton_riscv_commit 9ded1d4c19462dd13a9addef5551a4d09e7e3e97
%global triton_riscv_src triton-riscv-%{triton_riscv_commit}
%global buddy_version 0.1.4

%global bootstrap_llvm_maj_ver 22
%global bootstrap_llvm_bindir %{_libdir}/llvm%{bootstrap_llvm_maj_ver}/bin

# Build the bundled LLVM and the Triton extension with clang
%global toolchain clang
%global _lto_cflags %{nil}
%define _find_debuginfo_dwz_opts %{nil}

Name:           python-%{srcname}
Version:        3.9.0
Release:        %autorelease
Summary:        Language and compiler for custom deep-learning primitives
# Triton itself is MIT.  The statically bundled LLVM/MLIR/LLD is
# "Apache-2.0 WITH LLVM-exception OR NCSA"; nanobind is BSD-3-Clause
License:        MIT AND (Apache-2.0 WITH LLVM-exception OR NCSA) AND BSD-3-Clause
URL:            https://triton-lang.org/main/index.html
VCS:            git:https://github.com/triton-lang/triton.git
#!RemoteAsset:  sha256:78fc9ff4403a856dce609c8529b6f341a7aaf331c2582ed7167949b40f864cd5
Source0:        https://github.com/triton-lang/triton/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:d5e5a0b206ac7ff12b0deef16b5b3d289d9b6d151a8c4f2f35fc97588d149118
Source1:        https://codeload.github.com/RuyiAI-Stack/llvm-project/tar.gz/%{llvm_commit}#/llvm-project-%{llvm_commit}.tar.gz
#!RemoteAsset:  sha256:b59c65078650e0cac853b5df9a5a8756f701659660ebda215a6bdede79911317
Source2:        https://codeload.github.com/RuyiAI-Stack/triton-riscv/tar.gz/%{triton_riscv_commit}#/%{triton_riscv_src}.tar.gz
BuildSystem:    pyproject

# Unpack triton-riscv (Source2) before applying patches to both source trees.
BuildOption(prep):  -a 2
BuildOption(install):  -l %{srcname}
BuildOption(check):  -e 'triton.instrumentation.*'
BuildOption(check):  -e 'triton.plugins.*'
BuildOption(check):  -e 'triton.runtime.interpreter'
BuildOption(check):  -e 'triton.tools.mxfp'
# Optional NVIDIA GSan helpers need PyTorch and the disabled NVIDIA backend.
BuildOption(check):  -e 'triton.experimental.gsan*'
BuildOption(check):  -e 'triton.tools.gsan'
# Loaded via ctypes, not a Python extension module.
BuildOption(check):  -e 'triton.backends.amd.lib.libtriton_amd_codegen'

BuildRequires:  buddy-mlir = %{buddy_version}
BuildRequires:  buddy-mlir-llvm = %{buddy_version}
BuildRequires:  clang(major) = %{bootstrap_llvm_maj_ver}
BuildRequires:  compiler-rt(major) = %{bootstrap_llvm_maj_ver}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libstdc++-devel
BuildRequires:  lld(major) = %{bootstrap_llvm_maj_ver}
BuildRequires:  ninja
BuildRequires:  nlohmann-json
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(build)
BuildRequires:  python3dist(installer)
BuildRequires:  python3dist(nanobind) >= 2.10.2
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Requires:       buddy-mlir%{?_isa} = %{buddy_version}
Requires:       buddy-mlir-llvm%{?_isa} = %{buddy_version}
# CPU JIT compiles its launcher against Python headers with g++.
Requires:       gcc-c++
Requires:       pkgconfig(python3)
Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%patchlist
# Backport LLVM/MLIR API updates for newer LLVM (plus 3.9.0 GCNBuilder fix).
# https://github.com/triton-lang/triton/pull/12236
1001-newer-llvm-compatibility.patch
# Use system cmake/ninja and relax the pinned nanobind version.
2001-use-system-build-tools.patch
# Disable the NVIDIA backend while keeping shared dialects used by AMD and Gluon.
2002-disable-nvidia-backend.patch
# Find Buddy's LLVM tools for triton-riscv.
2003-triton-riscv-find-buddy-tools.patch
# Port pending LLVM/MLIR API updates for newer LLVM.
# https://github.com/triton-lang/triton/pull/12608
2004-newer-llvm-api-updates.patch
# Drop NVIDIA code from GPU instrumentation so AMD instrumentation still builds.
2005-remove-nvidia-from-gpu-instrumentation.patch

%description
Triton is a language and compiler for writing highly efficient custom
deep-learning primitives. It provides a Python programming interface and a
compiler stack that uses MLIR and LLVM. Triton kernels can run on AMD GPUs
or on CPUs through the triton_shared backend. The CPU backend uses Buddy's
LLVM tools. For AMD GPUs, Triton uses its own LLVM build from the same source
revision as Buddy.

%prep -a
tar -xf %{SOURCE1}
# Keep the Python wrappers for libdevice functions such as sin.
# triton_shared uses them to run these functions on the CPU.
cp -a third_party/nvidia/language/cuda python/triton/language/extra/
cp %{triton_riscv_src}/LICENSE LICENSE.triton-shared
# nanobind-static is compiled into libtriton from the system build dependency.
cp %{_datadir}/licenses/python-nanobind/LICENSE LICENSE.nanobind
sed -i 's|@BUDDY_LLVM_BINDIR@|%{_libdir}/buddy-mlir/llvm/bin|' \
    %{triton_riscv_src}/backend/paths.py

%generate_buildrequires
export TRITON_BUILD_PROTON=OFF
%pyproject_buildrequires

%build -p
export PATH="%{bootstrap_llvm_bindir}:${PATH}"
export CC="%{bootstrap_llvm_bindir}/clang"
export CXX="%{bootstrap_llvm_bindir}/clang++"

llvm_src="$(pwd)/llvm-project-%{llvm_commit}"
llvm_install="$(pwd)/llvm-install"

mem_gb=$(awk '/MemTotal/ {print int($2/1024/1024)}' /proc/meminfo)
compile_jobs=$(nproc)
mem_jobs=$(( 1 + mem_gb / 2 ))
[ "$mem_jobs" -lt "$compile_jobs" ] && compile_jobs=$mem_jobs
[ "$compile_jobs" -lt 1 ] && compile_jobs=1
link_jobs=$(( 1 + mem_gb / 16 ))
[ "$link_jobs" -lt 1 ] && link_jobs=1

llvm_targets="X86;RISCV;AMDGPU;NVPTX"

cmake -S "$llvm_src/llvm" -B "$llvm_src/build" -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX="$llvm_install" \
    -DCMAKE_C_COMPILER="$CC" \
    -DCMAKE_CXX_COMPILER="$CXX" \
    -DLLVM_USE_LINKER=lld \
    -DLLVM_ENABLE_PROJECTS="mlir;lld" \
    -DLLVM_TARGETS_TO_BUILD="$llvm_targets" \
    -DLLVM_ENABLE_ASSERTIONS=OFF \
    -DLLVM_ENABLE_DUMP=ON \
    -DBUILD_SHARED_LIBS=OFF \
    -DLLVM_BUILD_LLVM_DYLIB=OFF \
    -DLLVM_INSTALL_UTILS=ON \
    -DLLVM_ENABLE_ZSTD=ON \
    -DLLVM_INCLUDE_BENCHMARKS=OFF \
    -DLLVM_INCLUDE_EXAMPLES=OFF \
    -DLLVM_INCLUDE_TESTS=OFF \
    -DLLVM_PARALLEL_COMPILE_JOBS=$compile_jobs \
    -DLLVM_PARALLEL_LINK_JOBS=$link_jobs
cmake --build "$llvm_src/build" --target install -- -j$compile_jobs

# The AMD backend has a separate codegen library in Triton 3.9. Build it
# against the same source-built LLVM rather than fetching an upstream binary.
amd_backend="$PWD/third_party/amd/backend"
cmake -S "$amd_backend/codegen" -B amd-codegen-build -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX="$amd_backend" \
    -DLLVM_DIR="$llvm_install/lib/cmake/llvm" \
    -DTRITON_AMD_LLVM_REVISION=%{llvm_commit}
cmake --build amd-codegen-build --target install --parallel "$compile_jobs"
export TRITON_AMD_CODEGEN_PATH="$amd_backend/lib/libtriton_amd_codegen.so"

export LLVM_SYSPATH="$llvm_install"
export PATH="$llvm_install/bin:$PATH"
export JSON_SYSPATH="%{_prefix}"
export MAX_JOBS=$compile_jobs
export TRITON_PARALLEL_LINK_JOBS=$link_jobs
export TRITON_BUILD_WITH_CLANG_LLD=ON
export TRITON_BUILD_PROTON=OFF
export TRITON_PLUGIN_DIRS="$PWD/%{triton_riscv_src}"
export TRITON_OFFLINE_BUILD=1
# Triton builds with -Werror; do not fail on deprecated MLIR builder APIs.
export TRITON_APPEND_CMAKE_ARGS="-DTRITON_BUILD_TOOLS=OFF \
    -DTRITON_SHARED_BUILD_TRITON_SAN=OFF \
    -DLLVM_EXTERNAL_LIT=$llvm_src/llvm/utils/lit/lit.py \
    -DCMAKE_CXX_FLAGS_INIT=-Wno-error=deprecated-declarations"

%check -a
triton_cmake_dir=$(%{python3} -c 'from python.build_helpers import get_cmake_dir; print(get_cmake_dir())')
PATH="$PWD/llvm-install/bin:$PATH" %{python3} \
    llvm-project-%{llvm_commit}/llvm/utils/lit/lit.py -sv \
    --filter='Conversion/TritonToLinalg/' \
    "$triton_cmake_dir/third_party/triton_shared/test"

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%license llvm-project-%{llvm_commit}/llvm/LICENSE.TXT
%license LICENSE.triton-shared
%license LICENSE.nanobind

%changelog
%autochangelog
