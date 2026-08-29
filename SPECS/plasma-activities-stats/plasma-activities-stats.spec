# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0
# Full Plasma 6 version
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           plasma-activities-stats
Version:        6.7.4
Release:        %autorelease
Summary:        KDE Plasma Activities support
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/plasma-activities-stats
#!RemoteAsset:  sha256:e2ee0892769fe5f30a0f8ccaaebdc043be7b1bd89258d0e540a7a45044df3a1a
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DBUILD_QCH:BOOL=ON

BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
Kactivities provides an API for using and interacting with the Plasma Activities Manager.

%package        devel
Summary:        KDE Plasma Activities support
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description    devel
Kactivities provides an API for using and interacting with the Plasma Activities Manager.
Development files.

%files
%license LICENSES/*
%{_kf6_debugdir}/plasma-activities-stats.categories
%{_kf6_debugdir}/plasma-activities-stats.renamecategories
%{_kf6_libdir}/libPlasmaActivitiesStats.so.*

%files devel
%doc %{_kf6_qchdir}/PlasmaActivitiesStats.*
%{_includedir}/PlasmaActivitiesStats/
%{_kf6_cmakedir}/PlasmaActivitiesStats/
%{_kf6_libdir}/libPlasmaActivitiesStats.so
%{_kf6_pkgconfigdir}/PlasmaActivitiesStats.pc

%changelog
%autochangelog
