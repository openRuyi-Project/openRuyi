# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname knotifications

# Full KF6 version (e.g. 6.21.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-knotifications
Version:        6.28.0
Release:        %autorelease
Summary:        KDE Desktop notifications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/knotifications
#!RemoteAsset:  sha256:e5d3b284ccc907f190d3ab10995a0ae7fa0f505088acc69edc7adfcc6a8140d6
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DBUILD_PYTHON_BINDINGS=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libcanberra)
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

Provides:       kf6-knotifications-imports = %{version}-%{release}
Obsoletes:      kf6-knotifications-imports < %{version}-%{release}

%description
KNotification is used to notify the user of an event. It covers feedback and
persistent events.

%package        devel
Summary:        KDE Desktop notifications: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description    devel
KNotification is used to notify the user of an event. It covers feedback and
persistent events. Development files.

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
%{_kf6_debugdir}/knotifications.categories
%{_kf6_debugdir}/knotifications.renamecategories
%{_kf6_libdir}/libKF6Notifications.so.*
%{_datadir}/locale/*/LC_MESSAGES/knotifications6_qt.qm
%{_kf6_qmldir}/org/kde/notification/

%files devel
%{_kf6_cmakedir}/KF6Notifications/
%{_kf6_includedir}/KNotifications/
%{_kf6_libdir}/libKF6Notifications.so

%files -n python-kf6-knotifications
# Python bindings disabled; package intentionally empty

%changelog
%autochangelog
