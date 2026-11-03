# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

%global __requires_exclude qt6qmlimport\\(org\\.kde\\.kinfocenter\\.private.*

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           kinfocenter
Version:        6.8.2
Release:        %autorelease
Summary:        Utility that provides information about a computer system
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/kinfocenter.git
#!RemoteAsset:  sha256:091599588b69a5cd994bffab6b068981a78cc76b76a44ea689a2a184ded01a2a
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
# For creating the post-install symlink
BuildRequires:  systemsettings
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Graphs) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds

Requires:       kf6-kcmutils >= %{kf6_version}
# needed for the fileindexermonitor
Requires:       kf6-baloo >= %{kf6_version}
# The executable is now a link to systemsettings
Requires:       systemsettings
# lspci is called by the PCI KCM
Requires:       pciutils
# GLX is always present
Requires:       /usr/bin/glxinfo
# Vulkan might not be needed
Requires:       (/usr/bin/vulkaninfo if libvulkan1)
# Plasma Wayland is always installed
Requires:       /usr/bin/wayland-info
# The "Firmware Security" page does fwupdmgr ... | aha | ...
Requires:       (aha if fwupd)

Recommends:      /usr/bin/xdpyinfo
# Note: Not available as /usr/bin/eglinfo yet (boo#1195695)
Recommends:     /usr/bin/eglinfo
# clinfo if OpenCL is installed
Requires:       (clinfo if libOpenCL1)
# dmidecode is used to show information on memory
Recommends:     dmidecode
# EDID kcm requires di-edid-decode
Recommends:     libdisplay-info-tools >= 0.2.0
# Temperature sensors
Recommends:     sensors

%description
KDE Utility that provides information about a computer system.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --with-html --generate-subpackages

%files -f %{name}.lang
%doc %lang(en) %{_kf6_htmldir}/en/kinfocenter/
%license LICENSES/*.txt
%{_libexecdir}/kinfocenter-vulkan-helper
%{_kf6_applicationsdir}/kcm_about-distro.desktop
%{_kf6_applicationsdir}/org.kde.kinfocenter.desktop
%{_kf6_appstreamdir}/org.kde.kinfocenter.appdata.xml
%{_kf6_bindir}/kinfocenter
%{_kf6_libdir}/libKInfoCenterInternal.so
%{_kf6_plugindir}/plasma/kcms/kcm_about-distro.so
%dir %{_kf6_plugindir}/plasma/kcms/kinfocenter/
%{_kf6_plugindir}/plasma/kcms/kinfocenter/*.so
%{_kf6_qmldir}/org/kde/kinfocenter/
%{_kf6_sharedir}/dbus-1/system-services/org.kde.kinfocenter.dmidecode.service
%{_kf6_dbuspolicydir}/org.kde.kinfocenter.dmidecode.conf
%dir %{_kf6_sharedir}/kinfocenter/
%dir %{_kf6_sharedir}/kinfocenter/edid
%dir %{_kf6_sharedir}/kinfocenter/network
%{_kf6_sharedir}/kinfocenter/edid/edid.sh
%{_kf6_sharedir}/kinfocenter/network/ip.sh
%{_kf6_sharedir}/kinfocenter/categories/
%{_kf6_sharedir}/kinfocenter/firmware_security/
%{_kf6_sharedir}/polkit-1/actions/org.kde.kinfocenter.dmidecode.policy
%{_kf6_libexecdir}/kauth/kinfocenter-dmidecode-helper
%{_libexecdir}/kinfocenter-*-helper

%changelog
%autochangelog
