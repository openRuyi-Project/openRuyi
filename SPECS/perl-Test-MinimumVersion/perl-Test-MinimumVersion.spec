# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-MinimumVersion
Version:        0.101083
Release:        %autorelease
Summary:        Test::MinimumVersion Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-MinimumVersion
#!RemoteAsset:  sha256:32a1ebcd803fa10eefca553bc3cedd43596a759dc3975adebd22688823c36aea
Source0:        https://www.cpan.org/authors/id/R/RJ/RJBS/Test-MinimumVersion-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(base)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Find::Rule::Perl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Perl::MinimumVersion) >= 1.32
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(version) >= 0.70
BuildRequires:  perl(warnings)
BuildRequires:  perl(Number::Compare)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(YAML::PP)
BuildRequires:  perl(PPIx::Utils)

Requires:       perl(Perl::MinimumVersion) >= 1.32
Requires:       perl(version) >= 0.70

%description
Test::MinimumVersion Perl module

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
