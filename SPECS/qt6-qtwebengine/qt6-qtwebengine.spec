# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtwebengine
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtwebengine
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - QtWebEngine components
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtwebengine
#!RemoteAsset:  sha256:77b5ea6186a0429a6b8e656faedd5cd3e8019d33856ee59637698ab578ead1e3
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

# workaround FTBFS against kernel-headers-5.2.0+
Patch0:         0001-qtwebengine-SIOCGSTAMP.patch
# enable to link pipewire
Patch1:         0002-qtwebengine-link-pipewire.patch
## Upstreamable patches:
Patch2:         0003-qtwebengine-add-missing-pipewire-headers.patch
%ifarch riscv64
# Patches from https://build.opensuse.org/package/show/openSUSE:Factory:RISCV/qt6-webengine
# At revision dd1924eb288d26a395e5cd4841bd51d6.
# Nov 09, 2025
Patch3:         0004-riscv-sandbox.patch
Patch4:         0005-riscv-v8.patch
Patch5:         0006-riscv-enable-v8-webasm.patch
%endif

BuildOption(conf):  -DCMAKE_TOOLCHAIN_FILE="%{_libdir}/cmake/Qt6/qt.toolchain.cmake"
BuildOption(conf):  -DFEATURE_webengine_build_gn=ON
BuildOption(conf):  -DFEATURE_webengine_jumbo_build=ON
BuildOption(conf):  -DFEATURE_qtwebengine_build=ON
BuildOption(conf):  -DFEATURE_qtwebengine_core_build=ON
BuildOption(conf):  -DFEATURE_qtwebengine_widgets_build=ON
BuildOption(conf):  -DFEATURE_qtwebengine_quick_build=ON
BuildOption(conf):  -DFEATURE_qtpdf_build=ON
BuildOption(conf):  -DFEATURE_qtpdf_widgets_build=ON
BuildOption(conf):  -DFEATURE_qtpdf_quick_build=ON
BuildOption(conf):  -DFEATURE_webengine_system_re2=ON
BuildOption(conf):  -DFEATURE_webengine_system_icu=ON
BuildOption(conf):  -DFEATURE_webengine_system_libwebp=ON
BuildOption(conf):  -DFEATURE_webengine_system_opus=ON
BuildOption(conf):  -DFEATURE_webengine_system_ffmpeg=ON
BuildOption(conf):  -DFEATURE_webengine_system_libvpx=OFF
BuildOption(conf):  -DFEATURE_webengine_system_snappy=ON
BuildOption(conf):  -DFEATURE_webengine_system_glib=ON
BuildOption(conf):  -DFEATURE_webengine_system_zlib=ON
BuildOption(conf):  -DFEATURE_webengine_system_minizip=OFF
BuildOption(conf):  -DFEATURE_webengine_system_libevent=ON
BuildOption(conf):  -DFEATURE_webengine_system_libxml=ON
BuildOption(conf):  -DFEATURE_webengine_system_lcms2=ON
BuildOption(conf):  -DFEATURE_webengine_system_libpng=ON
BuildOption(conf):  -DFEATURE_webengine_system_libtiff=ON
BuildOption(conf):  -DFEATURE_webengine_system_libjpeg=ON
BuildOption(conf):  -DFEATURE_webengine_system_libopenjpeg2=ON
BuildOption(conf):  -DFEATURE_webengine_system_harfbuzz=ON
BuildOption(conf):  -DFEATURE_webengine_system_freetype=ON
BuildOption(conf):  -DFEATURE_webengine_system_libpci=ON
BuildOption(conf):  -DFEATURE_webengine_system_libudev=ON
BuildOption(conf):  -DFEATURE_webengine_system_alsa=ON
BuildOption(conf):  -DFEATURE_webengine_system_pulseaudio=ON
BuildOption(conf):  -DFEATURE_webengine_system_gbm=ON
BuildOption(conf):  -DFEATURE_webengine_pepper_plugins=ON
BuildOption(conf):  -DFEATURE_webengine_printing_and_pdf=ON
BuildOption(conf):  -DFEATURE_webengine_proprietary_codecs=ON
BuildOption(conf):  -DFEATURE_webengine_spellchecker=ON
# TODO
BuildOption(conf):  -DFEATURE_webengine_webrtc=OFF
BuildOption(conf):  -DFEATURE_webengine_webrtc_pipewire=OFF
BuildOption(conf):  -DFEATURE_webengine_geolocation=ON
BuildOption(conf):  -DFEATURE_webengine_webchannel=ON
BuildOption(conf):  -DFEATURE_webengine_kerberos=ON
BuildOption(conf):  -DFEATURE_webengine_extensions=ON
BuildOption(conf):  -DFEATURE_webengine_ozone_x11=ON
BuildOption(conf):  -DFEATURE_webengine_vulkan=ON
BuildOption(conf):  -DFEATURE_webengine_vaapi=ON
BuildOption(conf):  -DFEATURE_webengine_v8_context_snapshot=ON
BuildOption(conf):  -DFEATURE_webenginedriver=ON
BuildOption(conf):  -GNinja
BuildOption(conf):  -DQT_BUILD_EXAMPLES=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  python3-html5lib
BuildRequires:  gperf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  perl
BuildRequires:  nodejs
BuildRequires:  python3-six
BuildRequires:  pkgconfig(krb5)
BuildRequires:  qt6-macros
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlModels)
BuildRequires:  cmake(Qt6QmlTools)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6WebChannelQuick)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WidgetsTools)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(opus)
BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig(vpx)
BuildRequires:  snappy-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(zlib)
# BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(poppler-cpp)

