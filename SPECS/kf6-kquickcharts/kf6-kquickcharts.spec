# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kquickcharts
# Full KF6 version (e.g. 6.28.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kquickcharts
Version:        6.28.0
Release:        %autorelease
Summary:        Set of charts for QtQuick applications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kquickcharts.git
#!RemoteAsset:  sha256:c5d361d90861b4cd3db861568da5279ae2b1cb953e874126c15abbd7138378e5
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

Requires:       kf6-kirigami >= %{_kf6_version}
Requires:       qt6-qtdeclarative >= %{qt6_version}

%description
The Quick Charts module provides a set of charts that can be used from QtQuick
applications. They are intended to be used for both simple display of data as
well as continuous display of high-volume data (often referred to as plotters).
The charts use a system called distance fields for their accelerated rendering,
which provides ways of using the GPU for rendering 2D shapes without loss of
quality.

%package        devel
Summary:        Header files for kquickcharts, a set of charts for QtQuick applications
Requires:       kf6-kquickcharts >= %{version}

%description    devel
Development files for KQuickCharts, a set of charts that can be used from QtQuick
applications.

%files
%doc README.md
%license LICENSES/*
%{_kf6_debugdir}/kquickcharts.categories
%{_kf6_libdir}/libQuickCharts.so.*
%{_kf6_libdir}/libQuickChartsControls.so.*
%{_kf6_qmldir}/org/kde/quickcharts/

%files devel
%{_kf6_cmakedir}/KF6QuickCharts/
%{_kf6_libdir}/libQuickCharts.so
%{_kf6_libdir}/libQuickChartsControls.so

%changelog
%autochangelog
