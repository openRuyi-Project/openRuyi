# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libnetfilter_log
Version:        1.0.2
Release:        %autorelease
Summary:        Netfilter logging userspace library
License:        GPL-2.0-only
URL:            http://netfilter.org
VCS:            git:https://git.netfilter.org/libnetfilter_log
#!RemoteAsset
Source0:        http://netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-rpath

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libnfnetlink)
BuildRequires:  pkgconfig
BuildRequires:  linux-headers

%description
libnetfilter_log is a userspace library providing an interface to packets
that have been logged by the kernel packet filter. It is part of a system
that deprecates the old syslog/dmesg based packet logging.

%package        devel
Summary:        Development files for the Netfilter logging library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       linux-headers
Requires:       pkgconfig(libnfnetlink)

%description    devel
This package contains the header files and development library for
libnetfilter_log.

%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
