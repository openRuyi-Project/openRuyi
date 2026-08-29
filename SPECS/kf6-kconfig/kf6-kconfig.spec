# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kconfig
# Full KF6 version (e.g. 6.28.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kconfig
Version:        6.28.0
Release:        %autorelease
Summary:        Advanced configuration system
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            https://invent.kde.org/frameworks/kconfig
#!RemoteAsset:  sha256:24e26e516b7904a26661eab7d2064bee1ac57165571e85b4da6020fd36f14322
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

Provides:       kf6-kconfig-imports = %{version}-%{release}
Obsoletes:      kf6-kconfig-imports < %{version}-%{release}

%description
KConfig provides an advanced configuration system. It is made of three parts:
KConfigCore, KConfigGui and KConfigQml.

KConfigCore provides access to the configuration files themselves. It features:

- centralized definition: define your configuration in an XML file and use
`kconfig_compiler` to generate classes to read and write configuration entries.

- lock-down (kiosk) support.

KConfigGui provides a way to hook widgets to the configuration so that they are
automatically initialized from the configuration and automatically propagate
their changes to their respective configuration files.

KConfigQml provides QtQuick bindings to KConfig, allowing it to be used with QML.

%package        devel
Summary:        KConfig Development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Qml) >= %{qt6_version}
Requires:       cmake(Qt6Xml) >= %{qt6_version}

%description    devel
KConfig provides an advanced configuration system. It is made of two parts:
KConfigCore and KConfigGui.

KConfigCore provides access to the configuration files themselves. It features:

- centralized definition: define your configuration in an XML file and use
`kconfig_compiler` to generate classes to read and write configuration entries.

- lock-down (kiosk) support.

KConfigGui provides a way to hook widgets to the configuration so that they are
automatically initialized from the configuration and automatically propagate
their changes to their respective configuration files. Development files.

%files
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/kreadconfig6
%{_kf6_bindir}/kwriteconfig6
%{_kf6_debugdir}/kconfig.categories
%{_kf6_debugdir}/kconfig.renamecategories
%{_kf6_libdir}/libKF6ConfigCore.so.*
%{_kf6_libdir}/libKF6ConfigGui.so.*
%{_kf6_libdir}/libKF6ConfigQml.so.*
%{_kf6_libdir}/qt6/metatypes/qt6kf6configcore_metatypes.json
%{_kf6_libdir}/qt6/metatypes/qt6kf6configgui_metatypes.json
%{_datadir}/locale/*/LC_MESSAGES/kconfig6_qt.qm
%{_kf6_libexecdir}/kconf_update
%{_kf6_qmldir}/org/kde/config/

%files devel
%{_kf6_includedir}/KConfig/
%{_kf6_includedir}/KConfigCore/
%{_kf6_includedir}/KConfigGui/
%{_kf6_includedir}/KConfigQml/
%{_kf6_cmakedir}/KF6Config/
%{_kf6_libdir}/libKF6ConfigCore.so
%{_kf6_libdir}/libKF6ConfigGui.so
%{_kf6_libdir}/libKF6ConfigQml.so
%{_kf6_libexecdir}/kconfig_compiler_kf6

%changelog
%autochangelog
