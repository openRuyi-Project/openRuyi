# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cpp-httplib
Version:        0.30.1
Release:        %autorelease
Summary:        A C++11 single-file header-only cross platform HTTP/HTTPS library
License:        MIT
URL:            https://github.com/yhirose/cpp-httplib
#!RemoteAsset:  sha256:2818b183757e29dd52b47a185f0cea9ef2d0fba377d8710b450a26328e51c2fe
Source0:        https://github.com/yhirose/cpp-httplib/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

# https://github.com/yhirose/cpp-httplib/issues/2324
Patch0:         0001-cpp-httplib-test-issue2301-online.patch

BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DHTTPLIB_COMPILE=ON
BuildOption(conf):  -DHTTPLIB_USE_OPENSSL_IF_AVAILABLE=ON
BuildOption(conf):  -DHTTPLIB_TEST=ON
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
%license LICENSE
%doc README.md
%{_libdir}/libcpp-httplib.so.*

%files devel
%{_libdir}/libcpp-httplib.so
%{_includedir}/httplib.h
%{_libdir}/cmake/httplib/

%changelog
%autochangelog
