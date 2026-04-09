# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libmng
Version:        2.0.3
Release:        %autorelease
Summary:        Library for Multiple-image Network Graphics support
License:        Zlib
URL:            http://www.libmng.com/
# VCS: No VCS link available
#!RemoteAsset
Source0:        https://sourceforge.net/projects/libmng/files/libmng-devel/%{version}/libmng-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --enable-shared
BuildOption(conf):  --disable-static
BuildOption(conf):  --with-zlib
BuildOption(conf):  --with-jpeg
BuildOption(conf):  --with-gnu-ld
BuildOption(conf):  --with-lcms2

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(lcms2)

%description
LibMNG is a library for accessing graphics in MNG (Multi-image Network
Graphics) and JNG (JPEG Network Graphics) formats.

%package        devel
Summary:        Development files for libmng
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(zlib)
Requires:       pkgconfig(libjpeg)

%description    devel
This package contains files needed for developing or compiling applications
which use MNG graphics.

%conf -p
autoreconf -fiv

%files
%doc CHANGES LICENSE README*
%{_libdir}/*.so.*

%files devel
%doc doc/*
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_libdir}/pkgconfig/libmng.pc

%changelog
%autochangelog
