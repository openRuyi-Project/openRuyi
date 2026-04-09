# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: jchzhou <zhoujiacheng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Originally extracted from Fedora Project
# Authors: The Fedora Project Contributors

%define _unpackaged_files_terminate_build 0

%global maj_ver 21
%global min_ver 1
%global patch_ver 7
#global rc_ver rc3

# Build compat packages llvmN instead of main package for the current LLVM
# version.
%bcond compat_build 0
# Bundle compat libraries for a previous LLVM version, as part of llvm-libs and
# clang-libs.
%bcond bundle_compat_lib 0
%bcond check 0
%if %{with bundle_compat_lib}
%global compat_maj_ver 20
%global compat_ver %{compat_maj_ver}.1.8
%endif
# Compat builds do not include python-lit
%if %{with compat_build}
%bcond python_lit 0
%else
%bcond python_lit 1
%endif
%bcond lldb 1

%bcond offload 0

%bcond sphinx 0

%if %{without compat_build} && 0%{?maj_ver} >= 22
%bcond mlir 1
%else
%bcond mlir 0
%endif
# The libcxx build condition also enables libcxxabi and libunwind.
%if %{without compat_build}
%bcond libcxx 1
%else
%bcond libcxx 0
%endif
# I've called the build condition "build_bolt" to indicate that this does not
# necessarily "use" BOLT in order to build LLVM.
%if %{without compat_build}
%ifarch x86_64
%bcond build_bolt 1
%else
%bcond build_bolt 0
%endif
%else
%bcond build_bolt 0
%endif
%if %{without compat_build}
%bcond polly 1
%else
%bcond polly 0
%endif
# Disable LTO on riscv in order to reduce memory consumption.
%ifarch riscv64
%bcond lto_build 0
%else
%bcond lto_build 1
%endif

%if %{without lto_build}
%global _lto_cflags %{nil}
%endif

# Make sure that we are not building with a newer compiler than the targeted
# version. For example, if we build LLVM 19 with Clang 20, then we'd build
# LLVM libraries with Clang 20, and then the runtimes build would use the
# just-built Clang 19. Runtimes that link against LLVM libraries would then
# try to make Clang 19 perform LTO involving LLVM 20 bitcode.
%if %{with compat_build}
%global host_clang_maj_ver %{maj_ver}
%endif
%if %{defined host_clang_maj_ver}
%global __cc /usr/bin/clang-%{host_clang_maj_ver}
%global __cxx /usr/bin/clang++-%{host_clang_maj_ver}
%endif
%bcond libedit 1

# Suffixless tarball name (essentially: basename -s .tar.xz llvm-project-17.0.6.src.tar.xz)
%global src_tarball_dir llvm-project-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-%{rc_ver}}.src

%global build_ldflags %{?build_ldflags} -Wl,--build-id=sha1

# llvm
%if %{with compat_build}
%global pkg_name_llvm llvm%{maj_ver}
%global pkg_suffix %{maj_ver}
%global exec_suffix -%{maj_ver}
%else
%global pkg_name_llvm llvm
%global pkg_suffix %{nil}
%global exec_suffix %{nil}
%endif
# Apart from compiler-rt and libcxx, everything is installed into a
# version-specific prefix. Non-compat packages add symlinks to this prefix.
%global install_prefix %{_libdir}/llvm%{maj_ver}
%global install_bindir %{install_prefix}/bin
%global install_includedir %{install_prefix}/include
%global install_libdir %{install_prefix}/%{_lib}
%global install_datadir %{install_prefix}/share
%global install_mandir %{install_prefix}/share/man
%global install_libexecdir %{install_prefix}/libexec
%global build_libdir llvm/%{_vpath_builddir}/%{_lib}
%global unprefixed_libdir %{_lib}
%global targets_to_build "X86;AMDGPU;NVPTX;BPF;WebAssembly;RISCV"
%global experimental_targets_to_build ""
%global build_install_prefix %{buildroot}%{install_prefix}
%global llvm_triple %{_target_platform}

# clang
%global pkg_name_clang clang%{pkg_suffix}

# compiler-rt
%global pkg_name_compiler_rt compiler-rt%{pkg_suffix}
# see https://sourceware.org/bugzilla/show_bug.cgi?id=25271
%global optflags %(echo %{optflags} -D_DEFAULT_SOURCE)
# see https://gcc.gnu.org/bugzilla/show_bug.cgi?id=93615
%global optflags %(echo %{optflags} -Dasm=__asm__)

# openmp
%global pkg_name_libomp libomp%{pkg_suffix}
%global so_suffix %{maj_ver}.%{min_ver}
%global libomp_arch %{_arch}
# lld
%global pkg_name_lld lld%{pkg_suffix}
# lldb
%global pkg_name_lldb lldb%{pkg_suffix}
# mlir
%global pkg_name_mlir mlir%{pkg_suffix}
# libcxx
%global pkg_name_libcxx libcxx
%global pkg_name_libcxxabi libcxxabi
%global pkg_name_llvm_libunwind llvm-libunwind
# bolt
%global pkg_name_bolt llvm-bolt%{pkg_suffix}
# polly
%global pkg_name_polly polly%{pkg_suffix}


Name:           %{pkg_name_llvm}
Version:        %{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:~%{rc_ver}}
Release:        %{autorelease}
Summary:        The Low Level Virtual Machine
License:        Apache-2.0 WITH LLVM-exception OR NCSA
URL:            http://llvm.org
VCS:            git:https://github.com/llvm/llvm-project.git
#!RemoteAsset
Source0:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-%{rc_ver}}/%{src_tarball_dir}.tar.xz
#!RemoteAsset
Source1:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-%{rc_ver}}/%{src_tarball_dir}.tar.xz.sig
%if %{without compat_build}
Source2:        macros.%{pkg_name_clang}
%endif
%if %{with bundle_compat_lib}
#!RemoteAsset
Source3000:     https://github.com/llvm/llvm-project/releases/download/llvmorg-%{compat_ver}/llvm-project-%{compat_ver}.src.tar.xz
#!RemoteAsset
Source3001:     https://github.com/llvm/llvm-project/releases/download/llvmorg-%{compat_ver}/llvm-project-%{compat_ver}.src.tar.xz.sig
%endif

# please keep the patches in different groups for easier maintenance

# clang patches
Patch0:         0001-PATCH-clang-Make-funwind-tables-the-default-on-all-a.patch
Patch1:         0003-PATCH-clang-Don-t-install-static-libraries.patch
# With the introduction of --gcc-include-dir in the clang config file,
# this might no longer be needed.
Patch2:         0001-Driver-Give-devtoolset-path-precedence-over-Installe.patch
Patch3:         0001-Add-riscv64-openruyi-linux-triple-and-set-it-to-rva2.patch
# lld patches
Patch100:       0001-19-Always-build-shared-libs-for-LLD.patch
# polly patches
Patch200:       0001-20-polly-shared-libs.patch
# Fix for offload builds: The DeviceRTL libraries target device code and
# don't support the mtls-dialect flag, so we need to patch the clang driver
# to ignore it for these targets.
Patch201:        0001-clang-Add-a-hack-to-fix-the-offload-build-with-the-m.patch

BuildRequires:  gcc15
BuildRequires:  gcc15-c++
# %%if %%{defined host_clang_maj_ver}
# BuildRequires:  clang(major) = %%{host_clang_maj_ver}
# %%else
# BuildRequires:  clang
# %%endif
BuildRequires:  cmake
BuildRequires:  chrpath
BuildRequires:  ninja
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  binutils-devel

%if %{with sphinx}
BuildRequires:  python3dist(sphinx)
%endif

%ifarch %{valgrind_arches}
BuildRequires:  pkgconfig(valgrind)
%endif
%if %{with libedit}
BuildRequires:  pkgconfig(libedit)
%endif
# For %%py3_shebang_fix
BuildRequires:  pkgconfig(python3)
BuildRequires:  swig
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  doxygen
%if %{with offload}
BuildRequires:  perl
BuildRequires:  perl-Data-Dumper
BuildRequires:  perl-Encode
BuildRequires:  pkgconfig(libffi)
%endif
BuildRequires:  libatomic
%if %{with mlir}
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(nanobind)
%endif
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

Requires:       %{pkg_name_llvm}-libs%{?_isa} = %{version}-%{release}
Provides:       llvm(major) = %{maj_ver}

%description
LLVM is a compiler infrastructure designed for compile-time, link-time,
runtime, and idle-time optimization of programs from arbitrary programming
languages. The compiler infrastructure includes mirror sets of programming
tools as well as libraries with equivalent functionality.

%if %{with python_lit}
%package     -n python-lit
Summary:        LLVM lit test runner for Python
BuildArch:      noarch
BuildRequires:  python3dist(psutil)
Provides:       python3-lit
%python_provide python3-lit

%description -n python-lit
lit is a tool used by the LLVM project for executing its test suites.
%endif

%package     -n %{pkg_name_llvm}-filesystem
Summary:        Filesystem package that owns the versioned llvm prefix
%if %{with compat_build}
Conflicts:      llvm-filesystem < %{maj_ver}.99
%endif

%description -n %{pkg_name_llvm}-filesystem
This packages owns the versioned llvm prefix directory: $libdir/llvm$version

