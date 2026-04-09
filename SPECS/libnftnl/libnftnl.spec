# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libnftnl
Version:        1.3.0
Release:        %autorelease
Summary:        Library for low-level interaction with nftables Netlink's API over libmnl
License:        GPL-2.0-or-later
URL:            https://netfilter.org/projects/libnftnl/
VCS:            git:https://git.netfilter.org/libnftnl
#!RemoteAsset
Source0:        %{url}/files/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        %{url}/files/%{name}-%{version}.tar.xz.sig
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-silent-rules

BuildRequires:  pkgconfig(libmnl)
BuildRequires:  make

%description
A library for low-level interaction with nftables Netlink's API over libmnl.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%doc COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/libnft*.so
%{_libdir}/pkgconfig/libnftnl.pc
%{_includedir}/libnftnl

%changelog
%autochangelog
