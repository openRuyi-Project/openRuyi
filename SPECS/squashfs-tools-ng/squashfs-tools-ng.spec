# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: ayostl <yao_xp@yeah.net>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           squashfs-tools-ng
Version:        1.3.2
Release:        %autorelease
Summary:        A new set of tools and libraries for working with SquashFS images
License:        LGPL-3.0-or-later AND GPL-3.0-or-later AND BSD-2-Clause AND MIT
URL:	        https://github.com/AgentD/squashfs-tools-ng
#!RemoteAsset
Source0:        https://infraroot.at/pub/squashfs/squashfs-tools-ng-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  help2man

%description
Squashfs is a highly compressed read-only filesystem for Linux.  This package
contains modified utilities for manipulating squashfs filesystems.

%package        devel
Summary:        Header files for squashfs-tools-ng development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The squashfs-tools-ng-devel package contains the header files needed to
develop programs that use the squashfs-tools-ng libsquashfs library.

%files
%license COPYING*
%doc README* CHANGELOG*
%{_bindir}/gensquashfs
%{_bindir}/rdsquashfs
%{_bindir}/sqfs2tar
%{_bindir}/sqfsdiff
%{_bindir}/tar2sqfs
%{_mandir}/man1/gensquashfs.1.*
%{_mandir}/man1/rdsquashfs.1.*
%{_mandir}/man1/sqfs2tar.1.*
%{_mandir}/man1/sqfsdiff.1.*
%{_mandir}/man1/tar2sqfs.1.*
%{_libdir}/libsquashfs.so.1{,.*}

%files devel
%license COPYING*
%doc doc/architecture.md doc/benchmark.txt doc/format.adoc doc/parallelism.txt
%{_libdir}/libsquashfs.so
%{_includedir}/sqfs/
%{_libdir}/pkgconfig/libsquashfs1.pc

%changelog
%autochangelog
