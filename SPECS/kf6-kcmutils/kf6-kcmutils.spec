# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kcmutils
# Internal QML import
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.kcmutils\\.private.*\\)

# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kcmutils
Version:        6.22.0
Release:        %autorelease
Summary:        Classes to work with KCModules
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kcmutils
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
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

%package        imports
Summary:        QtQuick bindings for classes to work with KCModules
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    imports
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework. This package provides QtQuick bindings
for the KCMUtils libraries.

%package        devel
Summary:        Build environment for kcmutils, a set of classes to work with KCModules
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6ConfigWidgets) >= %{_kf6_version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_version}
Requires:       cmake(Qt6Qml) >= %{qt6_version}

%description    devel
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework. Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name}6 --with-qt --all-name --generate-subpackages

%files -f %{name}6.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/kcmshell6
%{_kf6_debugdir}/kcmutils.categories
%{_kf6_libexecdir}/kcmdesktopfilegenerator
%{_kf6_libdir}/libKF6KCMUtils.so.*
%{_kf6_libdir}/libKF6KCMUtilsCore.so.*
%{_kf6_libdir}/libKF6KCMUtilsQuick.so.*

%files imports
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
