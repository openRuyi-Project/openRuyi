# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

Name:           qqc2-breeze-style
Version:        6.7.4
Release:        %autorelease
Summary:        Breeze Style for Qt Quick
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/qqc2-breeze-style.git
#!RemoteAsset:  sha256:23d31e8c5aa1ec49a405149500be7e1966de2e5ca73f4a9771517186afbeb433
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6QuickCharts) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickTemplates2) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)

Requires:       kf6-kirigami >= %{kf6_version}
Requires:       qt6-qtdeclarative >= %{qt6_version}

%description
A Qt Quick Controls 2 style engine that uses the desktop style to draw controls
with QStyle.

%package        devel
Summary:        Development Files for the Breeze Qt Quick Controls 2 Style
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf6-extra-cmake-modules >= %{kf6_version}

%description    devel
This file contains cmake files to be used by projects that depend on
qqc2-breeze-style.
Usually not needed as it is only a runtime dependency.

%files
%license LICENSES/*
%dir %{_kf6_plugindir}/kf6/kirigami/
%dir %{_kf6_plugindir}/kf6/kirigami/platform
%{_kf6_qmldir}/org/kde/breeze/
%{_kf6_plugindir}/kf6/kirigami/platform/org.kde.breeze.so

%files devel
%{_kf6_cmakedir}/QQC2BreezeStyle/

%changelog
%autochangelog
