# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           iwd
Version:        3.10
Release:        %autorelease
Summary:        Wireless daemon for Linux
License:        LGPL-2.1-or-later
URL:            https://archive.kernel.org/oldwiki/iwd.wiki.kernel.org/
VCS:            git:https://git.kernel.org/pub/scm/network/wireless/iwd.git
#!RemoteAsset
Source:         https://www.kernel.org/pub/linux/network/wireless/iwd-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --enable-external-ell
BuildOption(conf):  --enable-sim-hardcoded
BuildOption(conf):  --enable-ofono
BuildOption(conf):  --enable-wired
BuildOption(conf):  --enable-hwsim
BuildOption(conf):  --enable-tools
BuildOption(conf):  --with-systemd-unitdir=%{_unitdir}
BuildOption(conf):  --with-systemd-networkdir=%{_systemd_util_dir}/network
BuildOption(conf):  --with-systemd-modloaddir=%{_modulesloaddir}
BuildOption(conf):  --disable-manual

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ell)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(readline)

Requires:       dbus
Requires:       systemd

%description
The iwd package contains a daemon and utilities for controlling and configuring
Wi-Fi network hardware.

%install -a
mkdir -p %{buildroot}%{_sharedstatedir}/iwd
mkdir -p %{buildroot}%{_sharedstatedir}/ead
rm -f %{buildroot}%{_systemd_util_dir}/network/80-iwd.link

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/iwctl
%{_bindir}/iwmon
%{_bindir}/hwsim
%{_libexecdir}/iwd
%{_libexecdir}/ead
%{_modulesloaddir}/pkcs8.conf
%{_unitdir}/ead.service
%{_unitdir}/iwd.service
%{_datadir}/dbus-1/system-services/net.connman.iwd.service
%{_datadir}/dbus-1/system-services/net.connman.ead.service
%{_datadir}/dbus-1/system.d/iwd-dbus.conf
%{_datadir}/dbus-1/system.d/ead-dbus.conf
%{_datadir}/dbus-1/system.d/hwsim-dbus.conf
%{_mandir}/man*/*
%dir %{_sharedstatedir}/iwd
%dir %{_sharedstatedir}/ead

%changelog
%autochangelog
