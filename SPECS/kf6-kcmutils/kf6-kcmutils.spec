# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kcmutils
# Internal QML import
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.kcmutils\\.private.*\\)

# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kcmutils
Version:        6.27.0
Release:        %autorelease
Summary:        Classes to work with KCModules
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kcmutils
#!RemoteAsset:  sha256:beb0a50a22230fdd94164a5d6e53ea7f4cbc97b86cbab3ff2a592ea8663efa41
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  kf6-kirigami >= %{_kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{_kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{_kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

%package        devel
Summary:        Build environment for kcmutils, a set of classes to work with KCModules
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6ConfigWidgets) >= %{_kf6_version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_version}
Requires:       cmake(Qt6Qml) >= %{qt6_version}

%description    devel
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework. Development files.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_bindir}/kcmshell6
%{_kf6_debugdir}/kcmutils.categories
%{_kf6_libexecdir}/kcmdesktopfilegenerator
%{_kf6_libdir}/libKF6KCMUtils.so.*
%{_kf6_libdir}/libKF6KCMUtilsCore.so.*
%{_kf6_libdir}/libKF6KCMUtilsQuick.so.*
%{_kf6_qmldir}/org/kde/kcmutils/

%files devel
%{_kf6_cmakedir}/KF6KCMUtils/
%{_kf6_includedir}/KCMUtils/
%{_kf6_includedir}/KCMUtilsCore/
%{_kf6_includedir}/KCMUtilsQuick/
%{_kf6_libdir}/libKF6KCMUtils.so
%{_kf6_libdir}/libKF6KCMUtilsCore.so
%{_kf6_libdir}/libKF6KCMUtilsQuick.so

%changelog
%autochangelog
