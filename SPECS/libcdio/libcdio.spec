# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libcdio
Version:        2.3.0
Release:        %autorelease
Summary:        CD-ROM input and control library
License:        GPL-3.0-or-later AND BSD-2-Clause AND LGPL-2.1-or-later
URL:            https://github.com/libcdio/libcdio
#!RemoteAsset:  sha256:53e83d284667535a767fd2d31edad1a6701591960459df373a10f1f21e80a7ed
Source0:        https://github.com/libcdio/libcdio/releases/download/%{version}/libcdio-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-vcd-info
BuildOption(conf):  --disable-cddb

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  help2man
BuildRequires:  gettext-devel

%description
This library provides an interface for CD-ROM access. It can be used
by applications that need OS- and device-independent access to CD-ROM
devices.

%package        devel
Summary:        Header files and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains header files and libraries for developing
applications that use %{name}.

%files
%license COPYING
%doc AUTHORS NEWS.md README.md README-libcdio.md THANKS TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_infodir}/*
%{_mandir}/man1/*

%files devel
%{_includedir}/cdio
%{_includedir}/cdio++
%{_libdir}/*.so
%{_libdir}/pkgconfig/libcdio++.pc
%{_libdir}/pkgconfig/libcdio.pc
%{_libdir}/pkgconfig/libiso9660++.pc
%{_libdir}/pkgconfig/libiso9660.pc
%{_libdir}/pkgconfig/libudf.pc

%changelog
%autochangelog
