# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libnetfilter_cttimeout
Version:        1.0.1
Release:        %autorelease
Summary:        Netfilter/conntrack Timeout policy tuning
License:        GPL-2.0-or-later
URL:            http://netfilter.org
#!RemoteAsset
Source0:        http://netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf): --disable-static

BuildRequires:  libmnl-devel pkgconfig linux-headers gcc make

%description
libnetfilter_cttimeout is the userspace library that provides the programming
interface to the fine-grain connection tracking timeout infrastructure.

%package        devel
Summary:        Development files for the libnetfilter_cttimeout library
Requires:       %{name} = %{version}
Requires:       libmnl-devel
Requires:       linux-headers

%description    devel
This package includes header files and libraries necessary for developing
applications that use the libnetfilter_cttimeout library.

%install -a
find %{buildroot} -type f -name "*.la" -delete -print

%files
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/libnetfilter_cttimeout
%{_includedir}/libnetfilter_cttimeout/*.h

%changelog
%{?autochangelog}
