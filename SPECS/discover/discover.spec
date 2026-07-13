# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

%bcond fwupd 0
%bcond flatpak 0

Name:           discover
Version:        6.7.1
Release:        %autorelease
Summary:        Software store for the KDE Plasma desktop
License:        GPL-2.0-only AND GPL-3.0-only AND GPL-3.0-or-later
URL:            https://apps.kde.org/discover/
VCS:            git:https://invent.kde.org/plasma/discover.git
#!RemoteAsset:  sha256:e9ea51658dbc14178bd8a6470c287c5259b6276e0012b4faff7ea781e76ba2ba
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(AppStreamQt) >= 1.0.0
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Attica) >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebView) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  cmake(packagekitqt6) >= 1.1.3
BuildRequires:  kf6-kitemmodels
%if %{with fwupd}
BuildRequires:  pkgconfig(fwupd) >= 1.9.4
%endif
#BuildRequires:  pkgconfig(libmarkdown) >= 3.0

Requires:       kf6-kdeclarative >= %{kf6_version}
Requires:       kf6-kirigami >= %{kf6_version}
Requires:       kf6-kuserfeedback >= %{kf6_version}
Requires:       kirigami-addons
Requires:       qt6-qtdeclarative >= %{qt6_version}

Recommends:     discover-backend-flatpak
Recommends:     discover-backend-fwupd
Recommends:     discover-backend-packagekit
Recommends:     discover-notifier

%description
Discover is a graphical software manager for the KDE Plasma desktop. It helps users to find software they might want easily and quickly.

By allowing to navigate a software library by search, categories, top lists along with detailed application information including screenshots and reviews, users can more quickly find applications that suit their needs.

%package        backend-packagekit
Summary:        PackageKit Backend for Discover
Requires:       PackageKit
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       appstream

%description    backend-packagekit
A plugin for Discover to support management of system packages and repositories
using PackageKit.

%if %{with flatpak}
%package        backend-flatpak
Summary:        Flatpak Backend for Discover
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       flatpak

%description    backend-flatpak
A plugin for Discover to support installation and management of Flatpak
applications and repositories.
%endif

%if %{with fwupd}
%package        backend-fwupd
Summary:        fwupd Backend for Discover
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    backend-fwupd
A plugin for Discover to support updates of system firmware using fwupd.
%endif

%package        notifier
Summary:        Update notifier for KDE Software Manager
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    notifier
This is a notifier for Discover to inform the user that updates are available and allows the
user to install them using Discover.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

# Even without the snap backend, this is installed...
rm %{buildroot}%{_kf6_applicationsdir}/org.kde.discover.snap.desktop

%files -f %{name}.lang
%license LICENSES/*
%dir %{_kf6_plugindir}/discover/
%{_kf6_applicationsdir}/org.kde.discover.desktop
%{_kf6_applicationsdir}/org.kde.discover.urlhandler.desktop
%{_kf6_appstreamdir}/org.kde.discover.appdata.xml
%{_kf6_bindir}/plasma-discover
%{_kf6_debugdir}/discover.categories
%{_kf6_iconsdir}/hicolor/*/apps/plasmadiscover.*
%{_kf6_kxmlguidir}/plasmadiscover/
%{_kf6_libdir}/plasma-discover/
%{_kf6_notificationsdir}/discoverabstractnotifier.notifyrc
%{_kf6_plugindir}/discover/kns-backend.so
%dir %{_kf6_sharedir}/libdiscover
%dir %{_kf6_sharedir}/libdiscover/categories

%files backend-packagekit
%license LICENSES/*
%{_kf6_plugindir}/discover/packagekit-backend.so
%{_kf6_sharedir}/libdiscover/categories/packagekit-backend-categories.xml
%{_kf6_appstreamdir}/org.kde.discover.packagekit.appdata.xml

%if %{with flatpak}
%files backend-flatpak
%license LICENSES/*
%{_kf6_plugindir}/discover/flatpak-backend.so
%{_kf6_sharedir}/libdiscover/categories/flatpak-backend-categories.xml
%{_kf6_appstreamdir}/org.kde.discover.flatpak.appdata.xml
%{_kf6_applicationsdir}/org.kde.discover.flatpak.desktop
%{_kf6_iconsdir}/hicolor/scalable/apps/flatpak-discover.svg
%endif

%if %{with fwupd}
%files backend-fwupd
%license LICENSES/*
%{_kf6_plugindir}/discover/fwupd-backend.so
%endif

%files notifier
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_updates.desktop
%dir %{_kf6_plugindir}/discover-notifier
%{_kf6_plugindir}/discover-notifier/DiscoverPackageKitNotifier.so
%if %{with flatpak}
%{_kf6_plugindir}/discover-notifier/FlatpakNotifier.so
%endif
%{_kf6_configdir}/autostart/org.kde.discover.notifier.desktop
%{_kf6_applicationsdir}/org.kde.discover.notifier.desktop
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_updates.so
%{_libexecdir}/DiscoverNotifier

%changelog
%autochangelog
