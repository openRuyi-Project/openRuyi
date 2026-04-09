# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           luksmeta
Version:        10
Release:        %autorelease
Summary:        Utility for storing small metadata in the LUKSv1 header
License:        LGPL-2.1-or-later
URL:            https://github.com/latchset/luksmeta
#!RemoteAsset
Source0:        https://github.com/latchset/luksmeta/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcryptsetup)
BuildRequires:  cryptsetup
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

%description
LUKSMeta is a command line utility for storing small portions of metadata in
the LUKSv1 header for use before unlocking the volume.

%package        devel
Summary:        Development files for libluksmeta
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for the LUKSMeta library.

%conf -p
autoreconf -fiv

%files
%{_bindir}/luksmeta
%{_libdir}/libluksmeta.so.0*

%files devel
%{_includedir}/luksmeta.h
%{_libdir}/libluksmeta.so
%{_libdir}/pkgconfig/luksmeta.pc

%changelog
%autochangelog
