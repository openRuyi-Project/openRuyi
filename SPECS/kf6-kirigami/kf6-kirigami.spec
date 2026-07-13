# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kirigami
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kirigami
Version:        6.27.0
Release:        %autorelease
Summary:        Set of QtQuick components
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kirigami
#!RemoteAsset:  sha256:d7daa74e9fe81b674e54e6e979feb85d3d2f4216bf6d9c02bfaa2c021fe1ac2d
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DQT_QML_NO_CACHEGEN:BOOL=TRUE

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
Requires:       qt6-qtdeclarative >= %{qt6_version}
Requires:       qt6-qt5compat >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
QtQuick plugins to build user interfaces based on the KDE UX guidelines.

%package        devel
Summary:        Development package for kirigami
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Concurrent) >= %{qt6_version}
Requires:       cmake(Qt6Qml) >= %{qt6_version}
Requires:       cmake(Qt6Quick) >= %{qt6_version}

%description    devel
QtQuick plugins to build user interfaces based on the KDE UX guidelines.
Development files.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kirigami.categories
%{_kf6_qmldir}/org/kde/kirigami/
# This is actually a plugin
%{_kf6_libdir}/libKirigamiPrivate.so.*
%{_kf6_libdir}/libKirigami.so.*
%{_kf6_libdir}/libKirigamiControls.so.*
%{_kf6_libdir}/libKirigamiDelegates.so.*
%{_kf6_libdir}/libKirigamiDialogs.so.*
%{_kf6_libdir}/libKirigamiForms.so.*
%{_kf6_libdir}/libKirigamiFormsPrivateCards.so.*
%{_kf6_libdir}/libKirigamiFormsPrivateFlat.so.*
%{_kf6_libdir}/libKirigamiFormsPrivateTemplates.so.*
%{_kf6_libdir}/libKirigamiLayouts.so.*
%{_kf6_libdir}/libKirigamiLayoutsPrivate.so.*
%{_kf6_libdir}/libKirigamiPlatform.so.*
%{_kf6_libdir}/qt6/metatypes/qt6kirigamiplatform_metatypes.json
%{_kf6_libdir}/libKirigamiPrimitives.so.*
%{_kf6_libdir}/libKirigamiPolyfill.so.*
%{_kf6_libdir}/libKirigamiTemplates.so.*

%files devel
%{_kf6_cmakedir}/KF6Kirigami/
%{_kf6_cmakedir}/KF6Kirigami2/
%{_kf6_cmakedir}/KF6KirigamiPlatform/
%dir %{_kf6_includedir}/Kirigami/
%{_kf6_includedir}/Kirigami/Platform/
%{_kf6_libdir}/libKirigami.so
%{_kf6_libdir}/libKirigamiControls.so
%{_kf6_libdir}/libKirigamiDelegates.so
%{_kf6_libdir}/libKirigamiDialogs.so
%{_kf6_libdir}/libKirigamiForms.so
%{_kf6_libdir}/libKirigamiFormsPrivateCards.so
%{_kf6_libdir}/libKirigamiFormsPrivateFlat.so
%{_kf6_libdir}/libKirigamiFormsPrivateTemplates.so
%{_kf6_libdir}/libKirigamiLayouts.so
%{_kf6_libdir}/libKirigamiLayoutsPrivate.so
%{_kf6_libdir}/libKirigamiPlatform.so
%{_kf6_libdir}/libKirigamiPrimitives.so
%{_kf6_libdir}/libKirigamiPrivate.so
%{_kf6_libdir}/libKirigamiPolyfill.so
%{_kf6_libdir}/libKirigamiTemplates.so
%{_kf6_sharedir}/kdevappwizard/templates/kirigami6.tar.bz2

%changelog
%autochangelog
