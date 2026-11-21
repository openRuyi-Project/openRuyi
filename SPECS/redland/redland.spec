# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           redland
Version:        1.0.17
Release:        %autorelease
Summary:        RDF graph storage and query library
License:        LGPL-2.1-or-later OR GPL-2.0-or-later OR Apache-2.0
URL:            https://librdf.org/
VCS:            git:https://github.com/dajobe/librdf.git
#!RemoteAsset:  sha256:de1847f7b59021c16bdc72abb4d8e2d9187cd6124d69156f3326dd34ee043681
Source0:        https://download.librdf.org/source/redland-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-storages="hashes memory file"
# The default BDB search covers only versions through 5.3 and the lib directory.
BuildOption(conf):  --with-bdb=%{_prefix}
BuildOption(conf):  --with-bdb-lib=%{_libdir}
BuildOption(conf):  --with-bdb-include=%{_includedir}
BuildOption(conf):  --with-bdb-dbname=db

BuildRequires:  db-devel
BuildRequires:  make
BuildRequires:  pkgconfig(raptor2) >= 2.0.7
BuildRequires:  pkgconfig(rasqal) >= 0.9.25
BuildRequires:  pkgconfig(rasqal) <= 0.9.99

%description
Redland stores RDF statements and evaluates SPARQL queries through a C
interface. It uses Raptor for parsing and serialization and Rasqal for
query evaluation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc AUTHORS README
%license COPYING COPYING.LIB LICENSE.txt LICENSE-2.0.txt NOTICE
%{_bindir}/rdfproc
%{_bindir}/redland-db-upgrade
%{_libdir}/librdf.so.*
%{_mandir}/man1/rdfproc.1*
%{_mandir}/man1/redland-db-upgrade.1*

%files devel
%doc %{_datadir}/gtk-doc/html/redland/
%{_bindir}/redland-config
%{_includedir}/librdf.h
%{_includedir}/rdf_*.h
%{_includedir}/redland.h
%{_libdir}/librdf.so
%{_libdir}/pkgconfig/redland.pc
%dir %{_datadir}/redland
%{_datadir}/redland/Redland.i
%{_mandir}/man1/redland-config.1*
%{_mandir}/man3/redland.3*

%changelog
%autochangelog
