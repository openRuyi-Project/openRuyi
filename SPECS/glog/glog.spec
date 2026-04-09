# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           glog
Version:        0.7.1
Release:        %autorelease
Summary:        A C++ application logging library
License:        BSD-3-Clause
URL:            https://github.com/google/glog
#!RemoteAsset
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
%ifarch riscv64
# TODO: We need to add ucontext/mcontext support for riscv64
BuildOption(check):  --output-on-failure -E "(logging|stacktrace|symbolize)"
%else
BuildOption(check):  --output-on-failure -E stacktrace
%endif

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  pkgconfig(gflags)
BuildRequires:  cmake
BuildRequires:  make

%description
Google glog is a library that implements application-level
logging. This library provides logging APIs based on C++-style
streams and various helper macros.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%doc ChangeLog COPYING README.rst
%{_libdir}/libglog.so.*

%files devel
%{_libdir}/libglog.so
%{_libdir}/cmake/glog/
%dir %{_includedir}/glog
%{_includedir}/glog/*

%changelog
%autochangelog
