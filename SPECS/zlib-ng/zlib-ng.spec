# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond systemtap 0

# defining BUILD_SHARED_LIBS disables the static library
%undefine _cmake_shared_libs

Name:           zlib-ng
Version:        2.3.3
Release:        %autorelease
Summary:        Zlib replacement with optimizations
License:        Zlib
URL:            https://github.com/zlib-ng/zlib-ng
#!RemoteAsset
Source:         https://github.com/zlib-ng/zlib-ng/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

# Support V/Zbc detection via riscv_hwprobe syscall
Patch0:         zlib-ng-2.3.2-riscv-hwprobe.patch

BuildOption(conf):  -DINSTALL_LIB_DIR=%{_libdir}
BuildOption(conf):  -DWITH_RVV:BOOL=ON
BuildOption(conf):  -DWITH_GTEST:BOOL=OFF
BuildOption(conf):  -DWITH_NEW_STRATEGIES:BOOL=OFF
BuildOption(conf):  -DWITH_ARMV6:BOOL=OFF
BuildOption(conf):  -DZLIB_COMPAT:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
%if %{with systemtap}
BuildRequires:  systemtap-sdt-devel
%endif

%description
zlib-ng is a zlib replacement with support for CPU intrinsics.

%package        compat
Summary:        Zlib replacement with optimizations (compat version)
Provides:       zlib = %{version}-%{release}
Provides:       zlib%{?_isa} = %{version}-%{release}

%description    compat
zlib-ng is a zlib replacement with support for CPU intrinsics.
This package provides a drop-in zlib-compatible library.

%package        compat-devel
Summary:        Development files for zlib-ng-compat
Requires:       %{name}-compat%{?_isa} = %{version}-%{release}
Provides:       zlib-devel = %{version}-%{release}
Provides:       zlib-devel%{?_isa} = %{version}-%{release}

%description    compat-devel
The zlib-ng-compat-devel package contains header files and development libraries for zlib-ng-compat.
This package provides a drop-in zlib-compatible header files and development libraries.

%package        compat-static
Summary:        Static library for zlib-ng-compat
Requires:       %{name}-compat-devel%{?_isa} = %{version}-%{release}

%description    compat-static
The %{name}-static package contains static libraries for zlib-ng-compat.

%files compat
%license LICENSE.md
%doc README.md
%{_libdir}/libz.so*

%files compat-devel
%{_includedir}/zconf.h
%{_includedir}/zlib.h
%{_includedir}/zlib_name_mangling.h
%{_libdir}/libz.so
%{_libdir}/pkgconfig/zlib.pc
%{_libdir}/cmake/ZLIB/

%files compat-static
%{_libdir}/libz.a

%changelog
%autochangelog
