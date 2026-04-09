# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtspeech
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtspeech
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - Speech component
License:        (GPL-2.0-only OR LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0) AND BSD-3-Clause
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtspeech
#!RemoteAsset
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core) >= %{version}
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Multimedia) >= %{version}
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  pkgconfig(speech-dispatcher)
BuildRequires:  flite-devel

%description
The module enables a Qt application to support accessibility features
such as text-to-speech.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Core)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%install -a
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

%files
%license LICENSES/GPL* LICENSES/LGPL* LICENSES/BSD*
%{_qt6_libdir}/libQt6TextToSpeech.so.6*
%dir %{_qt6_pluginsdir}/texttospeech/
%{_qt6_pluginsdir}/texttospeech/libqtexttospeech_mock.so
%dir %{_qt6_qmldir}/QtTextToSpeech
%{_qt6_qmldir}/QtTextToSpeech/*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx
%{_qt6_pluginsdir}/texttospeech/libqtexttospeech_flite.so
%{_qt6_libdir}/cmake/Qt6TextToSpeech/Qt6QTextToSpeechFlitePlugin*.cmake
%{_qt6_pluginsdir}/texttospeech/libqtexttospeech_speechd.so
%{_qt6_libdir}/cmake/Qt6TextToSpeech/Qt6QTextToSpeechSpeechdPlugin*.cmake

%files devel
%{_qt6_includedir}/QtTextToSpeech/
%{_qt6_libdir}/libQt6TextToSpeech.so
%{_qt6_libdir}/libQt6TextToSpeech.prl
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6TextToSpeech/
%{_qt6_libdir}/cmake/Qt6TextToSpeechPrivate/
%{_qt6_libdir}/pkgconfig/Qt6TextToSpeech.pc
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_texttospeech*.pri
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/qt6/metatypes/*.json

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
