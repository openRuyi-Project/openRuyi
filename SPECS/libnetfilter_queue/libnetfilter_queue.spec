# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libnetfilter_queue
Version:        1.0.5
Release:        %autorelease
Summary:        Netfilter queue userspace library
License:        GPL-2.0-only
URL:            http://netfilter.org
VCS:            git:https://git.netfilter.org/libnetfilter_queue
#!RemoteAsset
Source0:        https://netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  linux-headers
BuildRequires:  pkgconfig(libnfnetlink)
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  make

%description
libnetfilter_queue is a userspace library providing an API to packets
that have been queued by the kernel packet filter. It deprecates the
old ip_queue / libipq mechanism.

%package        devel
Summary:        Development files for the libnetfilter_queue library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libnfnetlink)
Requires:       linux-headers
Requires:       pkgconfig

%description    devel
This package includes header files and libraries for developing applications
that use the libnetfilter_queue library.

%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnetfilter_queue.pc
%{_includedir}/libnetfilter_queue/*.h

%changelog
%{?autochangelog}
