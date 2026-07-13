# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.9.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Full KF6 version (e.g. 6.0.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}

Name:           plasma5support
Version:        6.7.1
Release:        %autorelease
Summary:        KF6 Porting aid
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/plasma5support
#!RemoteAsset:  sha256:28410789f5af6f00e7d5f4c88a58e7777a31ea9df7e7db75daf73a5d463ab39c
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DBUILD_QCH:BOOL=TRUE

BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Holidays) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6IdleTime) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6KIO) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6NetworkManagerQt) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Notifications) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Service) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Solid) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6UnitConversion)
BuildRequires:  cmake(KF6XmlGui) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KSysGuard) >= 6
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(libgps)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)

%description
Support components for porting from KF5/Qt5 to KF6/Qt6.

%package        devel
Summary:        Development Files for the plasma5support framework
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6Service) >= %{_kf6_bugfix_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description    devel
Development Files for the plasma5support framework.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_debugdir}/plasma5support.categories
%{_kf6_debugdir}/plasma5support.renamecategories
%dir %{_kf6_qmldir}/org/kde/plasma
%{_kf6_qmldir}/org/kde/plasma/plasma5support/
%{_kf6_sharedir}/plasma5support/
%{_kf6_libdir}/libPlasma5Support.so.*
%{_kf6_libdir}/libplasma-geolocation-interface.so.*
%{_kf6_libdir}/libweather_ion.so.*
%dir %{_kf6_plugindir}/plasma5support
%dir %{_kf6_plugindir}/plasma5support/dataengine
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_apps.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_devicenotifications.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_favicons.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_geolocation.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_hotplug.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_keystate.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_mouse.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_packagekit.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_powermanagement.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_soliddevice.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_filebrowser.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_places.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_activities.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_bbcukmet.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_dwd.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_envcan.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_noaa.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_weather.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_wettercom.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_executable.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_time.so
%dir %{_kf6_plugindir}/plasma5support/geolocationprovider
%{_kf6_plugindir}/plasma5support/geolocationprovider/plasma-geolocation-gps.so
%{_kf6_plugindir}/plasma5support/geolocationprovider/plasma-geolocation-ip.so
%{_kf6_sharedir}/plasma/weather_legacy/

%files devel
%doc %{_kf6_qchdir}/Plasma5Support.*
%{_kf6_cmakedir}/Plasma5Support/
%{_includedir}/Plasma5Support/
%dir %{_includedir}/plasma
%{_includedir}/plasma/geolocation/
%dir %{_includedir}/plasma5support/
%{_includedir}/plasma5support/weather/
%{_kf6_libdir}/libPlasma5Support.so
%{_kf6_libdir}/libweather_ion.so
%{_kf6_libdir}/libplasma-geolocation-interface.so

%changelog
%autochangelog
