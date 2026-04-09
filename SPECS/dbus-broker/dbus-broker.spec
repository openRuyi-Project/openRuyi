# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# default without launcher
%bcond launcher 0

Name:           dbus-broker
Version:        37
Release:        %autorelease
Summary:        D-Bus message bus implementation
License:        Apache-2.0
URL:            https://github.com/bus1/dbus-broker
#!RemoteAsset
Source:         https://github.com/bus1/dbus-broker/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:         test-sockopt-loosen-verification-of-stale-pidfds.patch
BuildSystem:    meson

BuildOption(conf):  -Daudit=true
BuildOption(conf):  -Dselinux=true
%if %{with launcher}
BuildOption(conf):  -Dlauncher=true
%else
BuildOption(conf):  -Dlauncher=false
%endif
BuildOption(conf):  -Dtests=false

BuildRequires:  linux-headers
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libselinux)
%if %{with launcher}
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
%endif

%description
dbus-broker is an implementation of a message bus as defined by the D-Bus
specification. It offers improved performance and reliability compared
to the reference implementation.

%files
%license LICENSE
%{_bindir}/dbus-broker
%if %{with launcher}
%{_bindir}/dbus-broker-launch
%{_journalcatalogdir}/*
%{_unitdir}/dbus-broker.service
%{_userunitdir}/dbus-broker.service
%endif

%changelog
%autochangelog
