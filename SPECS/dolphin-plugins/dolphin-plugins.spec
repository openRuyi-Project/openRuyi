# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.19.0
%define qt6_version 6.9.0

Name:           dolphin-plugins
Version:        26.04.2
Release:        %autorelease
Summary:        Version control plugins for Dolphin
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/system/dolphin-plugins.git
#!RemoteAsset:  sha256:8c53ce19b2b910f087de42180c034dd9c087598d3b145815a3eba713006e22e7
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(DolphinVcs) >= 24.02.0
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

Recommends:     dolphin

%description
Dolphin file manager specific version control plugins that:
- Show the version state of a file by an emblem + color
- Provide a context menu with version control specific actions
- Provide context menu actions to mount ISO disk images

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_appstreamdir}/org.kde.dolphin-plugins.metainfo.xml
%{_kf6_configkcfgdir}/fileviewgitpluginsettings.kcfg
%{_kf6_configkcfgdir}/fileviewhgpluginsettings.kcfg
%{_kf6_configkcfgdir}/fileviewsvnpluginsettings.kcfg
%{_kf6_debugdir}/dolphingit.categories
%dir %{_kf6_plugindir}/dolphin
%dir %{_kf6_plugindir}/dolphin/vcs
%{_kf6_plugindir}/dolphin/vcs/fileviewbazaarplugin.so
%{_kf6_plugindir}/dolphin/vcs/fileviewdropboxplugin.so
%{_kf6_plugindir}/dolphin/vcs/fileviewgitplugin.so
%{_kf6_plugindir}/dolphin/vcs/fileviewhgplugin.so
%{_kf6_plugindir}/dolphin/vcs/fileviewsvnplugin.so
%dir %{_kf6_plugindir}/kf6/kfileitemaction
%{_kf6_plugindir}/kf6/kfileitemaction/makefileactions.so
%{_kf6_plugindir}/kf6/kfileitemaction/mountisoaction.so

%changelog
%autochangelog
