# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: jchzhou <zhoujiacheng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Originally extracted from Fedora Project
# Authors: The Fedora Project Contributors

%define _unpackaged_files_terminate_build 0

%global maj_ver 22
%global min_ver 1
%global patch_ver 5
#global rc_ver rc3

%bcond check 0

# Make sure that we are not building with a newer compiler than the targeted
# version. For example, if we build LLVM 19 with Clang 20, then we'd build
# LLVM libraries with Clang 20, and then the runtimes build would use the
# just-built Clang 19. Runtimes that link against LLVM libraries would then
# try to make Clang 19 perform LTO involving LLVM 20 bitcode.
%if %{defined host_clang_maj_ver}
%global __cc /usr/bin/clang-%{host_clang_maj_ver}
%global __cxx /usr/bin/clang++-%{host_clang_maj_ver}
%endif

# Suffixless tarball name (essentially: basename -s .tar.xz llvm-project-17.0.6.src.tar.xz)
%global src_tarball_dir llvm-project-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-%{rc_ver}}.src

%global build_ldflags %{?build_ldflags} -Wl,--build-id=sha1
%global build_cflags %{?build_cflags} -fno-lto
%global build_cxxflags %{?build_cxxflags} -fno-lto
%global build_fflags %{?build_fflags} -fno-lto

# llvm
# Apart from compiler-rt and libcxx, everything is installed into a
# version-specific prefix. Non-compat packages add symlinks to this prefix.
%global install_prefix %{_libdir}/llvm%{maj_ver}
%global install_bindir %{install_prefix}/bin
%global install_includedir %{install_prefix}/include
%global install_libdir %{install_prefix}/lib
%global install_datadir %{install_prefix}/share
%global install_mandir %{install_prefix}/share/man
%global install_libexecdir %{install_prefix}/libexec
%global install_python3mod %{install_libdir}/python%{python3_version}/site-packages
%global build_libdir llvm/%{_vpath_builddir}/%{_lib}
%global unprefixed_libdir %{_lib}
%global targets_to_build "X86;AMDGPU;NVPTX;BPF;WebAssembly;RISCV;AArch64"
%global experimental_targets_to_build ""
%global build_install_prefix %{buildroot}%{install_prefix}
%global llvm_triple %{_target_platform}

# clang

# compiler-rt
# pkg_name removed - using hardcoded names like clang

# openmp
%global so_suffix %{maj_ver}.%{min_ver}
%global libomp_arch %{_arch}

Name:           llvm%{maj_ver}
Version:        %{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:~%{rc_ver}}
Release:        %{autorelease}
Summary:        The Low Level Virtual Machine (%{maj_ver})
License:        Apache-2.0 WITH LLVM-exception OR NCSA
URL:            http://llvm.org
VCS:            git:https://github.com/llvm/llvm-project.git
#!RemoteAsset
Source0:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-%{rc_ver}}/%{src_tarball_dir}.tar.xz
#!RemoteAsset
Source1:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-%{rc_ver}}/%{src_tarball_dir}.tar.xz.sig

# please keep the patches in different groups for easier maintenance
Patch0:         0001-Add-riscv64-openruyi-linux-triple-and-set-it-to-rva2.patch

# clang patches

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  chrpath
BuildRequires:  ninja
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  binutils-devel

%ifarch %{valgrind_arches}
BuildRequires:  pkgconfig(valgrind)
%endif
BuildRequires:  pkgconfig(libedit)
# For %%py3_shebang_fix
BuildRequires:  pkgconfig(python3)
BuildRequires:  swig
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  doxygen
BuildRequires:  perl
BuildRequires:  pkgconfig(libffi)
BuildRequires:  libatomic
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(nanobind)
# for python buildrequires
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  pyproject-rpm-macros
# for tests
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(lib)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  procps-ng

Requires:       llvm%{maj_ver}-libs%{?_isa} = %{version}-%{release}
Provides:       llvm(major) = %{maj_ver}

%description
LLVM is a compiler infrastructure designed for compile-time, link-time,
runtime, and idle-time optimization of programs from arbitrary programming
languages. The compiler infrastructure includes mirror sets of programming
tools as well as libraries with equivalent functionality.

%package     -n llvm%{maj_ver}-devel
Summary:        Libraries and header files for LLVM (%{maj_ver})
Requires:       llvm%{maj_ver} = %{version}-%{release}
Requires:       llvm%{maj_ver}-libs = %{version}-%{release}
# The installed LLVM cmake files will add -ledit to the linker flags for any
# app that requires the libLLVMLineEditor, so we need to make sure
# libedit-devel is available.
Requires:       pkgconfig(libedit)
Requires:       pkgconfig(libzstd)
# The installed cmake files reference binaries from llvm-test, llvm-static, and
# llvm-gtest.
Requires:       llvm%{maj_ver}-static = %{version}-%{release}
Provides:       llvm-devel(major) = %{maj_ver}
Requires(post): chkconfig
Requires(postun): chkconfig

%description -n llvm%{maj_ver}-devel
This package contains library and header files needed to develop new native
programs that use the LLVM infrastructure.

%package     -n llvm%{maj_ver}-libs
Summary:        LLVM shared libraries (%{maj_ver})

%description -n llvm%{maj_ver}-libs
Shared libraries for the LLVM compiler infrastructure.

%package     -n llvm%{maj_ver}-static
Summary:        LLVM static libraries (%{maj_ver})
Provides:       llvm-static(major) = %{maj_ver}

%description -n llvm%{maj_ver}-static
Static libraries for the LLVM compiler infrastructure.

%package     -n llvm%{maj_ver}-cmake-utils
Summary:        CMake utilities shared across LLVM subprojects (%{maj_ver})

%description -n llvm%{maj_ver}-cmake-utils
CMake utilities shared across LLVM subprojects.
This is for internal use by LLVM packages only.

%package     -n clang%{maj_ver}
Summary:        A C language family front-end for LLVM (%{maj_ver})
Requires:       clang%{maj_ver}-libs%{?_isa} = %{version}-%{release}
# clang requires gcc, clang++ requires libstdc++-devel
Requires:       libstdc++-devel
Requires:       gcc-c++
Provides:       clang(major) = %{maj_ver}

