# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit        0b7d66eb8fc40607ef014e05e4927dffa11d0b03
%global shortcommit   %(c=%{commit}; echo ${c:0:7})

%global srcname       tilelang-riscv
%global pymodule      tilelang

# Submodule revisions pinned by upstream at the packaged commit.  The GitHub
# snapshot archive ships empty submodule directories, but the CMake configure
# step (3rdparty/tvm/cmake/config.cmake) and the TVM sources need the real
# trees: dmlc-core, rang (rang.hpp is included by src/ir/diagnostic.cc),
# tvm-ffi and DLPack.  The wheel also needs the TVM Python tree, so they are
# packaged as separate sources.
%global tvm_commit     882a774844993d103ae6e317ba3c7bbb5952b662
%global dmlc_commit    3031e4a61a98f49f07a42cfdec6242340fb2fd8c
%global rang_commit    cabe04d6d6b05356fa8f9741704924788f0dd762
%global tvmffi_commit  ae346ec92a3c386f1376064ae086aae72947c329
%global dlpack_commit  93c8f2a3c774b84af6f652b1992c48164fae60fc

# The RISC-V lowering path is built and exercised with clang.
%global toolchain     clang
# The upstream build does not enable LTO and links large LLVM/MLIR
# libraries; keep the distribution default from adding -flto.
%global _lto_cflags   %nil

# libtilelang.so and libtvm.so are private, unversioned libraries inside the
# Python package directory; do not publish them as global capabilities.
%global __provides_exclude_from ^%{python3_sitearch}/%{pymodule}/lib/

Name:           python-%{srcname}
Version:        0+git20261028.%{shortcommit}
Release:        %autorelease
Summary:        TileLang compiler backend for RISC-V platforms
License:        MIT AND Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-2-Clause AND Unlicense
URL:            https://github.com/RuyiAI-Stack/tilelang-riscv
VCS:            git:https://github.com/RuyiAI-Stack/tilelang-riscv.git
#!RemoteAsset:  sha256:6362cf79ae4c4f81fdba27f9dc747cf9dc71e0df1fbe4e389da54a7c7e51f06c
Source0:        %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz
#!RemoteAsset:  sha256:07b180fed34044c3d6dd874087fa2e75d8cb2ee32b0b98526e7be0f3b4f88e01
Source1:        https://github.com/TileLang/tvm/archive/%{tvm_commit}.tar.gz#/%{srcname}-tvm.tar.gz
#!RemoteAsset:  sha256:a382eb6fb7aa9dbabeeb06a49c8d68d9123aee32b4c4cc91b20987673360d703
Source2:        https://github.com/dmlc/dmlc-core/archive/%{dmlc_commit}.tar.gz#/%{srcname}-dmlc-core.tar.gz
#!RemoteAsset:  sha256:1f1cdf9016af45fbb37c8992041547c8ccc1edf2fc04d121d86c894c0e45a8b1
Source3:        https://github.com/agauniyal/rang/archive/%{rang_commit}.tar.gz#/%{srcname}-rang.tar.gz
#!RemoteAsset:  sha256:a4f9a6ba284265b0f8c6ca27913118819749418574cea33585cb0c116b1eb080
Source4:        https://github.com/apache/tvm-ffi/archive/%{tvmffi_commit}.tar.gz#/%{srcname}-tvm-ffi.tar.gz
#!RemoteAsset:  sha256:e54dc7852c06af7f748e58838236205574f2ad6264089cb1deb1831f9deac495
Source5:        https://github.com/dmlc/dlpack/archive/%{dlpack_commit}.tar.gz#/%{srcname}-dlpack.tar.gz
BuildSystem:    pyproject

BuildOption(build):  -Ccmake.define.USE_CUDA=OFF
BuildOption(build):  -Ccmake.define.USE_ROCM=OFF
BuildOption(build):  -Ccmake.define.USE_METAL=OFF
BuildOption(build):  -Ccmake.define.USE_PYPI_Z3=OFF
BuildOption(build):  -Ccmake.define.USE_LIBBACKTRACE=OFF
BuildOption(build):  -Ccmake.define.TILELANG_RISCV_MLIR_MODE=ON
BuildOption(build):  -Ccmake.define.TILELANG_RISCV_LLVM_ROOT=%{_libdir}/buddy-mlir/llvm
BuildOption(build):  -Ccmake.define.TVM_FFI_USE_LIBBACKTRACE=OFF
BuildOption(install):  -L %{pymodule}
# Exclude NVIDIA GPU backends and plain shared libraries.
BuildOption(check):  -e 'tilelang.contrib.cutedsl*'
BuildOption(check):  -e 'tilelang.contrib.nvrtc'
BuildOption(check):  -e 'tilelang.jit.adapter.nvrtc*'
BuildOption(check):  -e 'tilelang.lib.libtilelang'
BuildOption(check):  -e 'tilelang.lib.libtvm'
# Exclude legacy tvm-script AST and parser modules, which are not usable with
# the vendored TVM tree.
BuildOption(check):  -e 'tilelang.language.ast*'
BuildOption(check):  -e 'tilelang.language.parser*'

BuildRequires:  buddy-mlir-llvm-devel
BuildRequires:  clang
BuildRequires:  cmake
# version_provider.py shells out to git while computing the wheel version; the
# source archive has no .git, but the binary must still be available.
BuildRequires:  git
BuildRequires:  ninja
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(z3)
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

