# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Exception
Version:        0.43
Release:        %autorelease
Summary:        Test exception-based code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Exception
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/E/EX/EXODIST/Test-Exception-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.1
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Uplevel) >= 0.18
BuildRequires:  perl(Test::Builder) >= 0.7
BuildRequires:  perl(Test::Builder::Tester) >= 1.07
BuildRequires:  perl(Test::Harness) >= 2.03
BuildRequires:  perl(Test::More) >= 0.7
BuildRequires:  perl(warnings)

Requires:       perl(Sub::Uplevel) >= 0.18
Requires:       perl(Test::Builder) >= 0.7
Requires:       perl(Test::Builder::Tester) >= 1.07
Requires:       perl(Test::Harness) >= 2.03

%description
This module provides a few convenience methods for testing exception
based code. It is built with Test::Builder and plays happily with
Test::More and friends.

%prep
%setup -q -n Test-Exception-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes

%changelog
%autochangelog
