# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           black-hole-solver
Version:        1.14.0
Release:        %autorelease
Summary:        A solver for Black Hole Solitaire and similar card games
License:        MIT
URL:            https://www.shlomifish.org/open-source/projects/black-hole-solitaire-solver/
VCS:            git:https://github.com/shlomif/black-hole-solitaire.git
#!RemoteAsset:  sha256:5c47bd093dbb160f4b090fd670ab7c12b4371d39b17b3bbd8c6c4a12975557c0
Source0:        https://fc-solve.shlomifish.org/downloads/fc-solve/black-hole-solver-%{version}.tar.xz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  python3
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  cmake(Rinutils)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Env::Path)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::RunValgrind)
BuildRequires:  perl(Test::Some)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Dir::Manifest)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Data::Dump)

%description
This is a solver, written in C, to solve Golf solitaire,
the Solitaire variant called “Black Hole” and the one called “All in a Row”.
It provides a portable C library, and a command line application that after being
fed with a layout will emit the cards to move.

%package        libs
Summary:        Development files for %{name}

%description    libs
The %{name}-libs package contains the shared libraries for %{name},
a solver for Black Hole Solitaire and similar card games.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%check -p
rm -f t/valgrind.t
rm -f t/clang-format.t
rm -f t/perltidy.t
rm -f t/style-trailing-space.t

%files
%doc README.md NEWS.asciidoc
%license COPYING
%{_bindir}/black-hole-solve
%{_mandir}/*/*

%files libs
%{_libdir}/libblack_hole_solver.so.*

%files devel
%{_libdir}/libblack_hole_solver.so
%{_includedir}/black-hole-solver/
%{_libdir}/pkgconfig/libblack-hole-solver.pc

%changelog
%autochangelog
