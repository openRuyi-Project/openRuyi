# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtbase
%define real_version 6.10.1
%define short_version 6.10

%bcond xcb 1
%bcond mysql 0
%bcond postgresql 0
%bcond tests 0

Name:           qt6-qtbase
Version:        6.10.1
Release:        %autorelease
Summary:        Qt 6 core components
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://code.qt.io/qt/qtbase.git
#!RemoteAsset:  sha256:5a6226f7e23db51fdc3223121eba53f3f5447cf0cc4d6cb82a3a2df7a65d265d
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
Source1:        macros.qt6-qtbase
BuildSystem:    cmake

# Moves object files installation destination to ARCHDATADIR.
Patch0:         0001-qtbase-CMake-Install-objects-files-into-ARCHDATADIR.patch
# Removes patch version from the private API version tag.
Patch1:         0002-qtbase-use-only-major-minor-for-private-api-tag.patch
# namespace QT_VERSION_CHECK to workaround major/minor being pre-defined (#1396755)
Patch2:         0003-qtbase-version-check.patch
# Adds _SYS_SYSMACROS_H_OUTER and __WORDSIZE macros to the moc preprocessor.
Patch3:         0004-qtbase-moc-macros.patch
# drop -O3 and make -O2 by default
Patch4:         0005-qtbase-cxxflag.patch
# fix for new mariadb
Patch5:         0006-qtbase-mysql.patch
# fix FTBFS against libglvnd-1.3.4+
Patch6:         0007-qtbase-libglvnd.patch

BuildOption(conf):  -DINSTALL_ARCHDATADIR=%{_qt6_archdatadir}
BuildOption(conf):  -DINSTALL_BINDIR=%{_qt6_bindir}
BuildOption(conf):  -DINSTALL_DATADIR=%{_qt6_datadir}
BuildOption(conf):  -DINSTALL_DESCRIPTIONSDIR=%{_qt6_descriptionsdir}
BuildOption(conf):  -DINSTALL_DOCDIR=%{_qt6_docdir}
BuildOption(conf):  -DINSTALL_EXAMPLESDIR=%{_qt6_examplesdir}
BuildOption(conf):  -DINSTALL_INCLUDEDIR=%{_qt6_includedir}
BuildOption(conf):  -DINSTALL_LIBDIR=%{_qt6_libdir}
BuildOption(conf):  -DINSTALL_LIBEXECDIR=%{_qt6_libexecdir}
BuildOption(conf):  -DINSTALL_MKSPECSDIR=%{_qt6_mkspecsdir}
BuildOption(conf):  -DINSTALL_PLUGINSDIR=%{_qt6_pluginsdir}
BuildOption(conf):  -DINSTALL_QMLDIR=%{_qt6_qmldir}
BuildOption(conf):  -DINSTALL_SYSCONFDIR=%{_qt6_sysconfdir}
BuildOption(conf):  -DINSTALL_TESTSDIR=%{_qt6_testsdir}
BuildOption(conf):  -DINSTALL_TRANSLATIONSDIR=%{_qt6_translationsdir}
BuildOption(conf):  -DBUILD_WITH_PCH=OFF
BuildOption(conf):  -DQT_CREATE_VERSIONED_HARD_LINK=OFF
BuildOption(conf):  -DQT_DISABLE_RPATH=OFF
BuildOption(conf):  -DQT_GENERATE_SBOM=OFF
BuildOption(conf):  -DFEATURE_elf_private_full_version=ON
BuildOption(conf):  -DFEATURE_enable_new_dtags=ON
BuildOption(conf):  -DFEATURE_reduce_relocations=OFF
BuildOption(conf):  -DFEATURE_relocatable=OFF
BuildOption(conf):  -DFEATURE_journald=ON
BuildOption(conf):  -DFEATURE_libproxy=ON
BuildOption(conf):  -DFEATURE_accessibility=ON
BuildOption(conf):  -DFEATURE_fontconfig=ON
BuildOption(conf):  -DFEATURE_glib=ON
BuildOption(conf):  -DFEATURE_sctp=ON
BuildOption(conf):  -DINPUT_opengl=es2
BuildOption(conf):  -DFEATURE_opengles3=ON
BuildOption(conf):  -DFEATURE_wayland=ON
BuildOption(conf):  -DQT_BUILD_EXAMPLES=ON -DQT_INSTALL_EXAMPLES_SOURCES=ON
BuildOption(conf):  -DINPUT_openssl=linked
BuildOption(conf):  -DFEATURE_openssl_hash=ON
BuildOption(conf):  -DFEATURE_system_sqlite=ON
%if %{with tests}
BuildOption(conf):  -DQT_BUILD_TESTS=ON
%else
BuildOption(conf):  -DQT_BUILD_TESTS=OFF
%endif
%if %{with xcb}
BuildOption(conf):  -DFEATURE_system_xcb_xinput=ON
BuildOption(conf):  -DFEATURE_xcb_native_painting=ON
BuildOption(conf):  -DFEATURE_xcb=ON
%else
BuildOption(conf):  -DFEATURE_xcb=OFF
%endif
%if %{with mysql}
BuildOption(conf):  -DFEATURE_sql_mysql=ON
%endif
%if %{with postgresql}
BuildOption(conf):  -DFEATURE_sql_psql=ON
%endif
BuildOption(conf):  -DFEATURE_sql_odbc=ON

