# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# TODO sort
# Internal QML imports
%global __requires_exclude qt6qmlimport\\((org\\.kde\\.plasma\\.shell\\.panel|org\\.kde\\.plasma\\.private).*
# %%global __requires_exclude qt6qmlimport\\((org\\.kde\\.private\\.kcms|org\\.kde\\.plasma\\.kcm|org\\.kde\\.desktopsession\\.private|org\\.kde\\.plasma\\.tablet|org\\.kde\\.plasma\\.touchscreen\\.kcm).*
%global have_gamecontroller_kcm 1

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           plasma-desktop
Version:        6.7.1
Release:        %autorelease
Summary:        The KDE Plasma Workspace Components
License:        GPL-2.0-only
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/plasma-desktop.git
#!RemoteAsset:  sha256:ec264cbc67c7e16d646684082f971816c0d475d0be3b92443c4e4802c89f8eee
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

Patch2000:      2000-Apply-branding-to-default-favorites.patch
Patch2001:      2001-Remove-discover-from-taskmanager-default-launchers.patch

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DBUILD_KCM_MOUSE_X11=OFF
BuildOption(conf):  -DBUILD_KCM_TOUCHPAD_X11=OFF

BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# Due to KWinDBusInterface not having a cmake version config file, we need to BR kwin6-devel instead
# BuildRequires:  cmake(KWinDBusInterface) >= %%{_plasma6_bugfix}
# Also applies to ScreenSaverDBusInterface
# BuildRequires:  cmake(ScreenSaverDBusInterface) >= %%{_plasma6_bugfix}
BuildRequires:  kscreenlocker-devel >= %{_plasma6_bugfix}
BuildRequires:  kwin-devel >= %{_plasma6_bugfix}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(KAccounts6)
BuildRequires:  cmake(KF6Attica) >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Baloo) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KDED) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6QQC2DesktopStyle) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KNightTime) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KRunnerAppDBusInterface) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KSMServerDBusInterface) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KSysGuard) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LibKLookAndFeel) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LibKWorkspace) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LibNotificationManager) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LibTaskManager) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma5Support) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivitiesStats) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.10.0
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(packagekitqt6)
BuildRequires:  cmake(SDL2)
BuildRequires:  SDL2-static
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwacom)
%if %{with scim}
BuildRequires:  pkgconfig(scim)
%endif
BuildRequires:  signon-plugin-oauth2-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.44
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xkbregistry)
BuildRequires:  pkgconfig(xkeyboard-config)

Requires:       plasma-desktop-branding = %{version}
Requires:       plasma-workspace >= %{_plasma6_bugfix}
# Required by the 'recent files' kcm
Requires:       qt6-qtbase >= %{qt6_version}
%requires_ge    libplasma
# Various KCMs use it
Requires:       kinfocenter
Requires:       kf6-kirigami >= %{kf6_version}
Requires:       kirigami-addons >= 1.12.1
Requires:       kmenuedit
# Needed for sensors
Requires:       libksysguard >= %{_plasma6_bugfix}
# kcm_style does DBus calls to the KDED module.
# However, that depends on xsettingsd and gio, so
# let the Supplements in kde-gtk-config5 handle it.
Requires:       kde-gtk-config
# Needed for several KCMs
Requires:       kf6-knewstuff >= %{kf6_version}
# needed for the ActivityManager
Requires:       plasma-activities >= %{_plasma6_bugfix}
Requires:       signon-plugin-oauth2

Recommends:     plasma-addons
Recommends:     plasma-desktop-emojier
Recommends:     xdg-user-dirs

Requires:       (plasma-kimpanel-ibus if ibus)
%if %{with scim}
Requires:       (plasma-kimpanel-scim if scim)
%endif

Provides:       plasma-desktop-branding = %{version}

%description
This package contains the basic packages for a Plasma workspace.

%package        emojier
Summary:        Selection window for emoji text input
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Other color fonts don't really work that well
Recommends:     fonts-noto-color-emoji

%description    emojier
Press Meta+. to open an emoji selection window.

%package     -n plasma-kimpanel-ibus
Summary:        Plasma IBus Configuration
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      plasma-kimpanel-scim

%description -n plasma-kimpanel-ibus
Plasma Input Method Backend for IBus support.

%if %{with scim}
%package     -n plasma-kimpanel-scim
Summary:        Plasma SCIM Configuration
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      plasma-kimpanel-ibus

%description -n plasma-kimpanel-scim
Plasma Input Method Backend for SCIM (Smart Chinese/Common Input Method) support.
%endif

%install -a
# no devel files needed here
rm -rv %{buildroot}%{_kf6_sharedir}/dbus-1/interfaces/

# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --with-html --generate-subpackages

%post
%systemd_user_post plasma-kaccess.service

%preun
%systemd_user_preun plasma-kaccess.service

%postun
%systemd_user_postun plasma-kaccess.service

