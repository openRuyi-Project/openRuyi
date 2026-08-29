# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname modemmanager-qt
# Full KF6 version (e.g. 6.28.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-modemmanager-qt
Version:        6.28.0
Release:        %autorelease
Summary:        Qt wrapper for ModemManager DBus API
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/modemmanager-qtt.git
#!RemoteAsset:  sha256:742891c3c1dfcd6c9eaa2b1664cfe7e9b311187eec7ecd9d8812829dce8485c9
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(ModemManager) >= 1.0.0

%description
Qt wrapper for ModemManager DBus API.

%package        devel
Summary:        Development package for the libmm-qt library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(ModemManager) >= 1.0.0

%description    devel
Qt wrapper for ModemManager DBus API. Development files.

%files
%doc README.md
%license LICENSES/*
%{_kf6_debugdir}/modemmanagerqt.categories
%{_kf6_debugdir}/modemmanagerqt.renamecategories
%{_kf6_libdir}/libKF6ModemManagerQt.so.*

%files devel
%{_kf6_cmakedir}/KF6ModemManagerQt/
%{_kf6_includedir}/ModemManagerQt/
%{_kf6_libdir}/libKF6ModemManagerQt.so

%changelog
%autochangelog
