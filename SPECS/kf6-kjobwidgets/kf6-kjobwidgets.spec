# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kjobwidgets

# Full KF6 version (e.g. 6.28.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kjobwidgets
Version:        6.28.0
Release:        %autorelease
Summary:        Widgets for showing progress of asynchronous jobs
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kjobwidgets
#!RemoteAsset:  sha256:a13fcc9c861a90a540e5f93028fa7fae48f4c8643dadd287f3d54f5f24fab3da
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DBUILD_PYTHON_BINDINGS=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
KJobWIdgets provides widgets for showing progress of asynchronous jobs.

%package        devel
Summary:        Widgets for showing progress of asynchronous jobs
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description    devel
KJobWIdgets provides widgets for showing progress of asynchronous jobs.
Development files.

%files
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kjobwidgets.categories
%{_kf6_debugdir}/kjobwidgets.renamecategories
%{_kf6_libdir}/libKF6JobWidgets.so.*
%{_datadir}/locale/*/LC_MESSAGES/kjobwidgets6_qt.qm

%files devel
%{_kf6_cmakedir}/KF6JobWidgets/
%{_kf6_dbusinterfacesdir}/kf6_org.kde.JobView.xml
%{_kf6_dbusinterfacesdir}/kf6_org.kde.JobViewServer.xml
%{_kf6_dbusinterfacesdir}/kf6_org.kde.JobViewV2.xml
%{_kf6_includedir}/KJobWidgets/
%{_kf6_libdir}/libKF6JobWidgets.so

%changelog
%autochangelog
