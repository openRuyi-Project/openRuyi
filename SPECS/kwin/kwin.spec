# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Internal QML imports
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.KWin\\.Effect\\.WindowView.*

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           kwin
Version:        6.7.4
Release:        %autorelease
Summary:        KDE Window Manager
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/kwin.git
#!RemoteAsset:  sha256:94cbbd1c2fa26d8acabcf735b77f140edb0d4c99a93d1fdf2fadab40e4e23054
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds
BuildRequires:  cmake(Breeze) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KDecoration3) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KGlobalAccelD) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KNightTime) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KScreenLocker) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.14.0
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sensors) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(epoxy) >= 1.3
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libdisplay-info) >= 0.2.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.116
BuildRequires:  pkgconfig(libeis-1.0)
BuildRequires:  pkgconfig(libinput) >= 1.26
BuildRequires:  pkgconfig(libpipewire-0.3) >= 1.2.0
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  pkgconfig(wayland-cursor) >= 1.22
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.38
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb) >= 1.10
BuildRequires:  pkgconfig(xcb-composite) >= 1.10
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-dri3) >= 1.10
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-present) >= 1.10
BuildRequires:  pkgconfig(xcb-randr) >= 1.10
BuildRequires:  pkgconfig(xcb-render) >= 1.10
BuildRequires:  pkgconfig(xcb-res) >= 1.10
BuildRequires:  pkgconfig(xcb-shape) >= 1.10
BuildRequires:  pkgconfig(xcb-shm) >= 1.10
BuildRequires:  pkgconfig(xcb-sync) >= 1.10
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes) >= 1.10
BuildRequires:  pkgconfig(xcb-xinerama) >= 1.10
BuildRequires:  pkgconfig(xcb-xinput) >= 1.10
BuildRequires:  pkgconfig(xcb-xkb) >= 1.10
BuildRequires:  pkgconfig(xkbcommon) >= 0.7.0
BuildRequires:  pkgconfig(xkbcommon-x11)

Requires:       breeze-decoration >= %{_plasma6_bugfix}
Requires:       kdialog
Requires:       kf6-kirigami >= %{kf6_version}
Requires:       kglobalacceld >= %{_plasma6_bugfix}
Requires:       Xwayland
Requires:       kf6-kdeclarative >= %{kf6_version}
Requires:       kf6-kitemmodels >= %{kf6_version}
Requires:       libplasma >= %{_plasma6_bugfix}
Requires:       qt6-qtdeclarative >= %{qt6_version}
Requires:       qt6-qtmultimedia >= %{qt6_version}

# For displaying full monitor vendor names
Recommends:     hwdata
Recommends:     xorg-x11-server-wayland

%description
KWin is Plasma window manager.

%package        devel
Summary:        KDE Window Manager - development files
Requires:       kdecoration-devel >= %{_plasma6_bugfix}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(epoxy)
Requires:       pkgconfig(libdrm) >= 2.4.116

%description    devel
KWin is Plasma window manager.
This package provides development files.

%preun
%systemd_user_preun plasma-kwin_wayland.service

%post
%systemd_user_post plasma-kwin_wayland.service

%postun
%systemd_user_postun plasma-kwin_wayland.service

