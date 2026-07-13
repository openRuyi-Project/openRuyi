# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Remove when gpsd has a qt6 flavor
%global __qml_requires_opts --qtver 6

%global __requires_exclude qt6qmlimport\\((org\\.kde\\.plasma\\.private|org\\.kde\\.plasma\\.workspace|org\\.kde\\.notificationmanager|org\\.kde\\.plasma\\.lookandfeel|org\\.kde\\.plasma\\.wallpapers|org\\.kde\\.taskmanager|org\\.kde\\.holidayeventshelperplugin|org\\.kde\\.kscreenlocker).*

%define kf6_version 6.18.0
%define qt6_version 6.9.0

%bcond x11 0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           plasma-workspace
Version:        6.7.1
Release:        %autorelease
Summary:        The KDE Plasma Workspace Components
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/plasma-workspace.git
#!RemoteAsset:  sha256:0a822d6f371a73757ad496f68908dd2ca64439e418074d9e5c5380c0817073ff
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        sddm.conf
Source2:        waitforkded.conf
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DGLIBC_LOCALE_GENERATED:BOOL=TRUE
BuildOption(conf):  -DGLIBC_LOCALE_GEN:BOOL=FALSE
%if %{with x11}
BuildOption(conf):  -DPLASMA_X11_DEFAULT_SESSION:BOOL=TRUE
BuildOption(conf):  -DBUILD_X11=ON
%else
BuildOption(conf):  -DPLASMA_X11_DEFAULT_SESSION:BOOL=FALSE
BuildOption(conf):  -DBUILD_X11=OFF
%endif

BuildRequires:  kf6-breeze-icons
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# Due to KWinDBusInterface not having a cmake version config file, we need to BR kwin6-devel instead
# BuildRequires:  cmake(KWinDBusInterface) >= %%{_plasma6_bugfix}
BuildRequires:  kwin-devel >= %{_plasma6_bugfix}
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  qt6-qtwayland-devel >= %{qt6_version}
BuildRequires:  cmake(AppStreamQt) >= 1.0
BuildRequires:  cmake(Breeze) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KExiv2Qt6)
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Baloo) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KDED) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6NetworkManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Prison) >= %{kf6_version}
BuildRequires:  cmake(KF6QuickCharts) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(KF6Screen) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6UnitConversion) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KNightTime) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KPipeWire) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KScreenLocker) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KSysGuard) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LayerShellQt) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma5Support) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivitiesStats) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.6
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Location) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Positioning) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandCompositor) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(ScreenSaverDBusInterface) >= %{_plasma6_bugfix}
BuildRequires:  cmake(packagekitqt6)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libgps)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libqalculate) >= 2.0
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(wayland-client) >= 1.15
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds

Requires:       iso-codes
Requires:       iso-codes-lang
Requires:       plasma-workspace-libs = %{version}-%{release}
Requires:       accountsservice
Requires:       breeze >= %{_plasma6_bugfix}
Requires:       kf6-frameworkintegration-plugin
Requires:       kactivitymanagerd
Requires:       kde-cli-tools >= %{_plasma6_bugfix}
Requires:       kf6-kded
Requires:       kf6-kquickcharts
Requires:       kglobalacceld >= %{_plasma6_bugfix}
Requires:       kirigami-addons >= 1.12.1
Requires:       kscreen >= %{_plasma6_bugfix}
Requires:       kscreenlocker >= %{_plasma6_bugfix}
Requires:       kwin >= %{_plasma6_bugfix}
Requires:       libkscreen-plugin >= %{_plasma6_bugfix}
Requires:       qt6-qtpositioning >= %{qt6_version}
Requires:       qt6-qttools
Requires:       qt6-qtdeclarative >= %{qt6_version}
Requires:       kf6-kconfig
Requires:       milou >= %{_plasma6_bugfix}
Requires:       qt6-qtbase >= %{qt6_version}

Recommends:     drkonqi >= %{_plasma6_bugfix}
Recommends:     ocean-sound-theme >= %{_plasma6_bugfix}

Requires:       kf6-knewstuff >= %{kf6_version}
Requires:       ksystemstats
Requires:       kf6-kuserfeedback
Requires:       cpp
Requires:       %{_bindir}/grep
Requires:       sddm
Requires:       kio-extras
Requires:       knighttime >= %{_plasma6_bugfix}
%requires_ge    libplasma

