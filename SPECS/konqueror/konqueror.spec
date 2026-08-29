# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.19.0
%define qt6_version 6.9.0

Name:           konqueror
Version:        26.04.2
Release:        %autorelease
Summary:        KDE File Manager and Browser
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/network/konqueror.git
#!RemoteAsset:  sha256:aa9a35f81fa1f30aac1d77b9008d074fb041b2a7c12319d1f8c9b194137e57de
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6Su) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6TextToSpeech) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(zlib)
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds

Requires:       webenginepart

Recommends:     konqueror-plugins
Recommends:     dolphin-part

%description
Konqueror allows you to manage your files and browse the web in a
unified interface.

%package     -n webenginepart
Summary:        KDE WebEngine web browser component

%description -n webenginepart
This package contains a HTML rendering engine for Konqueror using Qt web engine.

%package     -n konqueror-plugins
Summary:        KDE File Manager and Browser
Requires:       konqueror = %{version}

%description -n konqueror-plugins
These plugins extend the functionality of Konqueror.

%package        devel
Summary:        KDE Konqueror Libraries: Build Environment
Requires:       konqueror = %{version}
Obsoletes:      libkonq-devel < %{version}
Provides:       libkonq-devel = %{version}

%description    devel
Development package for the konqueror libraries.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --with-html --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%config %{_kf6_configdir}/autostart/konqy_preload.desktop
%{_kf6_sharedir}/kcontrol/
%{_kf6_applicationsdir}/bookmarks.desktop
%{_kf6_applicationsdir}/kcm_bookmarks.desktop
%{_kf6_applicationsdir}/kcm_speeddial.desktop
%{_kf6_applicationsdir}/kfmclient.desktop
%{_kf6_applicationsdir}/kfmclient_dir.desktop
%{_kf6_applicationsdir}/kfmclient_html.desktop
%{_kf6_applicationsdir}/kfmclient_war.desktop
%{_kf6_applicationsdir}/konqbrowser.desktop
%{_kf6_applicationsdir}/org.kde.konqueror.desktop
%{_kf6_applicationsdir}/speeddial.desktop
%{_kf6_appstreamdir}/org.kde.konqueror.appdata.xml
%{_kf6_bindir}/kfmclient
%{_kf6_bindir}/konqueror
%{_kf6_configdir}/konqautofiltersrc
%{_kf6_configdir}/useragenttemplatesrc
%{_kf6_configkcfgdir}/konqueror.kcfg
%{_kf6_datadir}/kbookmark/
%{_kf6_dbusinterfacesdir}/org.kde.Konqueror.Main.xml
%{_kf6_dbusinterfacesdir}/org.kde.Konqueror.MainWindow.xml
%{_kf6_debugdir}/konqueror.categories
%{_kf6_iconsdir}/hicolor/*/*/konqueror.*
%{_kf6_libdir}/libKF6Konq.so.*
%{_kf6_libdir}/libkonquerorprivate.so.*
%dir %{_kf6_plugindir}/konqueror_kcms
%{_kf6_plugindir}/konqueror_kcms/kcm_bookmarks.so
%{_kf6_plugindir}/konqueror_kcms/kcm_history.so
%{_kf6_plugindir}/konqueror_kcms/kcm_konq.so
%{_kf6_plugindir}/konqueror_kcms/kcm_performance.so
%{_kf6_plugindir}/konqueror_kcms/kcm_speeddial.so
%{_kf6_plugindir}/konqueror_kcms/khtml_*.so
%{_kf6_sharedir}/kcmcss/
%{_kf6_sharedir}/kconf_update/webenginepart.upd
%{_kf6_sharedir}/konqueror/

%files -n webenginepart
%{_kf6_iconsdir}/hicolor/*/*/webengine.*
%{_kf6_libdir}/libkwebenginepart.so
%{_kf6_plugindir}/kf6/parts/webenginepart.so
%{_kf6_sharedir}/webenginepart/

%files -n konqueror-plugins
%config %{_kf6_configdir}/konqsidebartngrc
%config %{_kf6_configdir}/translaterc
%{_kf6_bindir}/fsview
%{_kf6_bindir}/kcreatewebarchive
%{_kf6_configkcfgdir}/kcreatewebarchive.kcfg
%{_kf6_debugdir}/akregatorplugin.categories
%{_kf6_debugdir}/fsview.categories
%{_kf6_iconsdir}/*/*/actions/babelfish.png
%{_kf6_iconsdir}/*/*/actions/imagegallery.png
%{_kf6_iconsdir}/*/*/actions/webarchiver.png
%{_kf6_iconsdir}/hicolor/*/apps/fsview.png
%{_kf6_libdir}/libKF6KonqSettings.so.*
%{_kf6_libdir}/libkonqsidebarplugin.so.*
%{_kf6_plugindir}/akregatorkonqfeedicon.so
%{_kf6_plugindir}/autorefresh.so
%{_kf6_plugindir}/babelfishplugin.so
%dir %{_kf6_plugindir}/dolphinpart
%dir %{_kf6_plugindir}/dolphinpart/kpartplugins
%{_kf6_plugindir}/dolphinpart/kpartplugins/dirfilterplugin.so
%{_kf6_plugindir}/dolphinpart/kpartplugins/kimgallery.so
%{_kf6_plugindir}/dolphinpart/kpartplugins/konq_shellcmdplugin.so
%dir %{_kf6_plugindir}/kf6/kfileitemaction/
%{_kf6_plugindir}/kf6/kfileitemaction/akregatorplugin.so
%{_kf6_plugindir}/kf6/kio/bookmarks.so
%{_kf6_plugindir}/kf6/parts/fsviewpart.so
%{_kf6_plugindir}/kf6/parts/konq_sidebar.so
%dir %{_kf6_plugindir}/kf6/thumbcreator
%{_kf6_plugindir}/kf6/thumbcreator/webarchivethumbnail.so
# webenginepart/kpartplugins/khtmlsettingspluginwebenginepart_kpartplugins.so is a symlink to this file
%{_kf6_plugindir}/khtmlsettingsplugin.so
%dir %{_kf6_plugindir}/konqueror
%dir %{_kf6_plugindir}/konqueror/kpartplugins
%{_kf6_plugindir}/konqueror/kpartplugins/searchbarplugin.so
%{_kf6_plugindir}/konqueror/sidebar/
%{_kf6_plugindir}/konqueror_kget_browser_integration.so
%{_kf6_plugindir}/temporarysavedir.so
%{_kf6_plugindir}/uachangerplugin.so
%{_kf6_plugindir}/webarchiverplugin.so
%{_kf6_plugindir}/webenginepart/
%{_kf6_sharedir}/akregator/
%{_kf6_sharedir}/kio_bookmarks/
%{_kf6_sharedir}/konqsidebartng/

%files devel
%{_kf6_cmakedir}/KF6Konq/
%{_kf6_includedir}/*konq*.h
%{_kf6_includedir}/selectorinterface.h
%{_kf6_libdir}/libKF6Konq.so
%{_kf6_libdir}/libKF6KonqSettings.so
%{_kf6_libdir}/libkonqsidebarplugin.so

%changelog
%autochangelog
