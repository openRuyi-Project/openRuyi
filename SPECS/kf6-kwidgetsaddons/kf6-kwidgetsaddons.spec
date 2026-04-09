# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kwidgetsaddons

# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kwidgetsaddons
Version:        6.22.0
Release:        %autorelease
Summary:        Large set of desktop widgets
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kwidgetsaddons
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

%description
This repository contains add-on widgets and classes for applications
that use the Qt Widgets module.

%package        devel
Summary:        Large set of desktop widgets: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description    devel
This repository contains add-on widgets and classes for applications
that use the Qt Widgets module.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
  -DBUILD_PYTHON_BINDINGS=OFF

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name}6 --with-qt --all-name --generate-subpackages

%files -f %{name}6.lang
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kwidgetsaddons.categories
%{_kf6_libdir}/libKF6WidgetsAddons.so.*
%{_datadir}/locale/en/LC_MESSAGES/kwidgetsaddons6_qt.qm

%files devel
%{_kf6_cmakedir}/KF6WidgetsAddons/
%{_kf6_includedir}/KWidgetsAddons/
%{_kf6_libdir}/libKF6WidgetsAddons.so
%{_kf6_plugindir}/designer/kwidgetsaddons6widgets.so

%changelog
%autochangelog
