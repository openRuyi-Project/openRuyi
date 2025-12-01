# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libtar
Version:        1.2.20
Release:        %autorelease
Summary:        Library for manipulating tar files from within C programs
License:        BSD-3-Clause
URL:            http://repo.or.cz/libtar.git
#!RemoteAsset
Source:         http://repo.or.cz/libtar.git/snapshot/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): --disable-static
BuildRequires:  libtool autoconf automake gcc

%description
Libtar is a C library for manipulating POSIX tar files. It handles adding
and extracting files to/from a tar archive. Requires gcc, make, and zlib.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
This package contains the header files, documentation, and other development
files for the libtar library.

%prep -a
# set correct version for .so build
%global ltversion %(echo %{version} | tr '.' ':')
sed -i 's/-rpath $(libdir)/-rpath $(libdir) -version-number %{ltversion}/' \
  lib/Makefile.in

%conf -p
autoreconf -fi

%install -a
find %{buildroot} -type f -name "*.la" -delete -print

%files
%doc TODO README ChangeLog*
%license COPYRIGHT
%{_bindir}/%{name}
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/libtar.h
%{_includedir}/libtar_listhash.h
%{_libdir}/lib*.so
%{_mandir}/man3/*.3*

%changelog
%{?autochangelog}
