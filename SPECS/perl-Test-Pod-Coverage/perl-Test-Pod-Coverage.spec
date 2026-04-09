# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Pod-Coverage
Version:        1.10
Release:        %autorelease
Summary:        Check for pod coverage in your distribution
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Test-Pod-Coverage
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/N/NE/NEILB/Test-Pod-Coverage-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(lib)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
Test::Pod::Coverage is used to create a test for your distribution, to
ensure that all relevant files in your distribution are appropriately
documented in pod.

%prep
%setup -q -n Test-Pod-Coverage-%{version}

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
