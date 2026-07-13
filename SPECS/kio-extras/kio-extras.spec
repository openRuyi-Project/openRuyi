# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.19.0
%define plasma6_version 5.27.80
%define qt6_version 6.9.0

Name:           kio-extras
Version:        26.04.2
Release:        %autorelease
Summary:        Additional KIO slaves for KDE applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/utilities/kio-extras.git
#!RemoteAsset:  sha256:af4941af624f883891d33701aa0ce4216d6de114db3e4a250099c52d3d42acaa
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  gperf
BuildRequires:  libmtp-devel
BuildRequires:  libssh-devel
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KDSoap-qt6)
BuildRequires:  cmake(KDSoapWSDiscoveryClient)
BuildRequires:  cmake(KExiv2Qt6)
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DNSSD) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(Microsoft.GSL)
BuildRequires:  cmake(PlasmaActivities) >= %{plasma6_version}
BuildRequires:  cmake(PlasmaActivitiesStats) >= %{plasma6_version}
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(OpenEXR) >= 3.0
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(taglib)

Requires:       qt6-qtbase >= %{qt6_version}

Recommends:     kf6-kimageformats >= %{kf6_version}
Recommends:     qt6-imageformats >= %{qt6_version}

%description
Additional KIO-slaves for KDE applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --with-html --all-name --generate-subpackages

%files -f %{name}.lang
%doc %lang(en) %{_kf6_htmldir}/en/kcontrol6/
%doc %lang(en) %{_kf6_htmldir}/en/kioworker6/
%license LICENSES/*
%{_datadir}/mime/packages/org.kde.kio.smb.xml
%{_kf6_applicationsdir}/*.desktop
%{_kf6_configkcfgdir}/jpegcreatorsettings5.kcfg
%{_kf6_debugdir}/kio-extras.categories
%{_kf6_debugdir}/kio-extras.renamecategories
%{_kf6_libexecdir}/smbnotifier
%dir %{_kf6_plugindir}/kf6/kded/
%{_kf6_plugindir}/kf6/kded/filenamesearchmodule.so
%{_kf6_plugindir}/kf6/kded/smbwatcher.so
%{_kf6_plugindir}/kf6/kded/wpad-detector.so
%dir %{_kf6_plugindir}/kf6/kfileitemaction
%{_kf6_plugindir}/kf6/kfileitemaction/forgetfileitemaction.so
%{_kf6_plugindir}/kf6/kfileitemaction/kactivitymanagerd_fileitem_linking_plugin.so
%dir %{_kf6_plugindir}/kf6/kio
%{_kf6_plugindir}/kf6/kio/activities.so
%{_kf6_plugindir}/kf6/kio/afc.so
%{_kf6_plugindir}/kf6/kio/archive.so
%{_kf6_plugindir}/kf6/kio/filter.so
%{_kf6_plugindir}/kf6/kio/fish.so
%{_kf6_plugindir}/kf6/kio/info.so
%{_kf6_plugindir}/kf6/kio/kio_filenamesearch.so
%{_kf6_plugindir}/kf6/kio/man.so
%{_kf6_plugindir}/kf6/kio/mtp.so
%{_kf6_plugindir}/kf6/kio/nfs.so
%{_kf6_plugindir}/kf6/kio/recentlyused.so
%{_kf6_plugindir}/kf6/kio/sftp.so
%{_kf6_plugindir}/kf6/kio/smb.so
%{_kf6_plugindir}/kf6/kio/thumbnail.so
%dir %{_kf6_plugindir}/kf6/kiod
%{_kf6_plugindir}/kf6/kiod/kmtpd.so
%dir %{_kf6_plugindir}/kf6/thumbcreator
%{_kf6_plugindir}/kf6/thumbcreator/audiothumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/comicbookthumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/directorythumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/djvuthumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/ebookthumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/exrthumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/imagethumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/jpegthumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/kraorathumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/opendocumentthumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/svgthumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/textthumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/windowsexethumbnail.so
%{_kf6_plugindir}/kf6/thumbcreator/windowsimagethumbnail.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_netpref.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_proxy.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_webshortcuts.so
%{_kf6_sharedir}/dbus-1/services/org.kde.kmtpd5.service
%dir %{_kf6_sharedir}/kio_filenamesearch
%{_kf6_sharedir}/kio_filenamesearch/kio-filenamesearch-grep
%{_kf6_sharedir}/kio_info/
%{_kf6_sharedir}/konqueror/
%{_kf6_sharedir}/remoteview/
%{_kf6_sharedir}/solid/
%{_libdir}/libkioarchive6.so.6*
%{_libexecdir}/wpad-detector-helper
%{_kf6_applicationsdir}/kcm_trash.desktop
%{_kf6_plugindir}/kcm_trash.so

%files devel
%{_includedir}/KioArchive6/
%{_libdir}/cmake/KioArchive6/

%changelog
%autochangelog
