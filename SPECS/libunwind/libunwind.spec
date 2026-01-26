# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libunwind
Version:        1.8.3
Release:        %autorelease
Summary:        An unwinding library
License:        MIT
URL:            https://www.nongnu.org/libunwind/
VCS:            git:https://github.com/libunwind/libunwind
#!RemoteAsset
Source:         https://github.com/libunwind/libunwind/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-shared
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-tests
BuildOption(conf):  --disable-documentation

BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  gcc-c++

%description
Libunwind provides a C ABI to determine the call-chain of a program.

%package        devel
Summary:        Development files for libunwind
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the libraries, header files, and documentation
needed for developing applications that use libunwind.

%conf -p
autoreconf -fiv

%files
%license COPYING
%doc README NEWS
%{_libdir}/libunwind*.so.*

%files devel
%{_libdir}/libunwind*.so
%{_libdir}/pkgconfig/libunwind*.pc
%{_includedir}/unwind.h
%{_includedir}/libunwind*.h

%changelog
%{?autochangelog}
