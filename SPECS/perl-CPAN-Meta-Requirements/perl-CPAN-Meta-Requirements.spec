# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-CPAN-Meta-Requirements
Version:        2.143
Release:        %autorelease
Summary:        Set of version requirements for a CPAN dist
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/CPAN-Meta-Requirements
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/CPAN-Meta-Requirements-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.10.0
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version) >= 0.88
BuildRequires:  perl(warnings)

Requires:       perl(version) >= 0.88

%description
A CPAN::Meta::Requirements object models a set of version constraints like
those specified in the META.yml or META.json files in CPAN distributions,
and as defined by CPAN::Meta::Spec. It can be built up by adding more and
more constraints, and it will reduce them to the simplest representation.

%prep
%setup -q -n CPAN-Meta-Requirements-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.mkdn perlcritic.rc README

%changelog
%autochangelog
