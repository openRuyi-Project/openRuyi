# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           plasma-sdk
Version:        6.7.1
Release:        %autorelease
Summary:        Plasma SDK
License:        GPL-2.0-only AND LGPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/plasma-sdk.git
#!RemoteAsset:  sha256:3d5e8980ef066eb5405cb5be1e000e89e72e17da3a1124fffbaf022d3d3d0c14
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-breeze-icons
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma5Support) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds

Requires:       bash
Requires:       kf6-kirigami >= %{kf6_version}

Provides:       plasmaengineexplorer = %{version}
Obsoletes:      plasmaengineexplorer < %{version}

Conflicts:      plasmate

%description
Plasma SDK taylored for development of Plasma components,
such as Widgets, Runners, Dataengines.

%install -a
mkdir -p %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/apps/
cp -L %{_kf6_iconsdir}/breeze/apps/22/plasma-symbolic.svg %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/apps/plasma.svg
cp -L %{_kf6_iconsdir}/breeze/apps/48/cuttlefish.svg %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/apps/
cp -L %{_kf6_iconsdir}/breeze/actions/22/tools-wizard.svg %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/apps/

# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/iconexplorer
%{_kf6_bindir}/plasmaengineexplorer
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_kqml
%{_datadir}/zsh/site-functions/_plasmoidviewer
%{_kf6_applicationsdir}/org.kde.iconexplorer.desktop
%{_kf6_applicationsdir}/org.kde.plasma.lookandfeelexplorer.desktop
%{_kf6_applicationsdir}/org.kde.plasma.themeexplorer.desktop
%{_kf6_applicationsdir}/org.kde.plasmaengineexplorer.desktop
%{_kf6_applicationsdir}/org.kde.plasmoidviewer.desktop
%{_kf6_appstreamdir}/org.kde.plasma.iconexplorer.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasmaengineexplorer.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasmoidviewer.appdata.xml
%{_kf6_bindir}/kqml
%{_kf6_bindir}/lookandfeelexplorer
%{_kf6_bindir}/plasmathemeexplorer
%{_kf6_bindir}/plasmoidviewer
%{_kf6_iconsdir}/*/*/*/*.*
%dir %{_kf6_plasmadir}/shells
%{_kf6_plasmadir}/shells/org.kde.plasma.plasmoidviewershell/
%dir %{_kf6_plugindir}/kf6/ktexteditor/
%{_kf6_plugindir}/kf6/ktexteditor/iconexplorerplugin.so
%{_mandir}/man1/kqml.1%{?ext_man}
%{_mandir}/man1/plasmaengineexplorer.1%{?ext_man}
%{_mandir}/man1/plasmoidviewer.1%{?ext_man}
%{_mandir}/*/man1/kqml.1%{?ext_man}
%{_mandir}/*/man1/plasmaengineexplorer.1%{?ext_man}
%{_mandir}/*/man1/plasmoidviewer.1%{?ext_man}

%changelog
%autochangelog
