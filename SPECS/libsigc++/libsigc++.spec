# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libsigc++
Version:        3.6.0
Release:        %autorelease
Summary:        Typesafe signal framework for C++
License:        LGPL-2.1-or-later
URL:            https://github.com/libsigcplusplus/libsigcplusplus
#!RemoteAsset
Source:         https://download.gnome.org/sources/libsigc++/3.6/libsigc++-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dbuild-documentation=false

BuildRequires:  meson
BuildRequires:  gcc-c++

%description
libsigc++ implements a typesafe callback system for standard C++. It
allows you to define signals and to connect those signals to any
callback function.

%package        devel
Summary:        Development tools for the typesafe signal framework for C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains the libraries and header files
needed for development with %{name}.

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libsigc-3.0.so.0*

%files devel
%{_includedir}/sigc++-3.0/
%{_libdir}/sigc++-3.0/
%{_libdir}/pkgconfig/sigc++-3.0.pc
%{_libdir}/libsigc-3.0.so

%changelog
%autochangelog
