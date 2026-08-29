# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.19.0
%define qt6_version 6.9.0

Name:           konsole
Version:        26.04.2
Release:        %autorelease
Summary:        KDE Terminal
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/utilities/konsole.git
#!RemoteAsset:  sha256:d81a696d6a316d0c8fabe3cecd83783f656ee97c70ced89513b3fd16e9d216ac
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Pty) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  pkgconfig(icu-i18n) >= 61.0
BuildRequires:  pkgconfig(icu-uc) >= 61.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds

Requires:       konsole-part = %{version}
Provides:       konsole-zsh-completion = %{version}
Obsoletes:      konsole-zsh-completion < %{version}

%description
Konsole is a terminal emulator for the K Desktop Environment.

%package        part
Summary:        KDE Terminal
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    part
Konsole is a terminal emulator for the K Desktop Environment.
This package provides KPart of the Konsole application.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --with-man --with-html --generate-subpackages

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_konsole
%{_kf6_applicationsdir}/org.kde.konsole.desktop
%{_kf6_appstreamdir}/org.kde.konsole.appdata.xml
%{_kf6_bindir}/konsole
%{_kf6_bindir}/konsoleprofile
%dir %{_kf6_plugindir}/konsoleplugins
%{_kf6_plugindir}/konsoleplugins/konsole_quickcommandsplugin.so
%{_kf6_plugindir}/konsoleplugins/konsole_sshmanagerplugin.so
%{_kf6_libdir}/libkonsoleapp.so.*
%dir %{_kf6_sharedir}/kio
%dir %{_kf6_sharedir}/kio/servicemenus
%{_kf6_sharedir}/kio/servicemenus/konsolerun.desktop
%{_kf6_sharedir}/kglobalaccel/org.kde.konsole.desktop

%files part
%{_kf6_debugdir}/konsole.categories
%{_kf6_libdir}/libkonsoleprivate.so.*
%{_kf6_notificationsdir}/konsole.notifyrc
%dir %{_kf6_plugindir}/kf6/parts
%{_kf6_plugindir}/kf6/parts/konsolepart.so
%exclude %{_kf6_htmldir}/en/konsole/

%changelog
%autochangelog
