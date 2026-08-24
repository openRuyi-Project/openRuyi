# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname triton

# Triton pins an exact, in-development LLVM *commit*
%global llvm_commit 1f126a6dea50d185c0781743a667390037ae88bd

%global bootstrap_llvm_maj_ver 22
%global bootstrap_llvm_bindir %{_libdir}/llvm%{bootstrap_llvm_maj_ver}/bin

# Build the bundled LLVM and the Triton extension with clang
%global toolchain clang
%global _lto_cflags %{nil}
%define _find_debuginfo_dwz_opts %{nil}

Name:           python-%{srcname}
Version:        3.7.1
Release:        %autorelease
Summary:        Language and compiler for custom deep-learning primitives
# Triton itself is MIT.  The statically bundled LLVM/MLIR/LLD is
# "Apache-2.0 WITH LLVM-exception OR NCSA"; pybind11 headers are BSD-3-Clause
License:        MIT AND (Apache-2.0 WITH LLVM-exception OR NCSA) AND BSD-3-Clause
URL:            https://triton-lang.org/main/index.html
VCS:            git:https://github.com/triton-lang/triton.git
#!RemoteAsset:  sha256:21cab714d4fc9579b728f4d597660c9598fbbd52c1154896c71d2d42f9b61626
Source0:        https://github.com/triton-lang/triton/releases/download/v%{version}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:b6aa9fbc954895bbd69374529593bbcdc4342b0812d8884698bbfd3d92d3426d
Source1:        https://codeload.github.com/llvm/llvm-project/tar.gz/%{llvm_commit}#/llvm-project-%{llvm_commit}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e 'triton.instrumentation.*'
BuildOption(check):  -e 'triton.plugins.*'
BuildOption(check):  -e 'triton.runtime.interpreter'
BuildOption(check):  -e 'triton.tools.mxfp'

BuildRequires:  clang(major) = %{bootstrap_llvm_maj_ver}
BuildRequires:  compiler-rt(major) = %{bootstrap_llvm_maj_ver}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  lld(major) = %{bootstrap_llvm_maj_ver}
BuildRequires:  ninja
BuildRequires:  nlohmann-json
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(pybind11)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(build)
BuildRequires:  python3dist(installer)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

%patchlist
# Link X86 codegen libraries on the riscv64 host.
2001-Add-riscv64-host-codegen-libraries.patch
# Use system-provided build tools instead of vendored copies.
2002-use-system-build-tools.patch
# Disable the NVIDIA backend (not relevant for the RISC-V target).
2003-disable-nvidia-backend.patch
# Keep pure-Python descriptor types used by common specialization code.
2004-Retain-NVIDIA-Gluon-descriptor-types.patch

%description
Triton is a language and compiler for writing highly efficient custom
deep-learning primitives. It provides a Python programming interface and a
compiler stack that lowers Triton kernels through MLIR and LLVM backends for
GPU execution.

%prep -a
tar -xf %{SOURCE1}

%generate_buildrequires
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

%ifarch x86_64
llvm_targets="X86;AMDGPU;NVPTX"
%endif
%ifarch riscv64
llvm_targets="RISCV;X86;AMDGPU;NVPTX"
%endif

cmake -S "$llvm_src/llvm" -B "$llvm_src/build" -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX="$llvm_install" \
    -DCMAKE_C_COMPILER="$CC" \
    -DCMAKE_CXX_COMPILER="$CXX" \
    -DLLVM_USE_LINKER=lld \
    -DLLVM_ENABLE_PROJECTS="mlir;lld" \
    -DLLVM_TARGETS_TO_BUILD="$llvm_targets" \
    -DLLVM_ENABLE_ASSERTIONS=OFF \
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

export LLVM_SYSPATH="$llvm_install"
export PATH="$llvm_install/bin:$PATH"
export JSON_SYSPATH="%{_prefix}"
export PYBIND11_SYSPATH="%{_prefix}"
export PYBIND11_CMAKE_DIR="%{_datadir}/cmake/pybind11"
export MAX_JOBS=$compile_jobs
export TRITON_PARALLEL_LINK_JOBS=$link_jobs
export TRITON_BUILD_WITH_CLANG_LLD=ON
export TRITON_BUILD_PROTON=OFF
export TRITON_CODEGEN_BACKENDS=amd
export TRITON_OFFLINE_BUILD=1
export TRITON_APPEND_CMAKE_ARGS="-DTRITON_BUILD_EXAMPLES=OFF -DTRITON_BUILD_TOOLS=OFF"

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%license llvm-project-%{llvm_commit}/llvm/LICENSE.TXT

%changelog
%autochangelog
