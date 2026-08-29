# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fcitx5-configtool
Version:        5.1.13
Release:        %autorelease
Summary:        Configuration tools used by fcitx5
License:        GPL-2.0-or-later
URL:            https://github.com/fcitx/fcitx5-configtool
#!RemoteAsset:  sha256:994ea34888b97018cff7d5556f0434a0e00f90e1bee49ba4dd6f2e8c4ccc28eb
Source0:        https://download.fcitx-im.org/fcitx5/fcitx5-configtool/fcitx5-configtool-%{version}.tar.zst
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  ninja
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(Fcitx5Qt6DBusAddons)
BuildRequires:  cmake(Fcitx5Utils)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)

Requires:       qt6-qtsvg

%description
Configuration tools used by fcitx5.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%install -a
%find_lang %{name} --generate-subpackages
%find_lang kcm_fcitx5

%files -f %{name}.lang -f kcm_fcitx5.lang
%license LICENSES/GPL-2.0-or-later.txt
%{_bindir}/fcitx5-config-qt
%{_bindir}/kbd-layout-viewer5
%{_bindir}/fcitx5-migrator
%{_bindir}/fcitx5-plasma-theme-generator
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_fcitx5.so
%{_libdir}/libFcitx5Migrator.so.1
%{_libdir}/libFcitx5Migrator.so.5*
%{_datadir}/applications/org.fcitx.fcitx5-config-qt.desktop
%{_datadir}/applications/kbd-layout-viewer5.desktop
%{_datadir}/applications/kcm_fcitx5.desktop
%{_datadir}/applications/org.fcitx.fcitx5-migrator.desktop

%files devel
%{_libdir}/libFcitx5Migrator.so

%changelog
%autochangelog
