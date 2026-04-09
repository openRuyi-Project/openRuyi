# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libmd
Version:        1.1.0
Release:        %autorelease
Summary:        Message digest functions from BSD systems
License:        BSD-2-Clause OR BSD-3-Clause OR ISC OR LicenseRef-openRuyi-Public-Domain
URL:            https://www.hadrons.org/software/libmd/
VCS:            git:https://git.hadrons.org/git/libmd.git
#!RemoteAsset
Source0:        https://archive.hadrons.org/software/libmd/libmd-%{version}.tar.xz
#!RemoteAsset
Source1:        https://archive.hadrons.org/software/libmd/libmd-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-silent-rules

BuildRequires:  pkgconfig

%description
The libmd library provides a few message digest ("hash") functions, as
found on various BSDs on a library with the same name and with a compatible
API.

%package        devel
Summary:        Provides message digest functions from BSD systems
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libmd library provides a few message digest ("hash") functions, as
found on various BSDs on a library with the same name and with a compatible
API.

Digests supported: MD2/4/5, RIPEMD160, SHA1, SHA2-256/384/512.

%files
%license COPYING
%{_libdir}/libmd.so.*

%files devel
%license COPYING
%doc ChangeLog README
%{_includedir}/*
%{_libdir}/libmd.so
%{_libdir}/pkgconfig/libmd.pc
%{_mandir}/man3/*.3*
%{_mandir}/man7/libmd.7*

%changelog
%autochangelog
