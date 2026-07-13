# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

Name:           kde-cli-tools
Version:        6.7.1
Release:        %autorelease
Summary:        Additional CLI tools for KDE applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/kde-cli-tools.git
#!RemoteAsset:  sha256:056db6dd2d1761b7d005d27876f0afc798ab4b0768101f5208a87f510f87ee82
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Su) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)

# for kquitapp6
Requires:       kf6-kdbusaddons-tools

%description
Additional CLI tools for KDE applications and workspaces.

%install -a
# For xdg-su
ln -s %{_kf6_libexecdir}/kdesu %{buildroot}%{_kf6_bindir}/kdesu

# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --with-man --with-html --all-name --generate-subpackages

%files -f %{name}.lang
%doc %lang(en) %{_kf6_htmldir}/en/*
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_filetypes.desktop
%{_kf6_applicationsdir}/org.kde.keditfiletype.desktop
%{_kf6_applicationsdir}/org.kde.plasma.settings.open.desktop
%{_kf6_bindir}/kbroadcastnotification
%{_kf6_bindir}/kde-inhibit
%{_kf6_bindir}/kde-open{5,}
%{_kf6_bindir}/kdecp{5,}
%{_kf6_bindir}/kdemv{5,}
%{_kf6_bindir}/kdesu
%{_kf6_bindir}/keditfiletype{5,}
%{_kf6_bindir}/kinfo
%{_kf6_bindir}/kioclient{5,}
%{_kf6_bindir}/kmimetypefinder{5,}
%{_kf6_bindir}/kstart{5,}
%{_kf6_bindir}/ksvgtopng{5,}
%{_kf6_bindir}/plasma-open-settings
%{_kf6_libexecdir}/kdeeject
%{_kf6_libexecdir}/kdesu
%{_kf6_mandir}/man1/kdesu*
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_filetypes.so
%dir %{_kf6_sharedir}/zsh
%dir %{_kf6_sharedir}/zsh/site-functions
%{_kf6_sharedir}/zsh/site-functions/_kde-inhibit

%changelog
%autochangelog
