# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-SubCalls
Version:        1.10
Release:        %autorelease
Summary:        Track the number of times subs are called
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-SubCalls
#!RemoteAsset:  sha256:cbc1e9b35a05e71febc13e5ef547a31c8249899bb6011dbdc9d9ff366ddab6c2
Source0:        https://www.cpan.org/authors/id/E/ET/ETHER/Test-SubCalls-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Hook::LexWrap) >= 0.20
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

Requires:       perl(File::Spec) >= 0.80
Requires:       perl(Hook::LexWrap) >= 0.20
Requires:       perl(Test::More) >= 0.42

%description
There are a number of different situations (like testing caching code)
where you want to want to do a number of tests, and then verify that
some underlying subroutine deep within the code was called a specific
number of times.

%files -f %{name}.files
%doc Changes CONTRIBUTING README

%changelog
%autochangelog