%description -n clang%{maj_ver}
clang is a C language family front-end toolkit.
The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extensible.
Install compiler-rt if you want the Blocks C language extension or to
enable sanitization and profiling options when building, and
libomp-devel to enable -fopenmp.

%package     -n clang%{maj_ver}-libs
Summary:        Runtime library for clang (%{maj_ver})
Recommends:     compiler-rt%{maj_ver}%{?_isa} = %{version}-%{release}
Requires:       llvm%{maj_ver}-libs = %{version}-%{release}
# atomic support is not part of compiler-rt
Recommends:     libatomic%{?_isa}
# libomp-devel is required, so clang can find the omp.h header when compiling
# with -fopenmp.
Recommends:     libomp%{maj_ver}-devel%{_isa} = %{version}-%{release}
Recommends:     libomp%{maj_ver}%{_isa} = %{version}-%{release}

%description -n clang%{maj_ver}-libs
Runtime library for clang.

%package     -n clang%{maj_ver}-devel
Summary:        Development header files for clang (%{maj_ver})
Requires:       clang%{maj_ver}-libs = %{version}-%{release}
Requires:       clang%{maj_ver}%{?_isa} = %{version}-%{release}
# The clang CMake files reference tools from clang-tools-extra.
Requires:       clang%{maj_ver}-tools-extra%{?_isa} = %{version}-%{release}
# The clang cmake package depends on the LLVM cmake package.
Requires:       llvm%{maj_ver}-devel%{?_isa} = %{version}-%{release}
Provides:       clang-devel(major) = %{maj_ver}

%description -n clang%{maj_ver}-devel
Development header files for clang.

%package     -n clang%{maj_ver}-static
Summary:        Clang static libraries (%{maj_ver})
Requires:       clang%{maj_ver}-devel%{?_isa} = %{version}-%{release}
Provides:       clang-static(major) = %{maj_ver}

%description -n clang%{maj_ver}-static
Static libraries for Clang.

%package     -n clang%{maj_ver}-analyzer
Summary:        A source code analysis framework (%{maj_ver})
License:        Apache-2.0 WITH LLVM-exception OR NCSA OR MIT
Requires:       clang%{maj_ver} = %{version}-%{release}

%description -n clang%{maj_ver}-analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package     -n clang%{maj_ver}-tools-extra
Summary:        Extra tools for clang (%{maj_ver})
Requires:       clang%{maj_ver}-libs%{?_isa} = %{version}-%{release}

%description -n clang%{maj_ver}-tools-extra
A set of extra tools built using Clang's tooling API.

%package     -n clang%{maj_ver}-tools-extra-devel
Summary:        Development header files for clang tools (%{maj_ver})
Requires:       clang%{maj_ver}-tools-extra = %{version}-%{release}

%description -n clang%{maj_ver}-tools-extra-devel
Development header files for clang tools.

%package    -n python3-clang%{maj_ver}
Summary:        Python bindings for clang (%{maj_ver})
Requires:      clang%{maj_ver}-devel%{?_isa} = %{version}-%{release}
Requires:      python3

%description -n python3-clang%{maj_ver}
Python bindings for clang.

%package     -n flang%{maj_ver}
Summary:        A Fortran language family front-end for LLVM (%{maj_ver})
Provides:       flang(major) = %{maj_ver}

%description -n flang%{maj_ver}
Flang is a Fortran front-end for the LLVM compiler infrastructure.
It supports modern Fortran standards (Fortran 77, Fortran 90, Fortran 95,
Fortran 2003, Fortran 2008, and parts of Fortran 2018).
Flang is designed to be highly compatible with existing Fortran codebases
while providing excellent performance through LLVM's optimization
infrastructure. It integrates seamlessly with Clang and other LLVM tools
to provide a complete compilation solution for mixed-language projects.

%package     -n flang%{maj_ver}-static
Summary:        Flang static libraries (%{maj_ver})
Requires:       flang%{maj_ver}%{?_isa} = %{version}-%{release}
Provides:       flang-static(major) = %{maj_ver}

%description -n flang%{maj_ver}-static
Static libraries for the Flang Fortran front-end.

%package     -n compiler-rt%{maj_ver}
Summary:        LLVM "compiler-rt" runtime libraries (%{maj_ver})
License:        Apache-2.0 WITH LLVM-exception OR NCSA OR MIT
Provides:       compiler-rt(major) = %{maj_ver}

%description -n compiler-rt%{maj_ver}
The compiler-rt project is a part of the LLVM project. It provides
implementation of the low-level target-specific hooks required by
code generation, sanitizer runtimes and profiling library for code
instrumentation, and Blocks C language extension.

%package     -n libomp%{maj_ver}
Summary:        OpenMP runtime for clang (%{maj_ver})
URL:            http://openmp.llvm.org
Requires:       llvm%{maj_ver}-libs%{?_isa} = %{version}-%{release}
Provides:       libomp(major) = %{maj_ver}

%description -n libomp%{maj_ver}
OpenMP runtime for clang.

%package     -n libomp%{maj_ver}-devel
Summary:        OpenMP header files (%{maj_ver})
URL:            http://openmp.llvm.org
Requires:       libomp%{maj_ver}%{?_isa} = %{version}-%{release}
Provides:       libomp-devel(major) = %{maj_ver}

%description  -n libomp%{maj_ver}-devel
OpenMP header files.

%package      -n lld%{maj_ver}
Summary:        The LLVM Linker (%{maj_ver})
Requires(post):  chkconfig
Requires(preun): chkconfig
Provides:        lld(major) = %{maj_ver}

%description -n lld%{maj_ver}
The LLVM project linker.

%package     -n lld%{maj_ver}-devel
Summary:        Libraries and header files for LLD (%{maj_ver})
Requires:       lld%{maj_ver}%{?_isa} = %{version}-%{release}
Provides:       lld-devel(major) = %{maj_ver}