%files -f %{name}.lang
%doc %lang(en) %{_kf6_htmldir}/en/*/
%license COPYING*
%{_kf6_applicationsdir}/kaccess.desktop
%{_kf6_applicationsdir}/kcm_access.desktop
%{_kf6_applicationsdir}/kcm_activities.desktop
%{_kf6_applicationsdir}/kcm_baloofile.desktop
%{_kf6_applicationsdir}/kcm_clock.desktop
%{_kf6_applicationsdir}/kcm_desktoppaths.desktop
%if %{have_gamecontroller_kcm}
%{_kf6_applicationsdir}/kcm_gamecontroller.desktop
%endif
%{_kf6_applicationsdir}/kcm_kded.desktop
%{_kf6_applicationsdir}/kcm_keyboard.desktop
%{_kf6_applicationsdir}/kcm_keys.desktop
%{_kf6_applicationsdir}/kcm_krunnersettings.desktop
%{_kf6_applicationsdir}/kcm_landingpage.desktop
%{_kf6_applicationsdir}/kcm_plasmasearch.desktop
%{_kf6_applicationsdir}/kcm_qtquicksettings.desktop
%{_kf6_applicationsdir}/kcm_recentFiles.desktop
%{_kf6_applicationsdir}/kcm_smserver.desktop
%{_kf6_applicationsdir}/kcm_solid_actions.desktop
%{_kf6_applicationsdir}/kcm_splashscreen.desktop
%{_kf6_applicationsdir}/kcm_tablet.desktop
%{_kf6_applicationsdir}/kcm_touchscreen.desktop
%{_kf6_applicationsdir}/kcm_workspace.desktop
%{_kf6_applicationsdir}/kcmspellchecking.desktop
%{_kf6_applicationsdir}/kde-mimeapps.list
%{_kf6_applicationsdir}/org.kde.knetattach.desktop
%{_kf6_applicationsdir}/kcm_mouse.desktop
%{_kf6_applicationsdir}/kcm_touchpad.desktop
%{_kf6_appstreamdir}/*.xml
%{_kf6_bindir}/kaccess
%{_kf6_bindir}/knetattach
%{_kf6_bindir}/krunner-plugininstaller
%{_kf6_bindir}/solid-action-desktop-gen
%{_kf6_bindir}/tastenbrett
%{_kf6_configdir}/autostart/kaccess.desktop
%{_kf6_configkcfgdir}/*.kcfg
%{_kf6_debugdir}/*.categories
%{_kf6_knsrcfilesdir}/krunner.knsrc
%{_kf6_knsrcfilesdir}/ksplash.knsrc
%{_kf6_libdir}/libkglobalaccelmodel.so.*
%{_kf6_notificationsdir}/kaccess.notifyrc
%{_kf6_plasmadir}/layout-templates/
%{_kf6_plasmadir}/packages/
%{_kf6_plasmadir}/plasmoids/
%{_kf6_plasmadir}/shells/
%{_kf6_plugindir}/attica_kde.so
%{_kf6_plugindir}/kf6/kded/device_automounter.so
%{_kf6_plugindir}/kf6/kded/keyboard.so
%{_kf6_plugindir}/kf6/kded/kded_touchpad.so
%{_kf6_plugindir}/kf6/krunner/
%{_kf6_plugindir}/plasma/applets/org.kde.panel.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.keyboardlayout.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.kicker.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.kickoff.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.kimpanel.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.pager.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.showActivityManager.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.showdesktop.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.taskmanager.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.trash.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.windowlist.so
%dir %{_kf6_plugindir}/plasma/kcms/desktop/
%{_kf6_plugindir}/plasma/kcms/desktop/kcm_krunnersettings.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_access.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_activities.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_baloofile.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_desktoppaths.so
%if %{have_gamecontroller_kcm}
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_gamecontroller.so
%endif
%dir %{_kf6_plugindir}/plasma/kcminit
%{_kf6_plugindir}/plasma/kcminit/kcm_mouse_init.so
%{_kf6_plugindir}/plasma/kcminit/kcm_touchpad_init.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_mouse.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_touchpad.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_kded.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_keyboard.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_keys.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_landingpage.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_plasmasearch.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_smserver.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_splashscreen.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_tablet.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_touchscreen.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_workspace.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_clock.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_device_automounter.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_qtquicksettings.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_recentFiles.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_solid_actions.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcmspellchecking.so
%{_kf6_qmldir}/org/kde/plasma/
%{_kf6_qmldir}/org/kde/private/
%dir %{_kf6_sharedir}/accounts/
%dir %{_kf6_sharedir}/accounts/providers
%dir %{_kf6_sharedir}/accounts/providers/kde/
%{_kf6_sharedir}/accounts/providers/kde/opendesktop.provider
%dir %{_kf6_sharedir}/accounts/services
%dir %{_kf6_sharedir}/accounts/services/kde/
%{_kf6_sharedir}/accounts/services/kde/opendesktop-rating.service
%{_kf6_sharedir}/kcm_recentFiles/
%{_kf6_sharedir}/kcmkeys/
%{_kf6_sharedir}/kcmsolidactions/
%{_kf6_sharedir}/kconf_update/50-krunner-activate-typing.sh
%{_kf6_sharedir}/kconf_update/50-krunner-activate-typing.upd
%{_kf6_sharedir}/locale/sr/LC_SCRIPTS/kfontinst/kfontinst.js
%{_kf6_sharedir}/kglobalaccel/org.kde.touchpadshortcuts.desktop
%dir %{_kf6_sharedir}/sddm
%dir %{_kf6_sharedir}/sddm/themes
%{_kf6_sharedir}/sddm/themes/breeze/
%{_kf6_sharedir}/solid/
%{_kf6_iconsdir}/hicolor/*/devices/input-touchpad.*
%{_kf6_sharedir}/kcmmouse/
%exclude %{_kf6_plasmadir}/emoji/
%{_userunitdir}/plasma-kaccess.service

%files emojier
%{_kf6_applicationsdir}/org.kde.plasma.emojier.desktop
%{_kf6_bindir}/plasma-emojier
%{_kf6_plasmadir}/emoji/
%{_kf6_sharedir}/kglobalaccel/org.kde.plasma.emojier.desktop

%files -n plasma-kimpanel-ibus
%{_libexecdir}/kimpanel-ibus-panel
%{_libexecdir}/kimpanel-ibus-panel-launcher

%if %{with scim}
%files -n plasma-kimpanel-scim
%{_libexecdir}/kimpanel-scim-panel
%endif

%changelog
%autochangelog
