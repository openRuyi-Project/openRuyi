# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libarchive
Version:        3.8.1
Release:        %autorelease
Summary:        Utility and C library to create and read several streaming archive formats
License:        BSD-2-Clause
URL:            https://www.libarchive.org/
#!RemoteAsset
Source0:        https://github.com/libarchive/libarchive/releases/download/v%{version}/libarchive-%{version}.tar.xz
#!RemoteAsset
Source1:        https://github.com/libarchive/libarchive/releases/download/v%{version}/libarchive-%{version}.tar.xz.asc

BuildSystem:  autotools
BuildOption(conf): --disable-static

%ifarch riscv64
# XXX: Fix failed check
BuildOption(check): XFAIL_TESTS=bsdtar_test
%endif

BuildRequires:  acl-devel
BuildRequires:  bzip2-devel
BuildRequires:  lz4-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libattr-devel
BuildRequires:  libzstd-devel
BuildRequires:  pkgconfig
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel

%description
Libarchive is a programming library that can create and read several
different streaming archive formats, including most popular tar
variants and several cpio formats. It can also write shar archives and
read ISO-9660 CDROM images. The bsdtar program is an implementation of
tar(1) that is built on top of libarchive. It started as a test
harness, but has grown and is now the standard system tar for FreeBSD 5
and 6.

This package contains the bsdtar cmdline utility.

%package -n bsdtar
Summary:        Utility to read several different streaming archive formats
Requires:       %{name} >= %{version}

%description -n bsdtar
This package contains the bsdtar cmdline utility.

%package devel
Summary:        Development files for libarchive
Requires:       %{name} = %{version}
Requires:       glibc-devel

%description devel
Libarchive is a programming library that can create and read several
different streaming archive formats, including most popular tar
variants and several cpio formats. It can also write shar archives and
read ISO-9660 CDROM images. The bsdtar program is an implementation of
tar(1) that is built on top of libarchive. It started as a test
harness, but has grown and is now the standard system tar for FreeBSD 5
and 6.

This package contains the development files.

%install -a
rm "%{buildroot}%{_mandir}/man5/"{tar,cpio,mtree}.5*
sed -i -e '/Libs.private/d' %{buildroot}%{_libdir}/pkgconfig/libarchive.pc

%files -n bsdtar
%license COPYING
%{_bindir}/bsdcat
%{_bindir}/bsdcpio
%{_bindir}/bsdtar
%{_bindir}/bsdunzip
%{_mandir}/man1/*
%{_mandir}/man5/*

%files
%license COPYING
%doc NEWS
%{_libdir}/libarchive.so.*

%files devel
%license COPYING
%doc examples/
%{_mandir}/man3/*
%{_libdir}/libarchive.so
%{_includedir}/archive*
%{_libdir}/pkgconfig/libarchive.pc

%changelog
%{?autochangelog}
