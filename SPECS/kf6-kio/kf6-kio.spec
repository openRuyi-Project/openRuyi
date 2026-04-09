# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kio
# Full KF6 version (e.g. 6.21.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kio
Version:        6.22.0
Release:        %autorelease
Summary:        Network transparent access to files and data
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kio
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  attr-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Archive) >= %{_kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{_kf6_version}
BuildRequires:  cmake(KF6Bookmarks) >= %{_kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{_kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{_kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{_kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{_kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{_kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{_kf6_version}
BuildRequires:  cmake(KF6KDED) >= %{_kf6_version}
BuildRequires:  cmake(KF6Service) >= %{_kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{_kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{_kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds
Requires:       kf6-kded >= %{_kf6_version}
# For discrete GPU discovery
Recommends:     switcheroo-control

%description
This framework implements almost all the file management functions you
will ever need. In fact, the KDE file manager (Dolphin) and the KDE
file dialog also uses this to provide its network-enabled file management.

%package        doc
Summary:        HTML documentation for KIO

%description    doc
This package contains documentation for the KIO framework.

%package        devel
Summary:        Network transparent access to files and data
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Bookmarks) >= %{_kf6_version}
Requires:       cmake(KF6Completion) >= %{_kf6_version}
Requires:       cmake(KF6Config) >= %{_kf6_version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_version}
Requires:       cmake(KF6ItemViews) >= %{_kf6_version}
Requires:       cmake(KF6JobWidgets) >= %{_kf6_version}
Requires:       cmake(KF6Service) >= %{_kf6_version}
Requires:       cmake(KF6Solid) >= %{_kf6_version}
Requires:       cmake(KF6WindowSystem) >= %{_kf6_version}
Requires:       cmake(KF6XmlGui) >= %{_kf6_version}
Requires:       cmake(Qt6Concurrent) >= %{qt6_version}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Network) >= %{qt6_version}

%description    devel
This framework implements almost all the file management functions you
will ever need. In fact, the KDE file manager (Dolphin) and the KDE
file dialog also uses this to provide its network-enabled file management.
Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name}6 --with-qt --all-name --generate-subpackages

%files -f %{name}6.lang
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/ktelnetservice6.desktop
%{_kf6_applicationsdir}/org.kde.kiod6.desktop
%{_kf6_bindir}/ktelnetservice6
%{_kf6_bindir}/ktrash6
%{_kf6_datadir}/searchproviders/
%{_kf6_debugdir}/kio.categories
%{_kf6_debugdir}/kio.renamecategories
%{_kf6_libdir}/libkuriikwsfiltereng_private.so
%{_kf6_libexecdir}/kiod6
%{_kf6_libexecdir}/kioexec
%{_kf6_libexecdir}/kioworker
%{_kf6_plugindir}/designer/kio6widgets.so
%{_kf6_plugindir}/kf6/kded/remotenotifier.so
%{_kf6_plugindir}/kf6/kio/kio_file.so
%{_kf6_plugindir}/kf6/kio/kio_ftp.so
%{_kf6_plugindir}/kf6/kio/kio_ghelp.so
%{_kf6_plugindir}/kf6/kio/kio_help.so
%{_kf6_plugindir}/kf6/kio/kio_http.so
%{_kf6_plugindir}/kf6/kio/kio_remote.so
%{_kf6_plugindir}/kf6/kio/kio_trash.so
%dir %{_kf6_plugindir}/kf6/kiod
%{_kf6_plugindir}/kf6/kiod/kioexecd.so
%{_kf6_plugindir}/kf6/kiod/kpasswdserver.so
%{_kf6_plugindir}/kf6/kiod/kssld.so
%dir %{_kf6_plugindir}/kf6/kio_dnd
%{_kf6_plugindir}/kf6/kio_dnd/dropintonewfolder.so
%{_kf6_plugindir}/kf6/urifilters/
%{_kf6_sharedir}/dbus-1/services/org.kde.kiod6.service
%{_kf6_sharedir}/dbus-1/services/org.kde.kioexecd6.service
%{_kf6_sharedir}/dbus-1/services/org.kde.kpasswdserver6.service
%{_kf6_sharedir}/dbus-1/services/org.kde.kssld6.service
%{_kf6_libdir}/libKF6KIOCore.so.*
%{_kf6_libdir}/libKF6KIOFileWidgets.so.*
%{_kf6_libdir}/libKF6KIOGui.so.*
%{_kf6_libdir}/libKF6KIOWidgets.so.*

%files doc
%{_kf6_htmldir}/*

%files devel
%{_kf6_cmakedir}/KF6KIO/
%{_kf6_includedir}/KIO/
%{_kf6_includedir}/KIOCore/
%{_kf6_includedir}/KIOFileWidgets/
%{_kf6_includedir}/KIOGui/
%{_kf6_includedir}/KIOWidgets/
%{_kf6_libdir}/libKF6KIOCore.so
%{_kf6_libdir}/libKF6KIOFileWidgets.so
%{_kf6_libdir}/libKF6KIOGui.so
%{_kf6_libdir}/libKF6KIOWidgets.so
%{_kf6_sharedir}/kdevappwizard/templates/kioworker6.tar.bz2

%changelog
%autochangelog
