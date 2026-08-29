# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond llvmir 1
%if %{with llvmir}
  %ifarch x86_64
     %global emit_llvmir_flags -march=x86-64-v4
  %elifarch riscv64
     %global emit_llvmir_flags -march=rva23u64
  %else
     %global emit_llvmir_flags 1
  %endif

%global ___build_pre \
        set -x \
        export CMAKE_EMIT_LLVMIR=%{emit_llvmir_flags} \
        set +x \
        %{?___build_pre}
%global toolchain clang
%endif

Name:           libjpeg-turbo
Version:        3.1.2
Release:        %autorelease
Summary:        A SIMD-accelerated library for manipulating JPEG image files
License:        Zlib AND BSD-3-Clause AND MIT AND IJG
URL:            https://github.com/libjpeg-turbo/libjpeg-turbo
#!RemoteAsset:  sha256:560f6338b547544c4f9721b18d8b87685d433ec78b3c644c70d77adad22c55e6
Source:         https://github.com/libjpeg-turbo/libjpeg-turbo/archive/refs/tags/%{version}.tar.gz
Patch:          0001-libjpeg-turbo-cmake.patch
BuildSystem:    cmake

BuildOption(conf):  -DENABLE_STATIC:BOOL=NO
BuildOption(conf):  -DFLOATTEST:STRING="fp-contract"
%if %{with llvmir}
BuildOption(conf):  -DCMAKE_PROJECT_TOP_LEVEL_INCLUDES:STRING=%{_libdir}/clang-wrap/cmake/CMakeEmitLLVMIR.cmake
BuildOption(conf):  -DCMAKE_C_COMPILER:STRING=clang
BuildOption(conf):  -DCMAKE_CXX_COMPILER:STRING=clang++
%endif


BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  libtool
%if %{with llvmir}
BuildRequires:  clang
BuildRequires:  llvm
BuildRequires:  clang-wrap
%endif

%description
The libjpeg-turbo package contains a library of functions for manipulating JPEG
images, accelerated with SIMD instructions.

%package        devel
Summary:        Headers for the libjpeg-turbo library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains header files necessary for developing programs which use
the libjpeg-turbo library.

%package        utils
Summary:        Utilities for manipulating JPEG images
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
This package contains command-line utilities for creating, decompressing, and
transforming JPEG files.

%package -n     turbojpeg
Summary:        TurboJPEG library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n turbojpeg
This package contains the TurboJPEG shared library, a higher-level API for
JPEG compression and decompression.

%package -n     turbojpeg-devel
Summary:        Headers for the TurboJPEG library
Requires:       turbojpeg = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n turbojpeg-devel
This package contains header files for developing programs that use the
TurboJPEG library.

%install -a
rm -f %{buildroot}/%{_bindir}/tjbench
%if %{with llvmir}
rm -f %{buildroot}/%{clang_wrap_llvmir_bin_dir}/tjbench*
%endif

%files
%license LICENSE.md
%doc README.md README.ijg ChangeLog.md
%{_libdir}/libjpeg.so.62*
%if %{with llvmir}
%{clang_wrap_llvmir_dir}/libjpeg.so.62*
%endif

%files devel
%doc doc/coderules.txt src/jconfig.txt doc/libjpeg.txt doc/structure.txt
%{_includedir}/jconfig.h
%{_includedir}/jerror.h
%{_includedir}/jmorecfg.h
%{_includedir}/jpeglib.h
%{_includedir}/jpegint.h
%{_libdir}/libjpeg.so
%{_libdir}/pkgconfig/libjpeg.pc
%dir %{_libdir}/cmake/libjpeg-turbo
%{_libdir}/cmake/libjpeg-turbo/*.cmake

%files utils
%doc doc/usage.txt doc/wizard.txt
%{_bindir}/cjpeg
%{_bindir}/djpeg
%{_bindir}/jpegtran
%{_bindir}/rdjpgcom
%{_bindir}/wrjpgcom
%if %{with llvmir}
%{clang_wrap_llvmir_bin_dir}/cjpeg*
%{clang_wrap_llvmir_bin_dir}/djpeg*
%{clang_wrap_llvmir_bin_dir}/jpegtran*
%{clang_wrap_llvmir_bin_dir}/rdjpgcom*
%{clang_wrap_llvmir_bin_dir}/wrjpgcom*
%endif
%{_mandir}/man1/cjpeg.1*
%{_mandir}/man1/djpeg.1*
%{_mandir}/man1/jpegtran.1*
%{_mandir}/man1/rdjpgcom.1*
%{_mandir}/man1/wrjpgcom.1*

%files -n turbojpeg
%license LICENSE.md
%doc README.md README.ijg ChangeLog.md
%{_libdir}/libturbojpeg.so.0*
%if %{with llvmir}
%{clang_wrap_llvmir_dir}/libturbojpeg.so.0*
%endif

%files -n turbojpeg-devel
%{_includedir}/turbojpeg.h
%{_libdir}/libturbojpeg.so
%{_libdir}/pkgconfig/libturbojpeg.pc

%changelog
%autochangelog
