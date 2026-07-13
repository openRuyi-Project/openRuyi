# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kholidays
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kholidays
Version:        6.27.0
Release:        %autorelease
Summary:        Holiday calculation library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kholidays.git
#!RemoteAsset:  sha256:84ce2acd5565a9510d74945ea2311f8c099cb031393255d1c8d399665d57b914
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
This package contains a library which helps developers determining when holidays occur.

%package        devel
Summary:        Development files for the KDE PIM Holiday API
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)

%description    devel
This package contains necessary include files and libraries needed
to develop applications depending on the kholidays library

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%{_kf6_debugdir}/kholidays.categories

%files devel
%doc DESIGN README.md
%license LICENSES/*
%{_kf6_qmldir}/org/kde/kholidays/
%{_kf6_libdir}/libKF6Holidays.so.*
%{_kf6_cmakedir}/KF6Holidays/
%{_kf6_includedir}/KHolidays/
%{_kf6_libdir}/libKF6Holidays.so

%changelog
%autochangelog
