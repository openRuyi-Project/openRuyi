# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libsigc++2
Version:        2.12.1
Release:        %autorelease
Summary:        Typesafe signal framework for C++
License:        LGPL-2.1-or-later
URL:            https://github.com/libsigcplusplus/libsigcplusplus
#!RemoteAsset:  sha256:a9dbee323351d109b7aee074a9cb89ca3e7bcf8ad8edef1851f4cf359bd50843
Source0:        https://github.com/libsigcplusplus/libsigcplusplus/releases/download/%{version}/libsigc++-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dbuild-documentation=false

BuildRequires:  meson
BuildRequires:  gcc-c++

%description
libsigc++ implements a typesafe callback system for standard C++.
This is the legacy 2.x version.

%package        devel
Summary:        Development tools for the typesafe signal framework for C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains the libraries and header files
needed for development with %{name}.

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libsigc-2.0.so.*

%files devel
%{_includedir}/sigc++-2.0/
%{_libdir}/sigc++-2.0/
%{_libdir}/pkgconfig/sigc++-2.0.pc
%{_libdir}/libsigc-2.0.so

%changelog
%autochangelog
