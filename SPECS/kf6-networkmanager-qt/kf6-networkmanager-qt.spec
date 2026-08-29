# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname networkmanager-qt
# Full KF6 version (e.g. 6.28.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-networkmanager-qt
Version:        6.28.0
Release:        %autorelease
Summary:        A Qt wrapper for NetworkManager DBus API
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/networkmanager-qt.git
#!RemoteAsset:  sha256:30604204bb00115f515146d05f981aa1f9824e14c0c537a1ec397581ac5d912e
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libnm) >= 1.4.0

%description
NetworkManagerQt provides access to all NetworkManager features
exposed on DBus. It allows you to manage your connections and control
your network devices and also provides a library for parsing connection
settings which are used in DBus communication.

%package        devel
Summary:        A Qt wrapper for NetworkManager DBus API
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       pkgconfig(gio-2.0)
Requires:       pkgconfig(libnm) >= 1.4.0

%description    devel
NetworkManagerQt provides access to all NetworkManager features
exposed on DBus. It allows you to manage your connections and control
your network devices and also provides a library for parsing connection
settings which are used in DBus communication. Development files.

%files
%doc README.md
%license LICENSES/*
%{_kf6_debugdir}/networkmanagerqt.categories
%{_kf6_debugdir}/networkmanagerqt.renamecategories
%{_kf6_qmldir}/org/kde/networkmanager/
%{_kf6_libdir}/libKF6NetworkManagerQt.so.*

%files devel
%{_kf6_cmakedir}/KF6NetworkManagerQt/
%{_kf6_includedir}/NetworkManagerQt/
%{_kf6_libdir}/libKF6NetworkManagerQt.so

%changelog
%autochangelog
