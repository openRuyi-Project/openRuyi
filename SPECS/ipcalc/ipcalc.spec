# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ipcalc
Version:        1.0.3
Release:        %autorelease
Summary:        IP network address calculator
License:        GPL-2.0-or-later
URL:            https://gitlab.com/ipcalc/ipcalc
#!RemoteAsset
Source0:        https://gitlab.com/ipcalc/ipcalc/-/archive/%{version}/ipcalc-%{version}.tar.gz
BuildSystem:    meson

# some tests relys on the build enviroment.
Patch0:         0001-remove-some-test.patch

BuildOption(conf):  -Duse_runtime_linking=enabled
BuildOption(conf):  -Duse_maxminddb=enabled

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(libmaxminddb)

%description
ipcalc provides a simple way to calculate IP information for a host or network.

%files
%license COPYING
%doc README.md
%{_bindir}/ipcalc

%changelog
%autochangelog
