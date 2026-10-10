# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libmnl
Version:        1.0.5
Release:        %autorelease
Summary:        A minimalistic user-space library oriented to netlink developers
License:        LGPL-2.1-or-later
URL:            https://netfilter.org/projects/libmnl
VCS:            git:https://git.netfilter.org/libmnl
#!RemoteAsset:  sha256:274b9b919ef3152bfb3da3a13c950dd60d6e2bcd54230ffeca298d03b40d0525
Source0:        https://netfilter.org/projects/libmnl/files/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-doxygen=no

BuildRequires:  gcc

%description
libmnl is a minimalistic user-space library oriented to Netlink developers.
It aims to provide simple helpers to avoid re-inventing the wheel when
dealing with Netlink headers and TLVs.

%package        devel
Summary:        Development files for libmnl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, libraries, and examples for
developing applications that use libmnl.

%files
%doc README
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc examples
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmnl.pc

%changelog
%autochangelog
