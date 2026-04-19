# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtlottie
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtlottie
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - Lottie Animation
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtlottie
#!RemoteAsset:  sha256:bc9c363c48486d790a998d25119bc0e7d2499266c3be96e61e3032422b0457c2
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  pkgconfig(Qt6Svg) >= %{version}
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(openssl)

%description
Qt Lottie Animation provides a QML API for rendering graphics and animations
that are exported in JSON format by the Bodymovin plugin for Adobe After
Effects.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%files
%license LICENSES/GPL*
%{_qt6_libdir}/libQt6Lottie.so.6*
%{_qt6_libdir}/libQt6LottieVectorImageGenerator.so.6*
%{_qt6_libdir}/libQt6LottieVectorImageHelpers.so.6*
%{_qt6_pluginsdir}/vectorimageformats/libqlottievectorimage.so
%{_qt6_qmldir}/Qt/labs/lottieqt/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_bindir}/lottietoqml
%{_qt6_libdir}/libQt6Lottie.so
%{_qt6_libdir}/libQt6LottieVectorImageGenerator.so
%{_qt6_libdir}/libQt6LottieVectorImageHelpers.so
%{_qt6_libdir}/libQt6Lottie.prl
%{_qt6_libdir}/libQt6LottieVectorImageGenerator.prl
%{_qt6_libdir}/libQt6LottieVectorImageHelpers.prl
%{_qt6_includedir}/QtLottie/
%{_qt6_includedir}/QtLottieVectorImageGenerator/
%{_qt6_includedir}/QtLottieVectorImageHelpers/
%{_qt6_libdir}/cmake/Qt6Lottie/
%{_qt6_libdir}/cmake/Qt6LottiePrivate/
%{_qt6_libdir}/cmake/Qt6LottieTools/
%{_qt6_libdir}/cmake/Qt6LottieVectorImageGeneratorPrivate/
%{_qt6_libdir}/cmake/Qt6LottieVectorImageHelpers/
%{_qt6_libdir}/cmake/Qt6LottieVectorImageHelpersPrivate/
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtLottieTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6Lottie.pc
%{_qt6_libdir}/pkgconfig/Qt6LottieVectorImageHelpers.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
