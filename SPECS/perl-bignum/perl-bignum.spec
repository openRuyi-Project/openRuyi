# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-bignum
Version:        0.67
Release:        %autorelease
Summary:        Transparent big number support for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/bignum
#!RemoteAsset:  sha256:1c9a824ab323e3e58d9808011c10ad27589dba1202806278215012ca7f522875
Source0:        https://www.cpan.org/authors/id/P/PJ/PJACKLAM/bignum-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp) >= 1.22
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::BigInt) >= 1.99983
BuildRequires:  perl(Math::BigRat) >= 0.2623
BuildRequires:  perl(Test::More) >= 0.94

Requires:       perl(Carp) >= 1.22
Requires:       perl(Math::BigInt) >= 1.99983
Requires:       perl(Math::BigRat) >= 0.2623

%description
Literal numeric constants

%files -f %{name}.files
%doc BUGS CHANGES README README.md TODO

%changelog
%autochangelog
