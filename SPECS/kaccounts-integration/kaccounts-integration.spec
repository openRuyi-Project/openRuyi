# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.19.0
%define qt6_version 6.9.0

Name:           kaccounts-integration
Version:        25.12.3
Release:        %autorelease
Summary:        KDE Accounts Providers
License:        GPL-2.0-or-later
VCS:            git:https://invent.kde.org/network/kaccounts-integration.git
#!RemoteAsset:  sha256:71c20ae5ca1459f732cc3c92248885b2d1d84e251f2d1b0f462b00adda8fc3b6
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(AccountsQt6)
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(SignOnQt6)

Requires:       signon-kwallet-extension
Recommends:     kaccounts-providers

%description
Small system to administer web accounts for the sites and services across the
Plasma desktop, including: Google, Facebook, Owncloud, IMAP, Jabber and others.

%package        devel
Summary:        KDE Accounts Providers - Development Files
# Used in KAccountsMacros.cmake
Requires:       intltool
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(AccountsQt6)
Requires:       cmake(KF6CoreAddons) >= %{kf6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Requires:       cmake(SignOnQt6)
Requires:       pkgconfig(libaccounts-glib)

%description    devel
Small system to administer web accounts for the sites and services across the
Plasma desktop, including: Google, Facebook, Owncloud, IMAP, Jabber and others.
This package provides development files.

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
rm -rf $RPM_BUILD_ROOT%{_mandir}/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --with-man --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_kaccounts.desktop
%{_kf6_debugdir}/kaccounts.categories
%{_kf6_libdir}/libkaccounts6.so.*
%dir %{_kf6_plugindir}/kaccounts
%dir %{_kf6_plugindir}/kaccounts/daemonplugins
%{_kf6_plugindir}/kaccounts/daemonplugins/kaccounts_kio_webdav_plugin.so
%{_kf6_plugindir}/kf6/kded/kded_accounts.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_kaccounts.so
%{_kf6_qmldir}/org/kde/kaccounts/

%files devel
%{_includedir}/KAccounts6/
%{_kf6_cmakedir}/KAccounts6/
%{_kf6_libdir}/libkaccounts6.so

%changelog
%autochangelog
