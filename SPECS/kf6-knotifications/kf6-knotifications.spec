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
Version:        6.22.0
Release:        %autorelease
Summary:        KDE Desktop notifications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/knotifications
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
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
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

%description
KNotification is used to notify the user of an event. It covers feedback and
persistent events.

%package        imports
Summary:        KDE Desktop notifications - QML files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    imports
KNotification is used to notify the user of an event. It covers feedback and
persistent events.
This package contains files that allow using knotification in QtQuick based
applications.

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

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
  -DBUILD_PYTHON_BINDINGS=OFF

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%files
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/knotifications.categories
%{_kf6_debugdir}/knotifications.renamecategories
%{_kf6_libdir}/libKF6Notifications.so.*
%{_datadir}/locale/*/LC_MESSAGES/knotifications6_qt.qm

%files imports
%{_kf6_qmldir}/org/kde/notification/

%files devel
%{_kf6_cmakedir}/KF6Notifications/
%{_kf6_includedir}/KNotifications/
%{_kf6_libdir}/libKF6Notifications.so

%files -n python-kf6-knotifications
# Python bindings disabled; package intentionally empty

%changelog
%autochangelog
