# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libdaemon
Version:        0.14
Release:        %autorelease
Summary:        A lightweight daemon framework in C
License:        LGPL-2.1-or-later
URL:            https://0pointer.de/lennart/projects/libdaemon/
# VCS: Upstream git dead
#!RemoteAsset
Source:         https://0pointer.de/lennart/projects/libdaemon/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool

%description
libdaemon is a lightweight C library that eases the writing of UNIX daemons.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, documentation, and other files needed
to develop applications that use the libdaemon framework.

%conf -p
autoreconf -fiv

%files
%doc README
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc doc/README.html doc/style.css
%{_datadir}/doc/%{name}/*

%changelog
%autochangelog
