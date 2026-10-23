# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cpp-httplib
Version:        0.63.0
Release:        %autorelease
Summary:        A C++11 single-file header-only cross platform HTTP/HTTPS library
License:        MIT
URL:            https://github.com/yhirose/cpp-httplib
#!RemoteAsset:  sha256:44ab42e16926e95f7641d286bc90d739ab1c16886114d7cc5bc7a9f905c5edf8
Source0:        https://github.com/yhirose/cpp-httplib/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DHTTPLIB_COMPILE=ON
BuildOption(conf):  -DHTTPLIB_USE_OPENSSL_IF_AVAILABLE=ON
BuildOption(conf):  -DHTTPLIB_TEST=ON
# Online cases require external network access unavailable in OBS builds.
BuildOption(check):  --parallel 1 --exclude-regex '_Online$'

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(gtest)

%description
A C++11 single-file header-only cross platform HTTP/HTTPS library.
It's extremely easy to setup. Just include the httplib.h file in your code!

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for cpp-httplib.

%install -a
rm -rf %{buildroot}%{_docdir}/httplib
rm -rf %{buildroot}%{_licensedir}/httplib

%files
%doc README.md
%license LICENSE
%{_libdir}/libcpp-httplib.so.*

%files devel
%{_libdir}/libcpp-httplib.so
%{_includedir}/httplib.h
%{_libdir}/cmake/httplib/

%changelog
%autochangelog
