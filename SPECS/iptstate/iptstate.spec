# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           iptstate
Summary:        A top-like display of IP Tables state table entries
Version:        2.2.7
Release:        %autorelease
License:        zlib
URL:            http://www.phildev.net/iptstate/
VCS:            git:https://github.com/jaymzh/iptstate
#!RemoteAsset
Source0:        https://github.com/jaymzh/iptstate/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

# to support right install.
Patch0:         0001-fix-install-dir.patch

BuildOption(build):  LIBS="-lncurses -lnetfilter_conntrack -ltinfo"
BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  SBIN=%{_sbindir}
BuildOption(install):  DESTDIR=%{buildroot}

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(libnetfilter_conntrack)
BuildRequires:  pkgconfig

Requires:       iptables

%description
IP Tables State (iptstate) displays the states held by your stateful firewall
in a top-like manner.

# No configure.
%conf

%check
# No tests here.

%files
%license LICENSE
%doc README.md
%{_sbindir}/iptstate
%{_mandir}/man8/iptstate.8*

%changelog
%autochangelog
