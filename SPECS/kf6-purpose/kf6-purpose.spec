# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Internal QML imports
%global __requires_exclude qt6qmlimport\\((org\\.kde\\.purpose|org\\.kde\\.kdeconnect|SSO\\.OnlineAccounts).*

%define qt6_version 6.8.0

%define rname purpose
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-purpose
Version:        6.22.0
Release:        %autorelease
Summary:        Framework to integrate services and actions in applications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/purpose.git
#!RemoteAsset:  sha256:a2912583948f423e4d666f9cbf1cf1ac463a246e10e717078b4831f60cc2198c
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KAccounts6)
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{_kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{_kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{_kf6_version}
BuildRequires:  cmake(KF6Service) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

Requires:       accounts-qml-module
Requires:       kf6-kdeclarative >= %{_kf6_version}
Requires:       kf6-kirigami >= %{_kf6_version}
Requires:       kf6-prison >= %{_kf6_version}
Requires:       qt6-qtdeclarative >= %{qt6_version}
Requires:       purpose-services >= %{version}

%description
This framework offers the possibility to create integrate services and actions
on any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

%package        services
Summary:        Online services for purpose
Provides:       purpose-services = %{version}-%{release}
Obsoletes:      purpose-services < %{version}-%{release}

%description    services
This package adds online services to kf6-purpose and are needed to connect to
Google and Nextcloud servers.

%package        devel
Summary:        Framework to integrate services and actions - Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_version}

%description    devel
This package contains development files needed to build applications which rely on the purpose framework.

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_datadir}/purpose/
%{_kf6_debugdir}/purpose.categories
%{_kf6_debugdir}/purpose.renamecategories
%{_kf6_iconsdir}/hicolor/*/apps/phabricator-purpose6.png
%{_kf6_iconsdir}/hicolor/*/apps/reviewboard-purpose6.png
%{_kf6_libexecdir}/purposeprocess
%{_kf6_libdir}/libKF6Purpose.so.*
%{_kf6_libdir}/libKF6PurposeWidgets.so.*
%{_kf6_plugindir}/kf6/kfileitemaction/
%{_kf6_plugindir}/kf6/purpose/
%{_kf6_qmldir}/org/kde/purpose/

%files services
%dir %{_kf6_sharedir}/accounts
%dir %{_kf6_sharedir}/accounts/services
%dir %{_kf6_sharedir}/accounts/services/kde
%{_kf6_sharedir}/accounts/services/kde/google-youtube.service
%{_kf6_sharedir}/accounts/services/kde/nextcloud-upload.service

%files devel
%{_kf6_cmakedir}/KF6Purpose/
%{_kf6_includedir}/Purpose/
%{_kf6_includedir}/PurposeWidgets/
%{_kf6_libdir}/libKF6Purpose.so
%{_kf6_libdir}/libKF6PurposeWidgets.so

%changelog
%autochangelog
