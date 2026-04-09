# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Memory-Cycle
Version:        1.06
Release:        %autorelease
Summary:        Test::Memory::Cycle Perl module
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Test-Memory-Cycle
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/P/PE/PETDANCE/Test-Memory-Cycle-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::Cycle) >= 1.07
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple) >= 0.62

Requires:       perl(Devel::Cycle) >= 1.07
Requires:       perl(Test::Simple) >= 0.62

%description
Test::Memory::Cycle Perl module

%prep
%setup -q -n Test-Memory-Cycle-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md

%changelog
%autochangelog
