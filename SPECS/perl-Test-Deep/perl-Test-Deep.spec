# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Deep
Version:        1.205
Release:        %autorelease
Summary:        Extremely flexible deep comparison
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Deep
#!RemoteAsset:  sha256:42781e9943a7a215e662c4973b9feafdc019fd16469bdb849a8537ee58956273
Source0:        https://www.cpan.org/authors/id/R/RJ/RJBS/Test-Deep-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.12.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util) >= 1.09
BuildRequires:  perl(Scalar::Util) >= 1.09
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Tester) >= 0.107

Requires:       perl(List::Util) >= 1.09
Requires:       perl(Scalar::Util) >= 1.09
Requires:       perl(Test::More) >= 0.96

%description
If you don't know anything about automated testing in Perl then you should
probably read about Test::Simple and Test::More before preceding.
Test::Deep uses the Test::Builder framework.

%files -f %{name}.files
%doc Changes README TODO

%changelog
%autochangelog