%description -n lld%{maj_ver}-devel
This package contains library and header files needed to develop new native
programs that use the LLD infrastructure.

%package      -n lldb%{maj_ver}
Summary:        Next generation high-performance debugger (%{maj_ver})
License:        Apache-2.0 WITH LLVM-exception OR NCSA
URL:            http://lldb.llvm.org/
Requires:       clang%{maj_ver}-libs%{?_isa} = %{version}-%{release}
Requires:       python3-lldb

%description -n lldb%{maj_ver}
LLDB is a next generation, high-performance debugger. It is built as a set
of reusable components which highly leverage existing libraries in the
larger LLVM Project, such as the Clang expression parser and LLVM
disassembler.

%package     -n lldb%{maj_ver}-devel
Summary:        Development header files for LLDB (%{maj_ver})
Requires:       lldb%{maj_ver}%{?_isa} = %{version}-%{release}

%description -n lldb%{maj_ver}-devel
The package contains header files for the LLDB debugger.

%package     -n python3-lldb
Summary:        Python module for LLDB (%{maj_ver})
Requires:       lldb%{maj_ver}%{?_isa} = %{version}-%{release}

%description -n python3-lldb
The package contains the LLDB Python module.

%package     -n mlir%{maj_ver}
Summary:        Multi-Level Intermediate Representation Overview (%{maj_ver})
License:        Apache-2.0 WITH LLVM-exception
URL:            http://mlir.llvm.org
Requires:       llvm%{maj_ver}-libs = %{version}-%{release}

%description -n mlir%{maj_ver}
The MLIR project is a novel approach to building reusable and extensible
compiler infrastructure. MLIR aims to address software fragmentation,
improve compilation for heterogeneous hardware, significantly reduce the
cost of building domain specific compilers, and aid in connecting
existing compilers together.

%package     -n mlir%{maj_ver}-static
Summary:        MLIR static files (%{maj_ver})
Requires:       mlir%{maj_ver}%{?_isa} = %{version}-%{release}

%description -n mlir%{maj_ver}-static
MLIR static files.

%package     -n mlir%{maj_ver}-devel
Summary:        MLIR development files (%{maj_ver})
Requires:       mlir%{maj_ver}%{?_isa} = %{version}-%{release}
Requires:       mlir%{maj_ver}-static%{?_isa} = %{version}-%{release}

%description -n mlir%{maj_ver}-devel
MLIR development files.

%package     -n python3-mlir%{maj_ver}
Summary:        MLIR python bindings (%{maj_ver})
Requires:       python3
Requires:       python3dist(numpy)

%description -n python3-mlir%{maj_ver}
MLIR python bindings.

%package     -n libcxx%{maj_ver}
Summary:        C++ standard library targeting C++11 (LLVM %{maj_ver})
License:        Apache-2.0 WITH LLVM-exception OR MIT OR NCSA
URL:            http://libcxx.llvm.org/
Requires:       libcxxabi%{maj_ver}%{?_isa} = %{version}-%{release}

%description -n libcxx%{maj_ver}
libc++ is a new implementation of the C++ standard library, targeting C++11 and above.
This package contains LLVM version %{maj_ver}.

%package     -n libcxx%{maj_ver}-devel
Summary:        Headers and libraries for libcxx%{maj_ver} development
Requires:       libcxx%{maj_ver}%{?_isa} = %{version}-%{release}
Requires:       libcxxabi%{maj_ver}-devel

%description -n libcxx%{maj_ver}-devel
Headers and libraries for libcxx%{maj_ver} development.
This package contains LLVM version %{maj_ver}.

%package     -n libcxx%{maj_ver}-static
Summary:        Static libraries for libcxx%{maj_ver}

%description -n libcxx%{maj_ver}-static
Static libraries for libcxx%{maj_ver}.
This package contains LLVM version %{maj_ver}.

%package     -n libcxxabi%{maj_ver}
Summary:        Low level support for a standard C++ library (LLVM %{maj_ver})

%description -n libcxxabi%{maj_ver}
libcxxabi provides low level support for a standard C++ library.
This package contains LLVM version %{maj_ver}.

%package     -n libcxxabi%{maj_ver}-devel
Summary:        Headers and libraries for libcxxabi%{maj_ver} development
Requires:       libcxxabi%{maj_ver}%{?_isa} = %{version}-%{release}

%description -n libcxxabi%{maj_ver}-devel
Headers and libraries for libcxxabi%{maj_ver} development.
This package contains LLVM version %{maj_ver}.

%package     -n libcxxabi%{maj_ver}-static
Summary:        Static libraries for libcxxabi%{maj_ver}

%description -n libcxxabi%{maj_ver}-static
Static libraries for libcxxabi%{maj_ver}.
This package contains LLVM version %{maj_ver}.

%package     -n llvm-libunwind%{maj_ver}
Summary:        LLVM libunwind (version %{maj_ver})

%description -n llvm-libunwind%{maj_ver}
LLVM libunwind is an implementation of the interface defined by the HP libunwind
project. It was contributed Apple as a way to enable clang++ to port to
platforms that do not have a system unwinder. It is intended to be a small and
fast implementation of the ABI, leaving off some features of HP's libunwind
that never materialized (e.g. remote unwinding).
This package contains LLVM version %{maj_ver}.

%package     -n llvm-libunwind%{maj_ver}-devel
Summary:        LLVM libunwind development files (version %{maj_ver})
Provides:       llvm-libunwind(major) = %{maj_ver}
Requires:       llvm-libunwind%{maj_ver}%{?_isa} = %{version}-%{release}

%description -n llvm-libunwind%{maj_ver}-devel
Development files for LLVM libunwind version %{maj_ver}.

%package     -n llvm-libunwind%{maj_ver}-static
Summary:        Static library for LLVM libunwind (version %{maj_ver})

%description -n llvm-libunwind%{maj_ver}-static
Static library for LLVM libunwind version %{maj_ver}.

%package     -n llvm-bolt%{maj_ver}
Summary:        A post-link optimizer developed to speed up large applications (%{maj_ver})
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/llvm/llvm-project/tree/main/bolt
# As hinted by bolt documentation
Recommends:     gperftools-devel