BuildRequires:  cmake >= 3.18.3
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libpcre2-16)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libsctp)
BuildRequires:  cups-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  unixODBC-devel
%if %{with xcb}
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(ice)
%endif
%if %{with mysql}
BuildRequires:  pkgconfig(libmariadb)
%endif
%if %{with postgresql}
BuildRequires:  pkgconfig(libpq)
%endif

%description
Qt is a software toolkit for developing applications.

%package        common
Summary:        Common files for Qt6
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    common
Common files for Qt6.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-gui%{?_isa} = %{version}-%{release}
Requires:       qt6-macros
Requires:       pkgconfig(egl)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(xkbcommon)
Requires:       pkgconfig(vulkan)

%description    devel
Development files for Qt6.

%package        private-devel
Summary:        Development files for %{name} private APIs
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       cups-devel

%description    private-devel
Private development files for Qt6.

%package        static
Summary:        Static library files for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(fontconfig)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(libinput)
Requires:       pkgconfig(xkbcommon)
Requires:       pkgconfig(zlib)

%description    static
Static library files for Qt6.

%package        gui
Summary:        Qt6 GUI-related libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{with xcb}
Requires:       pkgconfig(xcb-util)
Requires:       pkgconfig(xkbcommon-x11)
%endif
# Requires:       glx-utils

%description    gui
Qt6 libraries used for drawing widgets and OpenGL items.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
%{summary}.

%prep -a
rm -rf src/3rdparty/{harfbuzz-ng,freetype,libjpeg,libpng,sqlite,zlib,pcre2}

%install -a
mkdir -p %{buildroot}%{_qt6_pluginsdir}/{designer,iconengines,script,styles}
mkdir -p %{buildroot}%{_sysconfdir}/xdg/QtProject

mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
    qdbuscpp2xml|qdbusxml2cpp|qtpaths)
      ln -v ${i} %{buildroot}%{_bindir}/${i}-qt6
      ;;
    *)
      ln -v ${i} %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd

pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

