# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtwebengine
%global toolchain clang

# Keep GN response filenames below the filesystem limit. https://bugreports.qt.io/browse/QTBUG-59769
%global _vpath_builddir b

Name:           qt6-qtwebengine
Version:        6.140.0
Release:        %autorelease
Summary:        Qt6 - QtWebEngine components
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtwebengine
#!RemoteAsset:  sha256:82352854a1d01dfe6abeefaf023554e4722c1d7df48ba3ce0078f6c0a9c7e1a3
Source0:        https://download.qt.io/official_releases/qtwebengine/6.140/%{version}/src/%{qt_module}-everywhere-src-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(prep):  -n %{qt_module}-everywhere-src-%{version}

BuildOption(conf):  -DCMAKE_TOOLCHAIN_FILE="%{_libdir}/cmake/Qt6/qt.toolchain.cmake"
BuildOption(conf):  -DCMAKE_LINKER_TYPE=LLD
BuildOption(conf):  -DFEATURE_webengine_build_gn=ON
BuildOption(conf):  -DFEATURE_webengine_jumbo_build=ON
BuildOption(conf):  -DINPUT_webengine_jumbo_file_merge_limit=8
BuildOption(conf):  -DQT_SHOW_EXTRA_IDE_SOURCES=OFF
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
BuildOption(conf):  -DFEATURE_webengine_system_minizip=ON
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
BuildOption(conf):  -DFEATURE_webengine_webrtc=ON
BuildOption(conf):  -DFEATURE_webengine_webrtc_pipewire=ON
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
BuildRequires:  ninja
BuildRequires:  clang
BuildRequires:  lld
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(html5lib)
BuildRequires:  gperf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  perl
BuildRequires:  nodejs
BuildRequires:  python3dist(six)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  qt6-macros
BuildRequires:  qt6-qtbase-private-devel >= 6.12.0
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
BuildRequires:  snappy-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(minizip)
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
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(nss)

Recommends:     pipewire
Recommends:     xdg-desktop-portal

%patchlist
# Find PdfQuick for PDF examples; https://github.com/qt/qtwebengine/commit/667e0fe22e12663e0016a0c7af81730464d36ca4
0001-qtpdf-example-find.patch
# Serve extension resources to ordinary pages; https://github.com/qt/qtwebengine/commit/182770309831c9167a0e1102c92e4ddb9e0ab6c3
0002-webengine-extension-resources.patch
# Bind extension worker and frame interfaces; https://github.com/qt/qtwebengine/commit/85c4b70af12dd018f8188c4ae2f0425158a5f7be
0003-webengine-extension-workers.patch
# Report incompatible system FFmpeg; https://github.com/qt/qtwebengine/commit/9cd16a4802645aeb37ec3f2fa7ee8d47538cd0e2
0004-webengine-ffmpeg-diagnostic.patch

