# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global __requires_exclude qt6qmlimport\\(org\\.kde\\.private\\.kscreen.*

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           kscreen
Version:        6.7.1
Release:        %autorelease
Summary:        Screen management software by KDE
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/kscreen.git
#!RemoteAsset:  sha256:cf44c17e48afa069f4d654c51d1c0bfc7d91c2763a8482c55e4a757181a34b02
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  kf6-kitemmodels
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  qt6-qtwayland-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ImageFormats) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6Screen) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(LayerShellQt) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma5Support) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sensors) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  pkgconfig(wayland-protocols) >= 1.41
BuildRequires:  pkgconfig(wayland-client) >= 1.9
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xi)

Requires:       kf6-kded
Requires:       libkscreen-plugin >= %{_plasma6_bugfix}
Requires:       kf6-kimageformats
Requires:       xrdb

%description
KScreen handles screen management for both X11 and Wayland sessions, including rotation, size, refresh rate, and scaling.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%post
%systemd_user_post plasma-kscreen-osd.service

%preun
%systemd_user_preun plasma-kscreen-osd.service

%postun
%systemd_user_postun plasma-kscreen-osd.service

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_kscreen.desktop
%{_kf6_bindir}/hdrcalibrator
%{_kf6_bindir}/kscreen-console
%{_kf6_debugdir}/kscreen.categories
%{_kf6_plugindir}/kf6/kded/kscreen.so
%{_kf6_plugindir}/plasma/applets/org.kde.kscreen.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_kscreen.so
%{_kf6_sharedir}/dbus-1/services/org.kde.kscreen.osdService.service
%{_kf6_sharedir}/kglobalaccel/org.kde.kscreen.desktop
%{_libexecdir}/kscreen_osd_service
%{_userunitdir}/plasma-kscreen-osd.service

%changelog
%autochangelog
