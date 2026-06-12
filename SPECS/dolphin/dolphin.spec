# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.19.0
%define plasma6_version 5.27.80
%define qt6_version 6.9.0

Name:           dolphin
Version:        26.04.2
Release:        %autorelease
Summary:        KDE File Manager
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/system/dolphin.git
#!RemoteAsset:  sha256:c7e90beb8ce13aea091494ae7ddfabde999b1297986a596403828010bec59346
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6Baloo) >= %{kf6_version}
BuildRequires:  cmake(KF6BalooWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6MultimediaWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(packagekitqt6)
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds

Requires:       dolphin-part = %{version}-%{release}
Requires:       kf6-baloo-kioslaves >= %{kf6_version}
Recommends:     kio-extras
Recommends:     konsole-part

Provides:       dolphin-zsh-completion = %{version}
Obsoletes:      dolphin-zsh-completion < %{version}

%description
This package contains the default file manager of KDE Workspaces.

%package        part
Summary:        KDE File Manager

%description    part
This package contains the libraries used by Dolphin and Konqueror.

%package        devel
Summary:        KDE File Manager
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description    devel
This package contains the libraries used by Dolphin and Konqueror.

%install -a
# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
rm -rf $RPM_BUILD_ROOT%{_mandir}/*@*
rm -rf $RPM_BUILD_ROOT%{_kf6_htmldir}/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --with-man --with-html --generate-subpackages

# ZSH completion script prevents running dolphin <tab> to open the application in the selected folder
rm %{buildroot}%{_datadir}/zsh/site-functions/_dolphin
ln -sf ../applications/org.kde.dolphin.desktop %{buildroot}%{_kf6_sharedir}/kglobalaccel/org.kde.dolphin.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.dolphin.desktop
%{_kf6_appstreamdir}/org.kde.dolphin.appdata.xml
%{_kf6_bindir}/dolphin
%{_kf6_bindir}/servicemenuinstaller
%{_kf6_configkcfgdir}/dolphin_*.kcfg
%{_kf6_dbusinterfacesdir}/org.freedesktop.FileManager1.xml
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.dolphin.svg
%dir %{_kf6_libdir}/kconf_update_bin
%{_kf6_libdir}/kconf_update_bin/dolphin_25.04_update_statusandlocationbarssettings
%{_kf6_libdir}/kconf_update_bin/dolphin_update_splitviewsettings
%{_kf6_sharedir}/dbus-1/services/org.kde.dolphin.FileManager1.service
%{_kf6_sharedir}/kconf_update/dolphin_detailsmodesettings.upd
%{_kf6_sharedir}/kconf_update/dolphin_replace_view_mode_with_view_settings_in_toolbar.py
%{_kf6_sharedir}/kconf_update/dolphin_replace_view_mode_with_view_settings_in_toolbar.upd
%{_kf6_sharedir}/kconf_update/dolphin_statusandlocationbarssettings.upd
%dir %{_kf6_sharedir}/kglobalaccel
%{_kf6_sharedir}/kglobalaccel/org.kde.dolphin.desktop
%{_userunitdir}/plasma-dolphin.service
%{_kf6_libdir}/libdolphinvcs.so.*

%files part
%{_kf6_debugdir}/dolphin.categories
%{_kf6_knsrcfilesdir}/servicemenu.knsrc
%{_kf6_libdir}/libdolphinprivate.so.*
%dir %{_kf6_plugindir}/dolphin
%dir %{_kf6_plugindir}/dolphin/kcms
%{_kf6_plugindir}/dolphin/kcms/kcm_dolphin*.so
%dir %{_kf6_plugindir}/kf6/kfileitemaction/
%{_kf6_plugindir}/kf6/kfileitemaction/hidefileitemaction.so
%{_kf6_plugindir}/kf6/kfileitemaction/movetonewfolderitemaction.so
%{_kf6_plugindir}/kf6/kfileitemaction/setfoldericonitemaction.so
%{_kf6_plugindir}/kf6/parts/dolphinpart.so
%{_kf6_sharedir}/dolphin/dolphinpartactions.desktop
%dir %{_kf6_sharedir}/dolphin

%files devel
%{_includedir}/Dolphin/
%{_includedir}/dolphin_export.h
%{_includedir}/dolphinvcs_export.h
%{_kf6_cmakedir}/DolphinVcs/
%{_kf6_libdir}/libdolphinvcs.so

%changelog
%autochangelog