# Avoid SYS_SECCOMP conflicts with glibc; https://chromium.googlesource.com/chromium/src/+/83a9ccb1265dcdeeb8bf17205e00b751f86641d3
1000-chromium-seccomp-glibc.patch
# Fix the OSR code check; https://github.com/v8/v8/commit/3b52f29d09b8941a43696b207529fb11aec19c66
1001-v8-riscv-osr-check.patch
# Fix large Wasm lazy jumps; https://github.com/v8/v8/commit/def38dd3f8726ed595932624ee5d681a3f02ed4a
1002-v8-riscv-lazy-jump.patch
# Preserve character-code inputs; https://github.com/v8/v8/commit/953d0bd5b0629fc42775f8fc08ffe6e7599ce6a6
1003-v8-riscv-charcode-register.patch
# Preserve concurrent subword updates; https://github.com/v8/v8/commit/d45bc027023297658f992b72af33c466e9d4487b
1004-v8-riscv-subword-atomic.patch
# Guard GLX access when Ozone X11 is disabled; https://github.com/qt/qtwebengine/commit/ca137f50ec704caecba07f8c4a30fb046999ce02
1005-qt-ozone-x11-guard.patch
# Link PDF examples to PdfQuick; https://github.com/qt/qtwebengine/commit/dc73367655df769ca69c65ffa6c776e9edcc94a6
1006-qtpdf-example-link.patch
# Parse underscore-separated ISA features; https://github.com/v8/v8/commit/79b2369ad746e3208e6984ceccf7f661a83b2058
1007-v8-riscv-isa-parser.patch
# Relocate ELF string tables on RISC-V Linux; https://github.com/chromium/chromium/commit/fe71107697d8bccdc4e95048147f97826142ba75
1008-chromium-riscv-elf-strtab.patch
# Round clamped values to integers; https://github.com/v8/v8/commit/09e5fa753e99d658e77044ff9b9f150397cee059
1009-v8-riscv-clamped-rounding.patch
# Keep the high bits of signed products; https://github.com/v8/v8/commit/7c405ae0da48c68a2d558cbbc8fe38f5377f60b1
1010-v8-riscv-multiply-high.patch
# Preserve live registers during RISC-V byte swaps; https://github.com/v8/v8/commit/7e40e4bee05bbecad063f618ec64d48aa3a63ca7
1011-v8-riscv-byteswap-registers.patch
# Preserve saved RISC-V frames across signals; https://github.com/v8/v8/commit/6a0a25abaed397f83eb0d92e4b33a5e18204f8bc
1012-v8-riscv-leave-frame.patch
# Use Highway comparisons on RISC-V; https://github.com/v8/v8/commit/77c3daed6d2b89a45531bf4b0f81d9b697768f87
1013-v8-riscv-highway-comparisons.patch
# Check RISC-V assembler buffer growth; https://github.com/v8/v8/commit/639a7d02772c0bc212bc29b6b4eaddbed115488a
1014-v8-riscv-grow-buffer.patch
# Handle ICU 79 case folding; https://github.com/v8/v8/commit/f607706154eabc4a949628a88b38dbe95cd2274c.
1015-v8-icu79-case-folding.patch
# Correct RISC-V Wasm parameter spill slots; https://github.com/v8/v8/commit/792ce35f2cd9f65962030e8d536a8a480d721d2d.
1016-v8-riscv-frame-parameter-spills.patch
# Locate the saved RISC-V Wasm return address; https://github.com/v8/v8/commit/9235e225af3555365398cd7d24b31a2efe51650f.
1017-v8-riscv-frame-calling-pc.patch

# Support RISC-V seccomp (adapted from openSUSE); https://api.opensuse.org/public/source/openSUSE:Factory:RISCV/qt6-webengine/riscv-sandbox.patch?rev=41
2000-riscv-sandbox.patch
# Fix RISC-V audio and musttail builds (adapted from openSUSE); https://api.opensuse.org/public/source/openSUSE:Factory:RISCV/qt6-webengine/riscv-misc.patch?rev=41
2001-riscv-misc.patch
# Declare fixed-width integer types; https://src.fedoraproject.org/rpms/qt6-qtwebengine/blob/bd8905f045f73300ca319773fc8f5a1558ccfc9b/f/qtwebengine-fix-build-against-gcc16.patch.
2002-chromium-integer-header.patch
# Correct RISC-V Liftoff SIMD register handling; https://github.com/felixonmars/archriscv-packages/blob/90ecae0ca9cfa948345ef826082eec76eb234eac/qt6-webengine/riscv-v8.patch
2003-v8-riscv-liftoff-registers.patch
# Report the RISC-V extension platform; https://github.com/felixonmars/archriscv-packages/blob/7dad19467ed1a7e306510925de72558dbdc64b43/chromium/0001-chrome-runtime_api_delegate-add-riscv64-define.patch.
2004-runtime-riscv64.patch

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
sed -i -e '/toolprefix = /d' -e 's/\${toolprefix}//g' src/3rdparty/chromium/build/toolchain/linux/BUILD.gn

cp -p src/3rdparty/chromium/LICENSE LICENSE.Chromium

%conf -p
export NINJAFLAGS="%{__ninja_common_opts}"

%build -p
export STRIP=strip
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
%{_qt6_archdatadir}/sbom/%{qt_module}-%{version}.spdx
%{_qt6_archdatadir}/sbom/qtpdf-%{version}.spdx
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
%{_qt6_libdir}/cmake/Qt6/ConfigVersionOverrides/Pdf/
%{_qt6_libdir}/cmake/Qt6/ConfigVersionOverrides/PdfQuick/
%{_qt6_libdir}/cmake/Qt6/ConfigVersionOverrides/PdfWidgets/
%{_qt6_libdir}/cmake/Qt6/ConfigVersionOverrides/WebEngineCore/
%{_qt6_libdir}/cmake/Qt6/ConfigVersionOverrides/WebEngineQuick/
%{_qt6_libdir}/cmake/Qt6/ConfigVersionOverrides/WebEngineWidgets/
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
