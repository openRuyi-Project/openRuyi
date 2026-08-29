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
#!RemoteAsset:  sha256:9d53ddfdc964cd8454cb0da4c695b6a3ae47b45839291c34cb9d8d1cfaab3202
Source0:        https://www.cpan.org/authors/id/P/PE/PETDANCE/Test-Memory-Cycle-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
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

%files -f %{name}.files
%doc Changes README.md

%changelog
%autochangelog
