# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-CPAN-Meta
Version:        0.25
Release:        %autorelease
Summary:        Validate your CPAN META.yml files
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Test-CPAN-Meta
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/B/BA/BARBIE/Test-CPAN-Meta-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Parse::CPAN::Meta) >= 0.02
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More) >= 0.70
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 0.08

Requires:       perl(Parse::CPAN::Meta) >= 0.02
Requires:       perl(Test::Pod) >= 1.00
Requires:       perl(Test::Pod::Coverage) >= 0.08

%description
This distribution was written to ensure that a META.yml file, provided with
a standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of package makers
and installers such as ExtUtils::MakeMaker, Module::Build and
Module::Install.

%prep
%setup -q -n Test-CPAN-Meta-%{version}

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
