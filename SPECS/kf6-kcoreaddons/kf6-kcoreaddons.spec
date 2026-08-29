# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kcoreaddons

# Full KF6 version (e.g. 6.21.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kcoreaddons
Version:        6.28.0
Release:        %autorelease
Summary:        Utilities for core application functionality and accessing the OS
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            https://invent.kde.org/frameworks/kcoreaddons
#!RemoteAsset:  sha256:a713febee2f43bc31986d6c27d846ccab556fc7bc7c1919c3a662495720b431a
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DENABLE_PCH:BOOL=FALSE
BuildOption(conf):  -DBUILD_PYTHON_BINDINGS:BOOL=OFF
BuildOption(conf):  -DBUILD_QCH:BOOL=OFF
BuildOption(conf):  -DKCOREADDONS_BUILD_PYTHON_DOCS:BOOL=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  shared-mime-info
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickTest) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(build)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

Requires:       shared-mime-info >= 1.8

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package        devel
Summary:        Utilities for core application functionality and accessing the OS
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more. Development files.

%package     -n python-%{name}
Summary:        Qt for Python bindings for %{name}
Provides:       python3-%{name}
%python_provide python3-%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-%{name}
The package contains the PySide6 bindings library for %{name}.

%files
%license LICENSES/*
%doc README.md
%{_kf6_appsdir}/mime/packages/kde6.xml
%{_kf6_debugdir}/kcoreaddons.categories
%{_kf6_debugdir}/kcoreaddons.renamecategories
%{_kf6_libdir}/libKF6CoreAddons.so.*
%{_kf6_libdir}/qt6/metatypes/qt6kf6coreaddons_metatypes.json
%{_datadir}/locale/*/LC_MESSAGES/kcoreaddons6_qt.qm
%{_kf6_qmldir}/org/kde/coreaddons/

%files devel
%{_kf6_includedir}/KCoreAddons/
%{_kf6_cmakedir}/KF6CoreAddons/
%dir %{_kf6_datadir}/jsonschema
%{_kf6_datadir}/jsonschema/kpluginmetadata.schema.json
%{_kf6_libdir}/libKF6CoreAddons.so
%{_kf6_pkgconfigdir}/KF6CoreAddons.pc

%files -n python-kf6-kcoreaddons
# Python bindings disabled; package intentionally empty

%changelog
%autochangelog