%package     -n %{pkg_name_llvm}-devel
Summary:        Libraries and header files for LLVM
Requires:       %{pkg_name_llvm}%{?_isa} = %{version}-%{release}
Requires:       %{pkg_name_llvm}-libs%{?_isa} = %{version}-%{release}
# The installed LLVM cmake files will add -ledit to the linker flags for any
# app that requires the libLLVMLineEditor, so we need to make sure
# libedit-devel is available.
%if %{with libedit}
Requires:       pkgconfig(libedit)
%endif
Requires:       pkgconfig(libzstd)
# The installed cmake files reference binaries from llvm-test, llvm-static, and
# llvm-gtest.
Requires:       %{pkg_name_llvm}-static%{?_isa} = %{version}-%{release}
Requires:       %{pkg_name_llvm}-test%{?_isa} = %{version}-%{release}
Requires:       %{pkg_name_llvm}-googletest%{?_isa} = %{version}-%{release}
Provides:       llvm-devel(major) = %{maj_ver}
Requires(post): chkconfig
Requires(postun): chkconfig

%description -n %{pkg_name_llvm}-devel
This package contains library and header files needed to develop new native
programs that use the LLVM infrastructure.

%package     -n %{pkg_name_llvm}-doc
Summary:        Documentation for LLVM
BuildArch:      noarch
Requires:       %{pkg_name_llvm} = %{version}-%{release}

%description -n %{pkg_name_llvm}-doc
Documentation for the LLVM compiler infrastructure.

%package     -n %{pkg_name_llvm}-libs
Summary:        LLVM shared libraries
Requires:       %{pkg_name_llvm}-filesystem%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_llvm}-libs
Shared libraries for the LLVM compiler infrastructure.

%package     -n %{pkg_name_llvm}-static
Summary:        LLVM static libraries
Requires:       %{pkg_name_llvm}-filesystem%{?_isa} = %{version}-%{release}
Provides:       llvm-static(major) = %{maj_ver}

%description -n %{pkg_name_llvm}-static
Static libraries for the LLVM compiler infrastructure.

%package     -n %{pkg_name_llvm}-cmake-utils
Summary:        CMake utilities shared across LLVM subprojects
Requires:       %{pkg_name_llvm}-filesystem%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_llvm}-cmake-utils
CMake utilities shared across LLVM subprojects.
This is for internal use by LLVM packages only.

%package     -n %{pkg_name_llvm}-test
Summary:        LLVM regression tests
Requires:       %{pkg_name_llvm}%{?_isa} = %{version}-%{release}
Requires:       %{pkg_name_llvm}-libs%{?_isa} = %{version}-%{release}
Provides:       llvm-test(major) = %{maj_ver}

%description -n %{pkg_name_llvm}-test
LLVM regression tests.

%package     -n %{pkg_name_llvm}-googletest
Requires:       %{pkg_name_llvm}-filesystem%{?_isa} = %{version}-%{release}
Summary:        LLVM's modified googletest sources

%description -n %{pkg_name_llvm}-googletest
LLVM's modified googletest sources.

%package     -n %{pkg_name_clang}
Summary:        A C language family front-end for LLVM
Requires:       %{pkg_name_clang}-libs%{?_isa} = %{version}-%{release}
# clang requires gcc, clang++ requires libstdc++-devel
Requires:       libstdc++-devel
Requires:       gcc-c++
Provides:       clang(major) = %{maj_ver}

%description -n %{pkg_name_clang}
clang is a C language family front-end toolkit.
The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extensible.
Install compiler-rt if you want the Blocks C language extension or to
enable sanitization and profiling options when building, and
libomp-devel to enable -fopenmp.

%package     -n %{pkg_name_clang}-libs
Summary:        Runtime library for clang
Requires:       %{pkg_name_clang}-resource-filesystem%{?_isa} = %{version}-%{release}
Recommends:     %{pkg_name_compiler_rt}%{?_isa} = %{version}-%{release}
Requires:       %{pkg_name_llvm}-libs = %{version}-%{release}
# atomic support is not part of compiler-rt
Recommends:     libatomic%{?_isa}
# libomp-devel is required, so clang can find the omp.h header when compiling
# with -fopenmp.
Recommends:     %{pkg_name_libomp}-devel%{_isa} = %{version}-%{release}
Recommends:     %{pkg_name_libomp}%{_isa} = %{version}-%{release}

%description -n %{pkg_name_clang}-libs
Runtime library for clang.

%package     -n %{pkg_name_clang}-devel
Summary:        Development header files for clang
Requires:       %{pkg_name_clang}-libs = %{version}-%{release}
Requires:       %{pkg_name_clang}%{?_isa} = %{version}-%{release}
# The clang CMake files reference tools from clang-tools-extra.
Requires:       %{pkg_name_clang}-tools-extra%{?_isa} = %{version}-%{release}
# The clang cmake package depends on the LLVM cmake package.
Requires:       %{pkg_name_llvm}-devel%{?_isa} = %{version}-%{release}
Provides:       clang-devel(major) = %{maj_ver}

%description -n %{pkg_name_clang}-devel
Development header files for clang.

%package     -n %{pkg_name_clang}-resource-filesystem
Summary:        Filesystem package that owns the clang resource directory
Provides:       clang-resource-filesystem(major) = %{maj_ver}
%if %{with compat_build}
Conflicts:      clang-resource-filesystem < %{maj_ver}.99
%endif

%description -n %{pkg_name_clang}-resource-filesystem
This package owns the clang resouce directory: $libdir/clang/$version/

%package     -n %{pkg_name_clang}-analyzer
Summary:        A source code analysis framework
License:        Apache-2.0 WITH LLVM-exception OR NCSA OR MIT
Requires:       %{pkg_name_clang} = %{version}-%{release}

%description -n %{pkg_name_clang}-analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package     -n %{pkg_name_clang}-tools-extra
Summary:        Extra tools for clang
Requires:       %{pkg_name_clang}-libs%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_clang}-tools-extra
A set of extra tools built using Clang's tooling API.

%package     -n %{pkg_name_clang}-tools-extra-devel
Summary:        Development header files for clang tools
Requires:       %{pkg_name_clang}-tools-extra = %{version}-%{release}

%description -n %{pkg_name_clang}-tools-extra-devel
Development header files for clang tools.

%if %{without compat_build}
%package    -n python-clang
Summary:       Python bindings for clang
Requires:      %{pkg_name_clang}-devel%{?_isa} = %{version}-%{release}
Requires:      python3

%description -n python-clang
Python bindings for clang.
%endif

%package     -n %{pkg_name_compiler_rt}
Summary:        LLVM "compiler-rt" runtime libraries
License:        Apache-2.0 WITH LLVM-exception OR NCSA OR MIT
Requires:       %{pkg_name_clang}-resource-filesystem%{?_isa} = %{version}-%{release}
Provides:       compiler-rt(major) = %{maj_ver}

%description -n %{pkg_name_compiler_rt}
The compiler-rt project is a part of the LLVM project. It provides
implementation of the low-level target-specific hooks required by
code generation, sanitizer runtimes and profiling library for code
instrumentation, and Blocks C language extension.

%package     -n %{pkg_name_libomp}
Summary:        OpenMP runtime for clang
URL:            http://openmp.llvm.org
Requires:       %{pkg_name_llvm}-libs%{?_isa} = %{version}-%{release}
Provides:       libomp(major) = %{maj_ver}

%description -n %{pkg_name_libomp}
OpenMP runtime for clang.

%package     -n %{pkg_name_libomp}-devel
Summary:        OpenMP header files
URL:            http://openmp.llvm.org
Requires:       %{pkg_name_libomp}%{?_isa} = %{version}-%{release}
Requires:       %{pkg_name_clang}-resource-filesystem%{?_isa} = %{version}-%{release}
Provides:       libomp-devel(major) = %{maj_ver}

%description  -n %{pkg_name_libomp}-devel
OpenMP header files.

%package      -n %{pkg_name_lld}
Summary:         The LLVM Linker
Requires(post):  chkconfig
Requires(preun): chkconfig
Requires:        %{pkg_name_lld}-libs = %{version}-%{release}
Provides:        lld(major) = %{maj_ver}

%description -n %{pkg_name_lld}
The LLVM project linker.

%package     -n %{pkg_name_lld}-devel
Summary:        Libraries and header files for LLD
Requires:       %{pkg_name_lld}-libs%{?_isa} = %{version}-%{release}
%if %{without compat_build}
# lld tools are referenced in the cmake files, so we need to add lld as a
# dependency.
Requires:       %{pkg_name_lld}%{?_isa} = %{version}-%{release}
%endif
Provides:       lld-devel(major) = %{maj_ver}

%description -n %{pkg_name_lld}-devel
This package contains library and header files needed to develop new native
programs that use the LLD infrastructure.

%package     -n %{pkg_name_lld}-libs
Summary:        LLD shared libraries
Requires:       %{pkg_name_llvm}-libs%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_lld}-libs
Shared libraries for LLD.

%if %{with lldb}
%package      -n %{pkg_name_lldb}
Summary:        Next generation high-performance debugger
License:        Apache-2.0 WITH LLVM-exception OR NCSA
URL:            http://lldb.llvm.org/
Requires:       %{pkg_name_clang}-libs%{?_isa} = %{version}-%{release}
%if %{without compat_build}
Requires:       python3-lldb
%endif

%description -n %{pkg_name_lldb}
LLDB is a next generation, high-performance debugger. It is built as a set
of reusable components which highly leverage existing libraries in the
larger LLVM Project, such as the Clang expression parser and LLVM
disassembler.

%package     -n %{pkg_name_lldb}-devel
Summary:        Development header files for LLDB
Requires:       %{pkg_name_lldb}%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_lldb}-devel
The package contains header files for the LLDB debugger.

