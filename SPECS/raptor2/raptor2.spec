# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global libxslt_requirement pkgconfig(libxslt) > 1.0.18

Name:           raptor2
Version:        2.0.16
Release:        %autorelease
Summary:        RDF syntax parser and serializer
License:        (LGPL-2.1-or-later OR GPL-2.0-or-later OR Apache-2.0) AND LicenseRef-openRuyi-Public-Domain
URL:            https://librdf.org/raptor/
VCS:            git:https://github.com/dajobe/raptor.git
#!RemoteAsset:  sha256:089db78d7ac982354bdbf39d973baf09581e6904ac4c92a98c5caadb3de44680
Source0:        https://download.librdf.org/source/raptor2-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
# RDF parser and serializer checks share per-input .res and .err files.
BuildOption(check):  -j1

BuildRequires:  bison
BuildRequires:  perl
BuildRequires:  make
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  %{libxslt_requirement}

%patchlist
# https://github.com/dajobe/raptor/commit/4dbc4c1da2a033c497d84a1291c46f416a9cac51
0001-libxml2-2.11-entity-layout.patch
# https://github.com/dajobe/raptor/commit/da7a79976bd0314c23cce55d22495e7d29301c44
1000-CVE-2024-57823-uri-normalization.patch
# https://github.com/dajobe/raptor/commit/ece2c79df43091686a538b8231cf387d84bfa60e
1001-CVE-2024-57822-ntriples-bnode.patch
# Downstream fix for parser reuse with the 2.0.16 Turtle chunk reader.
# https://github.com/dajobe/raptor/blob/raptor2_2_0_16/src/turtle_parser.y
2000-reset-turtle-state-for-the-next-document.patch

%description
Raptor reads and writes RDF graphs in formats including RDF/XML, Turtle
and N-Triples. The rapper utility converts between supported syntaxes.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%prep -a
(cd src && bison -o turtle_parser.c turtle_parser.y && perl ../scripts/fix-bison.pl turtle_parser.c)

%files
%doc AUTHORS README
%license COPYING COPYING.LIB LICENSE.txt LICENSE-2.0.txt NOTICE
%{_bindir}/rapper
%{_libdir}/libraptor2.so.*
%{_mandir}/man1/rapper.1*

%files devel
%doc %{_datadir}/gtk-doc/html/raptor2/
%{_includedir}/raptor2/
%{_libdir}/libraptor2.so
%{_libdir}/pkgconfig/raptor2.pc
%{_mandir}/man3/libraptor2.3*

%changelog
%autochangelog
