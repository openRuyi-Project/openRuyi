# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Math-BigInt-FastCalc
Version:        0.5020
Release:        %autorelease
Summary:        Math::BigInt::Calc with some XS for more speed
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Math-BigInt-FastCalc
#!RemoteAsset:  sha256:6dfd72e784e612aab46136532a609c0b77a5b0b7854ab837682d64fb1af2a74e
Source0:        https://www.cpan.org/authors/id/P/PJ/PJACKLAM/Math-BigInt-FastCalc-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.1
BuildRequires:  perl(Carp) >= 1.22
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::BigInt) >= 2.005001
BuildRequires:  perl(Test::More) >= 0.82
BuildRequires:  perl(XSLoader)

Requires:       perl(Carp) >= 1.22
Requires:       perl(Math::BigInt) >= 2.005001

%description
Math::BigInt::FastCalc inherits from Math::BigInt::Calc.

%files -f %{name}.files
%doc CHANGES CREDITS README README.md TODO

%changelog
%autochangelog
