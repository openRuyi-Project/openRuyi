# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rtkit
Version:        0.11
Release:        %autorelease
Summary:        Realtime Policy and Watchdog Daemon
License:        GPL-3.0-or-later AND MIT
URL:            http://git.0pointer.net/rtkit.git/
VCS:            git:http://git.0pointer.net/clone/rtkit.git
#!RemoteAsset
Source0:        http://0pointer.de/public/rtkit-%{version}.tar.xz
Source1:        rtkit.sysusers
BuildSystem:    autotools

BuildOption(conf):  --with-systemdsystemunitdir=%{_unitdir}
# Avoid false positive -Werror=format-security.
BuildOption(conf):  CFLAGS='%{build_cflags} -Wno-error=format-security'

BuildRequires:  make
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

Requires:       dbus
Requires:       polkit

%description
RealtimeKit is a D-Bus system service that changes the
scheduling policy of user processes/threads to SCHED_RR (i.e. realtime
scheduling mode) on request.

%conf -p
autoreconf -fiv

%build -a
./rtkit-daemon --introspect > org.freedesktop.RealtimeKit1.xml

%install -a
install -Dm0644 org.freedesktop.RealtimeKit1.xml %{buildroot}%{_datadir}/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/rtkit.conf

mkdir -p %{buildroot}%{_datadir}/dbus-1/system.d
mv %{buildroot}%{_sysconfdir}/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf %{buildroot}%{_datadir}/dbus-1/system.d/

%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
%systemd_post rtkit-daemon.service

%preun
%systemd_preun rtkit-daemon.service

%postun
%systemd_postun_with_restart rtkit-daemon.service

%files
%doc README GPL LICENSE rtkit.c rtkit.h
%{_sbindir}/rtkitctl
%{_libexecdir}/rtkit-daemon
%{_datadir}/dbus-1/system-services/org.freedesktop.RealtimeKit1.service
%{_datadir}/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml
%{_datadir}/polkit-1/actions/org.freedesktop.RealtimeKit1.policy
%{_unitdir}/rtkit-daemon.service
%{_mandir}/man8/*
%{_sysusersdir}/rtkit.conf

%changelog
%autochangelog
