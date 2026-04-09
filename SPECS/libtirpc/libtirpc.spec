# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libtirpc
Version:        1.3.7
Release:        %autorelease
Summary:        Transport-independent RPC library
License:        SISSL AND BSD-3-Clause
URL:            https://sourceforge.net/projects/libtirpc/
VCS:            git:git://linux-nfs.org/~steved/libtirpc
#!RemoteAsset
Source:         https://downloads.sourceforge.net/libtirpc/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-gssapi

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(krb5)

%description
Libtirpc is a Transport-Independent RPC library for Linux

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(krb5)

%description    devel
This package contains the header files, pkg-config support file, and
symbolic links needed to develop applications that use libtirpc.

%files
%license COPYING
%doc AUTHORS
%config(noreplace) %{_sysconfdir}/netconfig
%config(noreplace) %{_sysconfdir}/bindresvport.blacklist
%{_mandir}/man5/netconfig.5*
%{_libdir}/libtirpc.so.*

%files devel
%{_includedir}/tirpc/
%{_libdir}/libtirpc.so
%{_libdir}/pkgconfig/libtirpc.pc
%{_mandir}/man3/*

%changelog
%autochangelog
