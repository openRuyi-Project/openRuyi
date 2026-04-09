# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libpcap
Version:        1.10.5
Release:        %autorelease
Summary:        A system-independent interface for user-level packet capture
License:        BSD-3-Clause
URL:            https://www.tcpdump.org
VCS:            git:https://github.com/the-tcpdump-group/libpcap
#!RemoteAsset
Source:         https://www.tcpdump.org/release/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc

%description
Libpcap provides a portable framework for low-level network monitoring.
Applications include network statistics collection, security monitoring,
network debugging, etc.

%package        devel
Summary:        Header files for libpcap development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, static libraries and documentation
for developing applications that use libpcap.

%package        help
Summary:        Documentation for libpcap
BuildArch:      noarch

%description    help
This package contains supplementary documentation files for libpcap.

%conf -p
export CFLAGS="%{optflags} -fno-strict-aliasing"

# no test
%check

%files
%license LICENSE
%{_libdir}/libpcap.so.*

%files  devel
%{_bindir}/pcap-config
%{_includedir}/pcap/
%{_includedir}/pcap.h
%{_includedir}/pcap-bpf.h
%{_includedir}/pcap-namedb.h
%{_libdir}/libpcap.so
%{_libdir}/libpcap.a
%{_libdir}/pkgconfig/libpcap.pc
%{_mandir}/man3/pcap*.3*

%files  help
%doc README.md CHANGES CREDITS
%{_mandir}/man1/pcap-config.1*
%{_mandir}/man5/pcap-savefile.5*
%{_mandir}/man7/pcap-filter.7*
%{_mandir}/man7/pcap-linktype.7*
%{_mandir}/man7/pcap-tstamp.7*

%changelog
%autochangelog
