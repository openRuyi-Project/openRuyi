# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libcaca
Version:        0.99.beta20
Release:        %autorelease
Summary:        Colour ASCII Art Library, text mode graphics
License:        WTFPL
URL:            https://github.com/cacalabs/libcaca
#!RemoteAsset:  sha256:ff9aa641af180a59acedc7fc9e663543fb397ff758b5122093158fd628125ac1
Source0:        https://github.com/cacalabs/libcaca/releases/download/v%{version}/libcaca-%{version}.tar.bz2
BuildSystem:    autotools

# just change to fix the compile error.
Patch0:         0001-fix-c99.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-csharp
BuildOption(conf):  --disable-java
BuildOption(conf):  --enable-python
BuildOption(conf):  --enable-gl
BuildOption(conf):  --enable-x11
BuildOption(conf):  --disable-ruby
BuildOption(conf):  --enable-doc
BuildOption(build):  CFLAGS="%{optflags} -Wno-error=implicit-function-declaration -Wno-error=int-conversion"

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(slang)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(glu)
BuildRequires:  doxygen

%description
libcaca is the Colour AsCii Art library. It provides high level functions for
color text drawing, simple primitives for line, polygon and ellipse drawing, as
well as powerful image to text conversion routines.

%package        devel
Summary:        Development files for libcaca
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files needed to compile applications or shared
objects that use libcaca.

%package     -n python-caca
Summary:        Python bindings for libcaca
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildArch:      noarch
Provides:       python3-caca
%python_provide python3-caca

%description -n python-caca
This package contains the python bindings for using libcaca from python.

%files
%license COPYING*
%doc AUTHORS NEWS NOTES README THANKS
%{_bindir}/cacaclock
%{_bindir}/cacademo
%{_bindir}/cacafire
%{_bindir}/cacaview
%{_bindir}/img2txt
%{_bindir}/cacaplay
%{_bindir}/cacaserver
%{_datadir}/libcaca/
%{_mandir}/man1/cacademo.1*
%{_mandir}/man1/cacafire.1*
%{_mandir}/man1/cacaplay.1*
%{_mandir}/man1/cacaserver.1*
%{_mandir}/man1/cacaview.1*
%{_mandir}/man1/img2txt.1*
%{_libdir}/libcaca.so.*
%{_libdir}/libcaca++.so.*

%files devel
%{_docdir}/libcaca-dev/html
%{_bindir}/caca-config
%{_includedir}/caca.h
%{_includedir}/caca++.h
%{_includedir}/caca0.h
%{_includedir}/caca_conio.h
%{_includedir}/caca_types.h
%{_libdir}/pkgconfig/caca.pc
%{_libdir}/pkgconfig/caca++.pc
%{_libdir}/libcaca.so
%{_libdir}/libcaca++.so
%{_mandir}/man1/caca-config.1*
%{_mandir}/man3/*

%files -n python-caca
%doc python/examples
%{python3_sitelib}/caca/

%changelog
%autochangelog
