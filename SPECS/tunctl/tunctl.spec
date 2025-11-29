# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tunctl
Version:        1.5
Release:        %autorelease
Summary:        Create and remove virtual network interfaces
License:        GPL-1.0-or-later
URL:            http://tunctl.sourceforge.net/
#!RemoteAsset
Source:         http://downloads.sourceforge.net/tunctl/tunctl-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install): BIN_DIR=%{_sbindir}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  docbook-utils

%description
tunctl is a tool to set up and maintain persistent TUN/TAP network
interfaces. It originates from the User Mode Linux project.

# No configure.
%conf

# No tests.
%check

%files
%doc ChangeLog
# %license COPYING
%{_sbindir}/tunctl
%{_mandir}/man8/tunctl.8*

%changelog
%{?autochangelog}
