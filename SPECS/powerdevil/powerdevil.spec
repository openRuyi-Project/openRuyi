# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           powerdevil
Version:        6.7.1
Release:        %autorelease
Summary:        KDE Power Management module
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/powerdevil.git
#!RemoteAsset:  sha256:212c7f64ab5db83d9b483560f2b272912614b1244535d743e35564840a6fa7f5
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libcap-progs
BuildRequires:  pkgconfig
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  qt6-qtwayland-devel >= %{qt6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Screen) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(LibKWorkspace) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(ddcutil)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dpms)
BuildRequires:  pkgconfig(xcb-randr)

Requires:       kf6-kidletime-plugins
Requires:       kf6-knotifications
%requires_ge    plasma-workspace-libs

Recommends:     upower

%description
KDE Power Management module. Provides kded daemon, DBus helper and KCM for
configuring Power settings.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --with-html --generate-subpackages

%post
%systemd_user_post plasma-powerdevil.service

%preun
%systemd_user_preun plasma-powerdevil.service

%postun
%systemd_user_postun plasma-powerdevil.service

%files -f %{name}.lang
%license COPYING*
%{_kf6_applicationsdir}/kcm_mobile_power.desktop
%{_kf6_applicationsdir}/kcm_powerdevilprofilesconfig.desktop
%{_kf6_configdir}/autostart/powerdevil.desktop
%{_kf6_dbuspolicydir}/org.kde.powerdevil.backlighthelper.conf
%{_kf6_dbuspolicydir}/org.kde.powerdevil.chargethresholdhelper.conf
%{_kf6_dbuspolicydir}/org.kde.powerdevil.discretegpuhelper.conf
%{_kf6_dbuspolicydir}/org.kde.powerdevil.wakeupsourcehelper.conf
%{_kf6_debugdir}/batterymonitor.categories
%{_kf6_debugdir}/powerdevil.categories
%{_kf6_debugdir}/brightness.categories
%{_kf6_libdir}/libpowerdevilcore.so
%{_kf6_libdir}/libpowerdevilcore.so.*
%{_kf6_libexecdir}/kauth/backlighthelper
%{_kf6_libexecdir}/kauth/chargethresholdhelper
%{_kf6_libexecdir}/kauth/discretegpuhelper
%{_kf6_libexecdir}/kauth/wakeupsourcehelper
%{_kf6_notificationsdir}/powerdevil.notifyrc
%dir %{_kf6_plugindir}/kf6/krunner
%{_kf6_plugindir}/kf6/krunner/krunner_powerdevil.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.battery.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.brightness.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_power.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_powerdevilprofilesconfig.so
%dir %{_kf6_plugindir}/powerdevil/
%dir %{_kf6_plugindir}/powerdevil/action
%{_kf6_plugindir}/powerdevil/action/powerdevil_brightnesscontrolaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_dimdisplayaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_dpmsaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_handlebuttoneventsaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_keyboardbrightnesscontrolaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_powerprofileaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_runscriptaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_screenbrightnesscontrolaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_suspendsessionaction.so
%dir %{_kf6_qmldir}/org/kde/plasma/private/
%{_kf6_qmldir}/org/kde/plasma/private/batterymonitor/
%{_kf6_qmldir}/org/kde/plasma/private/brightnesscontrolplugin/
%{_kf6_sharedir}/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
%{_kf6_sharedir}/dbus-1/system-services/org.kde.powerdevil.chargethresholdhelper.service
%{_kf6_sharedir}/dbus-1/system-services/org.kde.powerdevil.discretegpuhelper.service
%{_kf6_sharedir}/dbus-1/system-services/org.kde.powerdevil.wakeupsourcehelper.service
%{_kf6_sharedir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
%{_kf6_sharedir}/polkit-1/actions/org.kde.powerdevil.chargethresholdhelper.policy
%{_kf6_sharedir}/polkit-1/actions/org.kde.powerdevil.discretegpuhelper.policy
%{_kf6_sharedir}/polkit-1/actions/org.kde.powerdevil.wakeupsourcehelper.policy
%{_libexecdir}/org_kde_powerdevil
%{_userunitdir}/plasma-powerdevil.service

%changelog
%autochangelog
