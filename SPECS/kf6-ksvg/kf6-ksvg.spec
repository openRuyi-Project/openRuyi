# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname ksvg
# Full KF6 version (e.g. 6.28.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-ksvg
Version:        6.28.0
Release:        %autorelease
Summary:        Components for handling SVGs
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/ksvg
#!RemoteAsset:  sha256:d580e6038ab3fb8a8755c953abd27a55894c2ae05e72cdef9bca1cf4e265a325
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

Patch0:         0001-Revert-Support-for-fractional-scaling.patch

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6Archive) >= %{_kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

Requires:       kf6-kirigami >= %{_kf6_version}

%description
Components for handling SVGs

%package        devel
Summary:        Development Files for the ksvg framework
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development Files for the ksvg framework.

%files
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/ksvg.categories
%{_kf6_qmldir}/org/kde/ksvg/
%{_kf6_libdir}/libKF6Svg.so.*

%files devel
%{_kf6_cmakedir}/KF6Svg/
%{_kf6_includedir}/KSvg/
%{_kf6_libdir}/libKF6Svg.so

%changelog
%autochangelog
