# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           nghttp3
Version:        1.12.0
Release:        %autorelease
Summary:        The HTTP/3 library
License:        MIT
URL:            https://github.com/ngtcp2/nghttp3
#!RemoteAsset
Source:         https://github.com/ngtcp2/nghttp3/releases/download/v%{version}/nghttp3-%{version}.tar.xz
BuildSystem:    cmake
Patch:          0001-fix-install-path.patch

BuildOption(conf): -DENABLE_STATIC_LIB:BOOL=OFF

BuildRequires:  cmake >= 3.20
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(check)

%description
nghttp3 is a C library that implements QUIC and HTTP/3 framing layer.

%package devel
Summary:        Development files for the HTTP/3 library
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the header files and development libraries for nghttp3.

%files
%license COPYING
%doc %{_docdir}/%{name}
%{_libdir}/libnghttp3.so.9
%{_libdir}/libnghttp3.so.9.*

%files devel
%{_includedir}/nghttp3/
%{_libdir}/libnghttp3.so
%{_libdir}/pkgconfig/libnghttp3.pc
%{_libdir}/cmake/

%changelog
%{?autochangelog}
