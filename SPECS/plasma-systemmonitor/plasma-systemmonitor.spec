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

Name:           plasma-systemmonitor
Version:        6.7.1
Release:        %autorelease
Summary:        An application for monitoring system resources
License:        GPL-3.0-only
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/plasma-systemmonitor.git
#!RemoteAsset:  sha256:62c4982d3ec3040933894c57734eecba44dfb08b6a8806d00a581bfaae0d2f8a
Source0:        https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KSysGuard) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

Requires:       kf6-kiconthemes >= %{kf6_version}
Requires:       kf6-kirigami >= %{kf6_version}
Requires:       kf6-kitemmodels >= %{kf6_version}
Requires:       kf6-knewstuff >= %{kf6_version}
Requires:       kf6-kquickcharts >= %{kf6_version}
Requires:       kf6-qqc2-desktop-style >= %{kf6_version}
Requires:       kirigami-addons
Requires:       ksystemstats >= %{_plasma6_bugfix}
Requires:       qt6-qtdeclarative >= %{qt6_version}

%description
plasma-systemmonitor provides an interface for monitoring system sensors,
process information and other system resources.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.plasma-systemmonitor.desktop
%{_kf6_appstreamdir}/org.kde.plasma-systemmonitor.metainfo.xml
%{_kf6_bindir}/plasma-systemmonitor
%{_kf6_knsrcfilesdir}/plasma-systemmonitor.knsrc
# FIXME result of 105cb99d & bb8d4048
%{_kf6_libdir}/libPlasmaSystemMonitorPage.so
%{_kf6_libdir}/libPlasmaSystemMonitorTable.so
%dir %{_kf6_qmldir}/org/kde/ksysguard/
%{_kf6_qmldir}/org/kde/ksysguard/page/
%{_kf6_qmldir}/org/kde/ksysguard/table/
%dir %{_kf6_sharedir}/ksysguard/
%{_kf6_sharedir}/ksysguard/sensorfaces/
%{_kf6_sharedir}/plasma-systemmonitor/
%dir %{_kf6_sharedir}/kconf_update/
 %{_kf6_sharedir}/kconf_update/plasma-systemmonitor-replace-vmpss.py
 %{_kf6_sharedir}/kconf_update/plasma-systemmonitor.upd
%dir %{_kf6_sharedir}/plasma/kinfocenter/
%dir %{_kf6_sharedir}/plasma/kinfocenter/externalmodules/
%{_kf6_sharedir}/plasma/kinfocenter/externalmodules/kcm_external_plasma-systemmonitor.desktop
%dir %{_kf6_sharedir}/kglobalaccel/
%{_kf6_sharedir}/kglobalaccel/org.kde.plasma-systemmonitor.desktop

%changelog
%autochangelog
