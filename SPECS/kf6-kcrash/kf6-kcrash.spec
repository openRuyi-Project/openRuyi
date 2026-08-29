# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kcrash
# Full KF6 version (e.g. 6.21.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kcrash
Version:        6.28.0
Release:        %autorelease
Summary:        An application crash handler
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kcrash
#!RemoteAsset:  sha256:ddcc14c0c40e24f4c0dc04246b87d11b650e6fd8be2cb00e4f2cc2ee9e605702
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6OpenGL) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
KCrash provides support for intercepting and handling application crashes.

%package        devel
Summary:        Build environment for the KCrash application crash handler
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description    devel
KCrash provides support for intercepting and handling application crashes.
Development files.

%files
%license LICENSES/*
%doc README*
%{_kf6_debugdir}/kcrash.categories
%{_kf6_debugdir}/kcrash.renamecategories
%{_kf6_libdir}/libKF6Crash.so.*

%files devel
%{_kf6_cmakedir}/KF6Crash/
%{_kf6_includedir}/KCrash/
%{_kf6_libdir}/libKF6Crash.so

%changelog
%autochangelog
