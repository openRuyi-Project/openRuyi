# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.30.0
%define qt6_version 6.9.0

Name:           union
Version:        6.8.2
Release:        %autorelease
Summary:        Qt style supporting both QtQuick and QtWidgets
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/union.git
#!RemoteAsset:  sha256:1210768dd830ddd06944ba179a02526793d8aa0cd27074e2adad4ecf97b51ef4
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
# The CSS input plugin needs cxx-rust-cssparser, which is not packaged yet.
BuildOption(conf):  -DBUILD_INPUT_CSS=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

Requires:       kf6-kirigami >= %{kf6_version}
Requires:       qt6-qtdeclarative >= %{qt6_version}

%description
Union is a style engine for Qt that supports both Qt Quick and Qt Widgets,
with a Kirigami platform integration and a Plasma platform plugin.

%package        devel
Summary:        Development Files for Union
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf6-extra-cmake-modules >= %{kf6_version}

%description    devel
This package contains the headers and CMake files needed to develop
applications that use Union.

%files
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/union-ruleinspector
%{_kf6_bindir}/union-styletool
%{_kf6_debugdir}/union.categories
%{_kf6_libdir}/libUnion.so.*
%{_kf6_libdir}/libUnionQuickImpl.so.*
%{_kf6_libdir}/libUnionQuickStyle.so.*
%{_kf6_qmldir}/org/kde/union/
%{_kf6_qmldir}/org/kde/kirigami/styles/org.kde.union/
%{_kf6_plugindir}/union/
%dir %{_kf6_plugindir}/styles
%{_kf6_plugindir}/styles/UnionWidgetsStyle.so
%dir %{_kf6_plugindir}/kf6/kirigami/
%dir %{_kf6_plugindir}/kf6/kirigami/platform
%{_kf6_plugindir}/kf6/kirigami/platform/org.kde.union.so
%dir %{_kf6_sharedir}/kstyle/
%dir %{_kf6_sharedir}/kstyle/themes/
%{_kf6_sharedir}/kstyle/themes/union.themerc

%files devel
%{_includedir}/union/
%{_kf6_cmakedir}/Union/
%{_kf6_libdir}/libUnion.so

%changelog
%autochangelog
