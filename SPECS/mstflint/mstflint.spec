# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define ver 4.34.0-2

Name:           mstflint
Version:        4.34.0.2
Release:        %autorelease
Summary:        Mellanox firmware burning tool
License:        (GPL-2.0-only OR BSD-2-Clause) AND BSD-3-Clause AND MIT
URL:            https://github.com/Mellanox/mstflint
#!RemoteAsset
Source0:        https://github.com/Mellanox/mstflint/archive/refs/tags/v%{ver}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-fw-mgr
BuildOption(conf):  --enable-openssl
BuildOption(conf):  --enable-adb-generic-tools
BuildOption(conf):  --disable-inband

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(expat)

Requires:       python3

%description
This package contains firmware update tool, vpd dump and register dump tools
for network adapters based on Mellanox Technologies chips.

%conf -p
./autogen.sh

%install -a
rm -fr %{buildroot}%{_includedir}
chmod +x %{buildroot}/%{_libdir}/mstflint/python_tools/*.so 2>/dev/null || :
chmod +x %{buildroot}/%{_libdir}/mstflint/sdk/*.so 2>/dev/null || :

%files
%doc README
%{_bindir}/*
%{_sysconfdir}/mstflint
%{_libdir}/mstflint
%{_libdir}/libmtcr_ul.a
%{_datadir}/mstflint
%{_mandir}/man1/*

%changelog
%autochangelog