%if %{without compat_build}
%package     -n python3-lldb
Summary:        Python module for LLDB
Requires:       %{pkg_name_lldb}%{?_isa} = %{version}-%{release}

%description -n python3-lldb
The package contains the LLDB Python module.
%endif
%endif

%if %{with mlir}
%package     -n %{pkg_name_mlir}
Summary:        Multi-Level Intermediate Representation Overview
License:        Apache-2.0 WITH LLVM-exception
URL:            http://mlir.llvm.org
Requires:       %{pkg_name_llvm}-libs = %{version}-%{release}

%description -n %{pkg_name_mlir}
The MLIR project is a novel approach to building reusable and extensible
compiler infrastructure. MLIR aims to address software fragmentation,
improve compilation for heterogeneous hardware, significantly reduce
the cost of building domain specific compilers, and aid in connecting
existing compilers together.

%package     -n %{pkg_name_mlir}-static
Summary:        MLIR static files
Requires:       %{pkg_name_mlir}%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_mlir}-static
MLIR static files.

%package     -n %{pkg_name_mlir}-devel
Summary:        MLIR development files
Requires:       %{pkg_name_mlir}%{?_isa} = %{version}-%{release}
Requires:       %{pkg_name_mlir}-static%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_mlir}-devel
MLIR development files.

%package     -n python3-mlir
Summary:        MLIR python bindings
Requires:       python3
Requires:       python3dist(numpy)

%description -n python3-mlir
MLIR python bindings.
%endif

%if %{with libcxx}
%package     -n %{pkg_name_libcxx}
Summary:        C++ standard library targeting C++11
License:        Apache-2.0 WITH LLVM-exception OR MIT OR NCSA
URL:            http://libcxx.llvm.org/
Requires:       %{pkg_name_libcxxabi}%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_libcxx}
libc++ is a new implementation of the C++ standard library, targeting C++11 and above.

%package     -n %{pkg_name_libcxx}-devel
Summary:        Headers and libraries for %{pkg_name_libcxx} devel
Requires:       %{pkg_name_libcxx}%{?_isa} = %{version}-%{release}
Requires:       %{pkg_name_libcxxabi}-devel

%description -n %{pkg_name_libcxx}-devel
Headers and libraries for %{pkg_name_libcxx} devel.

%package     -n %{pkg_name_libcxx}-static
Summary:        Static libraries for %{pkg_name_libcxx}

%description -n %{pkg_name_libcxx}-static
Static libraries for %{pkg_name_libcxx}.

%package     -n %{pkg_name_libcxxabi}
Summary:        Low level support for a standard C++ library

%description -n %{pkg_name_libcxxabi}
libcxxabi provides low level support for a standard C++ library.

%package     -n %{pkg_name_libcxx}abi-devel
Summary:        Headers and libraries for %{pkg_name_libcxxabi} devel
Requires:       %{pkg_name_libcxxabi}%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_libcxxabi}-devel
Headers and libraries for %{pkg_name_libcxxabi} devel.

%package     -n %{pkg_name_libcxxabi}-static
Summary:        Static libraries for %{pkg_name_libcxxabi}

%description -n %{pkg_name_libcxxabi}-static
Static libraries for %{pkg_name_libcxxabi}.

%package     -n %{pkg_name_llvm_libunwind}
Summary:        LLVM libunwind

%description -n %{pkg_name_llvm_libunwind}
LLVM libunwind is an implementation of the interface defined by the HP libunwind
project. It was contributed Apple as a way to enable clang++ to port to
platforms that do not have a system unwinder. It is intended to be a small and
fast implementation of the ABI, leaving off some features of HP's libunwind
that never materialized (e.g. remote unwinding).

%package     -n %{pkg_name_llvm_libunwind}-devel
Summary:        LLVM libunwind development files
Provides:       %{pkg_name_llvm_libunwind}(major) = %{maj_ver}
Requires:       %{pkg_name_llvm_libunwind}%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_llvm_libunwind}-devel
Unversioned shared library for LLVM libunwind

%package     -n %{pkg_name_llvm_libunwind}-static
Summary:        Static library for LLVM libunwind

%description -n %{pkg_name_llvm_libunwind}-static
Static library for LLVM libunwind.
%endif

%if %{with build_bolt}
%package     -n %{pkg_name_bolt}
Summary:        A post-link optimizer developed to speed up large applications
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/llvm/llvm-project/tree/main/bolt
Requires:       %{pkg_name_llvm}-filesystem%{?_isa} = %{version}-%{release}
# As hinted by bolt documentation
Recommends:     gperftools-devel

%description -n %{pkg_name_bolt}
BOLT is a post-link optimizer developed to speed up large applications.
It achieves the improvements by optimizing application's code layout based on
execution profile gathered by sampling profiler, such as Linux `perf` tool.
%endif

%if %{with polly}
%package     -n %{pkg_name_polly}
Summary:        LLVM Framework for High-Level Loop and Data-Locality Optimizations
License:        Apache-2.0 WITH LLVM-exception
URL:            http://polly.llvm.org
Requires:       %{pkg_name_llvm}-libs = %{version}-%{release}

%description -n %{pkg_name_polly}
Polly is a high-level loop and data-locality optimizer and optimization
infrastructure for LLVM. It uses an abstract mathematical representation based
on integer polyhedron to analyze and optimize the memory access pattern of a
program.

%package     -n %{pkg_name_polly}-devel
Summary:        Polly header files
Requires:       %{pkg_name_polly} = %{version}-%{release}

%description  -n %{pkg_name_polly}-devel
Polly header files.
%endif

%prep
%if %{with bundle_compat_lib}
%setup -T -q -b 3000 -n llvm-project-%{compat_ver}.src
# Apply all patches
%autopatch -p1
%endif
%autosetup -N -T -b 0 -n %{src_tarball_dir}
# Apply all patches
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
# Compat builds don't build python bindings, but should still build man pages.
%if %{with compat_build}
sed -i 's/LLDB_ENABLE_PYTHON/TRUE/' lldb/docs/CMakeLists.txt
%endif
%if %{with libcxx}
%py3_shebang_fix libcxx/utils/
%endif
%if %{with python_lit}
%generate_buildrequires
cd llvm/utils/lit
%pyproject_buildrequires
%endif

%build
%global projects clang;clang-tools-extra;lld
%global runtimes compiler-rt;openmp
%if %{with lldb}
%global projects %{projects};lldb
%endif
%if %{with mlir}
%global projects %{projects};mlir
%endif
%if %{with build_bolt}
%global projects %{projects};bolt
%endif
%if %{with polly}
%global projects %{projects};polly
%endif
%if %{with libcxx}
%global runtimes %{runtimes};libcxx;libcxxabi;libunwind
%endif
%if %{with offload}
%global runtimes %{runtimes};offload
%endif
%global cfg_file_content --gcc-triple=%{_target_cpu}-openruyi-linux
%global cfg_file_content %{cfg_file_content} -gdwarf-4 -g0
export ASMFLAGS="%{build_cflags}"

cd llvm
# Remember old values to reset to
OLD_PATH="$PATH"
OLD_LD_LIBRARY_PATH="$LD_LIBRARY_PATH"
OLD_CWD="$PWD"

%if %{with python_lit}
pushd utils/lit
%pyproject_wheel
popd
%endif

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
%if %{maj_ver} >= 22
%global cmake_common_args %{cmake_common_args} \\\
    -DLLVM_ENABLE_EH=OFF
%else
%global cmake_common_args %{cmake_common_args} \\\
    -DLLVM_ENABLE_EH=ON
%endif

%global cmake_config_args %{cmake_common_args}
# clang options
%global cmake_config_args %{cmake_config_args} \\\
    -DCLANG_BUILD_EXAMPLES:BOOL=OFF \\\
    -DCLANG_CONFIG_FILE_SYSTEM_DIR=%{_sysconfdir}/%{pkg_name_clang}/ \\\
    -DCLANG_DEFAULT_PIE_ON_LINUX=OFF \\\
    -DCLANG_DEFAULT_UNWINDLIB=libgcc \\\
    -DCLANG_ENABLE_ARCMT:BOOL=ON \\\
    -DCLANG_ENABLE_STATIC_ANALYZER:BOOL=ON \\\
    -DCLANG_INCLUDE_DOCS:BOOL=ON \\\
    -DCLANG_INCLUDE_TESTS:BOOL=ON \\\
    -DCLANG_PLUGIN_SUPPORT:BOOL=ON \\\
    -DCLANG_REPOSITORY_STRING="%{?dist_vendor} %{version}-%{release}" \\\
    -DLLVM_EXTERNAL_CLANG_TOOLS_EXTRA_SOURCE_DIR=../clang-tools-extra
%if %{with compat_build}
%global cmake_config_args %{cmake_config_args} \\\
    -DCLANG_RESOURCE_DIR=../../../lib/clang/%{maj_ver}
%else
%global cmake_config_args %{cmake_config_args} \\\
    -DCLANG_RESOURCE_DIR=../lib/clang/%{maj_ver}
%endif

# compiler-rt options
%global cmake_config_args %{cmake_config_args} \\\
    -DCOMPILER_RT_INCLUDE_TESTS:BOOL=OFF \\\
    -DCOMPILER_RT_INSTALL_PATH=%{_prefix}/lib/clang/%{maj_ver}

