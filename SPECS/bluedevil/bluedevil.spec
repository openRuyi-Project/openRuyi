# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Internal QML import
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.plasma\\.private\\.bluetooth.*

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           bluedevil
Version:        6.8.2
Release:        %autorelease
Summary:        Bluetooth Manager for KDE Plasma
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/bluedevil.git
#!RemoteAsset:  sha256:7ecd11f142790bf9e6e08b82539b373fe5f5e0778c90f33777c8a245f06929e2
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  shared-mime-info
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds
BuildRequires:  cmake(KF6BluezQt) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

# On top of bluez itself, bluez-obexd is needed for kio_obexftp and send/receive
Requires:       bluez
Requires:       kf6-bluez-qt >= %{kf6_version}
Requires:       kf6-kirigami >= %{kf6_version}

# For connecting A2DP profile
Recommends:     (pulseaudio-module-bluetooth if pulseaudio)
Supplements:    (bluez and plasma-workspace)

%description
Bluetooth daemon for KDE Plasma, handling connections.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --with-html --generate-subpackages

%files -f %{name}.lang
%doc README
%doc %{_kf6_htmldir}/en/kcontrol/
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_bluetooth.desktop
%{_kf6_applicationsdir}/org.kde.bluedevilsendfile.desktop
%{_kf6_applicationsdir}/org.kde.bluedevilwizard.desktop
%{_kf6_bindir}/bluedevil-sendfile
%{_kf6_bindir}/bluedevil-wizard
%{_kf6_configkcfgdir}/bluedevilglobalsettings.kcfg
%{_kf6_configkcfgdir}/filereceiver.kcfg
%{_kf6_debugdir}/bluedevil.categories
%{_kf6_notificationsdir}/bluedevil.notifyrc
%{_kf6_plugindir}/kf6/kded/bluedevil.so
%{_kf6_plugindir}/kf6/kio/kio_bluetooth.so
%{_kf6_plugindir}/kf6/kio/kio_obexftp.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.bluetooth.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_bluetooth.so
%dir %{_kf6_qmldir}/org/kde/plasma/private
%{_kf6_qmldir}/org/kde/plasma/private/bluetooth/
%dir %{_kf6_qmldir}/org/kde/bluedevil/
%{_kf6_qmldir}/org/kde/bluedevil/components/
%dir %{_kf6_sharedir}/bluedevilwizard
%{_kf6_sharedir}/bluedevilwizard/pin-code-database.xml
%{_kf6_sharedir}/mime/packages/bluedevil-mime.xml
%dir %{_kf6_sharedir}/remoteview
%{_kf6_sharedir}/remoteview/bluetooth-network.desktop

%changelog
%autochangelog
