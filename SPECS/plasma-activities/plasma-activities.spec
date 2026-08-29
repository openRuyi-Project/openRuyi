# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0
%define sover 7

Name:           plasma-activities
Version:        6.7.4
Release:        %autorelease
Summary:        Plasma Activities support
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/plasma-activities
#!RemoteAsset:  sha256:aec18ca3387bc7abc1df177e7a048dd6a07e814bb7199e62683d5f37227966ca
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DBUILD_QCH:BOOL=ON

BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
Kactivities provides an API for using and interacting with the Plasma Activities Manager.

%package        devel
Summary:        Plasma Activities support
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description    devel
Kactivities provides an API for using and interacting with the Plasma Activities Manager.
Development files.

%files
%license LICENSES/*
%{_kf6_debugdir}/plasma-activities.categories
%{_kf6_debugdir}/plasma-activities.renamecategories
%{_kf6_bindir}/plasma-activities-cli6
%{_kf6_libdir}/libPlasmaActivities.so.*
%{_kf6_qmldir}/org/kde/activities/

%files devel
%{_kf6_cmakedir}/PlasmaActivities/
%{_includedir}/PlasmaActivities/
%{_kf6_libdir}/libPlasmaActivities.so
%{_kf6_pkgconfigdir}/PlasmaActivities.pc

%changelog
%autochangelog
