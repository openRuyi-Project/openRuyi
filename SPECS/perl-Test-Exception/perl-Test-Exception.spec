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
#!RemoteAsset:  sha256:156b13f07764f766d8b45a43728f2439af81a3512625438deab783b7883eb533
Source0:        https://www.cpan.org/authors/id/E/EX/EXODIST/Test-Exception-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
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

%files -f %{name}.files
%doc Changes

%changelog
%autochangelog
