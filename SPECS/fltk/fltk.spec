# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fltk
Version:        1.4.5
Release:        %autorelease
Summary:        C++ user interface toolkit
License:        LGPL-2.0-or-later WITH FLTK-exception
URL:            https://github.com/fltk/fltk
#!RemoteAsset:  sha256:7715e69ce081fa9ce6da48bb0dd3b07a4cf2cf937813814c04272f36fff593ea
Source0:        https://github.com/fltk/fltk/archive/refs/tags/release-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DFLTK_CONFIG_PATH:PATH=%{_libdir}/cmake/fltk
BuildOption(conf):  -DOpenGL_GL_PREFERENCE=GLVND
BuildOption(conf):  -DOPTION_BUILD_HTML_DOCUMENTATION:BOOL=ON
BuildOption(conf):  -DOPTION_BUILD_PDF_DOCUMENTATION:BOOL=OFF
BuildOption(conf):  -DFLTK_BUILD_SHARED_LIBS:BOOL=ON

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(zlib)

%description
FLTK (pronounced "fulltick") is a cross-platform C++ GUI toolkit.
It provides modern GUI functionality without the bloat, and supports
3D graphics via OpenGL. This package contains the runtime libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       pkgconfig(fontconfig)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(x11)

%description    devel
Development files for FLTK.

%package        fluid
Summary:        Fast Light User Interface Designer
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel

%description    fluid
Interactive GUI designer for FLTK.

%build -a
make docs -C %{_vpath_builddir}

%install -a
mv src/xutf8/COPYING ./COPYING.xutf8
rm -f %{buildroot}%{_libdir}/*.a

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/fluid.desktop

%files
%doc ANNOUNCEMENT
%license COPYING COPYING.xutf8
%{_libdir}/libfltk.so.*
%{_libdir}/libfltk_forms.so.*
%{_libdir}/libfltk_gl.so.*
%{_libdir}/libfltk_images.so.*
%{_bindir}/blocks
%{_bindir}/checkers
%{_bindir}/fltk-options
%{_bindir}/glpuzzle
%{_bindir}/sudoku
%{_bindir}/fluid-shared
%{_bindir}/fltk-options-shared
%{_datadir}/applications/fltk-options.desktop
%{_datadir}/mime/packages/fltk-options.xml
%{_mandir}/man1/fltk-options.1*

%files devel
%doc %{_vpath_builddir}/documentation/html
%{_bindir}/fltk-config
%{_includedir}/FL/
%{_libdir}/libfltk.so
%{_libdir}/libfltk_forms.so
%{_libdir}/libfltk_gl.so
%{_libdir}/libfltk_images.so
%{_datadir}/fltk/
%{_mandir}/man1/fltk-config.1*
%{_mandir}/man3/fltk.3*
%{_mandir}/man6/*.6*

%files fluid
%{_bindir}/fluid
%{_mandir}/man1/fluid.1*
%{_datadir}/applications/fluid.desktop
%{_datadir}/mime/packages/fluid.xml
%{_datadir}/icons/hicolor/*/*/*

%changelog
%autochangelog
