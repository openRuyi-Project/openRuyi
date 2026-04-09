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
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/P/PJ/PJACKLAM/bignum-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
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

%prep
%setup -q -n bignum-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc BUGS CHANGES README README.md TODO

%changelog
%autochangelog
