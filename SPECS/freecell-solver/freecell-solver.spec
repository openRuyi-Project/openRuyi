# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           freecell-solver
Version:        6.16.0
Release:        %autorelease
Summary:        Command-line tool to solve Freecell and similar card solitaire games
License:        MIT
URL:            https://fc-solve.shlomifish.org
VCS:            git:https://github.com/shlomif/fc-solve
#!RemoteAsset:  sha256:71b8882e68f1be62529069018d0c732b75078669077c96348279575849f34313
Source0:        https://fc-solve.shlomifish.org/downloads/fc-solve/freecell-solver-%{version}.tar.xz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gperf
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(pysol-cards)
BuildRequires:  python3dist(freecell-solver)
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(pycotap)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(librinutils)
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  perl(autodie)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CHI)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(File::Find::Object)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Template)
BuildRequires:  perl(Text::Glob)
BuildRequires:  perl(Test::RunValgrind)
BuildRequires:  perl(Test::Data::Split)
BuildRequires:  perl(Test::TrailingSpace)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX)
BuildRequires:  perl(MooX::late)
BuildRequires:  perl(Env::Path)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Games::Solitaire::Verify)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(Number::Compare)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(Digest::JHash)
BuildRequires:  perl(MooX::Types::MooseLike::Numeric)
BuildRequires:  perl(Hash::MoreUtils)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Exception::Class)

%description
The Freecell Solver package contains the fc-solve executable which is
a command-line program that can be used to solve games of Freecell and
similar card solitaire variants.

This package also contains command line executables to generate the initial
boards of several popular Freecell implementations.

%package        devel
Summary: The Freecell Solver development tools for solving Freecell games
Requires: %{name}%{?_isa} = %{version}-%{release}

%description    devel
Freecell Solver is a library for automatically solving boards of Freecell and
similar variants of card Solitaire. This package contains the header files and
static libraries necessary for developing programs using Freecell Solver.

You should install it if you are a game developer who would like to use
Freecell Solver from within your programs.

%install -a
# Change fc_solve_find_index_s2ints.py to a Python module
bn="fc_solve_find_index_s2ints.py"
dest="%{buildroot}/%{python3_sitelib}"
src="%{buildroot}/%{_bindir}/$bn"
mkdir -p "$dest"
%__perl -0777 -p -e 's=\A#!/usr/bin/env python3\r?\n==' < "$src" > "$dest"/"$bn"
rm -f "$src"
rm -f %{buildroot}/%{_docdir}/%{name}/INSTALL
chmod a-x "$dest/$bn"
# Make the preset scripts executable
dir="%{buildroot}/%{_datadir}/freecell-solver/presets"
chmod a+x "${dir}"/*.sh
# Generate manpage for each program
dir="%{buildroot}/%{_mandir}/man6"
mkdir -p "${dir}"
for prog in "depth-dbm-fc-solver" ; do
    printf ".so man6/%s\\n" "dbm-fc-solver" > "${dir}/${prog}.6"
done

for prog in "freecell-solver-fc-pro-range-solve" "freecell-solver-multi-thread-solve" ; do
    printf ".so man6/%s\\n" "freecell-solver-range-parallel-solve" > "${dir}/${prog}.6"
done

# Delete static libraries
find %{buildroot} -name *.a -delete

%check
export FCS_TEST_WITHOUT_VALGRIND=1
%__rm -f t/t/py-flake8.t t/t/spelling.t t/t/tidyall.t
src="`pwd`"
cd "%{__cmake_builddir}"
perl "$src"/run-tests.pl

%files
%doc AUTHORS HACKING NEWS README TODO USAGE
%license %{_docdir}/freecell-solver/COPYING
%{_bindir}/dbm-fc-solver
%{_bindir}/depth-dbm-fc-solver
%{_bindir}/fc-solve
%{_bindir}/find-freecell-deal-index.py
%{_bindir}/freecell-solver-fc-pro-range-solve
%{_bindir}/freecell-solver-multi-thread-solve
%{_bindir}/freecell-solver-range-parallel-solve
%{_bindir}/gen-multiple-pysol-layouts
%{_bindir}/make_pysol_freecell_board.py
%{_bindir}/pi-make-microsoft-freecell-board
%{_bindir}/transpose-freecell-board.py
%{_libdir}/libfreecell-solver.so.0.7.0
%{_libdir}/libfreecell-solver.so.0
%{_datadir}/freecell-solver/presetrc
%{_datadir}/freecell-solver/presets/*
%{python3_sitelib}/fc_solve_find_index_s2ints{.py,.pyc,.pyo}
%{_mandir}/man6/*

%files devel
%{_includedir}/freecell-solver/*.h
%{_libdir}/pkgconfig/libfreecell-solver.pc
%{_libdir}/libfreecell-solver.so

%changelog
%autochangelog