# The lockscreen has a button to open a virtual keyboard
Recommends:     qt6-qtvirtualkeyboard >= %{qt6_version}
# For dmenudbusmenuproxy
Recommends:     (appmenu-gtk3-module if gtk3)
# Used to be provided/obsoleted by xembedsniproxy
Provides:       xembed-sni-proxy = %{version}
Obsoletes:      xembed-sni-proxy < %{version}
# plasmashell implements the dbus interface org.freedesktop.Notifications directly
Provides:       dbus(org.freedesktop.Notifications)

%description
This package contains the basic packages for a Plasma workspace.

%package        libs
Summary:        The KDE Plasma Workspace Components
Requires:       libplasma >= %{_plasma6_bugfix}

%description    libs
This package contains the basic packages for a KDE Plasma 6 workspace.

%package        devel
Summary:        The KDE Plasma Workspace Components
Requires:       plasma-workspace-libs = %{version}-%{release}
Requires:       cmake(KF6ItemModels) >= %{kf6_version}
Requires:       cmake(LayerShellQt) >= %{_plasma6_bugfix}
Requires:       cmake(Plasma) >= %{_plasma6_bugfix}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}
Requires:       cmake(Qt6Quick) >= %{qt6_version}
Conflicts:      kapptemplate <= 16.03.80

%description    devel
This package contains the basic packages for a KDE Plasma 6 workspace.
Development files.

%package     -n plasma-session
Summary:        KDE Plasma Session
Requires:       breeze >= %{_plasma6_bugfix}
Requires:       breeze-decoration >= %{_plasma6_bugfix}
Requires:       kf6-kwindowsystem >= %{kf6_version}
Requires:       plasma-desktop >= %{_plasma6_bugfix}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       polkit-kde-agent-1 >= %{_plasma6_bugfix}
Requires:       powerdevil >= %{_plasma6_bugfix}
Requires:       systemsettings >= %{_plasma6_bugfix}
Requires:       qt6-qtwayland
# For screen sharing and window thumbnails in plasmashell
Requires:       pipewire
Requires:       xdg-user-dirs
Requires:       Xwayland
%if %{with x11}
# People may want the X11 session
Recommends:     plasma-session-x11 = %{version}
%endif
BuildArch:      noarch

%description -n plasma-session
This package contains the startup scripts necessary to start a KDE
Plasma 6 session.

%if %{with x11}
%package     -n plasma-session-x11
Summary:        KDE Plasma Session on X11
Requires:       kwin6-x11 >= %{_plasma6_bugfix}
Requires:       plasma-session = %{version}
Requires:       xf86-input-libinput
Requires:       xorg-x11-server
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description -n plasma-session-x11
This package contains the startup scripts and programs necessary to
start a KDE Plasma 6 session on X11.
%endif

%package     -n sddm-kde-config-openruyi
Summary:        Plasma branding for SDDM
Requires:       sddm
Supplements:    (%{name} and sddm)

%description -n sddm-kde-config-openruyi
This package confirms defaults for SDDM suitable for Plasma 6.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --with-html --all-name --generate-subpackages

# Copy the icon for org.kde.kcolorschemeeditor.desktop
mkdir -p %{buildroot}%{_kf6_iconsdir}/hicolor/32x32/apps/
cp %{_kf6_iconsdir}/breeze/preferences/32/preferences-desktop-color.svg %{buildroot}%{_kf6_iconsdir}/hicolor/32x32/apps/

%if %{with x11}
# Rename upstream session file to oS location
mv %{buildroot}%{_kf6_sharedir}/xsessions/{plasma,plasma6}.desktop

# Install compatibility symlink
ln -s %{_kf6_sharedir}/xsessions/plasma6.desktop %{buildroot}%{_kf6_sharedir}/xsessions/kde-plasma.desktop

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop
%else
rm -f %{buildroot}%{_sysconfdir}/xdg/autostart/xembedsniproxy.desktop
rm -f %{buildroot}%{_kf6_bindir}/startplasma-x11
rm -f %{buildroot}%{_kf6_bindir}/xembedsniproxy
rm -f %{buildroot}%{_userunitdir}/plasma-workspace-x11.target
rm -f %{buildroot}%{_userunitdir}/plasma-xembedsniproxy.service
rm -f %{buildroot}%{_kf6_libexecdir}/kauth/fontinst_x11
rm -f %{buildroot}%{_kf6_sharedir}/xsessions/plasmax11.desktop
%endif

