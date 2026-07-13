# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kconfigwidgets
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kconfigwidgets
Version:        6.27.0
Release:        %autorelease
Summary:        Widgets for configuration dialogs
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kconfigwidgets
#!RemoteAsset:  sha256:404ed0606dfb13cc44c36deaf5f880eeec75018ae878125dabf83f32efeb0a7f
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Codecs) >= %{_kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

%package        devel
Summary:        Widgets for configuration dialogs: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Codecs) >= %{_kf6_version}
Requires:       cmake(KF6ColorScheme) >= %{_kf6_version}
Requires:       cmake(KF6Config) >= %{_kf6_version}
Requires:       cmake(KF6WidgetsAddons) >= %{_kf6_version}

%description    devel
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings. Development files.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kconfigwidgets.categories
%{_kf6_debugdir}/kconfigwidgets.renamecategories
%{_kf6_sharedir}/locale/*/kf6_entry.desktop
%{_kf6_libdir}/libKF6ConfigWidgets.so.*

%files devel
%{_kf6_cmakedir}/KF6ConfigWidgets/
%{_kf6_includedir}/KConfigWidgets/
%{_kf6_libdir}/libKF6ConfigWidgets.so
%{_kf6_plugindir}/designer/kconfigwidgets6widgets.so

%changelog
%autochangelog
