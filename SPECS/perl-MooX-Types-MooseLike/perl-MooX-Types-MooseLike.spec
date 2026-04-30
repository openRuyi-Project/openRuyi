# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-MooX-Types-MooseLike
Version:        0.29
Release:        %autorelease
Summary:        Some Moosish types and a type builder
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/MooX-Types-MooseLike
#!RemoteAsset:  sha256:1d3780aa9bea430afbe65aa8c76e718f1045ce788aadda4116f59d3b7a7ad2b4
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATEU/MooX-Types-MooseLike-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Runtime) >= 0.014
BuildRequires:  perl(Moo) >= 1.004002
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(strictures) >= 2
Requires:       perl(Module::Runtime) >= 0.014
Requires:       perl(strictures) >= 2

%description
This module provides a possibility to build your own set of Moose-like
types. These custom types can then be used to describe fields in Moo-
based classes.

%prep
%setup -q -n MooX-Types-MooseLike-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license

%changelog
%autochangelog
