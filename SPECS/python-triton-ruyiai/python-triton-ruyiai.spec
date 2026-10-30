# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname triton

%global triton_commit 58895270e6230491acc15fe7ba6d4c849e838db1
%global triton_ruyiai_tag nightly/20260913-da5291b
%global triton_ruyiai_short nightly-20260913-da5291b
%global triton_ruyiai_commit da5291ba589a8b0006d5b8ef5b9adf3b64719523
%global triton_ruyiai_shortcommit %(c=%{triton_ruyiai_commit}; echo ${c:0:7})

# The RISC-V lowering path is built with clang/lld; %%toolchain makes the
# pyproject stage's %%set_build_flags select them.
%global toolchain clang
# The prebuilt LLVM/MLIR toolchain is linked narrowly and the wheel is ~900 MB;
# keep the distribution defaults from adding LTO or running dwz over it.
%global _lto_cflags %{nil}
%global _find_debuginfo_dwz_opts %{nil}

Name:           python-%{srcname}-riscv
Version:        3.8.0+git%{triton_ruyiai_shortcommit}
Release:        %autorelease
Summary:        Triton compiler with the triton-riscv RISC-V backend
License:        MIT
URL:            https://github.com/RuyiAI-Stack/triton-riscv
VCS:            git:https://github.com/RuyiAI-Stack/triton-riscv.git
# Source0 is the exact upstream Triton commit the fork builds against; Source1
# is the triton-riscv plugin tree that provides the RISC-V backend.
#!RemoteAsset:  sha256:e841d695a4dfecb4ee7a97631b8dd1b54e63c7d9e39655a669368ae2a373addb
Source0:        https://github.com/triton-lang/triton/archive/%{triton_commit}/triton-%{triton_commit}.tar.gz
#!RemoteAsset:  sha256:f35f304c131f17d1892a79697328d37db80fda5edcad46e977a71d7f90e82206
Source1:        https://github.com/RuyiAI-Stack/triton-riscv/archive/refs/tags/%{triton_ruyiai_tag}.tar.gz#/triton-riscv-%{triton_ruyiai_short}.tar.gz
BuildSystem:    pyproject

# The upstream setup.py metadata has no PEP 639 License-File entries, so -L
# disables the %%pyproject_save_files license assertion; the MIT text is
# shipped explicitly via %%license below.
BuildOption(install):  -L %{srcname}

# These modules import torch, numpy or pytest at module import time. They are
# developer/GPU helpers, not runtime requirements of the compiler.
BuildOption(check):  -e 'triton._compile_warmup'
BuildOption(check):  -e 'triton._internal_testing'
BuildOption(check):  -e 'triton.experimental.gsan*'
# BuildOption(check):  -e 'triton.instrumentation.*'
# BuildOption(check):  -e 'triton.plugins.*'
BuildOption(check):  -e 'triton.runtime.interpreter'
BuildOption(check):  -e 'triton.tools.gsan'
BuildOption(check):  -e 'triton.tools.mxfp'

BuildRequires:  buddy-mlir-llvm
BuildRequires:  buddy-mlir-llvm-devel
BuildRequires:  buddy-mlir-llvm-static
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  lld
BuildRequires:  ninja
BuildRequires:  nlohmann-json
# BuildRequires:  patchelf
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(pybind11)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(build)
BuildRequires:  python3dist(installer)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Requires:       buddy-mlir
Requires:       buddy-mlir-llvm
# The RISC-V JIT links kernels through a RISC-V-capable C compiler driver.
Requires:       clang

# This package is an alternative provider of the `triton` module, not a
# rename of python-triton. %%python_provide would add
# `Obsoletes: python-triton`, turning the fork into a replacement of the
# upstream package; keep the explicit provides instead.
Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}

# Both packages ship the `triton` Python module and its python3dist(triton)
# capability; this fork is built from a specific commit and is not
# interchangeable with the ROCm-oriented python-triton build.
Conflicts:      python-%{srcname}

