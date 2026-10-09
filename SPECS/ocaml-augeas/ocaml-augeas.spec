# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global debug_package %{nil}
# test_augeas.ml must compile after augeas.cmi; parallel make races.
%global _smp_mflags -j1

Name:           ocaml-augeas
Version:        0.7
Release:        %autorelease
Summary:        OCaml bindings for Augeas
License:        LGPL-2.1-or-later
URL:            https://libguestfs.org/
VCS:            git:https://github.com/libguestfs/libguestfs.git
#!RemoteAsset:  sha256:ee3899c85d5b22cdcc659183e571add0980725a8a705a9fe7bf53ddc2ba2dd63
Source0:        https://download.libguestfs.org/ocaml-augeas/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ocaml
BuildRequires:  ocaml-devel
BuildRequires:  ocaml-findlib
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(augeas)
BuildRequires:  pkgconfig(libxml-2.0)

Requires:       ocaml-findlib
Requires:       augeas%{?_isa}

%description
OCaml bindings for the Augeas configuration-editing library. Required
to build the libguestfs daemon.

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
mkdir -p ${OCAMLFIND_DESTDIR}
%make_install

%files
%license COPYING.LIB
%{_libdir}/ocaml/augeas/

%changelog
%autochangelog
