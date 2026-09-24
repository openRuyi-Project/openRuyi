# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 4e3d62d0e037dbf34b9a0267f1319c8e8d04dfbd
%global llvm_commit 2d26d272a0ff74b8c81eac0607b07f98b82ecc46

%global bootstrap_llvm_maj_ver 22
%global bootstrap_llvm_bindir %{_libdir}/llvm%{bootstrap_llvm_maj_ver}/bin

# Build tree of the pinned LLVM/MLIR, linked into the tools.
%global llvm_build %{_builddir}/llvm-build
%global llvm_prefix %{_libdir}/%{name}/llvm

# Build the pinned LLVM and buddy-mlir with clang.
%global toolchain clang
%global _lto_cflags %{nil}
%define _find_debuginfo_dwz_opts %{nil}

Name:           buddy-mlir
Version:        0.0.9
Release:        %autorelease
Summary:        MLIR-based compiler framework with RISC-V vector lowering passes
License:        Apache-2.0 AND (Apache-2.0 WITH LLVM-exception OR NCSA)
URL:            https://github.com/buddy-compiler/buddy-mlir
VCS:            git:https://github.com/buddy-compiler/buddy-mlir.git
#!RemoteAsset:  sha256:4c6be939b2d088bf963f6a2958431efefd15bec0373a11249612993d3b3efbcc
Source0:        https://codeload.github.com/buddy-compiler/buddy-mlir/tar.gz/%{commit}#/%{name}-%{commit}.tar.gz
#!RemoteAsset:  sha256:57494877cc36418887527744b4c92df4ac4518b9ccf2fed493db42464feb2fd9
Source1:        https://codeload.github.com/RuyiAI-Stack/llvm-project/tar.gz/%{llvm_commit}#/llvm-project-%{llvm_commit}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -G Ninja
BuildOption(conf):  -DBUDDY_ENABLE_TESTS=OFF
BuildOption(conf):  -DBUDDY_MLIR_ENABLE_PYTHON_PACKAGES=OFF
BuildOption(conf):  -DBUDDY_MLIR_ENABLE_RISCV_GNU_TOOLCHAIN=OFF
BuildOption(conf):  -DBUILD_SHARED_LIBS=OFF
BuildOption(conf):  -DLLVM_DIR=%{llvm_build}/lib/cmake/llvm
BuildOption(conf):  -DMLIR_DIR=%{llvm_build}/lib/cmake/mlir

BuildRequires:  clang(major) = %{bootstrap_llvm_maj_ver}
BuildRequires:  cmake
BuildRequires:  flatbuffers
BuildRequires:  flatbuffers-devel
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  lld(major) = %{bootstrap_llvm_maj_ver}
BuildRequires:  ninja
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(python3)

Provides:       %{name}-libs = %{version}-%{release}

%description
Buddy-MLIR is an MLIR-based compiler framework for DSL-to-DSA co-design. It
supplies dialects and passes for RISC-V vector (RVV) code generation; the
Triton-RISCV compiler stack uses it for the mid-end lowering between
triton-shared's Linalg output and LLVM IR.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Buddy-MLIR is an MLIR-based compiler framework for DSL-to-DSA co-design. It
supplies dialects and passes for RISC-V vector (RVV) code generation; the
Triton-RISCV compiler stack uses it for the mid-end lowering between
triton-shared's Linalg output and LLVM IR.

This package contains the interface headers and the CMake package file. The
file only sets the BUDDY_BINARY_DIR, BUDDY_MLIR_INTERFACE_DIR and
BUDDY_MLIR_LIB_DIR variables; upstream installs no CMake export set, so there
are no imported targets.

%package        llvm
Summary:        Pinned LLVM/MLIR toolchain for the Triton-RISCV stack
License:        Apache-2.0 WITH LLVM-exception

