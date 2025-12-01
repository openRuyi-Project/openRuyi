# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libnetfilter_log
Version:        1.0.2
Release:        %autorelease
Summary:        Netfilter logging userspace library
License:        GPL-2.0-only
URL:            http://netfilter.org
#!RemoteAsset
Source0:        http://netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf): --disable-static
BuildOption(conf): --disable-rpath

BuildRequires:  gcc make autoconf automake libtool libmnl-devel
BuildRequires:  libnfnetlink-devel pkgconfig linux-headers

%description
libnetfilter_log is a userspace library providing an interface to packets
that have been logged by the kernel packet filter. It is part of a system
that deprecates the old syslog/dmesg based packet logging.

%package        devel
Summary:        Development files for the Netfilter logging library
Requires:       %{name} = %{version}
Requires:       pkgconfig
Requires:       linux-headers
Requires:       libnfnetlink-devel

%description    devel
This package contains the header files and development library for
libnetfilter_log.

%install -a
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc

%changelog
%{?autochangelog}
