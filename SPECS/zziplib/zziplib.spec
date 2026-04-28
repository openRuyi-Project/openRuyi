# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           zziplib
Version:        0.13.80
Release:        %autorelease
Summary:        Lightweight library to extract data from zip files
License:        LGPL-2.0-or-later OR MPL-1.1
URL:            https://github.com/gdraheim/zziplib
#!RemoteAsset:  sha256:21f40d111c0f7a398cfee3b0a30b20c5d92124b08ea4290055fbfe7bdd53a22c
Source0:        https://github.com/gdraheim/zziplib/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  zip
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)

%description
The zziplib library offers the ability to easily extract data from files
archived in a single zip file.

%package        devel
Summary:        Development files for the zziplib library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       pkgconfig(zlib)

%description    devel
This package contains files required to build applications that use the
zziplib library.

%files
%doc ChangeLog TODO
%license docs/COPYING*
%{_libdir}/*.so.*
%{_bindir}/unzzip*
%{_bindir}/unzip-mem
%{_bindir}/zz*

%files devel
%doc docs/README.SDL docs/*.htm
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/zziplib/*.cmake
%{_libdir}/pkgconfig/zzipfseeko.pc
%{_libdir}/pkgconfig/zziplib.pc
%{_libdir}/pkgconfig/zzipmmapped.pc
%{_libdir}/pkgconfig/zzipwrap.pc
%{_datadir}/aclocal/*.m4
%{_mandir}/man3/*

%changelog
%autochangelog
