# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libnetfilter_conntrack
Version:        1.0.9
Release:        %autorelease
Summary:        Netfilter conntrack userspace library
License:        GPL-2.0-or-later
URL:            https://netfilter.org/projects/libnetfilter_conntrack
VCS:            git:https://git.netfilter.org/libnetfilter_conntrack
#!RemoteAsset
Source0:        %{url}/files/%name-%version.tar.bz2
#!RemoteAsset
Source1:        %{url}/files/%name-%version.tar.bz2.sig
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-rpath

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libnfnetlink)

%description
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table.

%package        devel
Summary:        Netfilter conntrack userspace library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table.

%conf -p
autoreconf -fiv

%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnetfilter_conntrack.pc
%dir %{_includedir}/libnetfilter_conntrack
%{_includedir}/libnetfilter_conntrack/*.h

%changelog
%{?autochangelog}
