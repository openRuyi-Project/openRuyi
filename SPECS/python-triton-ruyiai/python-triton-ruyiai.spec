# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname triton

%global triton_commit 58895270e6230491acc15fe7ba6d4c849e838db1
%global triton_ruyiai_tag nightly/20260913-da5291b
%global triton_ruyiai_short nightly-20260913-da5291b
%global triton_ruyiai_tag_commit da5291ba589a8b0006d5b8ef5b9adf3b64719523
%global triton_ruyiai_tag_shortcommit %(c=%{triton_ruyiai_tag_commit}; echo ${c:0:7})

%global toolchain clang
%global _lto_cflags %{nil}
%define _find_debuginfo_dwz_opts %{nil}

Name:           python-%{srcname}-riscv
Version:        3.8.0+git%{triton_ruyiai_tag_shortcommit}
Release:        %autorelease
Summary:        Triton compiler with the triton-riscv RISC-V backend
License:        MIT
URL:            https://github.com/RuyiAI-Stack/triton-riscv
VCS:            git:https://github.com/RuyiAI-Stack/triton-riscv.git
#!RemoteAsset:  sha256:e841d695a4dfecb4ee7a97631b8dd1b54e63c7d9e39655a669368ae2a373addb
Source0:        https://github.com/triton-lang/triton/archive/%{triton_commit}/triton-%{triton_commit}.tar.gz
#!RemoteAsset:  sha256:f35f304c131f17d1892a79697328d37db80fda5edcad46e977a71d7f90e82206
Source1:        https://github.com/RuyiAI-Stack/triton-riscv/archive/refs/tags/%{triton_ruyiai_tag}.tar.gz#/triton-riscv-%{triton_ruyiai_short}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# Exclude modules that need a working CUDA/GPU runtime or pull heavy deps.
BuildOption(check):  -e 'triton.instrumentation.*'
BuildOption(check):  -e 'triton.plugins.*'
BuildOption(check):  -e 'triton.runtime.interpreter'
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
BuildRequires:  patchelf
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

Requires:  buddy-mlir
Requires:  buddy-mlir-llvm

Provides:  python3-%{srcname} = %{version}-%{release}
Provides:  python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}
Conflicts:  python-%{srcname}

%patchlist
2001-use-system-build-tools.patch

%description
Triton compiler built with the triton-riscv backend for RISC-V platforms.

triton-riscv (forked from triton-shared) integrates into upstream Triton as a
backend plugin. Triton acts as the frontend (Python AST -> TTIR); the
triton-riscv backend then lowers TTIR -> Linalg MLIR -> LLVM IR -> a native
RISC-V object file via the Buddy Compiler MLIR/LLVM toolchain. No NVIDIA or
AMD toolchain is required.

This package conflicts with python-triton because both ship the `triton` Python
module; install one or the other.

%prep -a
# Unpack Source1 (triton-riscv plugin source) beside the triton build tree.
tar -xf %{SOURCE1}

# Source1 expands to triton-riscv-<tag>/; normalise the directory name.
triton_ruyiai_dir="$(ls -d ../triton-riscv-* 2>/dev/null | head -1)"
[ -z "$triton_ruyiai_dir" ] && triton_ruyiai_dir="$(ls -d triton-riscv-* | head -1)"
triton_ruyiai_dir="$(cd "$triton_ruyiai_dir" && pwd)"

# Apply the 3 enabling patches carried in Source1 to the triton source tree.
# (apply_patches.sh does the same with `git apply`; release tarballs are not
# git repos, so use plain `patch -p1`.)
for p in "$triton_ruyiai_dir"/patches/*.patch; do
    patch -p1 < "$p"
done

# Apply the openRuyi-specific tool-path patch (2002) to the triton-riscv
# plugin source tree — it patches backend/compiler.py and backend/paths.py,
# which live in Source1, not in the triton source tree.
cd "$triton_ruyiai_dir"
patch -p1 < "%{_sourcedir}/2002-bake-system-tool-paths.patch"
cd -

# Expose the plugin source tree to triton's setup.py via TRITON_PLUGIN_DIRS.
# The pyproject macro reads this from the environment in the build stage.
export TRITON_PLUGIN_DIRS="$triton_ruyiai_dir"
# Persist it for subsequent sections by writing it to a sourced env file.
echo "export TRITON_PLUGIN_DIRS=\"$triton_ruyiai_dir\"" > .triton-riscv-env

%generate_buildrequires
%pyproject_buildrequires

%build -p
export LLVM_SYSPATH=/usr/lib64/buddy-mlir/llvm
export LLVM_BINARY_DIR=$LLVM_SYSPATH/bin
export BUDDY_MLIR_BINARY_DIR=/usr/bin
export JSON_SYSPATH=%{_prefix}
export PYBIND11_SYSPATH=%{_prefix}
export TRITON_OFFLINE_BUILD=1
export TRITON_BUILD_PROTON=OFF
export TRITON_BUILD_WITH_CLANG_LLD=ON
export TRITON_CODEGEN_BACKENDS=""
export TRITON_APPEND_CMAKE_ARGS="-DTRITON_BUILD_EXAMPLES=OFF -DTRITON_BUILD_TOOLS=OFF"
. ./.triton-riscv-env

# Disable pip's wheel cache so the built wheel lands in the pyproject
# wheeldir (not pip's ~/.cache), which is where the install macro looks
# for it. The wheel is ~900 MB; pip's atomic copy to the cache can fail
# silently on some filesystems, leaving the wheel only in cache.
export PIP_NO_CACHE_DIR=1

%build -a
# pip 26.x stores the built wheel in an ephemeral cache inside TMPDIR and may
# fail to copy it to the pyproject wheeldir (the 900 MB wheel triggers a
# silent copy failure on some filesystems). Find it and copy it to where the
# install macro expects it.
wheeldir="$(dirname "$PWD")/pyproject-wheeldir"
mkdir -p "$wheeldir"
if [ -z "$(ls "$wheeldir"/*.whl 2>/dev/null)" ]; then
    wheel="$(find . -name 'triton-*.whl' -type f 2>/dev/null | head -1)"
    if [ -n "$wheel" ]; then
        cp "$wheel" "$wheeldir/"
    fi
fi

%install
. ./.triton-riscv-env
%pyproject_install
%pyproject_save_files %{srcname}

# Sync the pure-Python backend driver files into the installed
# triton_shared backend package (mirrors rebuild-triton-riscv.sh).
dst=%{buildroot}%{python3_sitearch}/triton/backends/triton_shared
mkdir -p "$dst"
for f in compiler.py driver.py riscv.py paths.py; do
    cp -p "$TRITON_PLUGIN_DIRS/backend/$f" "$dst/"
done
# name.conf tells triton the backend's name; ship it too.
cp -p "$TRITON_PLUGIN_DIRS/backend/name.conf" "$dst/" 2>/dev/null || :

# Install the triton-shared-opt binary built by CMake.
opt_bin="$(find . -path '*/third_party/triton_shared/tools/triton-shared-opt/triton-shared-opt' -type f 2>/dev/null | head -1)"
if [ -n "$opt_bin" ]; then
    install -D -m755 "$opt_bin" %{buildroot}%{_bindir}/triton-shared-opt
    # Make its runtime linker path relative so it finds the triton .so next door.
    patchelf --set-rpath '$ORIGIN/../..' %{buildroot}%{_bindir}/triton-shared-opt || :
fi

%check

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/triton-shared-opt

%changelog
%autochangelog