# docs options
%global cmake_config_args %{cmake_config_args} \\\
    -DLLVM_ENABLE_DOXYGEN:BOOL=OFF \\\
    -DLLVM_ENABLE_SPHINX:BOOL=%{?with_sphinx:ON}%{!?with_sphinx:OFF} \\\
    -DLLVM_BUILD_DOCS:BOOL=%{?with_sphinx:ON}%{!?with_sphinx:OFF}
%if %{with sphinx}
# Build man-pages but no HTML docs using sphinx
%global cmake_config_args %{cmake_config_args} \\\
    -DSPHINX_EXECUTABLE=/usr/bin/sphinx-build-3 \\\
    -DSPHINX_OUTPUT_HTML:BOOL=OFF \\\
    -DSPHINX_OUTPUT_MAN:BOOL=ON \\\
    -DSPHINX_WARNINGS_AS_ERRORS=OFF
%endif

# lldb options
%if %{with lldb}
%if %{with compat_build}
%global cmake_config_args %{cmake_config_args} -DLLDB_ENABLE_PYTHON=OFF
%endif
%global cmake_config_args %{cmake_config_args} -DLLDB_ENFORCE_STRICT_TEST_REQUIREMENTS:BOOL=ON
%endif

# libcxx options
%if %{with libcxx}
%global cmake_config_args %{cmake_config_args}  \\\
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON \\\
    -DLIBCXX_INCLUDE_BENCHMARKS=OFF \\\
    -DLIBCXX_STATICALLY_LINK_ABI_IN_STATIC_LIBRARY=ON \\\
    -DLIBCXX_ENABLE_ABI_LINKER_SCRIPT=ON \\\
    -DLIBCXXABI_USE_LLVM_UNWINDER=OFF \\\
    -DLIBUNWIND_INSTALL_INCLUDE_DIR=%{_includedir}/llvm-libunwind
%global cmake_config_args %{cmake_config_args}  \\\
    -DLIBCXX_INSTALL_LIBRARY_DIR=%{_libdir} \\\
    -DLIBCXXABI_INSTALL_LIBRARY_DIR=%{_libdir} \\\
    -DLIBUNWIND_INSTALL_LIBRARY_DIR=%{_libdir}
%global cmake_config_args %{cmake_config_args}  \\\
    -DLIBCXX_INSTALL_INCLUDE_TARGET_DIR=%{_includedir}/c++/v1 \\\
    -DLIBCXX_INSTALL_INCLUDE_DIR=%{_includedir}/c++/v1 \\\
    -DLIBCXX_INSTALL_MODULES_DIR=%{_datadir}/libc++/v1 \\\
    -DLIBCXXABI_INSTALL_INCLUDE_DIR=%{_includedir}/c++/v1
%endif

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
    -DLLVM_PARALLEL_LINK_JOBS=1 \\\
    -DLLVM_TOOLS_INSTALL_DIR:PATH=bin \\\
    -DLLVM_UNREACHABLE_OPTIMIZE:BOOL=OFF \\\
    -DLLVM_UTILS_INSTALL_DIR:PATH=bin

# mlir options
%if %{with mlir}
%global cmake_config_args %{cmake_config_args} \\\
    -DMLIR_INCLUDE_DOCS:BOOL=ON \\\
    -DMLIR_INCLUDE_TESTS:BOOL=ON \\\
    -DMLIR_INCLUDE_INTEGRATION_TESTS:BOOL=OFF \\\
    -DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF \\\
    -DMLIR_BUILD_MLIR_C_DYLIB=ON \\\
    -DMLIR_ENABLE_BINDINGS_PYTHON:BOOL=ON
%endif

# openmp options
%global cmake_config_args %{cmake_config_args} \\\
    -DOPENMP_INSTALL_LIBDIR=%{unprefixed_libdir} \\\
    -DLIBOMP_INSTALL_ALIASES=OFF
%if %{maj_ver} >= 22 && %{with offload}
# We reset the cxxflags to "" here because this is compiling for a GPU
# target, where our cflags are either questionable or actively wrong.
%global cmake_config_args %{cmake_config_args} \\\
    -DLLVM_RUNTIME_TARGETS='default;amdgcn-amd-amdhsa;nvptx64-nvidia-cuda' \\\
    -DRUNTIMES_nvptx64-nvidia-cuda_LLVM_ENABLE_RUNTIMES=openmp \\\
    -DRUNTIMES_amdgcn-amd-amdhsa_LLVM_ENABLE_RUNTIMES=openmp \\\
    -DRUNTIMES_amdgcn-amd-amdhsa_CMAKE_CXX_FLAGS="" \\\
    -DRUNTIMES_nvptx64-nvidia-cuda_CMAKE_CXX_FLAGS=""
# https://github.com/llvm/llvm-project/issues/159762
%global cmake_config_args %{cmake_config_args} \\\
    -DRUNTIMES_nvptx64-nvidia-cuda_LLVM_LIBDIR_SUFFIX=64
%endif

# polly options
%if %{with polly}
%global cmake_config_args %{cmake_config_args} \\\
    -DLLVM_POLLY_LINK_INTO_TOOLS=OFF
%endif

# test options
%global cmake_config_args %{cmake_config_args} \\\
    -DLLVM_BUILD_TESTS:BOOL=ON \\\
    -DLLVM_INCLUDE_TESTS:BOOL=ON \\\
    -DLLVM_INSTALL_GTEST:BOOL=ON \\\
    -DLLVM_LIT_ARGS="-vv"
%if %{with lto_build}
%global cmake_config_args %{cmake_config_args} -DLLVM_UNITTEST_LINK_FLAGS="-fno-lto"
%endif

# misc options
%global cmake_config_args %{cmake_config_args} \\\
    -DCMAKE_INSTALL_PREFIX=%{install_prefix} \\\
    -DENABLE_LINKER_BUILD_ID:BOOL=ON \\\
    -DPython3_EXECUTABLE=%{__python3}
%if %{with offload}
%global cmake_config_args %{cmake_config_args} \\\
    -DOFFLOAD_INSTALL_LIBDIR=%{unprefixed_libdir}
%endif
# During the build, we use both the system clang and the just-built clang, and
# they need to use the system and just-built shared objects respectively. If
# we use LD_LIBRARY_PATH to point to our build directory, the system clang
# may use the just-built shared objects instead, which may not be compatible
# even if the version matches (e.g. when building compat libs or different rcs).
# Instead, we make use of rpath during the build and only strip it on
# installation using the CMAKE_SKIP_INSTALL_RPATH option.
%global cmake_config_args %{cmake_config_args} -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \\\
    %{cmake_config_args} -DLLVM_LIBDIR_SUFFIX=64
%if %{without compat_build}
%global cmake_config_args %{cmake_config_args} -DLLVM_VERSION_SUFFIX=''
%endif
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
%if %{with mlir}
%cmake_build --target libMLIR.so
%cmake_build --target libMLIR-C.so
%cmake_build --target libMLIRPythonCAPI.so
%endif
%cmake_build
# build the runtimes target here
%cmake_build --target runtimes

# compat lib build
cd ..
%if %{with bundle_compat_lib}
%if %{compat_maj_ver} >= 22
%global compat_lib_cmake_args -DLLVM_ENABLE_EH=OFF
%else
%global compat_lib_cmake_args -DLLVM_ENABLE_EH=ON
%endif
%cmake -S ../llvm-project-%{compat_ver}.src/llvm -B ../llvm-compat-libs -G Ninja \
    -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_libdir}/llvm%{compat_maj_ver}/ \
    -DCMAKE_SKIP_RPATH=ON \
    -DLLVM_ENABLE_PROJECTS="clang;lldb" \
    -DLLVM_INCLUDE_BENCHMARKS=OFF \
    -DLLVM_INCLUDE_TESTS=OFF \
    %{cmake_common_args} \
    %{compat_lib_cmake_args}
%ninja_build -C ../llvm-compat-libs LLVM
%ninja_build -C ../llvm-compat-libs libclang.so
%ninja_build -C ../llvm-compat-libs libclang-cpp.so
%ninja_build -C ../llvm-compat-libs liblldb.so
%endif

