# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           kde-gtk-config
Version:        6.5.5
Release:        %autorelease
Summary:        Daemon for GTK2 and GTK3 Applications Appearance Under KDE
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/kde-gtk-config.git
#!RemoteAsset:  sha256:666b4a5ed1fcb969c98c102b5477c351d073422d4fa80eb84a41b007d9d9885a
Source:         https://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  gsettings-desktop-schemas
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  cmake(KDecoration3) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(x11)
# Needed for syncing GTK+ settings

Requires:       gsettings-desktop-schemas

Recommends:     xsettingsd
Recommends:     kde-gtk-config6-gtk3
Suggests:       gtk2-metatheme-breeze
Suggests:       gtk3-metatheme-breeze
Supplements:    (plasma-workspace and libgtk-2_0-0)
Supplements:    (plasma-workspace and libgtk-3-0)

Provides:       kde-gtk-config = %{version}-%{release}
Obsoletes:      kde-gtk-config < %{version}-%{release}

%description
kde-gtk-config is a KDED module which configures GTK2 and GTK3 applications
appearance under KDE.

%package        gtk3
Summary:        GTK3 Preview Helper for the GTK Configuration
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gtk3
This package contains a helper application that allows previewing
the GTK3 application style from within the application style KCM

%install -a

# E: env-script-interpreter
sed -i 's#/usr/bin/env sh$#/usr/bin/sh#' %{buildroot}%{_kf6_sharedir}/kconf_update/remove_window_decorations_from_gtk_css.sh

%files
%license LICENSES/*
%dir %{_kf6_libdir}/gtk-3.0/
%dir %{_kf6_libdir}/gtk-3.0/modules/
%{_kf6_debugdir}/kde-gtk-config.categories
%{_kf6_libdir}/gtk-3.0/modules/libcolorreload-gtk-module.so
%{_kf6_libdir}/gtk-3.0/modules/libwindow-decorations-gtk-module.so
%{_kf6_libdir}/kconf_update_bin/gtk_theme
%{_kf6_libdir}/kconf_update_bin/remove_deprecated_gtk4_option_v2
%{_kf6_plugindir}/kf6/kded/gtkconfig.so
%{_kf6_sharedir}/kcm-gtk-module/
%{_kf6_sharedir}/kconf_update/gtkconfig.upd
%{_kf6_sharedir}/kconf_update/remove_window_decorations_from_gtk_css.sh

%files gtk3
%license LICENSES/*
%dir %{_kf6_sharedir}/themes/Breeze/
%{_kf6_sharedir}/themes/Breeze/window_decorations.css
%{_libexecdir}/gtk3_preview

%changelog
%autochangelog
