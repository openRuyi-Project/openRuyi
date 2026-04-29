# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libraw
Version:        0.22.1
Release:        %autorelease
Summary:        LibRaw is a library for reading RAW files from digital cameras
License:        BSD-3-Clause and (CDDL-1.0 or LGPL-2.1-only)
URL:            https://www.libraw.org
VCS:            git:https://github.com/LibRaw/LibRaw
#!RemoteAsset:  sha256:a789dc4e2409e2901d93793a4e0b80c7b49d0d97cf6ad71c850eb7616acfd786
Source:         https://www.libraw.org/data/LibRaw-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

%description
LibRaw is a library for reading RAW files from digital cameras.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a
rm -rf %{buildroot}%{_datadir}/doc/libraw/
rm -f %{buildroot}%{_libdir}/*.a

%files
%doc Changelog.txt
%license LICENSE.CDDL LICENSE.LGPL COPYRIGHT
%{_libdir}/libraw.so.*
%{_libdir}/libraw_r.so.*
%{_bindir}/*

%files devel
%doc doc/*
%{_includedir}/libraw/
%{_libdir}/libraw.so
%{_libdir}/libraw_r.so
%{_libdir}/pkgconfig/libraw.pc
%{_libdir}/pkgconfig/libraw_r.pc

%changelog
%autochangelog