%description
The Qt WebEngine module provides a web browser engine that makes it easy to
embed content from the World Wide Web into your Qt application.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6Positioning)
Requires:       cmake(Qt6Quick)
Requires:       cmake(Qt6WebChannel)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Example files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Examples for %{name}.

%prep -a
system_libs=(re2 icu libwebp opus ffmpeg libvpx snappy glib zlib libevent libxml libxslt lcms2 libpng libtiff libjpegflint libopenjpeg2 harfbuzz freetype libpci)
sed -i -e '/toolprefix = /d' -e 's/\${toolprefix}//g' src/3rdparty/chromium/build/toolchain/linux/BUILD.gn

cp -p src/3rdparty/chromium/LICENSE LICENSE.Chromium

%build -p
export STRIP=strip
export NINJAFLAGS="%{__ninja_common_opts}"
export NINJA_PATH=%{__ninja}

%install -a
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
rm -fv Qt6WebEngineCore.la
popd

sed -i -e "s|%{version} \${_Qt6WebEngine|%{real_version} \${_Qt6WebEngine|" \
  %{buildroot}%{_qt6_libdir}/cmake/Qt6WebEngine*/Qt6WebEngine*Config.cmake

%files
%license LICENSE.*
%{_qt6_libdir}/libQt6WebEngineCore.so.*
%{_qt6_libdir}/libQt6WebEngineQuick.so.*
%{_qt6_libdir}/libQt6WebEngineQuickDelegatesQml.so.*
%{_qt6_libdir}/libQt6WebEngineWidgets.so.*
%{_qt6_libexecdir}/gn
%{_qt6_libexecdir}/qwebengine_convert_dict
%{_qt6_libexecdir}/QtWebEngineProcess
%{_qt6_libexecdir}/webenginedriver
%{_qt6_libdir}/qt6/qml/QtWebEngine/
%{_qt6_datadir}/resources/
%{_qt6_translationsdir}/qtwebengine_locales/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx
%{_qt6_archdatadir}/sbom/qtpdf-%{real_version}.spdx
%{_qt6_datadir}/resources/qtwebengine_devtools_resources.pak
%{_qt6_libdir}/libQt6Pdf.so.*
%{_qt6_libdir}/libQt6PdfQuick.so.*
%{_qt6_libdir}/libQt6PdfWidgets.so.*
%{_qt6_libdir}/qt6/qml/QtQuick/Pdf/
%{_qt6_pluginsdir}/imageformats/libqpdf.so

%files devel
%{_qt6_includedir}/QtWebEngineCore/
%{_qt6_includedir}/QtWebEngineQuick/
%{_qt6_includedir}/QtWebEngineWidgets/
%{_qt6_libdir}/qt6/metatypes/qt6webengine*.json
%{_qt6_datadir}/modules/WebEngine*.json
%{_qt6_libdir}/libQt6WebEngine*.so
%{_qt6_libdir}/libQt6WebEngine*.prl
%{_qt6_libdir}/cmake/Qt6Designer/Qt6QWebEngine*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6qtwebengine*.cmake
%{_qt6_libdir}/cmake/Qt6WebEngine*/
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtWebEngine*
%{_qt6_libdir}/pkgconfig/Qt6WebEngineCore.pc
%{_qt6_libdir}/pkgconfig/Qt6WebEngineQuick.pc
%{_qt6_libdir}/pkgconfig/Qt6WebEngineQuickDelegatesQml.pc
%{_qt6_libdir}/pkgconfig/Qt6WebEngineWidgets.pc
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_webengine*.pri
%{_qt6_pluginsdir}/designer/libqwebengineview.so
%{_qt6_includedir}/QtPdf*/
%{_qt6_libdir}/qt6/metatypes/qt6pdf*.json
%{_qt6_datadir}/modules/Pdf*.json
%{_qt6_libdir}/libQt6Pdf*.so
%{_qt6_libdir}/libQt6Pdf*.prl
%{_qt6_libdir}/cmake/Qt6Gui/Qt6QPdf*.cmake
%{_qt6_libdir}/cmake/Qt6Pdf*/
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6Pdf*.cmake
%{_qt6_libdir}/pkgconfig/Qt6Pdf.pc
%{_qt6_libdir}/pkgconfig/Qt6PdfQuick.pc
%{_qt6_libdir}/pkgconfig/Qt6PdfWidgets.pc
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_pdf*.pri

%files examples
%{_qt6_examplesdir}/webengine*
%{_qt6_examplesdir}/pdf*

%changelog
%autochangelog