# Keep historical session filename in package output
if [ -f %{buildroot}%{_kf6_sharedir}/wayland-sessions/plasma.desktop ]; then
  mv %{buildroot}%{_kf6_sharedir}/wayland-sessions/plasma.desktop %{buildroot}%{_kf6_sharedir}/wayland-sessions/plasmawayland.desktop
fi

install -Dm 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/10-plasma.conf
install -Dm 0644 %{SOURCE2} %{buildroot}%{_userunitdir}/plasma-plasmashell.service.d/waitforkded.conf

%post
%systemd_user_post plasma-gmenudbusmenuproxy.service
%systemd_user_post plasma-kcminit-phase1.service
%systemd_user_post plasma-kcminit.service
%systemd_user_post plasma-krunner.service
%systemd_user_post plasma-ksmserver.service
%systemd_user_post plasma-plasmashell.service
%systemd_user_post plasma-baloorunner.service
%systemd_user_post plasma-restoresession.service
%systemd_user_post plasma-ksplash.service
%if %{with x11}
%systemd_user_post plasma-xembedsniproxy.service
%endif

%preun
%systemd_user_preun plasma-gmenudbusmenuproxy.service
%systemd_user_preun plasma-kcminit-phase1.service
%systemd_user_preun plasma-kcminit.service
%systemd_user_preun plasma-krunner.service
%systemd_user_preun plasma-ksmserver.service
%systemd_user_preun plasma-plasmashell.service
%systemd_user_preun plasma-baloorunner.service
%systemd_user_preun plasma-restoresession.service
%systemd_user_preun plasma-ksplash.service
%if %{with x11}
%systemd_user_preun plasma-xembedsniproxy.service
%endif

%postun
%systemd_user_postun plasma-gmenudbusmenuproxy.service
%systemd_user_postun plasma-kcminit-phase1.service
%systemd_user_postun plasma-kcminit.service
%systemd_user_postun plasma-krunner.service
%systemd_user_postun plasma-ksmserver.service
%systemd_user_postun plasma-plasmashell.service
%systemd_user_postun plasma-baloorunner.service
%systemd_user_postun plasma-restoresession.service
%systemd_user_postun plasma-ksplash.service
%if %{with x11}
%systemd_user_postun plasma-xembedsniproxy.service
%endif

%if %{with x11}
%post -n plasma-session-x11
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/plasma6.desktop 25

