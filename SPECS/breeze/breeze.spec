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

Name:           breeze
Version:        6.5.5
Release:        %autorelease
Summary:        Plasma Desktop artwork, styles and assets
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/breeze
#!RemoteAsset:  sha256:09b3f7bd2386c4b91c418462f02b203510f2ae88489398ef05e0b6ddea3aa590
Source:         https://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_QT6:BOOL=TRUE
BuildOption(conf):  -DBUILD_QT5:BOOL=FALSE
BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  cmake >= 3.16
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# W: desktopfile-without-binary /usr/share/applications/kcm_breezedecoration.desktop
BuildRequires:  kf6-kcmutils >= %{kf6_version}
# Needed for Plasma/LookAndFeel service type declaration (kde#367923)
BuildRequires:  libplasma >= %{_plasma6_bugfix}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KDecoration3) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6FrameworkIntegration) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}

Requires:       breeze-cursors >= %{version}
Requires:       breeze-style >= %{version}
Requires:       kf6-breeze-icons >= %{kf6_version}

Recommends:     breeze-decoration >= %{version}
Recommends:     breeze-wallpapers >= %{version}

Provides:       breeze = %{version}-%{release}
Obsoletes:      breeze < %{version}-%{release}

%description
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.

%package     -n breeze-cursors
Summary:        Plasma Desktop artwork, styles and assets
BuildArch:      noarch

%description -n breeze-cursors
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.
This package provides Breeze cursor theme.

%package     -n breeze-style
Summary:        Plasma Desktop artwork, styles and assets
Requires:       kf6-kconfig

%description -n breeze-style
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.
This package provides Breeze style, color-scheme and aditional assets.

%package     -n breeze-wallpapers
Summary:        Plasma Desktop artwork, styles and assets
BuildArch:      noarch

%description -n breeze-wallpapers
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.
This package provides Breeze wallpaper theme.

%package     -n breeze-decoration
Summary:        Plasma Desktop artwork, styles and assets

%description -n breeze-decoration
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.
This package provides Breeze KWin decoration.

# NOTE: The CMake files were split from breeze*-style and don't require anything on purpose.
# Otherwise, BuildRequires: cmake(Breeze) would pull some Qt5 and KF5 packages.

%package        devel
Summary:        Information about breeze setup

%description    devel
This package ships a CMake config file used to get information about Breeze.

%prep -a

# Empty file used by the breeze packages
cat >> meta_package << EOF
This is a meta package, it does not contain any file
EOF

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%doc meta_package

%files -n breeze-cursors
%license LICENSES/*
%{_kf6_iconsdir}/breeze_cursors
%{_kf6_iconsdir}/Breeze_Light/

%files -n breeze-style
%license LICENSES/*
%{_kf6_applicationsdir}/breezestyleconfig.desktop
%{_kf6_bindir}/breeze-settings6
%{_kf6_iconsdir}/hicolor/scalable/apps/breeze-settings.svgz
%dir %{_kf6_plugindir}/kstyle_config
%{_kf6_plugindir}/kstyle_config/breezestyleconfig.so
%dir %{_kf6_plugindir}/styles
%{_kf6_plugindir}/styles/breeze*.so
%dir %{_kf6_sharedir}/QtCurve
%{_kf6_sharedir}/QtCurve/Breeze.qtcurve
%dir %{_kf6_sharedir}/color-schemes
%{_kf6_sharedir}/color-schemes/BreezeClassic.colors
%{_kf6_sharedir}/color-schemes/BreezeDark.colors
%{_kf6_sharedir}/color-schemes/BreezeLight.colors
%dir %{_kf6_sharedir}/kstyle
%dir %{_kf6_sharedir}/kstyle/themes
%{_kf6_sharedir}/kstyle/themes/breeze.themerc

%files -n breeze-wallpapers
%license LICENSES/*
%dir %{_kf6_sharedir}/wallpapers
%{_kf6_sharedir}/wallpapers/Next/

%files -n breeze-decoration
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_breezedecoration.desktop
%dir %{_kf6_plugindir}/org.kde.kdecoration3.kcm
%{_kf6_plugindir}/org.kde.kdecoration3.kcm/kcm_breezedecoration.so
%dir %{_kf6_plugindir}/org.kde.kdecoration3
%{_kf6_plugindir}/org.kde.kdecoration3/org.kde.breeze.so

%files devel
%{_kf6_bindir}/kcursorgen
%{_kf6_cmakedir}/Breeze/

%changelog
%autochangelog
