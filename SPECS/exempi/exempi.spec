# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           exempi
Version:        2.6.6
Release:        %autorelease
Summary:        Library for easy parsing of XMP metadata
License:        BSD-3-Clause
URL:            https://gitlab.freedesktop.org/libopenraw/exempi
#!RemoteAsset
Source0:        https://libopenraw.freedesktop.org/download/exempi-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  CPPFLAGS="-I%{_includedir} -fno-strict-aliasing -DBanAllEntityUsage=1"

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
Exempi provides a library for easy parsing of XMP metadata. It is a port of
Adobe XMP SDK to work on UNIX.

%package        devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the libraries and header files needed for
developing with exempi.

%conf -p
./autogen.sh

%install -a
rm -rf %{buildroot}%{_libdir}/*.a

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/exempi
%{_libdir}/libexempi.so.8*
%{_mandir}/man1/exempi.1*

%files devel
%{_includedir}/exempi-2.0/
%{_libdir}/libexempi.so
%{_libdir}/pkgconfig/exempi-2.0.pc

%changelog
%{?autochangelog}
