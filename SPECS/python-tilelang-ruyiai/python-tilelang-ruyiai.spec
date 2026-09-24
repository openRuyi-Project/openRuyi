# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 0b7d66eb8fc40607ef014e05e4927dffa11d0b03
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global srcname tilelang-riscv
%global pymodule tilelang

%global toolchain clang
%global _lto_cflags %nil

Name:           python-%{srcname}
Version:        20260921+git%{shortcommit}
Release:        %autorelease
Summary:        TileLang compiler backend for RISC-V platforms
License:        MIT AND Apache-2.0 AND (Apache-2.0 WITH LLVM-exception)
URL:            https://github.com/RuyiAI-Stack/tilelang-riscv
VCS:            git:https://github.com/RuyiAI-Stack/tilelang-riscv.git
#!RemoteAsset:  git+https://github.com/RuyiAI-Stack/tilelang-riscv#%{commit}
#!CreateArchive
Source0:        %{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(prep):  -n %{srcname}-%{version}

BuildOption(build):  -Ccmake.define.USE_CUDA=OFF
BuildOption(build):  -Ccmake.define.USE_ROCM=OFF
BuildOption(build):  -Ccmake.define.USE_METAL=OFF
BuildOption(build):  -Ccmake.define.USE_PYPI_Z3=OFF
BuildOption(build):  -Ccmake.define.TILELANG_RISCV_MLIR_MODE=ON
BuildOption(build):  -Ccmake.define.TILELANG_RISCV_LLVM_ROOT=%{_libdir}/buddy-mlir/llvm

BuildOption(install):  -L %{pymodule}

# Exclude NVIDIA GPU backends and plain shared libraries.
BuildOption(check):  -e 'tilelang.contrib.cutedsl*'
BuildOption(check):  -e 'tilelang.contrib.nvrtc'
BuildOption(check):  -e 'tilelang.jit.adapter.nvrtc*'
BuildOption(check):  -e 'tilelang.lib.libtilelang'
BuildOption(check):  -e 'tilelang.lib.libtvm'
# Exclude legacy tvm-script AST and parser modules package, tests or examples that not work
BuildOption(check):  -e 'tilelang.language.ast*'
BuildOption(check):  -e 'tilelang.language.parser*'

BuildRequires:  buddy-mlir-llvm-devel
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  ninja
BuildRequires:  patchelf
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  z3-devel
BuildRequires:  python3dist(apache-tvm-ffi)
BuildRequires:  python3dist(cloudpickle)
BuildRequires:  python3dist(ml-dtypes)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(z3-solver)

Requires:       buddy-mlir-llvm
Requires:       clang

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%patchlist
2001-allow-apache-tvm-ffi-0.1.10.patch
2002-use-system-build-dependencies.patch
2003-discover-buddy-mlir-toolchain.patch
2004-skip-z3-soname-rewrite.patch

%description
TileLang is a domain-specific language for writing high-performance kernels.
This package ships the RISC-V backend of TileLang: it lowers TVM TIR through
the structured MLIR Linalg/SCF/MemRef/Vector dialects to LLVM IR and native
RISC-V shared libraries, targeting native execution on machines such as the
SG2044.  The wheel carries the compiled TileLang and vendored TVM shared
libraries plus the Cython binding; the MLIR lowering engine is statically
linked from the buddy-mlir toolchain of the same LLVM source revision.

%generate_buildrequires
%pyproject_buildrequires

%build -p
export CC=clang
export CXX=clang++
export NO_VERSION_LABEL=1

%check -p
# Keep tvm-ffi from JIT-compiling its optional torch DLPack extension on
# first import; torch-c-dlpack-ext is not shipped on riscv64
export TVM_FFI_DISABLE_TORCH_C_DLPACK=1
# Using upstream riscv test suite.
%pytest testing/python/riscv/test_riscv_target_parse.py -q

%files -f %{pyproject_files}
%doc README.md
%license LICENSE THIRDPARTYNOTICES.txt

%changelog
%autochangelog
