# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           glew
Version:        2.2.0
Release:        %autorelease
Summary:        The OpenGL Extension Wrangler Library
License:        BSD-3-Clause AND MIT
URL:            https://github.com/nigels-com/glew
#!RemoteAsset
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

BuildRequires:  gcc
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
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig(glu)

%description    devel
Development files for glew.

# No configure.
%conf

%install -a
find %{buildroot} -type f -name "*.a" -delete

%files
%license LICENSE.txt
%{_bindir}/*
%{_libdir}/libGLEW.so.2.2*

%files devel
%{_libdir}/libGLEW.so
%{_libdir}/pkgconfig/glew.pc
%{_includedir}/GL/*.h
%doc doc/*

%changelog
%{?autochangelog}
