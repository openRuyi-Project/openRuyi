# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-namespace-autoclean
Version:        0.31
Release:        %autorelease
Summary:        Keep imports out of your namespace
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/namespace-autoclean
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/namespace-autoclean-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(B)
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.12
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(namespace::clean) >= 0.20
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(warnings)

Requires:       perl(B::Hooks::EndOfScope) >= 0.12
Requires:       perl(namespace::clean) >= 0.20

%description
When you import a function into a Perl package, it will naturally also be
available as a method.

%prep
%setup -q -n namespace-autoclean-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README

%changelog
%autochangelog
