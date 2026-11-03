# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rasqal
Version:        0.9.33
Release:        %autorelease
Summary:        RDF query parser and SPARQL engine
License:        (LGPL-2.1-or-later OR GPL-2.0-or-later OR Apache-2.0) AND Unlicense
URL:            https://librdf.org/rasqal/
VCS:            git:https://github.com/dajobe/rasqal.git
#!RemoteAsset:  sha256:6924c9ac6570bd241a9669f83b467c728a322470bf34f4b2da4f69492ccfd97c
Source0:        https://download.librdf.org/source/rasqal-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-regex-library=posix
BuildOption(conf):  --with-uuid-library=libuuid
BuildOption(conf):  --with-decimal=mpfr

BuildRequires:  make
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(raptor2) >= 2.0.7
BuildRequires:  pkgconfig(uuid)

%description
Rasqal parses and evaluates queries on RDF data. The roqet command runs
queries against local graphs and remote SPARQL endpoints.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%prep -a
sed -n '1,/\*\//p' libmtwist/mt.c > MTWIST-LICENSE.txt
grep -Fq "unlicense.org" MTWIST-LICENSE.txt

%files
%doc AUTHORS README
%license COPYING COPYING.LIB LICENSE.txt LICENSE-2.0.txt NOTICE MTWIST-LICENSE.txt
%{_bindir}/roqet
%{_libdir}/librasqal.so.*
%{_mandir}/man1/roqet.1*

%files devel
%doc %{_datadir}/gtk-doc/html/rasqal/
%{_bindir}/rasqal-config
%{_includedir}/rasqal/
%{_libdir}/librasqal.so
%{_libdir}/pkgconfig/rasqal.pc
%{_mandir}/man1/rasqal-config.1*
%{_mandir}/man3/librasqal.3*

%changelog
%autochangelog