%description -n llvm-bolt%{maj_ver}
BOLT is a post-link optimizer developed to speed up large applications.
It achieves the improvements by optimizing application's code layout based on
execution profile gathered by sampling profiler, such as Linux `perf` tool.

%package     -n polly%{maj_ver}-devel
Summary:        Polly static and header files (%{maj_ver})

%description  -n polly%{maj_ver}-devel
Polly is a high-level loop and data-locality optimizer and optimization
infrastructure for LLVM. It uses an abstract mathematical representation based
on integer polyhedron to analyze and optimize the memory access pattern of a
program.

%prep
%autosetup -N -T -b 0 -n %{src_tarball_dir}
%autopatch -p1

%py3_shebang_fix \
    llvm/test/BugPoint/compile-custom.ll.py \
    llvm/tools/opt-viewer/*.py \
    llvm/utils/update_cc_test_checks.py
%py3_shebang_fix \
    clang-tools-extra/clang-tidy/tool/ \
    clang-tools-extra/clang-include-fixer/find-all-symbols/tool/run-find-all-symbols.py
%py3_shebang_fix \
    clang/tools/clang-format/ \
    clang/tools/clang-format/git-clang-format \
    clang/utils/hmaptool/hmaptool \
    clang/tools/scan-view/bin/scan-view \
    clang/tools/scan-view/share/Reporter.py \
    clang/tools/scan-view/share/startfile.py \
    clang/tools/scan-build-py/bin/* \
    clang/tools/scan-build-py/libexec/*
%py3_shebang_fix compiler-rt/lib/hwasan/scripts/hwasan_symbolize
%py3_shebang_fix libcxx/utils/

%build
%global projects clang;clang-tools-extra;lld
%global runtimes compiler-rt;openmp
%global projects %{projects};lldb
%global projects %{projects};mlir
%global projects %{projects};bolt
%global projects %{projects};polly
%global projects %{projects};flang
%global runtimes %{runtimes};libcxx;libcxxabi;libunwind
export ASMFLAGS="%{build_cflags}"
export FFLAGS=`echo %{build_fflags} | sed -e "s/-pipe//g" -e "s/-funwind-tables//g" -e "s/-fasynchronous-unwind-tables//g" -e "s/-fstack-protector-strong//g" -e "s/-fstack-clash-protection//g" -e "s/-Wformat//g" -e "s/-Werror=format-security//g"`
export FCFLAGS=${FFLAGS}

cd llvm
# Remember old values to reset to
OLD_PATH="$PATH"
OLD_LD_LIBRARY_PATH="$LD_LIBRARY_PATH"
OLD_CWD="$PWD"

# general cmake options
# Any ABI-affecting flags should be in here
%global cmake_common_args \\\
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \\\
    -DLLVM_ENABLE_RTTI=ON \\\
    -DLLVM_USE_PERF=ON \\\
    -DLLVM_TARGETS_TO_BUILD=%{targets_to_build} \\\
    -DBUILD_SHARED_LIBS=OFF \\\
    -DLLVM_BUILD_LLVM_DYLIB=ON \\\
    -DLLVM_LINK_LLVM_DYLIB=ON \\\
    -DCLANG_LINK_CLANG_DYLIB=ON \\\
    -DLLVM_ENABLE_FFI:BOOL=ON \\\
    -DLLVM_BINUTILS_INCDIR=/usr/include
%global cmake_common_args %{cmake_common_args} \\\
    -DLLVM_ENABLE_EH=OFF

%ifarch riscv64
%global cmake_common_args %{cmake_common_args} \\\
    -DLLVM_PARALLEL_LINK_JOBS=2
%endif

%global cmake_config_args %{cmake_common_args}
# clang options
%global cmake_config_args %{cmake_config_args} \\\
    -DCLANG_BUILD_EXAMPLES:BOOL=OFF \\\
    -DCLANG_CONFIG_FILE_SYSTEM_DIR=%{_sysconfdir}/clang%{maj_ver}/ \\\
    -DCLANG_DEFAULT_PIE_ON_LINUX=OFF \\\
    -DCLANG_DEFAULT_UNWINDLIB=libgcc \\\
    -DCLANG_ENABLE_STATIC_ANALYZER:BOOL=ON \\\
    -DCLANG_INCLUDE_DOCS:BOOL=ON \\\
    -DCLANG_INCLUDE_TESTS:BOOL=ON \\\
    -DCLANG_PLUGIN_SUPPORT:BOOL=ON \\\
    -DCLANG_REPOSITORY_STRING="%{?dist_vendor} %{version}-%{release}" \\\
    -DLLVM_EXTERNAL_CLANG_TOOLS_EXTRA_SOURCE_DIR=../clang-tools-extra

# compiler-rt options
%global cmake_config_args %{cmake_config_args} \\\
    -DCOMPILER_RT_INCLUDE_TESTS:BOOL=OFF 

# docs options
%global cmake_config_args %{cmake_config_args} \\\
    -DLLVM_ENABLE_DOXYGEN:BOOL=OFF \\\
    -DLLVM_ENABLE_SPHINX:BOOL=OFF \\\
    -DLLVM_BUILD_DOCS:BOOL=OFF

# lldb options
%global cmake_config_args %{cmake_config_args} -DLLDB_ENFORCE_STRICT_TEST_REQUIREMENTS:BOOL=ON

# libcxx options
%global cmake_config_args %{cmake_config_args}  \\\
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON \\\
    -DLIBCXX_INCLUDE_BENCHMARKS=OFF \\\
    -DLIBCXX_STATICALLY_LINK_ABI_IN_STATIC_LIBRARY=ON \\\
    -DLIBCXX_ENABLE_ABI_LINKER_SCRIPT=ON \\\
    -DLIBCXXABI_USE_LLVM_UNWINDER=OFF

# llvm options
%global cmake_config_args %{cmake_config_args}  \\\
    -DLLVM_APPEND_VC_REV:BOOL=OFF \\\
    -DLLVM_BUILD_EXAMPLES:BOOL=OFF \\\
    -DLLVM_BUILD_EXTERNAL_COMPILER_RT:BOOL=ON \\\
    -DLLVM_BUILD_RUNTIME:BOOL=ON \\\
    -DLLVM_BUILD_TOOLS:BOOL=ON \\\
    -DLLVM_BUILD_UTILS:BOOL=ON \\\
    -DLLVM_DEFAULT_TARGET_TRIPLE=%{llvm_triple} \\\
    -DLLVM_ENABLE_LIBCXX:BOOL=OFF \\\
    -DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=ON \\\
    -DLLVM_ENABLE_PROJECTS="%{projects}" \\\
    -DLLVM_ENABLE_RUNTIMES="%{runtimes}" \\\
    -DLLVM_ENABLE_ZLIB:BOOL=FORCE_ON \\\
    -DLLVM_ENABLE_ZSTD:BOOL=FORCE_ON \\\
    -DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD=%{experimental_targets_to_build} \\\
    -DLLVM_INCLUDE_BENCHMARKS=OFF \\\
    -DLLVM_INCLUDE_EXAMPLES:BOOL=OFF \\\
    -DLLVM_INCLUDE_TOOLS:BOOL=ON \\\
    -DLLVM_INCLUDE_UTILS:BOOL=ON \\\
    -DLLVM_INSTALL_TOOLCHAIN_ONLY:BOOL=OFF \\\
    -DLLVM_INSTALL_UTILS:BOOL=ON \\\
    -DLLVM_TOOLS_INSTALL_DIR:PATH=bin \\\
    -DLLVM_UNREACHABLE_OPTIMIZE:BOOL=OFF \\\
    -DLLVM_UTILS_INSTALL_DIR:PATH=bin \\\
    -DLLVM_ENABLE_LTO=OFF

# mlir options
%global cmake_config_args %{cmake_config_args} \\\
    -DMLIR_INCLUDE_DOCS:BOOL=ON \\\
    -DMLIR_INCLUDE_TESTS:BOOL=ON \\\
    -DMLIR_INCLUDE_INTEGRATION_TESTS:BOOL=OFF \\\
    -DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF \\\
    -DMLIR_BUILD_MLIR_C_DYLIB=ON \\\
    -DMLIR_ENABLE_BINDINGS_PYTHON:BOOL=ON

# openmp options
%global cmake_config_args %{cmake_config_args} \\\
    -DLIBOMP_INSTALL_ALIASES=OFF

# polly options
%global cmake_config_args %{cmake_config_args} \\\
    -DLLVM_POLLY_LINK_INTO_TOOLS=OFF

# test options
%global cmake_config_args %{cmake_config_args} \\\
    -DLLVM_BUILD_TESTS:BOOL=ON \\\
    -DLLVM_INCLUDE_TESTS:BOOL=ON \\\
    -DLLVM_INSTALL_GTEST:BOOL=ON \\\
    -DLLVM_LIT_ARGS="-vv"

# misc options
%global cmake_config_args %{cmake_config_args} \\\
    -DCMAKE_INSTALL_PREFIX=%{install_prefix} \\\
    -DENABLE_LINKER_BUILD_ID:BOOL=ON \\\
    -DPython3_EXECUTABLE=%{__python3}
# During the build, we use both the system clang and the just-built clang, and
# they need to use the system and just-built shared objects respectively. If
# we use LD_LIBRARY_PATH to point to our build directory, the system clang
# may use the just-built shared objects instead, which may not be compatible
# even if the version matches (e.g. when building compat libs or different rcs).
# Instead, we make use of rpath during the build and only strip it on
# installation using the CMAKE_SKIP_INSTALL_RPATH option.
%global cmake_config_args %{cmake_config_args} -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
%global cmake_config_args %{cmake_config_args} -DLLVM_VERSION_SUFFIX=''
%global cmake_config_args %{cmake_config_args} -DLLVM_RAM_PER_COMPILE_JOB=2048

extra_cmake_args=''
# https://github.com/llvm/llvm-project/issues/111492
if grep 'flags.*la57' /proc/cpuinfo; then
  extra_cmake_args="$extra_cmake_args -DOPENMP_TEST_ENABLE_TSAN=OFF"
fi

# Now reset paths and globals
function reset_paths {
    export PATH="$OLD_PATH"
    export LD_LIBRARY_PATH="$OLD_LD_LIBRARY_PATH"
}
reset_paths
cd $OLD_CWD

%global _vpath_srcdir .
%global __cmake_builddir %{_vpath_builddir}

%global extra_cmake_opts %{nil}

# Now let's build
%cmake -G Ninja %{cmake_config_args} %{extra_cmake_opts} $extra_cmake_args
# Build libLLVM.so first to avoid OOM errors.
%cmake_build --target LLVM
# Also build libclang-cpp.so separately to avoid OOM errors.
%cmake_build --target libclang-cpp.so
# Same for the three large MLIR dylibs.
%cmake_build --target libMLIR.so
%cmake_build --target libMLIR-C.so
%cmake_build --target libMLIRPythonCAPI.so
%cmake_build
# build the runtimes target here
%cmake_build --target runtimes

%install
# First install LLVM
pushd llvm
%cmake_install
popd

pushd %{buildroot}/%{install_bindir}
e_src=`realpath --relative-to=. %{buildroot}/%{install_datadir}/clang/clang-format-diff.py`
ln -sf ${e_src} clang-format-diff
popd

mkdir -p %{buildroot}/%{_bindir}
pushd %{buildroot}/%{_bindir}
for e in `ls %{buildroot}/%{install_bindir}`;do
  e_src=`realpath --relative-to=. %{buildroot}/%{install_bindir}/$e`
  ln -sf ${e_src} ${e}-%{maj_ver}
done
rm -f *-%{maj_ver}-%{maj_ver}
popd

mkdir -p %{buildroot}/%{_libdir}
pushd %{buildroot}/%{_libdir}
relpath=`realpath --relative-to=. %{buildroot}/%{install_libdir}`
for e in `ls %{buildroot}/%{install_libdir} | grep -e '-%{maj_ver}.so' -e '.so.%{maj_ver}'`;do
  ln -sf $relpath/${e} .
done
popd

mkdir -p %{buildroot}/%{install_python3mod}
#FIXME: why lldb install python mod here?
mv -f %{buildroot}/%{install_prefix}/lib64/python%{python3_version}/site-packages/* %{buildroot}/%{install_python3mod}
cp -a clang/bindings/python/clang %{buildroot}/%{install_python3mod}
mv -f %{buildroot}/%{install_prefix}/python_packages/mlir_core/mlir %{buildroot}/%{install_python3mod}

rm -rf %{buildroot}/%{install_includedir}/llvm-gtest
rm -rf %{buildroot}/%{install_includedir}/llvm-gmock
rm -rf %{buildroot}/%{install_prefix}/src
rm -f %{buildroot}/%{install_libdir}/libllvm_gtest*

%check

%post -n lld%{maj_ver}
update-alternatives --install %{_bindir}/ld ld %{_bindir}/ld.lld 1

%postun -n lld%{maj_ver}
if [ $1 -eq 0 ] ; then
  update-alternatives --remove ld %{_bindir}/ld.lld
fi

%define expand_bins() %{lua:
  local bindir = rpm.expand("%{_bindir}")
  local install_bindir = rpm.expand("%{install_bindir}")
  local maj_ver = rpm.expand("%{maj_ver}")
  for arg in rpm.expand("%*"):gmatch("%S+") do
    print(install_bindir .. "/" .. arg .. "\\n")
    print(bindir .. "/" .. arg .. "-" .. maj_ver .. "\\n")
  end
}
%define expand_generic(d:i:) %{lua:
  local dir = rpm.expand("%{-d*}")
  local install_dir = rpm.expand("%{-i*}")
  for arg in rpm.expand("%*"):gmatch("%S+") do
    print(install_dir .. "/" .. arg .. "\\n")
    print(dir .. "/" .. arg .. "\\n")
  end
}
%define expand_libs() %{expand_generic -d %{_libdir} -i %{install_libdir}  %*}

%files -n llvm%{maj_ver}
%license llvm/LICENSE.TXT
%{expand_bins %{expand:
    bugpoint
    dsymutil
    FileCheck
    llc
    lli
    llvm-addr2line
    llvm-ar
    llvm-as
    llvm-bcanalyzer
    llvm-bitcode-strip
    llvm-c-test
    llvm-cat
    llvm-cfi-verify
    llvm-cgdata
    llvm-cov
    llvm-ctxprof-util
    llvm-cvtres
    llvm-cxxdump
    llvm-cxxfilt
    llvm-cxxmap
    llvm-debuginfo-analyzer
    llvm-debuginfod
    llvm-debuginfod-find
    llvm-diff
    llvm-dis
    llvm-dlltool
    llvm-dwarfdump
    llvm-dwarfutil
    llvm-dwp
    llvm-exegesis
    llvm-extract
    llvm-gsymutil
    llvm-ifs
    llvm-install-name-tool
    llvm-jitlink
    llvm-jitlink-executor
    llvm-lib
    llvm-libtool-darwin
    llvm-link
    llvm-lipo
    llvm-lto
    llvm-lto2
    llvm-mc
    llvm-mca
    llvm-ml
    llvm-ml64
    llvm-modextract
    llvm-mt
    llvm-nm
    llvm-objcopy
    llvm-objdump
    llvm-opt-report
    llvm-otool
    llvm-pdbutil
    llvm-PerfectShuffle
    llvm-profdata
    llvm-profgen
    llvm-ranlib
    llvm-rc
    llvm-readelf
    llvm-readobj
    llvm-readtapi
    llvm-reduce
    llvm-remarkutil
    llvm-rtdyld
    llvm-sim
    llvm-size
    llvm-split
    llvm-stress
    llvm-strings
    llvm-strip
    llvm-symbolizer
    llvm-tblgen
    llvm-tli-checker
    llvm-undname
    llvm-windres
    llvm-xray
    reduce-chunk-list
    obj2yaml
    opt
    sancov
    sanstats
    split-file
    UnicodeNameMappingGenerator
    verify-uselistorder
    yaml2obj
    llvm-ir2vec
    llvm-offload-wrapper
    llvm-offload-binary
    count
    lli-child-target
    llvm-cas
    llvm-test-mustache-spec
    not
    yaml-bench
}}
%{install_datadir}/opt-viewer

%files -n llvm%{maj_ver}-libs
%license llvm/LICENSE.TXT
%{install_libdir}/libLLVM*.so*
%{install_libdir}/libLTO*.so*
%{install_libdir}/libRemarks*.so*
%{install_libdir}/LLVMgold.so
%{install_libdir}/LLVMPolly.so
%{_libdir}/libLLVM*.so*
%{_libdir}/libLTO*.so*
%{_libdir}/libRemarks*.so*

%files -n llvm%{maj_ver}-devel
%license llvm/LICENSE.TXT
%{install_bindir}/llvm-config
%{_bindir}/llvm-config-%{maj_ver}
%{install_includedir}/llvm
%{install_includedir}/llvm-c
%{install_libdir}/libLLVM.so
%{install_libdir}/cmake/llvm

%files -n llvm%{maj_ver}-static
%license llvm/LICENSE.TXT
%{install_libdir}/libLLVM*.a
%exclude %{install_libdir}/libLLVMTestingSupport.a
%exclude %{install_libdir}/libLLVMTestingAnnotations.a

%files -n clang%{maj_ver}
%license clang/LICENSE.TXT
%{expand_bins %{expand:
    clang
    clang++
    clang-cl
    clang-cpp
    clang-scan-deps
}}
%{install_bindir}/clang-%{maj_ver}
%{install_datadir}/clang

%files -n clang%{maj_ver}-libs
%license clang/LICENSE.TXT
%{install_libdir}/clang/%{maj_ver}/include/*
# Part of compiler-rt:
%exclude %{install_libdir}/clang/%{maj_ver}/include/fuzzer
%exclude %{install_libdir}/clang/%{maj_ver}/include/orc
%exclude %{install_libdir}/clang/%{maj_ver}/include/profile
%exclude %{install_libdir}/clang/%{maj_ver}/include/sanitizer
%exclude %{install_libdir}/clang/%{maj_ver}/include/xray
# Part of libomp-devel:
%exclude %{install_libdir}/clang/%{maj_ver}/include/omp*.h
%{install_libdir}/libclang.so.%{maj_ver}*
%{_libdir}/libclang.so.%{maj_ver}*
%{install_libdir}/libclang-cpp.so.%{maj_ver}*
%{_libdir}/libclang-cpp.so.%{maj_ver}*

%files -n clang%{maj_ver}-devel
%license clang/LICENSE.TXT
%{install_libdir}/cmake/clang
%{install_libdir}/libclang-cpp.so
%{install_libdir}/libclang.so
%{install_includedir}/clang
%{install_includedir}/clang-c
%expand_bins clang-tblgen
%dir %{install_datadir}/clang/

%files -n clang%{maj_ver}-static
%license clang/LICENSE.TXT
%{install_libdir}/libclang*.a
%{install_libdir}/libfindAllSymbols.a

%files -n clang%{maj_ver}-analyzer
%license clang/LICENSE.TXT
%{expand_bins %{expand:
    scan-view
    scan-build
    scan-build-py
    analyze-build
    intercept-build
}}
%{install_libexecdir}/ccc-analyzer
%{install_libexecdir}/c++-analyzer
%{install_libexecdir}/analyze-c++
%{install_libexecdir}/analyze-cc
%{install_libexecdir}/intercept-c++
%{install_libexecdir}/intercept-cc
%{install_datadir}/scan-view
%{install_datadir}/scan-build
%{install_datadir}/man/man1/scan-build.1
%{install_prefix}/lib/libear
%{install_prefix}/lib/libscanbuild

%files -n clang%{maj_ver}-tools-extra
%license clang-tools-extra/LICENSE.TXT
%{expand_bins %{expand:
    amdgpu-arch
    clang-apply-replacements
    clang-change-namespace
    clang-check
    clang-doc
    clang-extdef-mapping
    clang-format
    clang-include-cleaner
    clang-include-fixer
    clang-installapi
    clang-move
    clang-offload-bundler
    clang-offload-packager
    clang-linker-wrapper
    clang-nvlink-wrapper
    clang-query
    clang-refactor
    clang-reorder-fields
    clang-repl
    clang-sycl-linker
    clang-tidy
    clangd
    git-clang-format
    diagtool
    hmaptool
    nvptx-arch
    pp-trace
    c-index-test
    find-all-symbols
    modularize
    clang-format-diff
    run-clang-tidy
    offload-arch
}}
%{install_datadir}/clang/clang-format.py*
%{install_datadir}/clang/clang-format-diff.py*
%{install_datadir}/clang/clang-include-fixer.py*
%{install_datadir}/clang/clang-tidy-diff.py*
%{install_datadir}/clang/run-find-all-symbols.py*
%{install_datadir}/clang-doc

%files -n clang%{maj_ver}-tools-extra-devel
%license clang-tools-extra/LICENSE.TXT
%{install_includedir}/clang-tidy

%files -n python3-clang%{maj_ver}
%license clang/LICENSE.TXT
%{install_python3mod}/clang

%files -n flang%{maj_ver}
%license flang/LICENSE.TXT
%{expand_bins %{expand:
    bbc
    f18-parse-demo
    fir-lsp-server
    fir-opt
    flang
    flang-new
    tco
}}
%{install_bindir}/flang-%{maj_ver}
%{install_libdir}/cmake/flang
%{install_libdir}/clang/%{maj_ver}/lib/%{llvm_triple}/libflang_rt.*
%{install_includedir}/flang
%{install_includedir}/flang-rt

%files -n flang%{maj_ver}-static
%license flang/LICENSE.TXT
%{install_libdir}/libCUF*.a
%{install_libdir}/libFIR*.a
%{install_libdir}/libFlang*.a
%{install_libdir}/libFortran*.a
%{install_libdir}/libHLFIR*.a
%{install_libdir}/libMIFDialect.a
%{install_libdir}/libflang*.a

%files -n compiler-rt%{maj_ver}
%license compiler-rt/LICENSE.TXT
%ifarch x86_64 riscv64
%{install_libdir}/clang/%{maj_ver}/bin/hwasan_symbolize
%endif
%{install_libdir}/clang/%{maj_ver}/include/fuzzer
%{install_libdir}/clang/%{maj_ver}/include/orc
%{install_libdir}/clang/%{maj_ver}/include/profile
%{install_libdir}/clang/%{maj_ver}/include/sanitizer
%{install_libdir}/clang/%{maj_ver}/include/xray
%{install_libdir}/clang/%{maj_ver}/share/*.txt
# Files that appear on all targets
%{install_libdir}/clang/%{maj_ver}/lib/%{llvm_triple}/libclang_rt.*
%{install_libdir}/clang/%{maj_ver}/lib/%{llvm_triple}/clang_rt.crtbegin.o
%{install_libdir}/clang/%{maj_ver}/lib/%{llvm_triple}/clang_rt.crtend.o
%ifnarch riscv64
%{install_libdir}/clang/%{maj_ver}/lib/%{llvm_triple}/liborc_rt.a
%endif

%files -n libomp%{maj_ver}
%license openmp/LICENSE.TXT
%{install_libdir}/%{llvm_triple}/libomp.so
%{install_libdir}/%{llvm_triple}/libompd.so
%{install_libdir}/%{llvm_triple}/libarcher.so

%files -n libomp%{maj_ver}-devel
%license openmp/LICENSE.TXT
%{install_libdir}/clang/%{maj_ver}/include/omp.h
%{install_libdir}/clang/%{maj_ver}/include/ompx.h
%{install_libdir}/clang/%{maj_ver}/include/omp-tools.h
%{install_libdir}/clang/%{maj_ver}/include/ompt.h
%{install_libdir}/clang/%{maj_ver}/include/ompt-multiplex.h
%{install_libdir}/%{llvm_triple}/libarcher.so
%{install_libdir}/%{llvm_triple}/libarcher_static.a
%{install_libdir}/%{llvm_triple}/cmake/openmp
%{install_datadir}/gdb/python/ompd

%files -n lld%{maj_ver}
%license lld/LICENSE.TXT
%ghost %{_bindir}/ld
%{expand_bins %{expand:
    lld
    lld-link
    ld.lld
    ld64.lld
    wasm-ld
}}

%files -n lld%{maj_ver}-devel
%license lld/LICENSE.TXT
%{install_includedir}/lld
%{install_libdir}/liblldCOFF.a
%{install_libdir}/liblldCommon.a
%{install_libdir}/liblldELF.a
%{install_libdir}/liblldMachO.a
%{install_libdir}/liblldMinGW.a
%{install_libdir}/liblldWasm.a
%{install_libdir}/cmake/lld

%files -n lldb%{maj_ver}
%license lldb/LICENSE.TXT
%{expand_bins %{expand:
    lldb
    lldb-argdumper
    lldb-dap
    lldb-instr
    lldb-server
    lldb-mcp
}}
# Usually, *.so symlinks are kept in devel subpackages. However, the python
# bindings depend on this symlink at runtime.
%{expand_libs %{expand:
    liblldb.so.*
    liblldbIntelFeatures.so.*
}}
%{install_libdir}/liblldb*.so

%files -n lldb%{maj_ver}-devel
%{install_includedir}/lldb
%{expand_bins %{expand:
    lldb-tblgen
    yaml2macho-core
}}

%files -n python3-lldb
%{install_python3mod}/lldb

%files -n mlir%{maj_ver}
%license LICENSE.TXT
%{expand_libs %{expand:
    libmlir_arm_runner_utils.so.%{maj_ver}*
    libmlir_arm_sme_abi_stubs.so.%{maj_ver}*
    libmlir_async_runtime.so.%{maj_ver}*
    libmlir_c_runner_utils.so.%{maj_ver}*
    libmlir_float16_utils.so.%{maj_ver}*
    libmlir_runner_utils.so.%{maj_ver}*
    libmlir_apfloat_wrappers.so.%{maj_ver}*
    libMLIR*.so.%{maj_ver}*
}}

%files -n mlir%{maj_ver}-static
%{install_libdir}/libMLIR*.a

%files -n mlir%{maj_ver}-devel
%{expand_bins %{expand:
    mlir-linalg-ods-yaml-gen
    mlir-lsp-server
    mlir-opt
    mlir-pdll
    mlir-pdll-lsp-server
    mlir-query
    mlir-reduce
    mlir-rewrite
    mlir-runner
    mlir-tblgen
    mlir-translate
    tblgen-lsp-server
    tblgen-to-irdl
}}
%{install_includedir}/mlir
%{install_includedir}/mlir-c
%{install_libdir}/cmake/mlir
%{install_libdir}/libmlir_*.so
%{install_libdir}/libMLIR*.so

%files -n python3-mlir%{maj_ver}
%{install_python3mod}/mlir

%files -n libcxx%{maj_ver}
%license libcxx/LICENSE.TXT
%doc libcxx/CREDITS.TXT libcxx/TODO.TXT
%{install_libdir}/%{llvm_triple}/libc++.so.*

%files -n libcxx%{maj_ver}-devel
%{install_includedir}/c++/
%exclude %{install_includedir}/c++/v1/cxxabi.h
%exclude %{install_includedir}/c++/v1/__cxxabi_config.h
%{install_includedir}/%{llvm_triple}/c++/
%{install_libdir}/%{llvm_triple}/libc++.so
%{install_libdir}/%{llvm_triple}/libc++.modules.json
%{install_datadir}/libc++/v1/*

%files -n libcxx%{maj_ver}-static
%license libcxx/LICENSE.TXT
%{install_libdir}/%{llvm_triple}/libc++.a
%{install_libdir}/%{llvm_triple}/libc++experimental.a

%files -n libcxxabi%{maj_ver}
%license libcxxabi/LICENSE.TXT
%doc libcxxabi/CREDITS.TXT
%{install_libdir}/%{llvm_triple}/libc++abi.so.*

%files -n libcxxabi%{maj_ver}-devel
%{install_includedir}/c++/v1/cxxabi.h
%{install_includedir}/c++/v1/__cxxabi_config.h
%{install_libdir}/%{llvm_triple}/libc++abi.so

%files -n libcxxabi%{maj_ver}-static
%{install_libdir}/%{llvm_triple}/libc++abi.a

%files -n llvm-libunwind%{maj_ver}
%license libunwind/LICENSE.TXT
%{install_libdir}/%{llvm_triple}/libunwind.so.1
%{install_libdir}/%{llvm_triple}/libunwind.so.1.0

%files -n llvm-libunwind%{maj_ver}-devel
%{install_includedir}/__libunwind_config.h
%{install_includedir}/libunwind.h
%{install_includedir}/libunwind.modulemap
%{install_includedir}/mach-o/compact_unwind_encoding.h
%{install_includedir}/unwind.h
%{install_includedir}/unwind_arm_ehabi.h
%{install_includedir}/unwind_itanium.h
%{install_libdir}/%{llvm_triple}/libunwind.so

%files -n llvm-libunwind%{maj_ver}-static
%{install_libdir}/%{llvm_triple}/libunwind.a

%files -n llvm-bolt%{maj_ver}
%license bolt/LICENSE.TXT
%{expand_bins %{expand:
    llvm-bolt
    llvm-boltdiff
    llvm-bolt-binary-analysis
    llvm-bolt-heatmap
    merge-fdata
    perf2bolt
}}
%{install_libdir}/libbolt_rt_hugify.a
%{install_libdir}/libbolt_rt_instr.a

%files -n polly%{maj_ver}-devel
%license polly/LICENSE.TXT
%{install_libdir}/libPolly*.a
%{install_includedir}/polly
%{install_libdir}/cmake/polly

%changelog
%{?autochangelog}
