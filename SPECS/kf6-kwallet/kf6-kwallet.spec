# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kwallet
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kwallet
Version:        6.22.0
Release:        %autorelease
Summary:        Safe desktop-wide storage for passwords
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kwallet
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  libgcrypt-devel >= 1.5.0
BuildRequires:  gpgmepp-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6ColorScheme) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{_kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{_kf6_version}
BuildRequires:  cmake(KF6Service) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{_kf6_version}
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds

%description
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

%package     -n kwalletd6
Summary:        Safe desktop-wide storage for passwords
Requires:       kf6-kwallet >= %{version}
Recommends:     kf6-kwallet-tools
# kwalletd6 ships a compat org.kde.kwalletd5.service file. It needs to replace
# kwalletd5 to keep using plasma5 with KF6-based apps
Provides:       kwalletd5 = %{version}-%{release}
Obsoletes:      kwalletd5 < %{version}
Obsoletes:      kwalletd5-lang < %{version}

%description -n kwalletd6
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

%package        devel
Summary:        Safe desktop-wide storage for passwords
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description    devel
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE workspaces.
* The kwalletd used to safely store the passwords on KDE work spaces.
Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name}6 --with-qt --all-name --generate-subpackages

%files -f %{name}6.lang
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kwallet.categories
%{_kf6_debugdir}/kwallet.renamecategories
%{_kf6_libdir}/libKF6Wallet.so.*
%{_kf6_libdir}/libKF6WalletBackend.so.*
%{_kf6_bindir}/kwallet-query
%{_kf6_mandir}/man1/kwallet-query.1%{?ext_man}

%files -n kwalletd6
%{_kf6_applicationsdir}/org.kde.ksecretd.desktop
%{_kf6_bindir}/ksecretd
%{_kf6_bindir}/kwalletd6
%{_kf6_notificationsdir}/ksecretd.notifyrc
%{_kf6_sharedir}/dbus-1/services/org.freedesktop.impl.portal.desktop.kwallet.service
%{_kf6_sharedir}/dbus-1/services/org.kde.kwalletd5.service
%{_kf6_sharedir}/dbus-1/services/org.kde.kwalletd6.service
%{_kf6_sharedir}/dbus-1/services/org.kde.secretservicecompat.service
%dir %{_kf6_sharedir}/xdg-desktop-portal
%dir %{_kf6_sharedir}/xdg-desktop-portal/portals
%{_kf6_sharedir}/xdg-desktop-portal/portals/kwallet.portal

%files devel
%{_kf6_libdir}/libKF6Wallet.so
%{_kf6_cmakedir}/KF6Wallet/
%{_kf6_includedir}/KWallet/
%{_kf6_dbusinterfacesdir}/kf6_org.kde.KWallet.xml

%changelog
%autochangelog
