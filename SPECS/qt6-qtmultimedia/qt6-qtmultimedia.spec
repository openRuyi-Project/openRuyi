# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtmultimedia
%define real_version 6.10.1
%define short_version 6.10

%bcond ffmpeg 0

Name:           qt6-qtmultimedia
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - Multimedia support
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://code.qt.io/qt/qtmultimedia.git
#!RemoteAsset:  sha256:f7a4f9bc2840d4f0f9f7329f0dcb3d3500c54177b8e368091a3727c7320e67b8
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON
BuildOption(conf):  -DFEATURE_gstreamer=OFF
%if %{with ffmpeg}
BuildOption(conf):  -DFEATURE_ffmpeg=ON
%else
BuildOption(conf):  -DFEATURE_ffmpeg=OFF
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core) >= %{version}
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  pkgconfig(Qt6ShaderTools) >= %{version}
BuildRequires:  pkgconfig(Qt6Quick3D) >= %{version}
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  pkgconfig(openssl)
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrandr)
%if %{with ffmpeg}
BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
%endif

%description
The Qt Multimedia module provides a rich feature set that enables you to
easily take advantage of a platforms multimedia capabilites and hardware.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Core)
Requires:       pkgconfig(Qt6Quick)
Requires:       pkgconfig(libpulse-mainloop-glib)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%install -a
pushd %{buildroot}%{_qt6_libdir}
for prl_file in *.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

rm -rf %{buildroot}%{_qt6_archdatadir}/mkspecs/features/ios

%files
%license LICENSES/*
%{_qt6_libdir}/libQt6Multimedia.so.6*
%{_qt6_libdir}/libQt6MultimediaQuick.so.6*
%{_qt6_libdir}/libQt6MultimediaWidgets.so.6*
%{_qt6_libdir}/libQt6SpatialAudio.so.6*
%{_qt6_libdir}/libQt6Quick3DSpatialAudio.so.6*
%{_qt6_qmldir}/QtMultimedia/
%{_qt6_qmldir}/QtQuick3D/SpatialAudio/
%if %{with ffmpeg}
%{_qt6_pluginsdir}/multimedia/libffmpegmediaplugin.so
%endif
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%if %{with ffmpeg}
%{_qt6_includedir}/QtFFmpegMediaPluginImpl/
%endif
%{_qt6_includedir}/QtMultimedia/
%{_qt6_includedir}/QtMultimediaTestLib/
%{_qt6_includedir}/QtMultimediaQuick/
%{_qt6_includedir}/QtMultimediaWidgets/
%{_qt6_includedir}/QtSpatialAudio/
%{_qt6_includedir}/QtQuick3DSpatialAudio/
%{_qt6_libdir}/libQt6BundledResonanceAudio.a
%if %{with ffmpeg}
%{_qt6_libdir}/libQt6FFmpegMediaPluginImpl.a
%{_qt6_libdir}/libQt6FFmpegMediaPluginImpl.prl
%endif
%{_qt6_libdir}/libQt6Multimedia.so
%{_qt6_libdir}/libQt6Multimedia.prl
%{_qt6_libdir}/libQt6MultimediaTestLib.a
%{_qt6_libdir}/libQt6MultimediaTestLib.prl
%{_qt6_libdir}/libQt6MultimediaQuick.so
%{_qt6_libdir}/libQt6MultimediaQuick.prl
%{_qt6_libdir}/libQt6MultimediaWidgets.so
%{_qt6_libdir}/libQt6MultimediaWidgets.prl
%{_qt6_libdir}/libQt6SpatialAudio.so
%{_qt6_libdir}/libQt6SpatialAudio.prl
%{_qt6_libdir}/libQt6Quick3DSpatialAudio.so
%{_qt6_libdir}/libQt6Quick3DSpatialAudio.prl
%{_qt6_libdir}/cmake/Qt6MultimediaQuickPrivate/
%{_qt6_libdir}/cmake/Qt6BundledResonanceAudio/
%if %{with ffmpeg}
%{_qt6_libdir}/cmake/Qt6FFmpegMediaPluginImplPrivate/
%endif
%{_qt6_libdir}/cmake/Qt6Multimedia/
%{_qt6_libdir}/cmake/Qt6MultimediaPrivate/
%{_qt6_libdir}/cmake/Qt6MultimediaTestLibPrivate/
%{_qt6_libdir}/cmake/Qt6MultimediaWidgets/
%{_qt6_libdir}/cmake/Qt6MultimediaWidgetsPrivate/
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6quickmultimedia*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6quick3dspatialaudio*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DSpatialAudioPrivate/
%{_qt6_libdir}/cmake/Qt6SpatialAudio/
%{_qt6_libdir}/cmake/Qt6SpatialAudioPrivate/
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6Multimedia.pc
%{_qt6_libdir}/pkgconfig/Qt6MultimediaWidgets.pc
%{_qt6_libdir}/pkgconfig/Qt6SpatialAudio.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