%files
%doc README.md
%doc %{_kf6_htmldir}/*
%verify(not caps) %{_kf6_bindir}/kwin_wayland
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_animations.desktop
%{_kf6_applicationsdir}/kcm_kwin_effects.desktop
%{_kf6_applicationsdir}/kcm_kwin_scripts.desktop
%{_kf6_applicationsdir}/kcm_kwin_virtualdesktops.desktop
%{_kf6_applicationsdir}/kcm_kwindecoration.desktop
%{_kf6_applicationsdir}/kcm_kwinoptions.desktop
%{_kf6_applicationsdir}/kcm_kwinrules.desktop
%{_kf6_applicationsdir}/kcm_kwintabbox.desktop
%{_kf6_applicationsdir}/kcm_kwinxwayland.desktop
%{_kf6_applicationsdir}/kcm_virtualkeyboard.desktop
%{_kf6_applicationsdir}/org.kde.kwin.killer.desktop
%{_kf6_applicationsdir}/org.kde.kwin.dialoghelper.desktop
%{_kf6_bindir}/kwin_wayland_wrapper
%{_kf6_bindir}/kwindowprop
%{_kf6_configkcfgdir}/*
%{_kf6_debugdir}/org_kde_kwin.categories
%{_kf6_iconsdir}/hicolor/*/apps/kwin.png
%{_kf6_iconsdir}/hicolor/scalable/apps/kwin.svgz
%{_kf6_knsrcfilesdir}/*.knsrc
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-delete-desktop-switching-shortcuts
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-remove-breeze-tabbox-default
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-reset-active-mouse-screen
%{_kf6_libdir}/kconf_update_bin/kwin-6.1-remove-gridview-expose-shortcuts
%{_kf6_libdir}/kconf_update_bin/kwin-6.5-showpaint-changes
%{_kf6_libdir}/kconf_update_bin/kwin5_update_default_rules
%{_kf6_libdir}/libkcmkwincommon.so.*
%{_kf6_libdir}/libkwin.so.*
%{_kf6_notificationsdir}/kwin.notifyrc
%dir %{_kf6_plugindir}/kwin
%dir %{_kf6_plugindir}/kwin/effects
%dir %{_kf6_plugindir}/kwin/effects/configs
%{_kf6_plugindir}/kwin/effects/configs/kcm_kwin4_genericscripted.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_blur_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_diminactive_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_glide_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_hidecursor_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_magiclamp_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_mouseclick_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_mousemark_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_overview_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_slide_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_thumbnailaside_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_tileseditor_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_trackmouse_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_windowview_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_wobblywindows_config.so
%dir %{_kf6_plugindir}/kwin/plugins
%{_kf6_plugindir}/kwin/plugins/BounceKeysPlugin.so
%{_kf6_plugindir}/kwin/plugins/KeyNotificationPlugin.so
%{_kf6_plugindir}/kwin/plugins/StickyKeysPlugin.so
%{_kf6_plugindir}/kwin/plugins/buttonsrebind.so
%{_kf6_plugindir}/kwin/plugins/SlowKeysPlugin.so
%{_kf6_plugindir}/kwin/plugins/eis.so
%{_kf6_plugindir}/kwin/plugins/krunnerintegration.so
%{_kf6_plugindir}/kwin/plugins/nightlight.so
%{_kf6_plugindir}/kwin/plugins/MouseKeysPlugin.so
%{_kf6_plugindir}/kwin/plugins/screencast.so
%{_kf6_plugindir}/kwin/plugins/screenshot.so
%{_kf6_plugindir}/kwin/plugins/TouchpadShortcutsPlugin.so
%dir %{_kf6_plugindir}/kf6/packagestructure
%{_kf6_plugindir}/kf6/packagestructure/kwin_aurorae.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_decoration.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_effect.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_scripts.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_windowswitcher.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm*.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kwin*.so
%dir %{_kf6_qmldir}/org/kde/kwin/
%{_kf6_qmldir}/org/kde/kwin/private/
%{_kf6_sharedir}/kconf_update/kwin.upd
%{_kf6_sharedir}/krunner/dbusplugins/kwin-runner-windows.desktop
%{_kf6_sharedir}/kwin-wayland/
%{_libexecdir}/kwin_killer_helper
%{_libexecdir}/kwin-applywindowdecoration
%{_libexecdir}/kwin-tabbox-preview
%{_libexecdir}/kwin_dialog_helper
%{_libexecdir}/kwin_eis_prompter
%{_userunitdir}/plasma-kwin_wayland.service
%{_datadir}/locale/*/LC_MESSAGES/kwin*.mo
%{_datadir}/locale/*/LC_MESSAGES/kcm*.mo

%files devel
%{_includedir}/kwin/
%{_kf6_cmakedir}/KWin/
%{_kf6_cmakedir}/KWinDBusInterface/
%{_kf6_dbusinterfacesdir}/org.kde.kwin.*
%{_kf6_dbusinterfacesdir}/org.kde.KWin.*
%{_kf6_libdir}/libkwin.so

%changelog
%autochangelog
