# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global __requires_exclude org.kde.kaccounts.(next|own)cloud

%define kf6_version 6.19.0
%define qt6_version 6.9.0

Name:           kaccounts-providers
Version:        26.04.2
Release:        %autorelease
Summary:        KDE Accounts Providers
License:        GPL-2.0-or-later
VCS:            git:https://invent.kde.org/network/kaccounts-providers.git
#!RemoteAsset:  sha256:0d3f278ffac88af2db4c7ba7d9cab4622a2e19dbb39fbd144f1daa1075caf8a0
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  intltool
BuildRequires:  cmake(KAccounts6)
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(QCoro6Network)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineQuick) >= %{qt6_version}

Requires:       signon-plugin-oauth2

%description
KDE Accounts Providers.

%install -a
# qtwebkit is long dead
rm -r %{buildroot}%{_kf6_sysconfdir}/signon-ui/

# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_iconsdir}/hicolor/256x256/apps/kaccounts-owncloud.png
%{_kf6_iconsdir}/hicolor/scalable/apps/kaccounts-nextcloud.svg
%{_kf6_plugindir}/kaccounts/
%dir %{_kf6_sharedir}/accounts
%dir %{_kf6_sharedir}/accounts/providers
%dir %{_kf6_sharedir}/accounts/providers/kde
%{_kf6_sharedir}/accounts/providers/kde/google.provider
%{_kf6_sharedir}/accounts/providers/kde/nextcloud.provider
%{_kf6_sharedir}/accounts/providers/kde/owncloud.provider
%dir %{_kf6_sharedir}/accounts/services
%dir %{_kf6_sharedir}/accounts/services/kde
%{_kf6_sharedir}/accounts/services/kde/nextcloud-contacts.service
%{_kf6_sharedir}/accounts/services/kde/nextcloud-storage.service
%{_kf6_sharedir}/accounts/services/kde/owncloud-storage.service
%dir %{_kf6_sharedir}/kpackage/
%{_kf6_sharedir}/kpackage/genericqml/

%changelog
%autochangelog
