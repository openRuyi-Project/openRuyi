# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kunitconversion

# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kunitconversion
Version:        6.27.0
Release:        %autorelease
Summary:        Tool for converting physical units
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kunitconversion.git
#!RemoteAsset:  sha256:404e064114c95eca0ef759b96ca4e0ba5f9b8bc563138574358270963f3f5554
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DBUILD_PYTHON_BINDINGS=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-build
BuildRequires:  python-setuptools
BuildRequires:  python-wheel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

%description
KUnitConversion provides functions to convert values in different physical
units. It supports converting different prefixes (e.g. kilo, mega, giga) as
well as converting between different unit systems (e.g. liters, gallons).

%package        devel
Summary:        Converting physical units: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description    devel
KUnitConversion provides functions to convert values in different physical
units. It supports converting different prefixes (e.g. kilo, mega, giga) as
well as converting between different unit systems (e.g. liters, gallons).
Development files.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_debugdir}/kunitconversion.categories
%{_kf6_libdir}/libKF6UnitConversion.so.*

%files devel
%{_kf6_includedir}/KUnitConversion/
%{_kf6_cmakedir}/KF6UnitConversion/
%{_kf6_libdir}/libKF6UnitConversion.so

%changelog
%autochangelog
