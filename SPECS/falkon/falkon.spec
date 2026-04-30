# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.19.0
%define qt6_version 6.9.0

Name:           falkon
Version:        25.12.3
Release:        %autorelease
Summary:        Modern web browser
License:        GPL-3.0-or-later
URL:            https://apps.kde.org/falkon
VCS:            git:https://invent.kde.org/network/falkon.git
#!RemoteAsset:  sha256:25f90957335058fff8536b511135e36d96e74c49fab45690be89b994015777b5
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebChannel) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineCore) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xcb-util)
# still fails to build with python deps
#BuildRequires:  cmake(PySide6)
#BuildRequires:  cmake(Shiboken6)
#BuildRequires:  python3-devel

Requires:       qt6-qtbase >= %{qt6_version}

Recommends:     falkon-kde

Provides:       qupzilla = %{version}-%{release}
Obsoletes:      qupzilla < %{version}-%{release}
Provides:       falkon-gnome-keyring = %{version}-%{release}
Obsoletes:      falkon-gnome-keyring < %{version}-%{release}

%description
Falkon is a web browser designed to well integrate with all
common Linux desktops like GNOME and KDE Plasma.
It supports current web standards and comes with many features,
such as an integrated ad blocker.

It was previously known as QupZilla.

%package        kde
Summary:        Plugin for tighter integration of KDE technologies
Requires:       falkon = %{version}-%{release}
Supplements:    (%{name} and plasma5-workspace)
Supplements:    (%{name} and plasma6-workspace)
Provides:       falkon-kwallet = %{version}-%{release}
Obsoletes:      falkon-kwallet < %{version}-%{release}
Provides:       qupzilla-kwallet = %{version}-%{release}
Obsoletes:      qupzilla-kwallet < %{version}-%{release}

%description    kde
Plugin for the Falkon browser that allows tighter integration of KDE technologies,
such as storing passwords in KWallet.

%prep -a

# The plugins are not installed if PySide is not present at build time.
find po/ -name "falkon_helloqml.po" -o -name "falkon_hellopython.po" -exec rm {} \;

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_kf6_appstreamdir}/org.kde.falkon.appdata.xml
%{_kf6_bindir}/falkon
%{_kf6_iconsdir}/hicolor/*/apps/falkon.*
%{_kf6_libdir}/libFalkonPrivate.so.*
%{_kf6_plugindir}/falkon/
%{_kf6_sharedir}/applications/org.kde.falkon.desktop
%{_kf6_sharedir}/bash-completion/
%{_kf6_sharedir}/falkon/
%exclude %{_kf6_plugindir}/falkon/KDEFrameworksIntegration.so

%files kde
%{_kf6_plugindir}/falkon/KDEFrameworksIntegration.so

%changelog
%autochangelog
