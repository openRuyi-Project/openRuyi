# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kstatusnotifieritem

# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kstatusnotifieritem
Version:        6.27.0
Release:        %autorelease
Summary:        Implementation of Status Notifier Items
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kstatusnotifieritem.git
#!RemoteAsset:  sha256:a2eec2a981ed9da6cffc955cc21a50dcbc77141cbb840d915f92d1897442d239
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DBUILD_PYTHON_BINDINGS=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{_kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  python-build
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-wheel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

%description
Implementation of Status Notifier Items.

%package        devel
Summary:        Development files for kstatusnotifieritem
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Requires:       cmake(Qt6Xml) >= %{qt6_version}

%description    devel
Development files for kstatusnotifieritem

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_debugdir}/kstatusnotifieritem.categories
%{_kf6_libdir}/libKF6StatusNotifierItem.so.*

%files devel
%{_kf6_libdir}/libKF6StatusNotifierItem.so
%{_kf6_cmakedir}/KF6StatusNotifierItem/
%{_kf6_dbusinterfacesdir}/kf6_org.kde.StatusNotifierItem.xml
%{_kf6_dbusinterfacesdir}/kf6_org.kde.StatusNotifierWatcher.xml
%{_kf6_includedir}/KStatusNotifierItem/

%changelog
%autochangelog
