# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

# Bytecode runtimes are mixed-mode images; stripping them destroys the
# interpreter. Skip debuginfo for the same reason.
%global debug_package %{nil}
%global __strip /bin/true

Name:           ocaml
Version:        5.4.1
Release:        %autorelease
Summary:        The OCaml programming language
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://ocaml.org/
VCS:            git:https://github.com/ocaml/ocaml.git
#!RemoteAsset:  sha256:d4528517aaa1a44b8e2b1bc109a1ed0a5e0014f3ddc4feb8906b11a7e063e89a
Source0:        https://github.com/ocaml/ocaml/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(libzstd)

Provides:       ocaml-runtime = %{version}-%{release}
Provides:       ocaml-compiler-libs = %{version}-%{release}

%description
OCaml is a functional, statically typed programming language from the
ML family. This package provides the bytecode and native-code compilers,
the runtime, and the standard library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Compiler libraries and extra development files for %{name}.

%prep
%autosetup -p1

%build
./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --libdir=%{_libdir}/ocaml \
    --mandir=%{_mandir} \
    --disable-ocamltest
%make_build

%install
%make_install
# Ship docs via %doc/%license from the source tree, not the make-install copies.
rm -rf %{buildroot}%{_docdir}/%{name}

%check
# ocamlc is a script with #!/usr/bin/ocamlrun; that path does not exist
# until the package is installed. Use the in-tree runtime and native
# compilers instead.
./runtime/ocamlrun -version
./ocamlc.opt -version
./ocamlopt.opt -version

%files
%doc README.adoc Changes README.win32.adoc
%license LICENSE
%{_bindir}/ocaml*
%{_libdir}/ocaml/
%exclude %{_libdir}/ocaml/compiler-libs
%{_mandir}/man1/ocaml*
%{_mandir}/man3/*.3o*

%files devel
%{_libdir}/ocaml/compiler-libs/

%changelog
%autochangelog
