# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libnetfilter_acct
Version:        1.0.3
Release:        %autorelease
Summary:        Netfilter extended accounting infrastructure library
License:        GPL-2.0-only
URL:            https://netfilter.org/projects/libnetfilter_acct/
VCS:            git:https://git.netfilter.org/libnetfilter_acct
#!RemoteAsset:  sha256:4250ceef3efe2034f4ac05906c3ee427db31b9b0a2df41b2744f4bf79a959a1a
Source0:        %{url}/files/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libnfnetlink)

%description
libnetfilter_acct is a userspace library providing an interface to
the Netfilter extended accounting infrastructure.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libnetfilter_acct is a userspace library providing an interface to
the Netfilter extended accounting infrastructure.

%files
%doc README
%license COPYING
%{_libdir}/libnetfilter_acct.so.*

%files devel
%{_libdir}/libnetfilter_acct.so
%{_libdir}/pkgconfig/libnetfilter_acct.pc
%dir %{_includedir}/libnetfilter_acct
%{_includedir}/libnetfilter_acct/*.h

%changelog
%autochangelog
