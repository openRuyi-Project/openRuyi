# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global debug_package %{nil}
%global __strip /bin/true
%global srcname ocamlfind

Name:           ocaml-findlib
Version:        1.9.8
Release:        %autorelease
Summary:        OCaml library manager
License:        MIT
URL:            https://github.com/ocaml/ocamlfind
VCS:            git:https://github.com/ocaml/ocamlfind.git
#!RemoteAsset:  sha256:d6899935ccabf67f067a9af3f3f88d94e310075d13c648fa03ff498769ce039d
Source0:        https://github.com/ocaml/ocamlfind/archive/refs/tags/findlib-%{version}.tar.gz#/%{srcname}-findlib-%{version}.tar.gz

BuildRequires:  ocaml
# topfind.cmo needs Toploop/Topdirs from compiler-libs.
BuildRequires:  ocaml-devel
# ocamlc -custom links a runtime that was built against zstd.
BuildRequires:  pkgconfig(libzstd)

Provides:       ocamlfind = %{version}-%{release}
Requires:       ocaml
Requires:       ocaml-devel

%description
Findlib is a library manager for OCaml. It provides a convention for
storing and referencing OCaml libraries, and the ocamlfind command
used to compile against those libraries.

%prep
%autosetup -p1 -n %{srcname}-findlib-%{version}

%build
./configure \
    -bindir %{_bindir} \
    -mandir %{_mandir} \
    -sitelib %{_libdir}/ocaml \
    -config %{_sysconfdir}/findlib.conf
# findlib's makefile is not safe for parallel make.
%make_build -j1 all
%make_build -j1 opt

%install
# findlib's Makefile honours prefix as the install root.
make prefix=%{buildroot} install
# Native ocamlfind is installed as ocamlfind; keep ocamlfind_opt as a copy
# when the opt backend was built.
if [ -f src/findlib/ocamlfind_opt ]; then
    install -p -m 0755 src/findlib/ocamlfind_opt %{buildroot}%{_bindir}/ocamlfind_opt
fi

%files
%doc README.md
%license LICENSE
%config(noreplace) %{_sysconfdir}/findlib.conf
%{_bindir}/ocamlfind
%{_bindir}/ocamlfind_opt
%{_libdir}/ocaml/findlib/
%{_libdir}/ocaml/topfind
%{_libdir}/ocaml/bytes/

%changelog
%autochangelog
