# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Internal QML import
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.xdgdesktopportal.*

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           xdg-desktop-portal-kde
Version:        6.7.1
Release:        %autorelease
Summary:        QT/KF6 backend for xdg-desktop-portal
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/xdg-desktop-portal-kde.git
#!RemoteAsset:  sha256:7f17ba54fccb62347944bef776f5fab5134a8f2421f2dd5ec36b8f29be62c7e4
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  qt6-qtbase-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.7.0
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(wayland-client) >= 1.15
BuildRequires:  pkgconfig(wayland-protocols) >= 1.25
BuildRequires:  pkgconfig(xkbcommon)

Requires:       kf6-kiconthemes >= %{kf6_version}
Requires:       kpipewire >= %{_plasma6_bugfix}
Requires:       plasma-workspace >= %{_plasma6_bugfix}
Requires:       xdg-desktop-portal

%description
A Qt/KF backend implementation for xdg-desktop-portal

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --with-man --all-name --generate-subpackages

%post
%systemd_user_post plasma-xdg-desktop-portal-kde.service

%preun
%systemd_user_preun plasma-xdg-desktop-portal-kde.service

%postun
%systemd_user_postun plasma-xdg-desktop-portal-kde.service

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_applicationsdir}/org.freedesktop.impl.portal.desktop.kde.desktop
%{_kf6_debugdir}/xdp-kde.categories
%{_kf6_notificationsdir}/xdg-desktop-portal-kde.notifyrc
%{_kf6_sharedir}/dbus-1/services/org.freedesktop.impl.portal.desktop.kde.service
%dir %{_kf6_sharedir}/xdg-desktop-portal/
%dir %{_kf6_sharedir}/xdg-desktop-portal/portals
%{_kf6_sharedir}/xdg-desktop-portal/portals/kde.portal
%{_libexecdir}/xdg-desktop-portal-kde
%{_userunitdir}/plasma-xdg-desktop-portal-kde.service

%changelog
%autochangelog
