# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Sub-Exporter
Version:        0.991
Release:        %autorelease
Summary:        Sophisticated exporter for custom-built routines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Sub-Exporter
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Sub-Exporter-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.12.0
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::OptList) >= 0.100
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::Util) >= 0.14
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Install) >= 0.92
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(warnings)

Requires:       perl(Data::OptList) >= 0.100
Requires:       perl(Params::Util) >= 0.14
Requires:       perl(Sub::Install) >= 0.92

%description
Sub::Exporter provides a sophisticated alternative to Exporter.pm. It allows
for renaming, currying/sub-generation, and other cool stuff.

%prep
%setup -q -n Sub-Exporter-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