%postun -n plasma-session-x11
[ -f %{_datadir}/xsessions/plasma6.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/plasma6.desktop
%endif

%files -f %{name}.lang
%license LICENSES/*
%dir %{_kf6_configdir}/menus
%config %{_kf6_configdir}/menus/plasma-applications.menu
%config %{_kf6_configdir}/plasmanotifyrc
%doc %lang(en) %{_kf6_htmldir}/en/PolicyKit-kde/
%doc %lang(en) %{_kf6_htmldir}/en/kcontrol/
%doc %lang(en) %{_kf6_htmldir}/en/klipper/
%exclude %{_kf6_libdir}/libkfontinst.so
%exclude %{_kf6_libdir}/libkfontinstui.so
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_plasmashell
%{_datadir}/zsh/site-functions/_krunner
%{_kf6_applicationsdir}/kcm_autostart.desktop
%{_kf6_applicationsdir}/kcm_componentchooser.desktop
%{_kf6_applicationsdir}/kcm_colors.desktop
%{_kf6_applicationsdir}/kcm_cursortheme.desktop
%{_kf6_applicationsdir}/kcm_desktoptheme.desktop
%{_kf6_applicationsdir}/kcm_feedback.desktop
%{_kf6_applicationsdir}/kcm_fontinst.desktop
%{_kf6_applicationsdir}/kcm_fonts.desktop
%{_kf6_applicationsdir}/kcm_icons.desktop
%{_kf6_applicationsdir}/kcm_lookandfeel.desktop
%{_kf6_applicationsdir}/kcm_nightlight.desktop
%{_kf6_applicationsdir}/kcm_nighttime.desktop
%{_kf6_applicationsdir}/kcm_notifications.desktop
%{_kf6_applicationsdir}/kcm_regionandlang.desktop
%{_kf6_applicationsdir}/kcm_soundtheme.desktop
%{_kf6_applicationsdir}/kcm_style.desktop
%{_kf6_applicationsdir}/kcm_users.desktop
%{_kf6_applicationsdir}/kcm_wallpaper.desktop
%{_kf6_applicationsdir}/org.kde.baloorunner.desktop
%{_kf6_applicationsdir}/org.kde.secretprompter.desktop
%{_kf6_applicationsdir}/org.kde.plasma-interactiveconsole.desktop
%{_kf6_applicationsdir}/org.kde.kcolorschemeeditor.desktop
%{_kf6_applicationsdir}/org.kde.kfontinst.desktop
%{_kf6_applicationsdir}/org.kde.kfontview.desktop
%{_kf6_applicationsdir}/org.kde.klipper.desktop
%{_kf6_applicationsdir}/org.kde.plasma-fallback-session-save.desktop
%{_kf6_applicationsdir}/org.kde.plasmashell.desktop
%{_kf6_applicationsdir}/org.kde.plasmawindowed.desktop
%{_kf6_bindir}/gmenudbusmenuproxy
%{_kf6_bindir}/kcminit
%{_kf6_bindir}/kcminit_startup
%{_kf6_bindir}/kcolorschemeeditor
%{_kf6_bindir}/kde-systemd-start-condition
%{_kf6_bindir}/kfontinst
%{_kf6_bindir}/kfontview
%{_kf6_bindir}/krunner
%{_kf6_bindir}/ksmserver
%{_kf6_bindir}/ksplashqml
%{_kf6_bindir}/lookandfeeltool
%{_kf6_bindir}/plasma-apply-colorscheme
%{_kf6_bindir}/plasma-apply-cursortheme
%{_kf6_bindir}/plasma-apply-desktoptheme
%{_kf6_bindir}/plasma-apply-lookandfeel
%{_kf6_bindir}/plasma-apply-wallpaperimage
%{_kf6_bindir}/plasma-interactiveconsole
%{_kf6_bindir}/plasma-shutdown
%{_kf6_bindir}/plasma_session
%{_kf6_bindir}/plasma_waitforname
%{_kf6_bindir}/plasmashell
%{_kf6_bindir}/plasmawindowed
%{_kf6_bindir}/startplasma-wayland
%if %{with x11}
%{_kf6_bindir}/xembedsniproxy
%endif
%{_kf6_configdir}/autostart/gmenudbusmenuproxy.desktop
%{_kf6_configdir}/autostart/org.kde.plasma-fallback-session-restore.desktop
%{_kf6_configdir}/autostart/org.kde.plasmashell.desktop
%if %{with x11}
%{_kf6_configdir}/autostart/xembedsniproxy.desktop
%endif
%{_kf6_configkcfgdir}/colorssettings.kcfg
%{_kf6_configkcfgdir}/cursorthemesettings.kcfg
%{_kf6_configkcfgdir}/feedbacksettings.kcfg
%{_kf6_configkcfgdir}/fontssettings.kcfg
%{_kf6_configkcfgdir}/freespacenotifier.kcfg
%{_kf6_configkcfgdir}/iconssettingsbase.kcfg
%{_kf6_configkcfgdir}/launchfeedbacksettings.kcfg
%{_kf6_configkcfgdir}/lookandfeelsettings.kcfg
%{_kf6_configkcfgdir}/stylesettings.kcfg
%{_kf6_debugdir}/*.categories
%{_kf6_iconsdir}/hicolor/*/apps/kfontview.png
%{_kf6_iconsdir}/hicolor/*/mimetypes/fonts-package.png
%{_kf6_iconsdir}/hicolor/32x32/apps/preferences-desktop-color.svg
%{_kf6_iconsdir}/hicolor/scalable/apps/preferences-desktop-font-installer.svgz
%{_kf6_knsrcfilesdir}/colorschemes.knsrc
%{_kf6_knsrcfilesdir}/gtk_themes.knsrc
%{_kf6_knsrcfilesdir}/icons.knsrc
%{_kf6_knsrcfilesdir}/kfontinst.knsrc
%{_kf6_knsrcfilesdir}/lookandfeel.knsrc
%{_kf6_knsrcfilesdir}/plasma-themes.knsrc
%{_kf6_knsrcfilesdir}/plasmoids.knsrc
%{_kf6_knsrcfilesdir}/wallpaper-mobile.knsrc
%{_kf6_knsrcfilesdir}/wallpaper.knsrc
%{_kf6_knsrcfilesdir}/wallpaperplugin.knsrc
%{_kf6_knsrcfilesdir}/xcursor.knsrc
%{_kf6_kxmlguidir}/kfontview/
%{_kf6_kxmlguidir}/kfontviewpart/
%{_kf6_libdir}/kconf_update_bin/plasma6.0-remove-dpi-settings
%{_kf6_libdir}/kconf_update_bin/plasma6.0-remove-old-shortcuts
%{_kf6_libdir}/kconf_update_bin/plasma6.3-update-clipboard-database-2-to-3
%{_kf6_libdir}/kconf_update_bin/plasma6.4-migrate-fullscreen-notifications-to-dnd
%{_kf6_libdir}/kconf_update_bin/plasmashell-6.0-keep-custom-position-of-panels
%{_kf6_libdir}/kconf_update_bin/plasmashell-6.0-keep-default-floating-setting-for-plasma-5-panels
%{_kf6_libdir}/kconf_update_bin/plasmashell-6.5-remove-stop-activity-shortcut
%{_kf6_libdir}/libkfontinst.so.*
%{_kf6_libdir}/libkfontinstui.so.*
%{_kf6_notificationsdir}/devicenotifications.notifyrc
%{_kf6_notificationsdir}/donationmessage.notifyrc
%{_kf6_notificationsdir}/freespacenotifier.notifyrc
%{_kf6_notificationsdir}/libnotificationmanager.notifyrc
%{_kf6_notificationsdir}/oom_notifier.notifyrc
%{_kf6_plasmadir}/avatars/
%{_kf6_plasmadir}/look-and-feel/
%{_kf6_plasmadir}/plasmoids/
%{_kf6_plasmadir}/wallpapers/
%{_kf6_plugindir}/kf6/kded/
%{_kf6_plugindir}/kf6/kfileitemaction/
%{_kf6_plugindir}/kf6/kio/
%{_kf6_plugindir}/kf6/krunner/
%{_kf6_plugindir}/kf6/packagestructure/
%{_kf6_plugindir}/kf6/parts/
%{_kf6_plugindir}/kf6/thumbcreator/
%{_kf6_plugindir}/plasma/
%{_kf6_plugindir}/plasmacalendarplugins/
%{_kf6_qmldir}/org/kde/breeze/
%{_kf6_qmldir}/org/kde/notificationmanager/
%{_kf6_qmldir}/org/kde/plasma/
%{_kf6_qmldir}/org/kde/taskmanager/
%{_kf6_sharedir}/dbus-1/services/org.kde.KSplash.service
%{_kf6_sharedir}/dbus-1/services/org.kde.LogoutPrompt.service
%{_kf6_sharedir}/dbus-1/services/org.kde.Shutdown.service
%{_kf6_sharedir}/dbus-1/services/org.kde.fontinst.service
%{_kf6_sharedir}/dbus-1/services/org.kde.krunner.service
%{_kf6_sharedir}/dbus-1/services/org.kde.plasma.Notifications.service
%{_kf6_sharedir}/dbus-1/services/org.kde.runners.baloo.service
%{_kf6_sharedir}/dbus-1/services/org.kde.secretprompter.service
%{_kf6_sharedir}/dbus-1/system-services/org.kde.fontinst.service
%{_kf6_sharedir}/dbus-1/system.d/org.kde.fontinst.conf
%{_kf6_sharedir}/desktop-directories/
%{_kf6_sharedir}/kconf_update/
%{_kf6_sharedir}/kfontinst/
%{_kf6_sharedir}/kglobalaccel/org.kde.krunner.desktop
%dir %{_kf6_sharedir}/kio
%dir %{_kf6_sharedir}/kio/servicemenus
%{_kf6_sharedir}/kio/servicemenus/installfont.desktop
%{_kf6_sharedir}/kio_desktop/
%{_kf6_sharedir}/konqsidebartng/
%{_kf6_sharedir}/krunner/dbusplugins/plasma-runner-baloosearch.desktop
%{_kf6_sharedir}/kstyle/
%{_kf6_sharedir}/polkit-1/actions/org.kde.fontinst.policy
%{_kf6_sharedir}/solid/
%dir %{_kf6_sharedir}/timezonefiles/
%{_kf6_sharedir}/timezonefiles/timezones.json
%dir %{_kf6_sharedir}/xdg-desktop-portal/
%{_kf6_sharedir}/xdg-desktop-portal/kde-portals.conf
%dir %{_kf6_sharedir}/xdg-desktop-portal/portals/
%{_kf6_sharedir}/xdg-desktop-portal/portals/plasmanotify.portal
%{_libexecdir}/baloorunner
%{_libexecdir}/ksecretprompter
%{_kf6_libexecdir}/kauth/fontinst
%{_kf6_libexecdir}/kauth/fontinst_helper
%if %{with x11}
%{_kf6_libexecdir}/kauth/fontinst_x11
%endif
%{_libexecdir}/kfontprint
%{_libexecdir}/ksmserver-logout-greeter
%{_libexecdir}/plasma-changeicons
%{_libexecdir}/plasma-dbus-run-session-if-needed
%{_libexecdir}/plasma-fallback-session-restore
%{_libexecdir}/plasma-fallback-session-save
%{_libexecdir}/plasma-sourceenv.sh
%{_libexecdir}/plasma-startup-sound
%{_userunitdir}/plasma-baloorunner.service
%{_userunitdir}/plasma-core.target
%{_userunitdir}/plasma-gmenudbusmenuproxy.service
%{_userunitdir}/plasma-kcminit-phase1.service
%{_userunitdir}/plasma-kcminit.service
%{_userunitdir}/plasma-krunner.service
%{_userunitdir}/plasma-ksmserver.service
%{_userunitdir}/plasma-ksplash.service
%{_userunitdir}/plasma-plasmashell.service
%dir %{_userunitdir}/plasma-plasmashell.service.d/
%{_userunitdir}/plasma-plasmashell.service.d/waitforkded.conf
%{_userunitdir}/plasma-restoresession.service
%{_userunitdir}/plasma-startupsound.service
%if %{with x11}
%{_userunitdir}/plasma-workspace-{wayland,x11}.target
%else
%{_userunitdir}/plasma-workspace-wayland.target
%endif
%{_userunitdir}/plasma-workspace.target
%if %{with x11}
%{_userunitdir}/plasma-xembedsniproxy.service
%endif

%files libs
%license LICENSES/*
%{_kf6_libdir}/libbatterycontrol.so.*
%{_kf6_libdir}/libklipper.so.*
%{_kf6_libdir}/libklookandfeel.so.*
%{_kf6_libdir}/libkmpris.so.*
%{_kf6_libdir}/libkrdb.so
%{_kf6_libdir}/libkworkspace6.so.*
%{_kf6_libdir}/libnotificationmanager.so.*
%{_kf6_libdir}/libtaskmanager.so.*

%files devel
%license LICENSES/*
%{_includedir}/klookandfeel/
%{_includedir}/krdb/
%{_includedir}/kworkspace6/
%{_includedir}/notificationmanager/
%{_includedir}/taskmanager/
%{_kf6_libdir}/cmake/Krdb/
%{_kf6_libdir}/cmake/KRunnerAppDBusInterface/
%{_kf6_libdir}/cmake/KSMServerDBusInterface/
%{_kf6_libdir}/cmake/LibKLookAndFeel/
%{_kf6_libdir}/cmake/LibKWorkspace/
%{_kf6_libdir}/cmake/LibNotificationManager/
%{_kf6_libdir}/cmake/LibTaskManager/
%{_kf6_libdir}/libbatterycontrol.so
%{_kf6_libdir}/libklipper.so
%{_kf6_libdir}/libklookandfeel.so
%{_kf6_libdir}/libkworkspace6.so
%{_kf6_libdir}/libnotificationmanager.so
%{_kf6_libdir}/libtaskmanager.so
%{_kf6_sharedir}/dbus-1/interfaces/

%files -n plasma-session
%license LICENSES/*
%dir %{_datadir}/wayland-sessions/
%{_kf6_sharedir}/wayland-sessions/plasmawayland.desktop

%if %{with x11}
%files -n plasma-session-x11
%{_kf6_bindir}/startplasma-x11
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%{_kf6_sharedir}/xsessions/default.desktop
%{_kf6_sharedir}/xsessions/kde-plasma.desktop
%{_kf6_sharedir}/xsessions/plasma6.desktop
%endif

%files -n sddm-kde-config-openruyi
%dir %{_prefix}/lib/sddm/
%dir %{_prefix}/lib/sddm/sddm.conf.d/
%{_prefix}/lib/sddm/sddm.conf.d/10-plasma.conf

%changelog
%autochangelog
