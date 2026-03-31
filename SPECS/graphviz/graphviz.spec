# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           graphviz
Summary:        Graph Visualization Tools
Version:        14.0.4
Release:        %autorelease
License:        EPL-1.0 AND CPL-1.0 AND BSD-3-Clause AND MIT AND GPL-3.0-or-later
URL:            http://www.graphviz.org/
VCS:            git:https://gitlab.com/graphviz/graphviz
#!RemoteAsset
Source:         https://gitlab.com/graphviz/graphviz/-/archive/%{version}/graphviz-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-dependency-tracking
BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --without-mylibgd
BuildOption(conf):  --with-ipsepcola
BuildOption(conf):  --with-pangocairo
BuildOption(conf):  --with-gdk-pixbuf
BuildOption(conf):  --enable-lefty
BuildOption(conf):  --without-lasi
BuildOption(conf):  --without-gtk
BuildOption(conf):  --without-qt
BuildOption(conf):  --without-gts
BuildOption(conf):  --without-smyrna
BuildOption(conf):  --without-ming
BuildOption(conf):  --without-devil
BuildOption(conf):  --disable-sharp
BuildOption(conf):  --disable-r
BuildOption(conf):  --disable-java
BuildOption(conf):  --disable-php
BuildOption(conf):  --disable-guile
BuildOption(conf):  --disable-ruby
BuildOption(conf):  --disable-lua
BuildOption(conf):  --disable-tcl
BuildOption(conf):  --disable-go
BuildOption(conf):  --enable-python=yes
BuildOption(conf):  --disable-lefty

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(freetype2) >= 2
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(cairo) >= 1.1.10
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xext)
BuildRequires:  python3-devel
BuildRequires:  swig >= 1.3.33

%description
A collection of tools for the manipulation and layout of graphs (as in nodes
and edges, not as in barcharts).

%package        libs
Summary:        Graphviz libraries

%description    libs
Graphviz libraries.

%package        devel
Summary:        Development package for graphviz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains development files for graphviz.

%package        python3
Summary:        Python 3 extension for graphviz
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    python3
Python 3 extension for graphviz.

%conf -p
./autogen.sh

%install -a
install -m0644 README %{buildroot}%{_docdir}/%{name}

find %{buildroot}%{_datadir}/%{name}/demo -type f -exec chmod a-x {} ';'
mv %{buildroot}%{_datadir}/%{name}/demo %{buildroot}%{_docdir}/%{name}/
find %{buildroot}%{_docdir}/%{name}/demo -type f -name "*.py" -exec mv {} {}.demo ';'

rm -f %{buildroot}%{_bindir}/dot_builtins
rm -rf %{buildroot}%{_datadir}/graphviz/graphs

mkdir -p %{buildroot}%{_libdir}/graphviz
touch %{buildroot}%{_libdir}/graphviz/config6

mkdir -p %{buildroot}%{_datadir}/%{name}/examples

%transfiletriggerin -- %{_libdir}/graphviz
%{_bindir}/dot -c 2>/dev/null || :

%transfiletriggerpostun -- %{_libdir}/graphviz
%{_bindir}/dot -c 2>/dev/null || :

%files
%license COPYING
%doc %{_docdir}/graphviz
%{_bindir}/*
%dir %{_libdir}/graphviz
%{_libdir}/graphviz/*.so.*
%{_prefix}/lib/perl5/vendor_perl/*
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*
%dir %{_datadir}/graphviz
%exclude %{_docdir}/graphviz/demo
%{_datadir}/graphviz/gvpr
%{_datadir}/graphviz/examples
%ghost %{_libdir}/graphviz/config6
%doc %{_docdir}/graphviz/demo

%exclude %{_libdir}/graphviz/*/*
%exclude %{_libdir}/graphviz/libgvplugin_gd.*

%files libs
%license COPYING
%{_libdir}/libcdt.so.*
%{_libdir}/libcgraph.so.*
%{_libdir}/libgvc.so.*
%{_libdir}/libgvpr.so.*
%{_libdir}/libpathplan.so.*
%{_libdir}/libxdot.so.*
%{_libdir}/graphviz/libgvplugin_gd.so.*

%files devel
%{_includedir}/graphviz
%{_libdir}/*.so
%{_libdir}/graphviz/*.so
%{_libdir}/pkgconfig/libcdt.pc
%{_libdir}/pkgconfig/libcgraph.pc
%{_libdir}/pkgconfig/libgvc.pc
%{_libdir}/pkgconfig/libgvpr.pc
%{_libdir}/pkgconfig/libpathplan.pc
%{_libdir}/pkgconfig/libxdot.pc
%{_mandir}/man3/*.3*

%files python3
%{python3_sitearch}/*
%{_mandir}/man3/gv.3python*

%changelog
%{?autochangelog}