# The RISC-V JIT path invokes mlir-opt/llc/ld.lld from the buddy-mlir tree
# and falls back to clang on PATH.
Requires:       buddy-mlir-llvm
Requires:       clang

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%patchlist
# Allow the apache-tvm-ffi 0.1.10 packaged in openRuyi; upstream pins <0.1.10.
2001-allow-apache-tvm-ffi-0.1.10.patch
# Drop the patchelf build dependency and the unpackaged torch-c-dlpack-ext
# helper; openRuyi uses the system z3 and does not ship the helper.
2002-use-system-build-dependencies.patch
# Teach the runtime toolchain lookup the openRuyi buddy-mlir install prefix.
2003-discover-buddy-mlir-toolchain.patch
# Skip the z3 SONAME rewrite when linking against the system z3.
2004-skip-z3-soname-rewrite.patch
# TVM's config.cmake unconditionally sets TVM_FFI_USE_LIBBACKTRACE=ON after
# the command-line cache is populated; honor the spec's OFF choice instead of
# trying to build the missing libbacktrace submodule.
2005-honor-tvm-ffi-libbacktrace-off.patch

%description
TileLang is a domain-specific language for writing high-performance kernels.
This package ships the RISC-V backend of TileLang: it lowers TVM TIR through
the structured MLIR Linalg/SCF/MemRef/Vector dialects to LLVM IR and native
RISC-V shared libraries, targeting native execution on machines such as the
SG2044.  The package carries the compiled TileLang and TVM shared libraries,
the Cython binding, and the vendored TVM, DLPack, dmlc-core and tvm-ffi
sources needed to compile kernels, and it links its lowering engine against
the LLVM/MLIR toolchain provided by buddy-mlir.

%generate_buildrequires
%pyproject_buildrequires

# The submodule trees have to exist before the patches are applied (patches
# 2004 and 2005 touch the TVM submodule), so unpack them after the main archive
# and apply the patchlist explicitly; the generated prep stage would run too
# early.
%prep
%autosetup -n %{srcname}-%{commit} -N
mkdir -p 3rdparty/tvm/3rdparty/dmlc-core
mkdir -p 3rdparty/tvm/3rdparty/rang
mkdir -p 3rdparty/tvm/3rdparty/tvm-ffi/3rdparty/dlpack
tar xf %{SOURCE1} -C 3rdparty/tvm --strip-components=1
tar xf %{SOURCE2} -C 3rdparty/tvm/3rdparty/dmlc-core --strip-components=1
tar xf %{SOURCE3} -C 3rdparty/tvm/3rdparty/rang --strip-components=1
tar xf %{SOURCE4} -C 3rdparty/tvm/3rdparty/tvm-ffi --strip-components=1
tar xf %{SOURCE5} -C 3rdparty/tvm/3rdparty/tvm-ffi/3rdparty/dlpack --strip-components=1
%autopatch -p1

%build -p
# Keep the wheel version at VERSION; the RPM Version already carries the
# snapshot identifier and the upstream +cpu.git<hash> suffix adds nothing.
export NO_VERSION_LABEL=1

%install -a
# The wheel vendors TVM, dmlc-core, tvm-ffi and DLPack.  The uniquely named
# license files are copied by the relative %license entries below; the ones
# that share LICENSE/NOTICE basenames are installed with component-qualified
# names so they do not overwrite each other.
licensedir=%{buildroot}%{_defaultlicensedir}/%{name}
install -d "$licensedir"
install -pm 0644 3rdparty/tvm/LICENSE "$licensedir"/LICENSE.tvm
install -pm 0644 3rdparty/tvm/NOTICE "$licensedir"/NOTICE.tvm
install -pm 0644 3rdparty/tvm/3rdparty/dmlc-core/LICENSE "$licensedir"/LICENSE.dmlc-core
install -pm 0644 3rdparty/tvm/3rdparty/tvm-ffi/LICENSE "$licensedir"/LICENSE.tvm-ffi
install -pm 0644 3rdparty/tvm/3rdparty/tvm-ffi/NOTICE "$licensedir"/NOTICE.tvm-ffi
install -pm 0644 3rdparty/tvm/3rdparty/tvm-ffi/3rdparty/dlpack/LICENSE "$licensedir"/LICENSE.dlpack

%check -p
# Keep tvm-ffi from JIT-compiling its optional torch DLPack extension on
# first import; openRuyi does not ship torch-c-dlpack-ext.
export TVM_FFI_DISABLE_TORCH_C_DLPACK=1
# The test conftest prepends the source tree to the module search path, and the
# package then insists on the development layout next to it.  Point that layout
# at the installed wheel so the test exercises the built libraries.
mkdir -p build/tvm
rm -rf build/lib
ln -sfn %{buildroot}%{python3_sitearch}/%{pymodule}/lib build/lib

%check -a
# The remaining tests under testing/python/riscv need the vendored TileKernels
# kernels and RISC-V execution, which the build environment does not provide.
%pytest testing/python/riscv/test_riscv_target_parse.py -q

# The bundled include trees are consumed by the runtime JIT compiler; they are
# not public headers for linking, so they stay in the main package.
%files -f %{pyproject_files}
%doc README.md
%license LICENSE THIRDPARTYNOTICES.txt
# The uniquely named texts from the bundled trees are copied into the package
# license directory by rpmbuild.
%license 3rdparty/tvm/licenses/*
%license 3rdparty/tvm/3rdparty/tvm-ffi/licenses/*
# These share LICENSE/NOTICE basenames with the main package, so use the
# component-qualified copies installed above.
%license %{_defaultlicensedir}/%{name}/LICENSE.tvm
%license %{_defaultlicensedir}/%{name}/NOTICE.tvm
%license %{_defaultlicensedir}/%{name}/LICENSE.dmlc-core
%license %{_defaultlicensedir}/%{name}/LICENSE.tvm-ffi
%license %{_defaultlicensedir}/%{name}/NOTICE.tvm-ffi
%license %{_defaultlicensedir}/%{name}/LICENSE.dlpack

%changelog
%autochangelog
