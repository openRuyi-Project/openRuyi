# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libarchive
Version:        3.8.7
Release:        %autorelease
Summary:        Utility and C library to create and read several streaming archive formats
License:        BSD-2-Clause
URL:            https://www.libarchive.org/
VCS:            git:https://github.com/libarchive/libarchive
#!RemoteAsset:  sha256:d3a8ba457ae25c27c84fd2830a2efdcc5b1d40bf585d4eb0d35f47e99e5d4774
Source0:        https://github.com/libarchive/libarchive/releases/download/v%{version}/libarchive-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  libtool
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(openssl)

%description
Libarchive is a programming library that can create and read several
different streaming archive formats, including most popular tar
variants and several cpio formats. It can also write shar archives and
read ISO-9660 CDROM images. The bsdtar program is an implementation of
tar(1) that is built on top of libarchive. It started as a test
harness, but has grown and is now the standard system tar for FreeBSD 5
and 6.

This package contains the bsdtar cmdline utility.

%package     -n bsdtar
Summary:        Utility to read several different streaming archive formats
Requires:       %{name}%{?_isa} >= %{version}-%{release}

%description -n bsdtar
This package contains the bsdtar cmdline utility.

%package        devel
Summary:        Development files for libarchive
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glibc-devel

%description    devel
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
%autochangelog
