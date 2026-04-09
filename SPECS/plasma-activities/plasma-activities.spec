# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0
%define sover 7

Name:           plasma-activities
Version:        6.5.5
Release:        %autorelease
Summary:        Plasma Activities support
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/plasma-activities
#!RemoteAsset
Source:         https://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  doxygen
BuildRequires:  fdupes
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

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake -DBUILD_QCH:BOOL=ON

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%files
%license LICENSES/*
%{_kf6_debugdir}/plasma-activities.categories
%{_kf6_debugdir}/plasma-activities.renamecategories
%{_kf6_bindir}/plasma-activities-cli6
%{_kf6_libdir}/libPlasmaActivities.so.*
%{_kf6_qmldir}/org/kde/activities/

%files devel
%doc %{_kf6_qchdir}/PlasmaActivities.*
%{_kf6_cmakedir}/PlasmaActivities/
%{_includedir}/PlasmaActivities/
%{_kf6_libdir}/libPlasmaActivities.so
%{_kf6_pkgconfigdir}/PlasmaActivities.pc

%changelog
%autochangelog