mkdir -p %{buildroot}%{_qt6_includedir}/QtXcb
if [ -d src/plugins/platforms/xcb ]; then
    install -m 644 src/plugins/platforms/xcb/*.h %{buildroot}%{_qt6_includedir}/QtXcb/
fi

find %{buildroot}%{_qt6_libdir} -type f -name "*.o" -delete -print
rm -f %{buildroot}%{_qt6_libexecdir}/{ensure_pro_file.cmake,qt-android-runner.py,qt-testrunner.py,sanitizer-testrunner.py}
rm -rf %{buildroot}%{_qt6_libdir}/cmake/Qt6ExamplesAssetDownloaderPrivate
rm -rf %{buildroot}%{_qt6_includedir}/QtExamplesAssetDownloader
rm -f %{buildroot}%{_qt6_descriptionsdir}/ExamplesAssetDownloaderPrivate.json
rm -f %{buildroot}%{_qt6_libdir}/libQt6ExamplesAssetDownloader.*
rm -f %{buildroot}%{_qt6_libdir}/qt6/metatypes/qt6examplesassetdownloaderprivate_metatypes.json
rm -rf %{buildroot}%{_qt6_mkspecsdir}/features/uikit

install -p -m644 -D %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.qt6-qtbase
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch:}}%{version}-%{release}|g" \
  %{buildroot}%{_rpmmacrodir}/macros.qt6-qtbase

%files
%license LICENSES/GPL* LICENSES/LGPL*
%{_qt6_libdir}/libQt6Core.so.6*
%{_qt6_libdir}/libQt6Concurrent.so.6*
%{_qt6_libdir}/libQt6DBus.so.6*
%{_qt6_libdir}/libQt6Network.so.6*
%{_qt6_libdir}/libQt6Sql.so.6*
%{_qt6_libdir}/libQt6Test.so.6*
%{_qt6_libdir}/libQt6Xml.so.6*
%{_qt6_docdir}/global/
%{_qt6_docdir}/config/
%dir %{_qt6_pluginsdir}/networkinformation/
%dir %{_qt6_pluginsdir}/sqldrivers/
%dir %{_qt6_pluginsdir}/tls/
%{_qt6_pluginsdir}/networkinformation/libqglib.so
%{_qt6_pluginsdir}/networkinformation/libqnetworkmanager.so
%{_qt6_pluginsdir}/sqldrivers/libqsqlite.so
%{_qt6_pluginsdir}/tls/libqcertonlybackend.so
%{_qt6_pluginsdir}/tls/libqopensslbackend.so
%{_qt6_pluginsdir}/sqldrivers/libqsqlodbc.so
%{_bindir}/qtpaths*
%{_qt6_bindir}/qtpaths*
%if %{with postgresql}
%{_qt6_pluginsdir}/sqldrivers/libqsqlpsql.so
%endif
%if %{with mysql}
%files mysql
%{_qt6_pluginsdir}/sqldrivers/libqsqlmysql.so
%endif

%files common
%{_rpmmacrodir}/macros.qt6-qtbase

%files devel
%{_bindir}/qmake*
%{_bindir}/qt-cmake
%{_bindir}/qt-cmake-create
%{_bindir}/qt-configure-module
%{_bindir}/qdbuscpp2xml*
%{_bindir}/qdbusxml2cpp*
%{_bindir}/androiddeployqt*
%{_bindir}/androidtestrunner
%{_qt6_bindir}/*
%{_qt6_libexecdir}/*
%{_qt6_includedir}/QtConcurrent/
%{_qt6_includedir}/QtCore/
%{_qt6_includedir}/QtDBus/
%{_qt6_includedir}/QtGui/
%{_qt6_includedir}/QtNetwork/
%{_qt6_includedir}/QtOpenGL/
%{_qt6_includedir}/QtOpenGLWidgets
%{_qt6_includedir}/QtPrintSupport/
%{_qt6_includedir}/QtSql/
%{_qt6_includedir}/QtTest/
%{_qt6_includedir}/QtWaylandClient/
%{_qt6_includedir}/QtWaylandGlobal/
%{_qt6_includedir}/QtWlShellIntegration/
%{_qt6_includedir}/QtWidgets/
%{_qt6_includedir}/QtXcb/
%{_qt6_includedir}/QtXml/
%{_qt6_libdir}/libQt6*.prl
%{_qt6_libdir}/libQt6*.so
%{_qt6_libdir}/cmake/Qt6/
%{_qt6_libdir}/cmake/Qt6BuildInternals/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/QtStandaloneTestTemplateProject/CMakeLists.txt
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtBaseTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/QtStandaloneTestTemplateProject/Main.cmake
%{_qt6_libdir}/cmake/Qt6Concurrent/*.cmake
%{_qt6_libdir}/cmake/Qt6Core/*.cmake
%{_qt6_libdir}/cmake/Qt6Core/Qt6CoreResourceInit.in.cpp
%{_qt6_libdir}/cmake/Qt6Core/Qt6CoreConfigureFileTemplate.in
%{_qt6_libdir}/cmake/Qt6CoreTools/*.cmake
%{_qt6_libdir}/cmake/Qt6DBus/*.cmake
%{_qt6_libdir}/cmake/Qt6DBusTools/*.cmake
%{_qt6_libdir}/cmake/Qt6Gui/*.cmake
%{_qt6_libdir}/cmake/Qt6GuiTools/*.cmake
%{_qt6_libdir}/cmake/Qt6HostInfo/*.cmake
%{_qt6_libdir}/cmake/Qt6Network/*.cmake
%{_qt6_libdir}/cmake/Qt6OpenGL/*.cmake
%{_qt6_libdir}/cmake/Qt6OpenGLWidgets/*.cmake
%{_qt6_libdir}/cmake/Qt6PrintSupport/*.cmake
%{_qt6_libdir}/cmake/Qt6Sql/Qt6Sql*.cmake
%{_qt6_libdir}/cmake/Qt6Sql/Qt6QSQLiteDriverPlugin*.cmake
%{_qt6_libdir}/cmake/Qt6Sql/Qt6QODBCDriverPlugin*.cmake
%{_qt6_libdir}/cmake/Qt6Test/*.cmake
%{_qt6_libdir}/cmake/Qt6WaylandClient/*.cmake
%{_qt6_libdir}/cmake/Qt6WaylandScannerTools/*.cmake
%{_qt6_libdir}/cmake/Qt6Widgets/*.cmake
%{_qt6_libdir}/cmake/Qt6WidgetsTools/*.cmake
%{_qt6_libdir}/cmake/Qt6Xml/*.cmake
%{_qt6_descriptionsdir}/*.json
%{_qt6_metatypesdir}/*.json
%{_qt6_libdir}/pkgconfig/Qt6Concurrent.pc
%{_qt6_libdir}/pkgconfig/Qt6Core.pc
%{_qt6_libdir}/pkgconfig/Qt6DBus.pc
%{_qt6_libdir}/pkgconfig/Qt6Gui.pc
%{_qt6_libdir}/pkgconfig/Qt6Network.pc
%{_qt6_libdir}/pkgconfig/Qt6OpenGL.pc
%{_qt6_libdir}/pkgconfig/Qt6OpenGLWidgets.pc
%{_qt6_libdir}/pkgconfig/Qt6Platform.pc
%{_qt6_libdir}/pkgconfig/Qt6PrintSupport.pc
%{_qt6_libdir}/pkgconfig/Qt6Sql.pc
%{_qt6_libdir}/pkgconfig/Qt6Test.pc
%{_qt6_libdir}/pkgconfig/Qt6WaylandClient.pc
%{_qt6_libdir}/pkgconfig/Qt6Widgets.pc
%{_qt6_libdir}/pkgconfig/Qt6Xml.pc
%{_qt6_mkspecsdir}/*
%{_qt6_includedir}/QtInputSupport
%{_qt6_includedir}/QtFbSupport
%{_qt6_includedir}/QtExampleIcons
%{_qt6_includedir}/QtDeviceDiscoverySupport

%files private-devel
%{_qt6_includedir}/QtEglFSDeviceIntegration/QtEglFSDeviceIntegration
%{_qt6_includedir}/QtEglFSDeviceIntegration/QtEglFSDeviceIntegrationDepends
%{_qt6_includedir}/QtEglFSDeviceIntegration/QtEglFSDeviceIntegrationVersion
%{_qt6_includedir}/QtEglFSDeviceIntegration/qteglfsdeviceintegrationversion.h
%{_qt6_includedir}/*/%{real_version}/
%{_qt6_libdir}/cmake/Qt6CorePrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6DBusPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6GuiPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6NetworkPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6OpenGLPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6PrintSupportPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6SqlPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6TestInternalsPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6TestInternalsPrivate/3rdparty/cmake/*.cmake
%{_qt6_libdir}/cmake/Qt6TestPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6WidgetsPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6XmlPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6EglFSDeviceIntegrationPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6XcbQpaPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6DeviceDiscoverySupportPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6ExampleIconsPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6FbSupportPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6InputSupportPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6WaylandClientPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6WaylandGlobalPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6WlShellIntegrationPrivate/

%files gui
%{_qt6_libdir}/libQt6Gui.so.6*
%{_qt6_libdir}/libQt6OpenGL.so.6*
%{_qt6_libdir}/libQt6OpenGLWidgets.so.6*
%{_qt6_libdir}/libQt6PrintSupport.so.6*
%{_qt6_libdir}/libQt6WaylandClient.so.6*
%{_qt6_libdir}/libQt6WlShellIntegration.so.6*
%{_qt6_libdir}/libQt6Widgets.so.6*
%{_qt6_libdir}/libQt6EglFSDeviceIntegration.so.6*
%{_qt6_pluginsdir}/generic/
%{_qt6_pluginsdir}/imageformats/
%{_qt6_pluginsdir}/platforminputcontexts/
%{_qt6_pluginsdir}/platforms/
%{_qt6_pluginsdir}/platformthemes/
%{_qt6_pluginsdir}/printsupport/
%{_qt6_pluginsdir}/wayland*/
%{_qt6_pluginsdir}/egldeviceintegrations/
%if %{with xcb}
%dir %{_qt6_pluginsdir}/xcbglintegrations/
%{_qt6_pluginsdir}/xcbglintegrations/libqxcb-egl-integration.so
%{_qt6_libdir}/libQt6XcbQpa.so.6*
%endif
%{_qt6_datadir}/wayland/

%files static
%{_qt6_libdir}/*.a

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
