# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtvirtualkeyboard
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtvirtualkeyboard
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - VirtualKeyboard component
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtvirtualkeyboard
#!RemoteAsset
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz

BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  pkgconfig(Qt6Svg) >= %{version}
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(hunspell)

%description
The Qt Virtual Keyboard project provides an input framework and reference keyboard
frontend for Qt 6. Key features include customizable keyboard layouts, predictive
text input, and handwriting support.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Gui)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%files
%license LICENSES/*
%{_qt6_libdir}/libQt6HunspellInputMethod.so.6*
%{_qt6_libdir}/libQt6VirtualKeyboard.so.6*
%{_qt6_libdir}/libQt6VirtualKeyboardSettings.so.6*
%{_qt6_libdir}/libQt6VirtualKeyboardQml.so.6*
%{_qt6_pluginsdir}/platforminputcontexts/libqtvirtualkeyboardplugin.so
%{_qt6_qmldir}/QtQuick/VirtualKeyboard/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtHunspellInputMethod/
%{_qt6_includedir}/QtVirtualKeyboard/
%{_qt6_includedir}/QtVirtualKeyboardSettings/
%{_qt6_includedir}/QtVirtualKeyboardQml/
%{_qt6_libdir}/libQt6HunspellInputMethod.prl
%{_qt6_libdir}/libQt6HunspellInputMethod.so
%{_qt6_libdir}/libQt6VirtualKeyboard.prl
%{_qt6_libdir}/libQt6VirtualKeyboard.so
%{_qt6_libdir}/libQt6VirtualKeyboardSettings.prl
%{_qt6_libdir}/libQt6VirtualKeyboardSettings.so
%{_qt6_libdir}/libQt6VirtualKeyboardQml.prl
%{_qt6_libdir}/libQt6VirtualKeyboardQml.so
%{_qt6_libdir}/cmake/Qt6HunspellInputMethod/
%{_qt6_libdir}/cmake/Qt6HunspellInputMethodPrivate/
%{_qt6_libdir}/cmake/Qt6VirtualKeyboard/
%{_qt6_libdir}/cmake/Qt6VirtualKeyboardPrivate/
%{_qt6_libdir}/cmake/Qt6VirtualKeyboardQml/
%{_qt6_libdir}/cmake/Qt6VirtualKeyboardQmlPrivate/
%{_qt6_libdir}/cmake/Qt6VirtualKeyboardSettings/
%{_qt6_libdir}/cmake/Qt6VirtualKeyboardSettingsPrivate/
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_libdir}/cmake/Qt6Gui/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/pkgconfig/Qt6VirtualKeyboard.pc
%{_qt6_libdir}/pkgconfig/Qt6HunspellInputMethod.pc
%{_qt6_libdir}/pkgconfig/Qt6VirtualKeyboardQml.pc
%{_qt6_libdir}/pkgconfig/Qt6VirtualKeyboardSettings.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
