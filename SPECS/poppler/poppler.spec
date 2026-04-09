# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           poppler
Version:        25.11.0
Release:        %autorelease
Summary:        PDF rendering library
License:        (GPL-2.0-only OR GPL-3.0-only) AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:            https://gitlab.freedesktop.org/poppler/poppler
#!RemoteAsset
Source:         https://gitlab.freedesktop.org/poppler/poppler/-/archive/poppler-%{version}/poppler-poppler-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DENABLE_CMS=lcms2
BuildOption(conf):  -DENABLE_DCTDECODER=libjpeg
BuildOption(conf):  -DENABLE_GTK_DOC=ON
BuildOption(conf):  -DENABLE_LIBOPENJPEG=openjpeg2
BuildOption(conf):  -DENABLE_UNSTABLE_API_ABI_HEADERS=ON
BuildOption(conf):  -DENABLE_ZLIB=OFF
BuildOption(conf):  -DENABLE_GPGME=OFF
BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DENABLE_GTK_DOC=OFF
BuildOption(conf):  -DENABLE_LIBOPENJPEG=none
BuildOption(conf):  -DENABLE_QT5=OFF
BuildOption(conf):  -DENABLE_QT6=ON
BuildOption(conf):  -DCMAKE_PREFIX_PATH=%{_libdir}/cmake/Qt6

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cairo-ps)
BuildRequires:  pkgconfig(cairo-svg)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(poppler-data)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  qt6-qtbase-gui
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)

%description
%{name} is a PDF rendering library.

%package        devel
Summary:        Libraries and headers for poppler
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
You should install the poppler-devel package if you would like to
compile applications based on poppler.

%prep -a
chmod -x poppler/CairoFontEngine.cc

%install -a
# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang pdfsig --generate-subpackages

# just skip now, or will segfault.
%check
# export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig

%files -f pdfsig.lang
%doc README.md
%license COPYING
%{_libdir}/libpoppler.so.*
%{_libdir}/libpoppler-glib.so.8*
%{_libdir}/girepository-1.0/Poppler-0.18.typelib
%{_libdir}/libpoppler-qt6.so.3*
%{_libdir}/libpoppler-cpp.so.2*
%{_bindir}/pdf*
%{_mandir}/man1/*

%files devel
%{_libdir}/pkgconfig/poppler.pc
%{_libdir}/libpoppler.so
%dir %{_includedir}/poppler/
%{_includedir}/poppler/*.h
%{_includedir}/poppler/fofi/
%{_includedir}/poppler/goo/
%{_includedir}/poppler/splash/
%{_libdir}/pkgconfig/poppler-glib.pc
%{_libdir}/libpoppler-glib.so
%{_datadir}/gir-1.0/Poppler-0.18.gir
%{_includedir}/poppler/glib/
%{_libdir}/libpoppler-qt6.so
%{_libdir}/pkgconfig/poppler-qt6.pc
%{_includedir}/poppler/qt6/
%{_libdir}/pkgconfig/poppler-cpp.pc
%{_libdir}/libpoppler-cpp.so
%{_includedir}/poppler/cpp

%changelog
%autochangelog
