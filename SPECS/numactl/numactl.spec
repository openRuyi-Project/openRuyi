# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           numactl
Version:        2.0.19
Release:        %autorelease
Summary:        Library for tuning for Non Uniform Memory Access machines
License:        GPL-2.0-only
URL:            https://github.com/numactl/numactl
#!RemoteAsset
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

%description
Simple NUMA policy support. It consists of a numactl program to run
other programs with a specific NUMA policy.

%package        devel
Summary:        Development package for building Applications that use numa
Requires:       %{name} = %{version}-%{release}
License:        LGPL-2.1-only and GPL-2.0-only

%description    devel
Provides development headers for numa library calls

%files
%doc README.md
%{_bindir}/numactl
%{_bindir}/numademo
%{_bindir}/numastat
%{_bindir}/memhog
%{_bindir}/migspeed
%{_bindir}/migratepages
%{_libdir}/libnuma.so.1.0.0
%{_libdir}/libnuma.so.1
%{_mandir}/man8/*.8*
# Already included this in man-pages package
%exclude %{_mandir}/man2/*.2*

%files devel
%{_libdir}/libnuma.so
%exclude %{_libdir}/libnuma.a
%{_libdir}/pkgconfig/numa.pc
%{_includedir}/numa.h
%{_includedir}/numaif.h
%{_includedir}/numacompat1.h
%{_mandir}/man3/*.3*

%changelog
%{?autochangelog}
