# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Math-BigInt
Version:        2.005003
Release:        %autorelease
Summary:        Arbitrary size integer math package
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Math-BigInt
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/P/PJ/PJACKLAM/Math-BigInt-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.1
BuildRequires:  perl(Carp) >= 1.22
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::Complex) >= 1.36
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.94

Requires:       perl(Carp) >= 1.22
Requires:       perl(Math::Complex) >= 1.36

%description
Math::BigInt provides support for arbitrary precision integers. Overloading
is also provided for Perl operators.

%prep
%setup -q -n Math-BigInt-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc BUGS CHANGES CREDITS GOALS HISTORY NEW README README.md TODO

%changelog
%autochangelog
