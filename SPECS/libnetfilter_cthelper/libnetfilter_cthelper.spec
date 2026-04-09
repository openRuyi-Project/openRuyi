# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libnetfilter_cthelper
Version:        1.0.1
Release:        %autorelease
Summary:        Library for the user-space conntrack helper infrastructure
License:        GPL-2.0-only
URL:            http://www.netfilter.org/projects/libnetfilter_cthelper/index.html
VCS:            git:https://git.netfilter.org/libnetfilter_cthelper
#!RemoteAsset
Source0:        http://www.netfilter.org/projects/libnetfilter_cthelper/files/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig
BuildRequires:  linux-headers

%description
libnetfilter_cthelper is the userspace library that provides the programming
interface to the user-space helper infrastructure. With this library,
you can register, configure, enable and disable user-space helpers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libmnl)
Requires:       linux-headers

%description    devel
This package contains libraries and header files for developing applications
that use the libnetfilter_cthelper library.

%files
%license COPYING
%doc README
%{_libdir}/*.so.*

%files devel
%doc examples
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/libnetfilter_cthelper
%{_includedir}/libnetfilter_cthelper/*.h

%changelog
%autochangelog
