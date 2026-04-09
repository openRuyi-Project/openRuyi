# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tcpdump
Version:        4.99.5
Release:        %autorelease
Summary:        A network traffic monitoring tool
License:        BSD-3-Clause AND ISC
URL:            https://www.tcpdump.org
VCS:            git:https://github.com/the-tcpdump-group/tcpdump.git
#!RemoteAsset
Source0:        https://www.tcpdump.org/release/tcpdump-%{version}.tar.xz
Source1:        tcpdump-sysusers.conf
BuildSystem:    autotools

BuildOption(conf):  --with-crypto
BuildOption(conf):  --with-user=tcpdump
BuildOption(conf):  --without-smi
BuildOption(build):  CFLAGS="%{optflags} -fno-strict-aliasing -DGUESS_TSO"

BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros

%description
Tcpdump is a command-line tool for monitoring network traffic. This package
also includes the tcpslice utility for manipulating tcpdump savefiles.

%install -a
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/tcpdump.conf

%files
%license LICENSE
%doc README.md CHANGES CREDITS
%{_bindir}/tcpdump*
%{_sysusersdir}/tcpdump.conf
%{_mandir}/man1/

%changelog
%autochangelog
