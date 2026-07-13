# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: kiritakekumi <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           plasma-login-manager
Version:        6.7.1
Release:        %autorelease
Summary:        QML based login manager from KDE
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause AND CC0-1.0 AND (GPL-2.0-only OR GPL-3.0-only)
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/plasma-login-manager.git
#!RemoteAsset:  sha256:ca82a14885af244706d2f15c780c5d1187ef471aa55ea8a74c0c81f9d17596a4
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
# Ship the Fedora/RPM-style PAM stack; "auto" detection aborts on unknown distros.
BuildOption(conf):  -DPAM_OS_CONFIGURATION=fedora

BuildRequires:  cmake >= 3.22
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  desktop-file-utils
BuildRequires:  systemd-rpm-macros
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickTest) >= %{qt6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6Screen) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LayerShellQt) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LibKLookAndFeel) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LibKWorkspace) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick) >= %{_plasma6_bugfix}

%{?systemd_requires}

%description
Plasma Login Manager (plasmalogin) is a QML based display and login manager
from KDE. It provides the graphical greeter and the session machinery used to
start Plasma on Wayland, along with a System Settings module to configure it.

%install -a
# Avoid clashing with sddm's DisplayManager D-Bus configuration file name
mv %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf \
   %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-plasmalogin.conf

# Home/state directory of the plasmalogin user (also (re)created at boot by tmpfiles)
mkdir -p %{buildroot}%{_localstatedir}/lib/plasmalogin

# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%pre
# Create the plasmalogin service account from the upstream sysusers.d file
%sysusers_create_package %{name} %{buildroot}%{_sysusersdir}/plasmalogin.conf

%post
%systemd_post plasmalogin.service
%systemd_user_post plasma-login.service plasma-login-kwin_wayland.service plasma-login-wayland.target plasma-wallpaper.service

%preun
%systemd_preun plasmalogin.service
%systemd_user_preun plasma-login.service plasma-login-kwin_wayland.service plasma-login-wayland.target plasma-wallpaper.service

%postun
%systemd_postun plasmalogin.service
%systemd_user_postun plasma-login.service plasma-login-kwin_wayland.service plasma-login-wayland.target plasma-wallpaper.service

%files -f %{name}.lang
%doc README.md
%license LICENSE LICENSE.* LICENSES/*
%{_prefix}/lib/pam.d/plasmalogin
%{_prefix}/lib/pam.d/plasmalogin-autologin
%{_prefix}/lib/pam.d/plasmalogin-greeter
%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-plasmalogin.conf
%{_bindir}/plasmalogin
%{_bindir}/plasma-login-wallpaper
%{_bindir}/startplasma-login-wayland
%{_libexecdir}/plasmalogin-helper
%{_libexecdir}/plasmalogin-helper-start-x11user
%{_libexecdir}/plasma-login-greeter
%{_tmpfilesdir}/plasmalogin.conf
%{_sysusersdir}/plasmalogin.conf
%{_unitdir}/plasmalogin.service
%{_userunitdir}/plasma-login.service
%{_userunitdir}/plasma-login-kwin_wayland.service
%{_userunitdir}/plasma-login-wayland.target
%{_userunitdir}/plasma-wallpaper.service
%dir %{_datadir}/plasmalogin
%{_datadir}/plasmalogin/scripts/
%attr(0750, plasmalogin, plasmalogin) %dir %{_localstatedir}/lib/plasmalogin
# System Settings module (kcm_plasmalogin)
%{_kf6_libexecdir}/kauth/kcmplasmalogin_authhelper
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_plasmalogin.so
%{_kf6_applicationsdir}/kcm_plasmalogin.desktop
%{_kf6_sharedir}/dbus-1/system-services/org.kde.kcontrol.kcmplasmalogin.service
%{_kf6_dbuspolicydir}/org.kde.kcontrol.kcmplasmalogin.conf
%{_kf6_sharedir}/polkit-1/actions/org.kde.kcontrol.kcmplasmalogin.policy

%changelog
%autochangelog
