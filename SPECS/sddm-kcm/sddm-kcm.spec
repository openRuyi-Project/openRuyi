# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

Name:           sddm-kcm
Version:        6.7.1
Release:        %autorelease
Summary:        A sddm control module for KDE
License:        GPL-2.0-only
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/sddm-kcm.git
#!RemoteAsset:  sha256:3fa0fd2e661d88cc412b5a4568afb9eee4d07acadad6db44f00d5df4eff42327
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

Supplements:    (sddm and plasma-workspace)

%description
SDDM control module for Plasma. It provides a graphical frontend for the SDDM.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_bindir}/sddmthemeinstaller
%{_kf6_applicationsdir}/kcm_sddm.desktop
%{_kf6_dbuspolicydir}/org.kde.kcontrol.kcmsddm.conf
%{_kf6_knsrcfilesdir}/sddmtheme.knsrc
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_sddm.so
%{_kf6_sharedir}/dbus-1/system-services/org.kde.kcontrol.kcmsddm.service
%{_kf6_sharedir}/polkit-1/actions/org.kde.kcontrol.kcmsddm.policy
%{_kf6_libexecdir}/kauth/kcmsddm_authhelper

%changelog
%autochangelog
