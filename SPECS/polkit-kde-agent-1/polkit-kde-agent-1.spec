# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

Name:           polkit-kde-agent-1
Version:        6.7.1
Release:        %autorelease
Summary:        PolicyKit authentication agent for Plasma
License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            https://www.kde.org/
VCS:            git:https://invent.kde.org/plasma/polkit-kde-agent-1.git
#!RemoteAsset:  sha256:a2db3a07634d664105ab701718aa492a0bb0ea98c3a9731f66c3eb9afa3920ce
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(PolkitQt6-1) >= 0.103.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
Provides Policy Kit Authentication Agent that nicely fits Plasma.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%post
%systemd_user_post plasma-polkit-agent.service

%preun
%systemd_user_preun plasma-polkit-agent.service

%postun
%systemd_user_postun plasma-polkit-agent.service

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.polkit-kde-authentication-agent-1.desktop
%{_kf6_configdir}/autostart/polkit-kde-authentication-agent-1.desktop
%{_kf6_notificationsdir}/polkit-kde-authentication-agent-1.notifyrc
%{_libexecdir}/polkit-kde-authentication-agent-1
%{_userunitdir}/plasma-polkit-agent.service

%changelog
%autochangelog
