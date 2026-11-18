# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           glew
Version:        2.3.1
Release:        %autorelease
Summary:        The OpenGL Extension Wrangler Library
License:        BSD-3-Clause AND MIT
URL:            https://github.com/nigels-com/glew
#!RemoteAsset:  sha256:09e0083ae46930aba9b53e72c92ee1a557e24ed393526fec26cb0ebabd834720
Source0:        https://github.com/nigels-com/glew/releases/download/glew-%{version}/glew-%{version}.zip
BuildSystem:    autotools

BuildOption(build):  CFLAGS.EXTRA="%{optflags} -fPIC"
BuildOption(build):  STRIP=
BuildOption(build):  GLEW_PREFIX=%{_prefix}
BuildOption(build):  GLEW_DEST=%{_prefix}
BuildOption(build):  includedir=%{_includedir}
BuildOption(build):  BINDIR=%{_bindir}
BuildOption(build):  LIBDIR=%{_libdir}
BuildOption(build):  PKGDIR=%{_libdir}/pkgconfig
BuildOption(install):  install.all
BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  GLEW_PREFIX=%{_prefix}
BuildOption(install):  GLEW_DEST=%{_prefix}
BuildOption(install):  includedir=%{_includedir}
BuildOption(install):  BINDIR=%{_bindir}
BuildOption(install):  LIBDIR=%{_libdir}
BuildOption(install):  PKGDIR=%{_libdir}/pkgconfig

BuildRequires:  zip
BuildRequires:  make
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform C/C++
extension loading library.
This package contains the demo GLEW utilities.

%package        devel
Summary:        Development files for glew
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(glu)

%description    devel
Development files for glew.

# No configure.
%conf

# No 'check' target
%check

%install -a
find %{buildroot} -type f -name "*.a" -delete

%files
%license LICENSE.txt
%{_bindir}/*
%{_libdir}/libGLEW.so.2.3*

%files devel
%{_libdir}/libGLEW.so
%{_libdir}/pkgconfig/glew.pc
%{_includedir}/GL/*.h
%doc doc/*

%changelog
%autochangelog
