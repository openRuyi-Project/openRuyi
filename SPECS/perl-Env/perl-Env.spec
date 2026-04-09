# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Env
Version:        1.04
Release:        %autorelease
Summary:        Perl module that imports environment variables as scalars or arrays
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Env
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/F/FL/FLORA/Env-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Tie::Array)

%description
Perl maintains environment variables in a special hash named %ENV. For when
this access method is inconvenient, the Perl module Env allows environment
variables to be treated as scalar or array variables.

%prep
%setup -q -n Env-%{version}

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
