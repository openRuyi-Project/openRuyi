# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xapian
Version:        1.4.29
Release:        %autorelease
Summary:        An Open Source Probabilistic Information Retrieval Library
License:        GPL-2.0-or-later
URL:            https://www.xapian.org/
#!RemoteAsset
Source0:        https://oligarchy.co.uk/xapian/%{version}/xapian-core-%{version}.tar.xz

BuildSystem:    autotools

BuildOption(conf): --disable-static
BuildOption(conf): --disable-rpath
%ifnarch x86_64
BuildOption(conf): --disable-sse
%endif

BuildRequires:    gcc-c++ libuuid zlib-devel

%description
Xapian is a highly adaptable toolkit which allows developers to easily add advanced
indexing and search facilities to their own applications.

%package devel
Summary:        Development files for the Xapian library
Requires:       %{name} = %{version}
Requires:       util-linux-devel
Requires:       zlib-devel

%description devel
This package provides the header files, libraries, and documentation for
developing applications that use the Xapian library.


%install -a
find %{buildroot} -type f -name "*.la" -delete -print
# Remove the dev docs, we pick them up below
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/*
%{_datadir}/xapian-core
%{_libdir}/libxapian.so.*

%files devel
%doc HACKING PLATFORMS docs/*html docs/apidoc
%{_libdir}/libxapian.so
%{_libdir}/cmake/xapian
%{_libdir}/pkgconfig/xapian-core.pc
%{_datadir}/aclocal/xapian.m4
%{_includedir}/xapian*
%{_mandir}/man1/*

%changelog
%{?autochangelog}
