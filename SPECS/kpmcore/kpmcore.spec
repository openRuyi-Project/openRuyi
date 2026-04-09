# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.19.0
%define qt6_version 6.9.0

Name:           kpmcore
Version:        25.12.2
Release:        %autorelease
Summary:        KDE Partition Manager core library
License:        GPL-3.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/system/kpmcore
#!RemoteAsset
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(blkid) >= 2.33.2

%description
Library for managing partitions. Common code for KDE Partition Manager and
other projects.

%package        devel
Summary:        Development package for KDE Partition Manager core library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Library for managing partitions. Common code for KDE Partition Manager and
other projects.

Development package for kpmcore.

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%files
%license LICENSES/*
%{_kf6_dbuspolicydir}/org.kde.kpmcore.*.conf
%{_kf6_plugindir}/kpmcore/
%{_kf6_sharedir}/dbus-1/system-services/org.kde.kpmcore.helperinterface.service
%{_kf6_sharedir}/polkit-1/actions/org.kde.kpmcore.externalcommand.policy
%{_libexecdir}/kpmcore_externalcommand
%{_kf6_libdir}/libkpmcore.so.*
%{_datadir}/locale/*/LC_MESSAGES/kpmcore.mo
%{_datadir}/locale/*/LC_MESSAGES/kpmcore._policy_.mo
%{_datadir}/locale/*/LC_MESSAGES/kpmcore.mo

%files devel
%{_includedir}/kpmcore/
%{_kf6_cmakedir}/KPMcore/
%{_kf6_libdir}/libkpmcore.so

%changelog
%autochangelog