%install
# First install LLVM
pushd llvm
%if %{with python_lit}
pushd utils/lit
%pyproject_install
# Strip out #!/usr/bin/env python
sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python3_sitelib}/lit/*.py
popd
%endif
%cmake_install
popd
mkdir -p %{buildroot}/%{_bindir}
# Install binaries needed for lit tests
%global test_binaries llvm-isel-fuzzer llvm-opt-fuzzer
for f in %{test_binaries}
do
    install -m 0755 llvm/%{_vpath_builddir}/bin/$f %{buildroot}%{install_bindir}
    chrpath --delete %{buildroot}%{install_bindir}/$f
done
# Install libraries needed for unittests
install %{build_libdir}/libLLVMTestingSupport.a %{buildroot}%{install_libdir}
install %{build_libdir}/libLLVMTestingAnnotations.a %{buildroot}%{install_libdir}
%if %{without compat_build}
%else
# Create ld.so.conf.d entry
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
cat >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{pkg_name_llvm}-%{_arch}.conf << EOF
%{install_libdir}
EOF
%endif
mkdir -p %{buildroot}%{install_datadir}/llvm-cmake
cp -Rv cmake/* %{buildroot}%{install_datadir}/llvm-cmake

# Then install clang
# Add a symlink in bindir to clang-format-diff
ln -s ../share/clang/clang-format-diff.py %{buildroot}%{install_bindir}/clang-format-diff
# File in the macros file for other packages to use.  We are not doing this
# in the compat package, because the version macros would # conflict with
# eachother if both clang and the clang compat package were installed together.
%if %{without compat_build}
install -p -m0644 -D %{SOURCE2} %{buildroot}%{_rpmmacrodir}/macros.%{pkg_name_clang}
sed -i -e "s|@@CLANG_MAJOR_VERSION@@|%{maj_ver}|" \
       -e "s|@@CLANG_MINOR_VERSION@@|%{min_ver}|" \
       -e "s|@@CLANG_PATCH_VERSION@@|%{patch_ver}|" \
       %{buildroot}%{_rpmmacrodir}/macros.%{pkg_name_clang}
# install clang python bindings
mkdir -p %{buildroot}%{python3_sitelib}/clang/
install -p -m644 clang/bindings/python/clang/* %{buildroot}%{python3_sitelib}/clang/
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/clang
mv %{buildroot}%{install_prefix}/lib/{libear,libscanbuild} %{buildroot}%{python3_sitelib}
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/libear
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/libscanbuild
%else
# We don't need these for the compat build.
rm -Rf %{buildroot}%{install_prefix}/lib/{libear,libscanbuild}
rm %{buildroot}%{install_bindir}/scan-build-py
rm -Rf %{buildroot}%{install_datadir}/clang/*.el
%endif

%if %{with sphinx}
# Create manpage symlink for clang++
ln -s clang-%{maj_ver}.1 %{buildroot}%{install_mandir}/man1/clang++.1
%endif

# Fix permissions of scan-view scripts
chmod a+x %{buildroot}%{install_datadir}/scan-view/{Reporter.py,startfile.py}
# remove editor integrations (bbedit, sublime, emacs, vim)
rm -vf %{buildroot}%{install_datadir}/clang/clang-format-bbedit.applescript
rm -vf %{buildroot}%{install_datadir}/clang/clang-format-sublime.py*
# Remove unpackaged files
rm -Rvf %{buildroot}%{install_datadir}/clang-doc
# Not sure if anybody need this?
rm -vf %{buildroot}%{install_datadir}/clang/bash-autocomplete.sh
%if %{without compat_build}
# Move clang resource directory to default prefix.
mkdir -p %{buildroot}%{_prefix}/lib/clang
mv %{buildroot}%{install_prefix}/lib/clang/%{maj_ver} %{buildroot}%{_prefix}/lib/clang/%{maj_ver}
%endif
# Create any missing sub-directories in the clang resource directory.
mkdir -p %{buildroot}%{_prefix}/lib/clang/%{maj_ver}/{bin,include,lib,share}/
# Add versioned resource directory macro
mkdir -p %{buildroot}%{_rpmmacrodir}/
echo "%%clang%{maj_ver}_resource_dir %%{_prefix}/lib/clang/%{maj_ver}" >> %{buildroot}%{_rpmmacrodir}/macros.%{pkg_name_clang}
mkdir -p %{buildroot}%{_sysconfdir}/%{pkg_name_clang}/
echo " %{cfg_file_content}" >> %{buildroot}%{_sysconfdir}/%{pkg_name_clang}/%{_target_platform}-clang.cfg
echo " %{cfg_file_content}" >> %{buildroot}%{_sysconfdir}/%{pkg_name_clang}/%{_target_platform}-clang++.cfg

# Then COMPILER-RT
# llvm_triple -> compiler_rt_triple.
%global compiler_rt_triple %{llvm_triple}

# And OPENMP
# Remove static libraries with equivalent shared libraries
rm -rf %{buildroot}%{install_libdir}/libarcher_static.a
# Remove the openmp gdb plugin
rm -rf %{buildroot}/%{install_datadir}/gdb
%if %{with offload}
# Remove files that we don't package, yet.
rm %{buildroot}%{install_bindir}/llvm-offload-device-info
rm %{buildroot}%{install_bindir}/llvm-omp-kernel-replay
%endif

# And LLD
%if %{without compat_build}
# For update-alternatives
touch %{buildroot}%{_bindir}/ld
%endif
install -D -m 644 -t  %{buildroot}%{install_mandir}/man1/ lld/docs/ld.lld.1

# And LLDB
%if %{with lldb}
%if %{without compat_build}
# Move python package out of llvm prefix.
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{install_prefix}/%{_lib}/python%{python3_version}/site-packages/lldb %{buildroot}/%{python3_sitearch}
rmdir %{buildroot}%{install_prefix}/%{_lib}/python%{python3_version}/site-packages
rmdir %{buildroot}%{install_prefix}/%{_lib}/python%{python3_version}
# python: fix binary libraries location
liblldb=$(basename $(readlink -e %{buildroot}%{install_libdir}/liblldb.so))
ln -vsf "../../../${liblldb}" %{buildroot}%{python3_sitearch}/lldb/_lldb.so
%py_byte_compile %{__python3} %{buildroot}%{python3_sitearch}/lldb
%endif
%endif

# And mlir
%if %{with mlir}
mkdir -p %{buildroot}/%{python3_sitearch}
mv %{buildroot}%{install_prefix}/python_packages/mlir_core/mlir %{buildroot}/%{python3_sitearch}
# Empty directories
rmdir %{buildroot}%{install_prefix}/python_packages/mlir_core %{buildroot}%{install_prefix}/python_packages
# And no need for this
rm -rf %{buildroot}%{install_prefix}/src/python
%endif

# And libcxx
%if %{with libcxx}
# gcc's libunwind ABI is different from llvm's libunwind ABI. To avoid confusion,
# we install llvm's libunwind under a separate directory.
rm %{buildroot}%{_libdir}/libunwind.so
mkdir -p %{buildroot}/%{_libdir}/llvm-unwind/
pushd %{buildroot}/%{_libdir}/llvm-unwind
ln -s ../libunwind.so.1.0 libunwind.so
popd
%endif

# And BOLT
rm -f %{buildroot}%{install_libdir}/libLLVMBOLT*.a

# Move files from src to dest and replace the old files in src with relative
# symlinks.
move_and_replace_with_symlinks() {
    local src="$1"
    local dest="$2"
    mkdir -p "$dest"
    # Change to source directory to simplify relative paths
    (cd "$src" && \
        find * -type d -exec mkdir -p "$dest/{}" \; && \
        find * \( -type f -o -type l \) -exec mv "$src/{}" "$dest/{}" \; \
             -exec ln -s --relative "$dest/{}" "$src/{}" \;)
}
%if %{without compat_build}
# Move files from the llvm prefix to the system prefix and replace them with
# symlinks. We do it this way around because symlinks between multilib packages
# would conflict otherwise.
move_and_replace_with_symlinks %{buildroot}%{install_bindir} %{buildroot}%{_bindir}
move_and_replace_with_symlinks %{buildroot}%{install_libdir} %{buildroot}%{_libdir}
move_and_replace_with_symlinks %{buildroot}%{install_libexecdir} %{buildroot}%{_libexecdir}
move_and_replace_with_symlinks %{buildroot}%{install_includedir} %{buildroot}%{_includedir}
move_and_replace_with_symlinks %{buildroot}%{install_datadir} %{buildroot}%{_datadir}
%endif

# Create versioned symlinks for binaries.
# Do this at the end so it includes any files added by preceding steps.
mkdir -p %{buildroot}%{_bindir}
for f in %{buildroot}%{install_bindir}/*; do
  filename=`basename $f`
  if [[ "$filename" =~ ^(lit|ld|clang-%{maj_ver})$ ]]; then
    continue
  fi
  %if %{with compat_build}
    ln -s ../../%{install_bindir}/$filename %{buildroot}/%{_bindir}/$filename-%{maj_ver}
  %else
    # clang-NN is already created by the build system.
    if [[ "$filename" == "clang" ]]; then
      continue
    fi
    ln -s $filename %{buildroot}/%{_bindir}/$filename-%{maj_ver}
  %endif
done
mkdir -p %{buildroot}%{_mandir}/man1
for f in %{buildroot}%{install_mandir}/man1/*; do
  filename=`basename $f`
  filename=${filename%.1}
  %if %{with compat_build}
    # Move man pages to system install prefix.
    mv $f %{buildroot}%{_mandir}/man1/$filename-%{maj_ver}.1
  %else
    # Create suffixed symlink.
    ln -s $filename.1 %{buildroot}%{_mandir}/man1/$filename-%{maj_ver}.1
  %endif
done
rm -rf %{buildroot}%{install_mandir}
# As an exception, always keep llvm-config in the versioned prefix.
# The llvm-config in the default prefix will be managed by alternatives.
%if %{without compat_build}
rm %{buildroot}%{install_bindir}/llvm-config
mv %{buildroot}%{_bindir}/llvm-config %{buildroot}%{install_bindir}/llvm-config
%endif
# ghost presence for llvm-config, managed by alternatives.
touch %{buildroot}%{_bindir}/llvm-config-%{maj_ver}
%if %{without compat_build}
touch %{buildroot}%{_bindir}/llvm-config
%endif
%if %{with bundle_compat_lib}
install -m 0755 ../llvm-compat-libs/lib/libLLVM.so.%{compat_maj_ver}* %{buildroot}%{_libdir}
install -m 0755 ../llvm-compat-libs/lib/libclang.so.%{compat_maj_ver}* %{buildroot}%{_libdir}
install -m 0755 ../llvm-compat-libs/lib/libclang-cpp.so.%{compat_maj_ver}* %{buildroot}%{_libdir}
install -m 0755 ../llvm-compat-libs/lib/liblldb.so.%{compat_maj_ver}* %{buildroot}%{_libdir}
%endif

%check
# TODO: Add this to XFAIL instead?
rm llvm/test/tools/dsymutil/X86/swift-interface.test
cd llvm
%if %{with check}
# Call this function before setting up a next component to test.
function reset_test_opts()
{
    # See https://llvm.org/docs/CommandGuide/lit.html#general-options
    export LIT_OPTS="-vv --time-tests"
    export LIT_OPTS="$LIT_OPTS --timeout=600"
    # Set to mark tests as expected to fail.
    # See https://llvm.org/docs/CommandGuide/lit.html#cmdoption-lit-xfail
    unset LIT_XFAIL
    # Set to mark tests to not even run.
    # See https://llvm.org/docs/CommandGuide/lit.html#cmdoption-lit-filter-out
    # Unfortunately LIT_FILTER_OUT is not accepting a list but a regular expression.
    # To make this easily maintainable, we'll create an associate array in bash,
    # to which you can append and later we'll join that array and escape dots (".")
    # in your test paths. The following line resets this array.
    # See also the function "test_list_to_regex".
    test_list_filter_out=()
    unset LIT_FILTER_OUT
    # Set for filtering out unit tests.
    # See http://google.github.io/googletest/advanced.html#running-a-subset-of-the-tests
    unset GTEST_FILTER
    # Some test (e.g. mlir) require this to be set.
    unset PYTHONPATH
}
# Convert array of test names into a regex.
# Call this function with an indexed array.
#
# Example:
#
#    testlist=()
#    testlist+=("foo")
#    testlist+=("bar")
#    export LIT_FILTER_OUT=$(test_list_to_regex testlist)
#
# Then $LIT_FILTER_OUT should evaluate to: (foo|bar)
function test_list_to_regex()
{
    local -n arr=$1
    # Prepare LIT_FILTER_OUT regex from index bash array
    # Join each element with a pipe symbol (regex for "or")
    arr=$(printf "|%s" "${arr[@]}")
    # Remove the initial pipe symbol
    arr=${arr:1}
    # Properly escape path dots (".") for use in regular expression
    arr=$(echo $arr | sed 's/\./\\./g')
    # Add enclosing parenthesis
    echo "($arr)"
}
# Similar to test_list_to_regex() except that this function exports
# the LIT_FILTER_OUT if there are tests in the given list.
# If there are no tests, the LIT_FILTER_OUT is unset in order to
# avoid issues with the llvm test system.
function adjust_lit_filter_out()
{
  local -n arr=$1
  local res=$(test_list_to_regex test_list_filter_out)
  if [[ "$res" != "()" ]]; then
    export LIT_FILTER_OUT=$res
  else
    unset LIT_FILTER_OUT
  fi
}

# Test LLVM lit
reset_test_opts
%cmake_build --target check-lit

# Test LLVM
reset_test_opts
# Xfail testing of update utility tools
export LIT_XFAIL="tools/UpdateTestChecks"
%cmake_build --target check-llvm

# Test CLANG
reset_test_opts
export LIT_XFAIL="$LIT_XFAIL;clang/test/CodeGen/profile-filter.c"
%cmake_build --target check-clang

# Test Clang Tools
reset_test_opts
%cmake_build --target check-clang-tools

# Test OPENMP
# This part is tricky because some tests are flaky
reset_test_opts
export LIT_XFAIL="api_tests/test_ompd_get_curr_task_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_enclosing_parallel_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_generating_task_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_icv_from_scope.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_scheduling_task_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_state.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_task_frame.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_task_function.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_task_in_parallel.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_task_parallel_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_thread_id.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_thread_in_parallel.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_parallel_handle_compare.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_rel_parallel_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_rel_task_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_rel_thread_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_task_handle_compare.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_thread_handle_compare.c"
export LIT_XFAIL="$LIT_XFAIL;openmp_examples/ompd_icvs.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_curr_parallel_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_display_control_vars.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_thread_handle.c"
test_list_filter_out+=("libomp :: affinity/kmp-abs-hw-subset.c")
test_list_filter_out+=("libomp :: ompt/teams/distribute_dispatch.c")
test_list_filter_out+=("libomp :: worksharing/for/omp_collapse_many_GELTGT_int.c")
test_list_filter_out+=("libomp :: worksharing/for/omp_collapse_many_GTGEGT_int.c")
test_list_filter_out+=("libomp :: worksharing/for/omp_collapse_many_LTLEGE_int.c")
test_list_filter_out+=("libomp :: worksharing/for/omp_collapse_one_int.c")
%ifnarch x86_64
# Passes on x86_64:
#   libomptarget :: x86_64-pc-linux-gnu :: mapping/target_derefence_array_pointrs.cpp
#   libomptarget :: x86_64-pc-linux-gnu-LTO :: mapping/target_derefence_array_pointrs.cpp
export LIT_XFAIL="$LIT_XFAIL;mapping/target_derefence_array_pointrs.cpp"
# Passes on x86_64:
#   libomptarget :: x86_64-pc-linux-gnu :: api/ompx_3d.c
#   libomptarget :: x86_64-pc-linux-gnu :: api/ompx_3d.cpp
#   libomptarget :: x86_64-pc-linux-gnu-LTO :: api/ompx_3d.c
#   libomptarget :: x86_64-pc-linux-gnu-LTO :: api/ompx_3d.cpp
# libomptarget :: aarch64-unknown-linux-gnu ::
export LIT_XFAIL="$LIT_XFAIL;api/ompx_3d.c"
export LIT_XFAIL="$LIT_XFAIL;api/ompx_3d.cpp"
%endif
adjust_lit_filter_out test_list_filter_out
# This allows openmp tests to be re-run 4 times. Once they pass
# after being re-run, they are marked as FLAKYPASS.
# See https://github.com/llvm/llvm-project/pull/141851 for the
# --max-retries-per-test option.
# We don't know if 4 is the right number to use here we just
# need to start with some number.
# Once https://github.com/llvm/llvm-project/pull/142413 landed
# we can see the exact number of attempts the tests needed
# to pass. And then we can adapt this number.
export LIT_OPTS="$LIT_OPTS --max-retries-per-test=4"
%cmake_build --target check-openmp

%if %{with lldb}
## TODO: Come back and re-enable testing for LLDB
## #region LLDB unit tests
## reset_test_opts
## %%cmake_build --target check-lldb-unit
## #endregion LLDB unit tests
##
## #region LLDB SB API tests
## reset_test_opts
## %%cmake_build --target check-lldb-api
## #endregion LLDB SB API tests
##
## #region LLDB shell tests
## reset_test_opts
## %%cmake_build --target check-lldb-shell
## #endregion LLDB shell tests
%endif

# Test LLD
reset_test_opts
%cmake_build --target check-lld

# Test MLIR
%if %{with mlir}
reset_test_opts
adjust_lit_filter_out test_list_filter_out
export PYTHONPATH=%{buildroot}/%{python3_sitearch}
%cmake_build --target check-mlir
%endif

# BOLT tests
%if %{with build_bolt}
reset_test_opts
# Beginning with LLVM 20 this test has the "non-root-user" requirement
# and then the test should pass. But now it is flaky, hence we can only
# filter it out.
test_list_filter_out+=("BOLT :: unreadable-profile.test")
%cmake_build --target check-bolt
%endif

# polly tests
%if %{with polly}
reset_test_opts
%cmake_build --target check-polly
%endif

%endif

%post -n %{pkg_name_llvm}-devel
update-alternatives --install %{_bindir}/llvm-config-%{maj_ver} llvm-config-%{maj_ver} %{install_bindir}/llvm-config %{__isa_bits}
%if %{without compat_build}
# Prioritize newer LLVM versions over older and 64-bit over 32-bit.
update-alternatives --install %{_bindir}/llvm-config llvm-config %{install_bindir}/llvm-config $((%{maj_ver}*100+%{__isa_bits}))
# Remove old llvm-config-%{__isa_bits} alternative. This will only do something during the
# first upgrade from a version that used it. In all other cases it will error, so suppress the
# expected error message.
update-alternatives --remove llvm-config %{_bindir}/llvm-config-%{__isa_bits} 2>/dev/null ||:
%endif

%postun -n %{pkg_name_llvm}-devel
if [ $1 -eq 0 ]; then
  update-alternatives --remove llvm-config%{exec_suffix} %{install_bindir}/llvm-config
fi
%if %{without compat_build}
# There are a number of different cases here:
# Uninstall: Remove alternatives.
# Patch version upgrade: Keep alternatives.
# Major version upgrade with installation of compat package: Keep alternatives for compat package.
# Major version upgrade without installation of compat package: Remove alternatives. However, we
# can't distinguish it from the previous case, so we conservatively leave it behind.
if [ $1 -eq 0 ]; then
  update-alternatives --remove llvm-config-%{maj_ver} %{install_bindir}/llvm-config
fi
%endif
%if %{without compat_build}
%post -n %{pkg_name_lld}
update-alternatives --install %{_bindir}/ld ld %{_bindir}/ld.lld 1
%postun -n %{pkg_name_lld}
if [ $1 -eq 0 ] ; then
  update-alternatives --remove ld %{_bindir}/ld.lld
fi
%endif

%define expand_bins() %{lua:
  local bindir = rpm.expand("%{_bindir}")
  local install_bindir = rpm.expand("%{install_bindir}")
  local maj_ver = rpm.expand("%{maj_ver}")
  for arg in rpm.expand("%*"):gmatch("%S+") do
    print(install_bindir .. "/" .. arg .. "\\n")
    print(bindir .. "/" .. arg .. "-" .. maj_ver .. "\\n")
    if rpm.expand("%{without compat_build}") == "1" then
      print(bindir .. "/" .. arg .. "\\n")
    end
  end
}
%define expand_mans() %{lua:
  local mandir = rpm.expand("%{_mandir}")
  local maj_ver = rpm.expand("%{maj_ver}")
  for arg in rpm.expand("%*"):gmatch("%S+") do
    print(mandir .. "/man1/" .. arg .. "-" .. maj_ver .. ".1.gz\\n")
    if rpm.expand("%{without compat_build}") == "1" then
      print(mandir .. "/man1/" .. arg .. ".1.gz\\n")
    end
  end
}
%define expand_generic(d:i:) %{lua:
  local dir = rpm.expand("%{-d*}")
  local install_dir = rpm.expand("%{-i*}")
  for arg in rpm.expand("%*"):gmatch("%S+") do
    print(install_dir .. "/" .. arg .. "\\n")
    if rpm.expand("%{without compat_build}") == "1" then
      print(dir .. "/" .. arg .. "\\n")
    end
  end
}
%define expand_libs() %{expand_generic -d %{_libdir} -i %{install_libdir}  %*}
%define expand_libexecs() %{expand_generic -d %{_libexecdir} -i %{install_libexecdir} %*}
%define expand_includes() %{expand_generic -d %{_includedir} -i %{install_includedir} %*}
%define expand_datas() %{expand_generic -d %{_datadir} -i %{install_datadir} %*}


%if %{with python_lit}
%files -n python-lit
%license llvm/utils/lit/LICENSE.TXT
%doc llvm/utils/lit/README.rst
%{python3_sitelib}/lit/
%{python3_sitelib}/lit-*-info/
%{_bindir}/lit
%endif

%files -n %{pkg_name_llvm}-filesystem
%dir %{install_prefix}
%dir %{install_bindir}
%dir %{install_includedir}
%dir %{install_libdir}
%dir %{install_libdir}/cmake
%dir %{install_libexecdir}
%dir %{install_datadir}

%files -n %{pkg_name_llvm}
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
}}
%if %{maj_ver} >= 22
%{expand_bins %{expand:
    llvm-ir2vec
    llvm-offload-wrapper
    llvm-offload-binary
}}
%endif
%if %{with sphinx}
%{expand_mans %{expand:
    bugpoint
    clang-tblgen
    dsymutil
    FileCheck
    lit
    llc
    lldb-tblgen
    lli
    llvm-addr2line
    llvm-ar
    llvm-as
    llvm-bcanalyzer
    llvm-cgdata
    llvm-cov
    llvm-cxxfilt
    llvm-cxxmap
    llvm-debuginfo-analyzer
    llvm-diff
    llvm-dis
    llvm-dwarfdump
    llvm-dwarfutil
    llvm-exegesis
    llvm-extract
    llvm-ifs
    llvm-install-name-tool
    llvm-lib
    llvm-libtool-darwin
    llvm-link
    llvm-lipo
    llvm-locstats
    llvm-mc
    llvm-mca
    llvm-nm
    llvm-objcopy
    llvm-objdump
    llvm-opt-report
    llvm-otool
    llvm-pdbutil
    llvm-profdata
    llvm-profgen
    llvm-ranlib
    llvm-readelf
    llvm-readobj
    llvm-reduce
    llvm-remarkutil
    llvm-size
    llvm-stress
    llvm-strings
    llvm-strip
    llvm-symbolizer
    llvm-tblgen
    llvm-tli-checker
    mlir-tblgen
    opt
    tblgen
}}
%endif
%if %{maj_ver} >= 22
%{expand_mans %{expand:
    llvm-ir2vec
    llvm-offload-binary
}}
%endif
%expand_datas opt-viewer

%files -n %{pkg_name_llvm}-libs
%license llvm/LICENSE.TXT
%{expand_libs %{expand:
    libLLVM-%{maj_ver}%{?llvm_snapshot_version_suffix}.so
    libLLVM.so.%{maj_ver}.%{min_ver}%{?llvm_snapshot_version_suffix}
    libLTO.so*
    libRemarks.so*
    LLVMgold.so
}}
%if %{with compat_build}
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{pkg_name_llvm}-%{_arch}.conf
%endif
%if %{with bundle_compat_lib}
%{_libdir}/libLLVM.so.%{compat_maj_ver}*
%endif

%files -n %{pkg_name_llvm}-devel
%license llvm/LICENSE.TXT
%{install_bindir}/llvm-config
%ghost %{_bindir}/llvm-config-%{maj_ver}
%if %{without compat_build}
%ghost %{_bindir}/llvm-config
%endif
%if %{with sphinx}
%expand_mans llvm-config
%endif
%expand_includes llvm llvm-c
%{expand_libs %{expand:
    libLLVM.so
    cmake/llvm
}}

%files -n %{pkg_name_llvm}-doc
%license llvm/LICENSE.TXT

%files -n %{pkg_name_llvm}-static
%license llvm/LICENSE.TXT
%expand_libs libLLVM*.a
%exclude %{install_libdir}/libLLVMTestingSupport.a
%exclude %{install_libdir}/libLLVMTestingAnnotations.a
%if %{without compat_build}
%exclude %{_libdir}/libLLVMTestingSupport.a
%exclude %{_libdir}/libLLVMTestingAnnotations.a
%endif

%files -n %{pkg_name_llvm}-cmake-utils
%license llvm/LICENSE.TXT
%expand_datas llvm-cmake

%files -n %{pkg_name_llvm}-test
%license llvm/LICENSE.TXT
%{expand_bins %{expand:
    not
    count
    yaml-bench
    lli-child-target
    llvm-isel-fuzzer
    llvm-opt-fuzzer
    llvm-test-mustache-spec
}}
%if %{with sphinx}
%{expand_mans %{expand:
    llvm-test-mustache-spec
}}
%endif

%files -n %{pkg_name_llvm}-googletest
%license llvm/LICENSE.TXT
%{expand_libs %{expand:
    libLLVMTestingSupport.a
    libLLVMTestingAnnotations.a
    libllvm_gtest.a
    libllvm_gtest_main.a
}}
%expand_includes llvm-gtest llvm-gmock

%files -n %{pkg_name_clang}
%license clang/LICENSE.TXT
%{expand_bins %{expand:
    clang
    clang++
    clang-cl
    clang-cpp
    clang-scan-deps
}}
%{install_bindir}/clang-%{maj_ver}
%{_sysconfdir}/%{pkg_name_clang}/%{_target_platform}-clang.cfg
%{_sysconfdir}/%{pkg_name_clang}/%{_target_platform}-clang++.cfg
%if %{with sphinx}
%{expand_mans clang clang++}
%endif

%files -n %{pkg_name_clang}-libs
%license clang/LICENSE.TXT
%{_prefix}/lib/clang/%{maj_ver}/include/*
# Part of compiler-rt:
%exclude %{_prefix}/lib/clang/%{maj_ver}/include/fuzzer
%exclude %{_prefix}/lib/clang/%{maj_ver}/include/orc
%exclude %{_prefix}/lib/clang/%{maj_ver}/include/profile
%exclude %{_prefix}/lib/clang/%{maj_ver}/include/sanitizer
%exclude %{_prefix}/lib/clang/%{maj_ver}/include/xray
# Part of libomp-devel:
%exclude %{_prefix}/lib/clang/%{maj_ver}/include/omp*.h
%expand_libs libclang.so.%{maj_ver}*
%expand_libs libclang-cpp.so.%{maj_ver}*
%if %{with bundle_compat_lib}
%{_libdir}/libclang.so.%{compat_maj_ver}*
%{_libdir}/libclang-cpp.so.%{compat_maj_ver}*
%endif

%files -n %{pkg_name_clang}-devel
%license clang/LICENSE.TXT
%{expand_libs %{expand:
    cmake/clang
    libclang-cpp.so
    libclang.so
}}
%expand_includes clang clang-c
%expand_bins clang-tblgen
%dir %{install_datadir}/clang/
%if %{without compat_build}
%dir %{_datadir}/clang
%endif

%files -n %{pkg_name_clang}-resource-filesystem
%license clang/LICENSE.TXT
%dir %{_prefix}/lib/clang/
%dir %{_prefix}/lib/clang/%{maj_ver}/
%dir %{_prefix}/lib/clang/%{maj_ver}/bin/
%dir %{_prefix}/lib/clang/%{maj_ver}/include/
%dir %{_prefix}/lib/clang/%{maj_ver}/lib/
%dir %{_prefix}/lib/clang/%{maj_ver}/share/
%{_rpmmacrodir}/macros.%{pkg_name_clang}

%files -n %{pkg_name_clang}-analyzer
%license clang/LICENSE.TXT
%{expand_bins %{expand:
    scan-view
    scan-build
    analyze-build
    intercept-build
}}
%{expand_libexecs %{expand:
    ccc-analyzer
    c++-analyzer
    analyze-c++
    analyze-cc
    intercept-c++
    intercept-cc
}}
%expand_datas scan-view scan-build
%expand_mans scan-build
%if %{without compat_build}
%expand_bins scan-build-py
%{python3_sitelib}/libear
%{python3_sitelib}/libscanbuild
%endif

%files -n %{pkg_name_clang}-tools-extra
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
%if %{with sphinx}
%expand_mans diagtool extraclangtools
%endif
%{expand_datas %{expand:
    clang/clang-format.py*
    clang/clang-format-diff.py*
    clang/clang-include-fixer.py*
    clang/clang-tidy-diff.py*
    clang/run-find-all-symbols.py*
}}

%files -n %{pkg_name_clang}-tools-extra-devel
%license clang-tools-extra/LICENSE.TXT
%expand_includes clang-tidy
%if %{without compat_build}

%files -n python-clang
%license clang/LICENSE.TXT
%{python3_sitelib}/clang/
%endif

%files -n %{pkg_name_compiler_rt}
%license compiler-rt/LICENSE.TXT
%ifarch x86_64 riscv64
%{_prefix}/lib/clang/%{maj_ver}/bin/hwasan_symbolize
%endif
%{_prefix}/lib/clang/%{maj_ver}/include/fuzzer
%{_prefix}/lib/clang/%{maj_ver}/include/orc
%{_prefix}/lib/clang/%{maj_ver}/include/profile
%{_prefix}/lib/clang/%{maj_ver}/include/sanitizer
%{_prefix}/lib/clang/%{maj_ver}/include/xray
%{_prefix}/lib/clang/%{maj_ver}/share/*.txt
# Files that appear on all targets
%{_prefix}/lib/clang/%{maj_ver}/lib/%{compiler_rt_triple}/libclang_rt.*
%{_prefix}/lib/clang/%{maj_ver}/lib/%{compiler_rt_triple}/clang_rt.crtbegin.o
%{_prefix}/lib/clang/%{maj_ver}/lib/%{compiler_rt_triple}/clang_rt.crtend.o
%ifnarch riscv64
%{_prefix}/lib/clang/%{maj_ver}/lib/%{compiler_rt_triple}/liborc_rt.a
%endif
# Additional symlink if two triples are in use.
%if "%{llvm_triple}" != "%{compiler_rt_triple}"
%{_prefix}/lib/clang/%{maj_ver}/lib/%{llvm_triple}
%endif

%files -n %{pkg_name_libomp}
%license openmp/LICENSE.TXT
%{expand_libs %{expand:
    libomp.so
    libompd.so
    libarcher.so
}}
%if %{with offload}
%expand_libs libomptarget.so.%{so_suffix}
%expand_libs libLLVMOffload.so.%{so_suffix}
%endif

%files -n %{pkg_name_libomp}-devel
%license openmp/LICENSE.TXT
%{_prefix}/lib/clang/%{maj_ver}/include/omp.h
%{_prefix}/lib/clang/%{maj_ver}/include/ompx.h
%{_prefix}/lib/clang/%{maj_ver}/include/omp-tools.h
%{_prefix}/lib/clang/%{maj_ver}/include/ompt.h
%{_prefix}/lib/clang/%{maj_ver}/include/ompt-multiplex.h
%expand_libs cmake/openmp
%if %{with offload}
%{expand_libs %{expand:
    libomptarget.so
    libLLVMOffload.so
}}
%{expand_libs %{expand:
    amdgcn-amd-amdhsa/libompdevice.a
    amdgcn-amd-amdhsa/libomptarget-amdgpu.bc
    nvptx64-nvidia-cuda/libompdevice.a
    nvptx64-nvidia-cuda/libomptarget-nvptx.bc
}}
%expand_includes offload
%endif

%files -n %{pkg_name_lld}
%license lld/LICENSE.TXT
%ghost %{_bindir}/ld
%{expand_bins %{expand:
    lld
    lld-link
    ld.lld
    ld64.lld
    wasm-ld
}}
%expand_mans ld.lld

%files -n %{pkg_name_lld}-devel
%license lld/LICENSE.TXT
%expand_includes lld
%{expand_libs %{expand:
    liblldCOFF.so
    liblldCommon.so
    liblldELF.so
    liblldMachO.so
    liblldMinGW.so
    liblldWasm.so
    cmake/lld
}}

%files -n %{pkg_name_lld}-libs
%license lld/LICENSE.TXT
%{expand_libs %{expand:
    liblldCOFF.so.*
    liblldCommon.so.*
    liblldELF.so.*
    liblldMachO.so.*
    liblldMinGW.so.*
    liblldWasm.so.*
}}

%if %{with lldb}
%files -n %{pkg_name_lldb}
%license lldb/LICENSE.TXT
%{expand_bins %{expand:
    lldb
    lldb-argdumper
    lldb-dap
    lldb-instr
    lldb-server
}}
%if %{maj_ver} >= 22
%{expand_bins %{expand:
    lldb-mcp
}}
%endif
# Usually, *.so symlinks are kept in devel subpackages. However, the python
# bindings depend on this symlink at runtime.
%{expand_libs %{expand:
    liblldb*.so
    liblldb.so.*
    liblldbIntelFeatures.so.*
}}
%if %{with sphinx}
%expand_mans lldb-server lldb
%endif
%if %{with bundle_compat_lib}
%{_libdir}/liblldb.so.%{compat_maj_ver}*
%endif

%files -n %{pkg_name_lldb}-devel
%expand_includes lldb
%if %{maj_ver} >= 22
%{expand_bins %{expand:
    lldb-tblgen
    yaml2macho-core
}}
%endif

%if %{without compat_build}
%files -n python3-lldb
%{python3_sitearch}/lldb
%endif
%endif

%if %{with mlir}
%files -n %{pkg_name_mlir}
%license LICENSE.TXT
%{expand_libs %{expand:
    libmlir_arm_runner_utils.so.%{maj_ver}*
    libmlir_arm_sme_abi_stubs.so.%{maj_ver}*
    libmlir_async_runtime.so.%{maj_ver}*
    libmlir_c_runner_utils.so.%{maj_ver}*
    libmlir_float16_utils.so.%{maj_ver}*
    libmlir_runner_utils.so.%{maj_ver}*
    libMLIR*.so.%{maj_ver}*
}}

%files -n %{pkg_name_mlir}-static
%expand_libs libMLIR*.a

%files -n %{pkg_name_mlir}-devel
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
%expand_includes mlir mlir-c
%{expand_libs %{expand:
    cmake/mlir
    libmlir_arm_runner_utils.so
    libmlir_arm_sme_abi_stubs.so
    libmlir_async_runtime.so
    libmlir_c_runner_utils.so
    libmlir_float16_utils.so
    libmlir_runner_utils.so
    libMLIR*.so
}}

%files -n python3-%{pkg_name_mlir}
%{python3_sitearch}/mlir/
%endif

%if %{with libcxx}
%files -n %{pkg_name_libcxx}
%license libcxx/LICENSE.TXT
%doc libcxx/CREDITS.TXT libcxx/TODO.TXT
%{_libdir}/libc++.so.*

%files -n %{pkg_name_libcxx}-devel
%{_includedir}/c++/
%exclude %{_includedir}/c++/v1/cxxabi.h
%exclude %{_includedir}/c++/v1/__cxxabi_config.h
%{_libdir}/libc++.so
%{_libdir}/libc++.modules.json
%{_datadir}/libc++/v1/*

%files -n %{pkg_name_libcxx}-static
%license libcxx/LICENSE.TXT
%{_libdir}/libc++.a
%{_libdir}/libc++experimental.a

%files -n %{pkg_name_libcxxabi}
%license libcxxabi/LICENSE.TXT
%doc libcxxabi/CREDITS.TXT
%{_libdir}/libc++abi.so.*

%files -n %{pkg_name_libcxxabi}-devel
%{_includedir}/c++/v1/cxxabi.h
%{_includedir}/c++/v1/__cxxabi_config.h
%{_libdir}/libc++abi.so

%files -n %{pkg_name_libcxxabi}-static
%{_libdir}/libc++abi.a

%files -n %{pkg_name_llvm_libunwind}
%license libunwind/LICENSE.TXT
%{_libdir}/libunwind.so.1
%{_libdir}/libunwind.so.1.0

%files -n %{pkg_name_llvm_libunwind}-devel
%{_includedir}/llvm-libunwind/__libunwind_config.h
%{_includedir}/llvm-libunwind/libunwind.h
%{_includedir}/llvm-libunwind/libunwind.modulemap
%{_includedir}/llvm-libunwind/mach-o/compact_unwind_encoding.h
%{_includedir}/llvm-libunwind/unwind.h
%{_includedir}/llvm-libunwind/unwind_arm_ehabi.h
%{_includedir}/llvm-libunwind/unwind_itanium.h
%dir %{_libdir}/llvm-unwind
%{_libdir}/llvm-unwind/libunwind.so

%files -n %{pkg_name_llvm_libunwind}-static
%{_libdir}/libunwind.a
%endif

%if %{with build_bolt}
%files -n %{pkg_name_bolt}
%license bolt/LICENSE.TXT
%{expand_bins %{expand:
    llvm-bolt
    llvm-boltdiff
    llvm-bolt-binary-analysis
    llvm-bolt-heatmap
    merge-fdata
    perf2bolt
}}
%{expand_libs %{expand:
    libbolt_rt_hugify.a
    libbolt_rt_instr.a
}}
%endif

%if %{with polly}
%files -n %{pkg_name_polly}
%license polly/LICENSE.TXT
%{expand_libs %{expand:
  LLVMPolly.so
  libPolly.so.*
  libPollyISL.so
}}
%if %{with sphinx}
%expand_mans polly
%endif

%files -n %{pkg_name_polly}-devel
%expand_libs libPolly.so
%expand_includes polly
%expand_libs cmake/polly
%endif

%changelog
%autochangelog
