# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           ksystemstats
Version:        6.7.1
Release:        %autorelease
Summary:        Plugin based system monitoring daemon
License:        BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/ksystemstats.git
#!RemoteAsset:  sha256:00dfd065ce556cc339886124c479b7067a1a2f5f82bfdc4fe71ddbb675d3356d
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  cmake >= 3.16
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  lm_sensors-devel
BuildRequires:  libdrm-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NetworkManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KSysGuard) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libudev)

%description
KSystemStats is a daemon that collects statistics about the running system.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%preun
%systemd_user_preun plasma-ksystemstats.service

%post
%systemd_user_post plasma-ksystemstats.service

%postun
%systemd_user_postun plasma-ksystemstats.service

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/ksystemstats
%{_kf6_bindir}/kstatsviewer
%{_kf6_debugdir}/ksystemstats.categories
%dir %{_kf6_plugindir}/ksystemstats/
%{_kf6_plugindir}/ksystemstats/ksystemstats_plugin_{cpu,disk,gpu,lmsensors,memory,network,osinfo,power,pressure}.so
%{_kf6_sharedir}/dbus-1/services/org.kde.ksystemstats1.service
%{_libexecdir}/ksystemstats_intel_helper
%{_userunitdir}/plasma-ksystemstats.service

%changelog
%autochangelog
