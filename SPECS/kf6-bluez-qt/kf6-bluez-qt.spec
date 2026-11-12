# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.9.0

%define rname bluez-qt
# Full KF6 version (e.g. 6.31.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-bluez-qt
Version:        6.31.0
Release:        %autorelease
Summary:        Async Bluez wrapper library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/bluez-qt
#!RemoteAsset:  sha256:22b25448c6b5372ee4fba15bb938e698a599cec0d69816ceb0405451c879c827
Source:         https://download.kde.org/stable/frameworks/6.31/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
Async Bluez wrapper library.

%package        devel
Summary:        Async Bluez wrapper library - development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6DBus) >= %{qt6_version}

%description    devel
Development files for QBluez Async Bluez wrapper library.

%files
%doc README.md
%license LICENSES/*
%{_kf6_debugdir}/bluezqt.categories
%{_kf6_debugdir}/bluezqt.renamecategories
%{_kf6_libdir}/libKF6BluezQt.so.*
%{_kf6_qmldir}/org/kde/bluezqt/

%files devel
%{_kf6_cmakedir}/KF6BluezQt/
%{_kf6_includedir}/BluezQt/
%{_kf6_libdir}/libKF6BluezQt.so
%{_kf6_pkgconfigdir}/KF6BluezQt.pc

%changelog
%autochangelog
