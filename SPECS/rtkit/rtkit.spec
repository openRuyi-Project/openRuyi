# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rtkit
Version:        0.14
Release:        %autorelease
Summary:        Realtime Policy and Watchdog Daemon
License:        GPL-3.0-or-later AND MIT
URL:            https://gitlab.freedesktop.org/pipewire/rtkit
VCS:            git:https://gitlab.freedesktop.org/pipewire/rtkit.git
#!RemoteAsset:  sha256:55dd379b11f52b81655e2dc676de9d602d050cb0beb18ef01f0f65569f0a5e59
Source0:        https://gitlab.freedesktop.org/pipewire/rtkit/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        rtkit.sysusers
BuildSystem:    meson

BuildOption(conf):  -Dsystemd_systemunitdir=%{_unitdir}
BuildOption(conf):  -Dinstalled_tests=false
BuildOption(conf):  -Dlibsystemd=enabled

BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  xxd

Requires:       dbus
Requires:       polkit

%description
RealtimeKit is a D-Bus system service that changes the
scheduling policy of user processes/threads to SCHED_RR (i.e. realtime
scheduling mode) on request.

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
