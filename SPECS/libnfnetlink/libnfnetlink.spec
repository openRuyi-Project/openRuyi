# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libnfnetlink
Version:        1.0.2
Release:        %autorelease
Summary:        Netlink library for netfilter
License:        GPL-2.0-or-later
URL:            http://netfilter.org
VCS:            git:https://git.netfilter.org/libnfnetlink
#!RemoteAsset
Source0:        http://netfilter.org/projects/libnfnetlink/files/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildRequires:  linux-headers
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  make

%description
libnfnetlink is the low-level library for netfilter related kernel/userspace
communication. It provides a generic messaging infrastructure for in-kernel
netfilter subsystems and their userspace management tools.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       linux-headers

%description    devel
This package contains libraries and header files for developing applications
that use the libnfnetlink library.

%files
%license COPYING
%doc README
%{_libdir}/*.so.*

%files          devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/*.h

%changelog
%autochangelog
