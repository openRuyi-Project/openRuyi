# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

Name:           plasma-disks
Version:        6.7.1
Release:        %autorelease
Summary:        Plasma service for monitoring disk health
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/plasma-disks.git
#!RemoteAsset:  sha256:2bbfa3dc968d90acb7facd9790df58edd17f59046691d116b7d54dd97e151daf
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}

Requires:       smartmontools

%description
Monitors S.M.A.R.T. capable devices for imminent failure and informs the user.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%{_datadir}/dbus-1/system-services/org.kde.kded.smart.service
%{_datadir}/polkit-1/actions/org.kde.kded.smart.policy
%{_kf6_appstreamdir}/org.kde.plasma.disks.metainfo.xml
%{_kf6_applicationsdir}/kcm_disks.desktop
%{_kf6_dbuspolicydir}/org.kde.kded.smart.conf
%{_kf6_notificationsdir}/org.kde.kded.smart.notifyrc
%{_kf6_plugindir}/kf6/kded/smart.so
%dir %{_kf6_plugindir}/plasma/kcms/kinfocenter/
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_disks.so
%{_kf6_libexecdir}/kauth/kded-smart-helper

%changelog
%autochangelog