%patchlist
# Use the distribution's nanobind, CMake and Ninja instead of the upstream
# build-time pins and isolated build requirements. Applied to the Triton tree.
2001-use-system-build-tools.patch
# Locate the openRuyi Buddy MLIR/LLVM tools. Applied to the Source1 plugin tree.
2002-bake-system-tool-paths.patch

%description
Triton compiler built with the triton-riscv backend for RISC-V platforms.

triton-riscv (forked from triton-shared) integrates into upstream Triton as a
backend plugin. Triton acts as the frontend (Python AST -> TTIR); the
triton-riscv backend then lowers TTIR -> Linalg MLIR -> LLVM IR -> a native
RISC-V object file via the Buddy Compiler MLIR/LLVM toolchain. No NVIDIA or
AMD toolchain is required.

This package conflicts with python-triton because both ship the `triton` Python
module; install one or the other.

%prep
# A manual prep is required: the generated pyproject prep applies every
# patchlist entry to the Triton tree, but 2002 targets the Source1 plugin tree.
%autosetup -C -N

# Patchlist entry 0: the Triton tree.
%autopatch -p1 0

# Unpack the triton-riscv plugin tree beside the Triton source tree so its
# patches/ and backend/ trees are independent of Source0.
triton_riscv_dir=%{_builddir}/triton-riscv-%{triton_ruyiai_short}
rm -rf "$triton_riscv_dir"
tar -xf %{SOURCE1} -C %{_builddir}

# The plugin carries three patches that must be applied to the upstream Triton
# tree (scripts/apply_patches.sh does the same with git apply).
for p in "$triton_riscv_dir"/patches/*.patch; do
    %{__patch} -p1 -s --fuzz=0 --no-backup-if-mismatch -f < "$p"
done

# Patchlist entry 1: backend/compiler.py and backend/paths.py in Source1.
cd "$triton_riscv_dir"
%autopatch -p1 1

%generate_buildrequires
%pyproject_buildrequires

%build -p
export LLVM_SYSPATH=%{_libdir}/buddy-mlir/llvm
export LLVM_BINARY_DIR=$LLVM_SYSPATH/bin
export BUDDY_MLIR_BINARY_DIR=%{_bindir}
export JSON_SYSPATH=%{_prefix}
export PYBIND11_SYSPATH=%{_prefix}
export TRITON_OFFLINE_BUILD=1
export TRITON_BUILD_PROTON=OFF
export TRITON_BUILD_WITH_CLANG_LLD=ON
export TRITON_PLUGIN_DIRS=%{_builddir}/triton-riscv-%{triton_ruyiai_short}
# pip's own cache is redundant with the pyproject wheeldir and copying the
# ~900 MB wheel into it can fail on some filesystems.
export PIP_NO_CACHE_DIR=1

%build -a
# pip can leave the wheel only in its ephemeral build directory instead of
# --wheel-dir. Copy it to where %%pyproject_install looks for it.
# %%{buildsubdir} is not expanded in user sections at parse time; the build
# stage runs in the source tree, which is where %%pyproject_wheel writes.
wheeldir="$PWD/pyproject-wheeldir"
mkdir -p "$wheeldir"
if [ -z "$(ls "$wheeldir"/*.whl 2>/dev/null)" ]; then
    wheel="$(find . -name 'triton-*.whl' -type f -print -quit)"
    if [ -z "$wheel" ]; then
        echo "ERROR: pyproject_wheel produced no triton wheel" >&2
        exit 1
    fi
    cp "$wheel" "$wheeldir/"
fi

%install -a
# Source1 is a separate upstream work (MIT) whose code is installed into the
# triton_shared backend; ship its license text next to Triton's.
licensedir=%{buildroot}%{_defaultlicensedir}/%{name}
install -d "$licensedir"
install -p -m0644 %{_builddir}/triton-riscv-%{triton_ruyiai_short}/LICENSE \
    "$licensedir"/LICENSE.triton-riscv

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%license %{_defaultlicensedir}/%{name}/LICENSE.triton-riscv
# Console script generated from the triton.backends entry point; it is not
# part of %%{pyproject_files} unless +auto is used.
%{_bindir}/triton-shared-opt

%changelog
%autochangelog
