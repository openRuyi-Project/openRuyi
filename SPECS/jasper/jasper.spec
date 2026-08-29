# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jasper
Version:        4.2.9
Release:        %autorelease
Summary:        Implementation of the JPEG-2000 standard, Part 1
License:        JasPer-2.0
URL:            http://www.ece.uvic.ca/~frodo/jasper/
VCS:            git:https://github.com/jasper-software/jasper
#!RemoteAsset:  sha256:b0e5af6b54c274b9670c7e32ddbf6c802d88c896062d760267695dd0aa7014ff
Source0:        https://github.com/jasper-software/jasper/archive/refs/tags/version-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DJAS_ENABLE_DOC:BOOL=OFF
BuildOption(conf):  -DJAS_ENABLE_SHARED=ON
BuildOption(conf):  -DALLOW_IN_SOURCE_BUILD=ON
BuildOption(conf):  -DJAS_ENABLE_OPENGL=OFF

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xi)

%description
This package contains an implementation of the image compression
standard JPEG-2000, Part 1. It consists of tools for conversion to and
from the JP2 and JPC formats.

%package        devel
Summary:        Header files, libraries and developer documentation
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libjpeg)

%description    devel
Header files and libraries for developing applications that use JasPer.

%install -a
rm -rf %{buildroot}%{_docdir}/JasPer

%files
%{_bindir}/imgcmp
%{_bindir}/imginfo
%{_bindir}/jasper
%{_mandir}/man1/img*
%{_mandir}/man1/jasper.1*
%doc README.md
%license COPYRIGHT.txt LICENSE.txt
%{_libdir}/libjasper.so.7*

%files devel
%doc doc/*
%{_includedir}/jasper/
%{_libdir}/libjasper.so
%{_libdir}/pkgconfig/jasper.pc

%changelog
%autochangelog
