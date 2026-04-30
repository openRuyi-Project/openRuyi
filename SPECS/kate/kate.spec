# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.19.0
%define plasma6_version 5.27.80
%define qt6_version 6.9.0


Name:           kate
Version:        25.12.3
Release:        %autorelease
Summary:        Advanced Text Editor
License:        GPL-3.0-or-later
URL:            https://kate-editor.org
VCS:            git:https://invent.kde.org/utilities/kate.git
#!RemoteAsset:  sha256:d761d976c19922843617211d9069ded08d6eb43891e28e56eb9385b626ce90ab
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(PlasmaActivities) >= %{plasma6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds

Recommends:     kate-plugins = %{version}-%{release}
Recommends:     kuiviewer
Recommends:     markdownpart
Recommends:     svgpart

%description
Kate is an advanced text editor by KDE.

%package     -n kwrite
Summary:        KDE Text Editor
Recommends:     kate-plugins = %{version}-%{release}

%description -n kwrite
KWrite is a text editor by KDE.

%package        plugins
Summary:        KDE Text Editor plugins
Provides:       ktexteditorpreviewplugin = %{version}-%{release}
Obsoletes:      ktexteditorpreviewplugin < %{version}-%{release}

%description    plugins
Kate is an advanced text editor by KDE. This package contains
plugins and data files for Kate and KWrite editors.

%install -a

# Remove exotic icon sizes
rm -r %{buildroot}%{_kf6_iconsdir}/hicolor/{150x150,310x310,44x44}

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
rm -rf $RPM_BUILD_ROOT%{_kf6_htmldir}/*@*
rm -rf $RPM_BUILD_ROOT%{_mandir}/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --with-man --with-html --all-name --generate-subpackages

%files -f %{name}.lang
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/kate/
%doc %lang(en) %{_kf6_htmldir}/en/katepart/
%doc %{_kf6_mandir}/man1/kate.1%{?ext_man}
%{_kf6_applicationsdir}/org.kde.kate.desktop
%{_kf6_appstreamdir}/org.kde.kate.appdata.xml
%{_kf6_bindir}/exec_inspect.sh
%{_kf6_bindir}/kate
%{_kf6_iconsdir}/hicolor/*/apps/kate.*
%{_kf6_libdir}/libkateprivate.so.*
%{_kf6_pluginsdir}/kf6/kio/kio_kateexec.so

%files -n kwrite
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/kwrite/
%{_kf6_applicationsdir}/org.kde.kwrite.desktop
%{_kf6_appstreamdir}/org.kde.kwrite.appdata.xml
%{_kf6_bindir}/kwrite
%{_kf6_iconsdir}/hicolor/*/apps/kwrite.*

%files plugins
%{_kf6_plugindir}/kf6/ktexteditor/
%{_kf6_sharedir}/kateproject/
%{_kf6_sharedir}/katexmltools/

%changelog
%autochangelog