%description    llvm
The pinned LLVM/MLIR build (RuyiAI's llvm-project fork, branch riscv) that
buddy-mlir and the Triton-RISCV stack compile and link against. It is
installed under %{llvm_prefix} and is deliberately not the distribution LLVM:
the MLIR version has to match buddy-mlir exactly, and the fork carries the
RISC-V backend work the lowering emits code for. It is built statically, so the
tools in this package are self-contained.

%package        llvm-devel
Summary:        Development files of the pinned LLVM/MLIR toolchain
License:        Apache-2.0 WITH LLVM-exception
Requires:       %{name}-llvm%{?_isa} = %{version}-%{release}
Requires:       %{name}-llvm-static%{?_isa} = %{version}-%{release}

%description    llvm-devel
Headers and CMake package configuration for the pinned LLVM/MLIR build shipped
in %{name}-llvm. Point LLVM_SYSPATH (respectively LLVM_DIR and MLIR_DIR) at
%{llvm_prefix} to build against it.

%package        llvm-static
Summary:        Static libraries of the pinned LLVM/MLIR toolchain
License:        Apache-2.0 WITH LLVM-exception
Requires:       %{name}-llvm%{?_isa} = %{version}-%{release}

%description    llvm-static
The static LLVM/MLIR libraries of the pinned toolchain; they are what the
Triton-RISCV stack links against when it builds its tools from the
%{name}-llvm-devel configuration.

%prep -a
tar -xf %{SOURCE1}

# buddy-opt links MLIR's test-only transform libraries unconditionally. They
# are built from mlir/test/lib and gated on MLIR_INCLUDE_TESTS, which inherits
# the -DLLVM_INCLUDE_TESTS=OFF below; with tests off the targets do not exist,
# so CMake degrades the names to -l flags that the linker cannot resolve.
# Nothing in buddy-opt references a symbol from either library.
sed -i -e '/^[[:space:]]*MLIRTestTransforms$/d' \
       -e '/^[[:space:]]*MLIRTestTransformDialect$/d' \
       tools/buddy-opt/CMakeLists.txt

%conf -p
export PATH="%{bootstrap_llvm_bindir}:${PATH}"

OLD_CWD="$PWD"
cd llvm-project-%{llvm_commit}/llvm
%define _vpath_builddir %{llvm_build}
%cmake -G Ninja \
    -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_C_COMPILER="%{bootstrap_llvm_bindir}/clang" \
    -DCMAKE_CXX_COMPILER="%{bootstrap_llvm_bindir}/clang++" \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_INSTALL_PREFIX="%{llvm_prefix}" \
    -DLLVM_ENABLE_ASSERTIONS=OFF \
    -DLLVM_ENABLE_LIBXML2=OFF \
    -DLLVM_ENABLE_PROJECTS='mlir;clang' \
    -DLLVM_ENABLE_TERMINFO=OFF \
    -DLLVM_ENABLE_ZSTD=ON \
    -DLLVM_INCLUDE_BENCHMARKS=OFF \
    -DLLVM_INCLUDE_EXAMPLES=OFF \
    -DLLVM_INCLUDE_TESTS=ON \
    -DLLVM_INSTALL_UTILS=ON \
    -DLLVM_LINK_LLVM_DYLIB=OFF \
    -DLLVM_PARALLEL_LINK_JOBS=2 \
    -DLLVM_RAM_PER_COMPILE_JOB=2048 \
    -DLLVM_TARGETS_TO_BUILD="host;RISCV" \
    -DLLVM_USE_LINKER=lld \
    -DMLIR_ENABLE_BINDINGS_PYTHON=OFF \
    -DMLIR_ENABLE_EXECUTION_ENGINE=ON \
    -DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF
%cmake_build
cd "$OLD_CWD"

# Restore the build directory for the generated stages of buddy-mlir.
%define _vpath_builddir %{_target_platform}

%install -a
# Install the pinned LLVM/MLIR into its private prefix.
%define _vpath_builddir %{llvm_build}
%cmake_install
%define _vpath_builddir %{_target_platform}

# Keep the tree to what the stack consumes (tools, libraries, headers, CMake
# files); drop whatever else upstream installs, including stray top-level files.
find %{buildroot}%{llvm_prefix} -mindepth 1 -maxdepth 1 \
     ! -name bin ! -name lib ! -name include -exec rm -rf {} +

# LLVM's cmake modules also install the libraries built through
# add_mlir_library as a side effect of the tool install rules, and they land in
# both %{_prefix}/lib and %{_libdir} (LLVM_LIBDIR_SUFFIX handling), together
# with the aggregate objects next to them. Upstream ships no CMake export set,
# so nothing can link them through find_package(BuddyMLIR); the tools plus the
# interface headers and package file in -devel are what this package provides.
# Keep them in a -static subpackage instead if out-of-tree pass development is
# wanted. The sweep stays at the top level so it cannot descend into
# %{llvm_prefix}/lib, whose archives are packaged by -llvm-static.
find %{buildroot}%{_libdir} %{buildroot}%{_prefix}/lib -maxdepth 1 \
     -name '*.a' -delete
rm -rf %{buildroot}%{_prefix}/lib/objects-RelWithDebInfo

%check
# The tools the pipeline shells out to.
%{buildroot}%{_bindir}/buddy-opt --version
printf 'module {}\n' | %{buildroot}%{_bindir}/buddy-opt > /dev/null
%{buildroot}%{_bindir}/buddy-opt --help 2>&1 | grep -q -- '--lower-linalg-to-vir'
%{buildroot}%{_bindir}/buddy-translate --help > /dev/null
%{buildroot}%{_bindir}/buddy-llc --version > /dev/null

# The pinned LLVM must be able to emit RVV code for both the JIT and the AOT
# paths of the Triton-RISCV backend.
%{buildroot}%{llvm_prefix}/bin/llc --version | grep -q riscv64
cat > rvv-smoke.ll <<'EOF'
define void @smoke() {
  ret void
}
EOF
%{buildroot}%{llvm_prefix}/bin/llc -mtriple=riscv64 -mattr=+v \
    -filetype=asm rvv-smoke.ll -o rvv-smoke.s
grep -q 'ret' rvv-smoke.s

%files
%doc README.md
%license LICENSE
%license llvm-project-%{llvm_commit}/llvm/LICENSE.TXT
%{_bindir}/buddy-cli
%{_bindir}/buddy-frontendgen
%{_bindir}/buddy-llc
%{_bindir}/buddy-lsp-server
%{_bindir}/buddy-opt
%{_bindir}/buddy-server
%{_bindir}/buddy-translate
%{_bindir}/rax-inspect
%{_bindir}/rax-pack
%{_libdir}/libbuddy_external_rng.so

%files devel
%{_includedir}/buddy-mlir/
%{_libdir}/cmake/BuddyMLIR/

%files llvm
%license llvm-project-%{llvm_commit}/llvm/LICENSE.TXT
%dir %{_libdir}/%{name}
%dir %{llvm_prefix}
%{llvm_prefix}/bin/
%dir %{llvm_prefix}/lib
%{llvm_prefix}/lib/*.so.*
# clang's resource directory
%{llvm_prefix}/lib/clang/
%{llvm_prefix}/lib/libear/
%{llvm_prefix}/lib/libscanbuild/

%files llvm-devel
%{llvm_prefix}/include/
%{llvm_prefix}/lib/cmake/
%{llvm_prefix}/lib/*.so

%files llvm-static
%{llvm_prefix}/lib/*.a

%changelog
%autochangelog
