# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           plasma-pa
Version:        6.7.1
Release:        %autorelease
Summary:        The Plasma Volume Manager
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/plasma-pa.git
#!RemoteAsset:  sha256:9740b99cef0e45b9ce1302ab4010370052bfe3dbaee6db75cbf467c10d30ebc8
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6PulseAudioQt)
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse)

Requires:       kf6-kirigami >= %{kf6_version}
Requires:       kirigami-addons
Requires:       pulseaudio

Suggests:       pipewire-pulseaudio

%description
A volume manager plasmoid superseding kmix.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --with-html --generate-subpackages

%files -f %{name}.lang
%doc %{_kf6_htmldir}/en/kcontrol/
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_pulseaudio.desktop
%{_kf6_debugdir}/plasmapa.categories
%{_kf6_libdir}/libplasma-volume.so.*
%{_kf6_plugindir}/kf6/kded/audioshortcutsservice.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.volume.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_pulseaudio.so
%dir %{_kf6_qmldir}/org/kde/plasma/private
%{_kf6_qmldir}/org/kde/plasma/private/volume/

%changelog
%autochangelog
