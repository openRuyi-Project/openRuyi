# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           hivex
Version:        1.3.24
Release:        %autorelease
Summary:        Windows Registry hive extraction library
License:        LGPL-2.1-or-later
URL:            https://libguestfs.org/
VCS:            git:https://github.com/libguestfs/hivex.git
#!RemoteAsset:  sha256:ad919b43b3b6da483bff475ec101581e97ebd2fd3309e2a0745d28bb6d3345d1
Source0:        https://github.com/libguestfs/hivex/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-perl
BuildOption(conf):  --disable-python
BuildOption(conf):  --disable-ruby
BuildOption(conf):  --enable-ocaml

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  ocaml
BuildRequires:  ocaml-devel
BuildRequires:  ocaml-findlib
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(readline)
BuildRequires:  perl

%description
Hivex is a library for reading and writing Windows Registry "hive"
files. It is used by libguestfs to inspect Windows virtual machines.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the headers and linker files needed to build
software against %{name}.

%package     -n ocaml-hivex
Summary:        OCaml bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-findlib

%description -n ocaml-hivex
OCaml bindings for %{name}. Required to build the libguestfs daemon.

%prep -a
autoreconf -fi
# GitHub tag archive omits generated headers, pods, and language bindings.
ocaml generator/generator.ml

%files
%doc README.md
%license LICENSE
%{_bindir}/hivexget
%{_bindir}/hivexml
%{_bindir}/hivexsh
%{_libdir}/libhivex.so.*
%{_datadir}/locale/*/LC_MESSAGES/hivex.mo
%{_mandir}/man1/hivexget.1*
%{_mandir}/man1/hivexml.1*
%{_mandir}/man1/hivexsh.1*

%files devel
%{_includedir}/hivex.h
%{_libdir}/libhivex.so
%{_libdir}/pkgconfig/hivex.pc
%{_mandir}/man3/hivex.3*

%files -n ocaml-hivex
%{_libdir}/ocaml/hivex/
%{_libdir}/ocaml/stublibs/dllmlhivex.so
%{_libdir}/ocaml/stublibs/dllmlhivex.so.owner

%changelog
%autochangelog
