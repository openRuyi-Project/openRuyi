# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libmspack
Version:        0.11
Release:        %autorelease
Summary:        Library for Microsoft CAB file compression and decompression
License:        LGPL-2.1-or-later
URL:            http://www.cabextract.org.uk/libmspack/
#!RemoteAsset
Source0:        https://github.com/kyz/libmspack/archive/v%{version}alpha/libmspack-%{version}alpha.tar.gz
BuildSystem:    autotools

BuildOption(conf): --disable-silent-rules
BuildOption(conf): --disable-static

BuildOption(build): CFLAGS="%{optflags} -fno-strict-aliasing" -C libmspack
BuildOption(install): -C libmspack
BuildRequires:  doxygen gcc autoconf automake libtool

%description
libmspack is a library for compressing and decompressing Microsoft cabinet
(CAB) files and other related formats.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
This package contains the header files, documentation, and other files needed
to develop applications that use libmspack.

%conf -p
cd libmspack
autoreconf -fi

%install -a
find %{buildroot} -type f -name "*.la" -delete -print

%files
%{_libdir}/libmspack.so.*

%files devel
%{_includedir}/mspack.h
%{_libdir}/libmspack.so
%{_libdir}/pkgconfig/libmspack.pc

%changelog
%{?autochangelog}
