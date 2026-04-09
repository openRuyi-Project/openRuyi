# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           iw
Version:        6.17
Release:        %autorelease
Summary:        A nl80211 based wireless configuration tool
License:        ISC
URL:            https://wireless.wiki.kernel.org/en/users/Documentation/iw
VCS:            git:https://git.kernel.org/pub/scm/linux/kernel/git/jberg/iw.git
#!RemoteAsset
Source0:        http://www.kernel.org/pub/software/network/iw/iw-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(build):  CFLAGS="%{optflags}"
BuildOption(build):  LDFLAGS="%{build_ldflags}"
BuildOption(install):  SBINDIR=%{_sbindir}
BuildOption(install):  DESTDIR=%{buildroot}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libnl-3.0)

%description
iw is a nl80211 based CLI configuration utility for wireless devices.
It supports all recent Linux wireless drivers.

# No configure.
%conf

%files
%license COPYING
%{_sbindir}/iw
%{_mandir}/man8/iw.8*

%changelog
%autochangelog
