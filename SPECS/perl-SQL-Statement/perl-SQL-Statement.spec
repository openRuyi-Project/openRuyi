# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-SQL-Statement
Version:        1.414
Release:        %autorelease
Summary:        SQL parsing and processing engine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/SQL-Statement
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RE/REHSACK/SQL-Statement-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone) >= 0.30
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::Base::Convert)
BuildRequires:  perl(Math::Complex) >= 1.56
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Params::Util) >= 1.00
BuildRequires:  perl(Scalar::Util) >= 1.0
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Text::Soundex) >= 3.04

Requires:       perl(Clone) >= 0.30
Requires:       perl(Math::Complex) >= 1.56
Requires:       perl(Params::Util) >= 1.00
Requires:       perl(Scalar::Util) >= 1.0
Requires:       perl(Text::Soundex) >= 3.04

%description
The SQL::Statement module implements a pure Perl SQL parsing and execution
engine. While it by no means implements full ANSI standard, it does support
many features including column and table aliases, built-in and user-defined
functions, implicit and explicit joins, complex nested search conditions,
and other features.

%prep
%setup -q -n SQL-Statement-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ARTISTIC-1.0 Changes GPL-1 GPL-2.0 README README.md

%changelog
%autochangelog
