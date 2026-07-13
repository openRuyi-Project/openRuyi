# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF6, but 5.8.95 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           libksysguard
Version:        6.7.1
Release:        %autorelease
Summary:        Task management and system monitoring library
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/libksysguard.git
#!RemoteAsset:  sha256:e652a923c3a2d28ccb15e1a657fda5d6b37e12f09ccd72bd6097fb9c0bc62390
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  lm_sensors-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(zlib)

Requires:       libksysguard-plugins

%description
Task management and system monitoring library.

%package        plugins
Summary:        Task management and system monitoring library -- plugins
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    plugins
Task management and system monitoring library. This package contains plugins.

%package        devel
Summary:        Task management and system monitoring library -- devel files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Config) >= %{kf6_version}
Requires:       cmake(KF6I18n) >= %{kf6_version}
Requires:       cmake(KF6IconThemes) >= %{kf6_version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Network) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description    devel
Task management and system monitoring library. This package contains development
files.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/ksysguard-identify
%{_kf6_debugdir}/libksysguard.categories
%{_kf6_knsrcfilesdir}/systemmonitor-faces.knsrc
%{_kf6_knsrcfilesdir}/systemmonitor-presets.knsrc
%{_kf6_libdir}/libKSysGuardFormatter.so.*
%{_kf6_libdir}/libKSysGuardSensorFaces.so.*
%{_kf6_libdir}/libKSysGuardSensors.so.*
%{_kf6_libdir}/libprocesscore.so.*
%dir %{_kf6_plugindir}/kf6/packagestructure/
%{_kf6_plugindir}/kf6/packagestructure/ksysguard_sensorface.so
%{_kf6_sharedir}/ksysguard/
%{_kf6_libdir}/libKSysGuardSystemStats.so.*
%dir %{_kf6_qmldir}/org/kde/ksysguard
%{_kf6_qmldir}/org/kde/ksysguard/faces/
%{_kf6_qmldir}/org/kde/ksysguard/formatter/
%{_kf6_qmldir}/org/kde/ksysguard/process/
%{_kf6_qmldir}/org/kde/ksysguard/sensors/
%{_kf6_sharedir}/dbus-1/interfaces/org.kde.ksystemstats1.xml

%files plugins
%{_kf6_dbuspolicydir}/org.kde.ksysguard.processlisthelper.conf
%dir %{_kf6_plugindir}/ksysguard/
%dir %{_kf6_plugindir}/ksysguard/process
%{_kf6_plugindir}/ksysguard/process/ksysguard_plugin_gpu.so
%{_kf6_plugindir}/ksysguard/process/ksysguard_plugin_network.so
%{_kf6_sharedir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%{_kf6_sharedir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy
%{_kf6_libexecdir}/kauth/ksysguardprocesslist_helper
%dir %{_libexecdir}/ksysguard/
%{_libexecdir}/ksysguard/ksgrd_network_helper

%files devel
%{_includedir}/ksysguard/
%{_kf6_cmakedir}/KSysGuard/
%{_kf6_libdir}/libKSysGuardFormatter.so
%{_kf6_libdir}/libKSysGuardSensorFaces.so
%{_kf6_libdir}/libKSysGuardSensors.so
%{_kf6_libdir}/libKSysGuardSystemStats.so
%{_kf6_libdir}/libprocesscore.so

%changelog
%autochangelog
