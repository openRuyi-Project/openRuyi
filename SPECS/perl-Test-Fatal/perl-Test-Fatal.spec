# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Fatal
Version:        0.018
Release:        %autorelease
Summary:        Incredibly simple helpers for testing code with exceptions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Fatal
#!RemoteAsset:  sha256:b8d2cccf9ee467271bc478f9cf7eba49545452be9302ae359bc538b8bf687cd6
Source0:        https://www.cpan.org/authors/id/R/RJ/RJBS/Test-Fatal-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.12.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More) >= 0.65
BuildRequires:  perl(Try::Tiny) >= 0.07
BuildRequires:  perl(warnings)

Requires:       perl(Exporter) >= 5.57
Requires:       perl(Try::Tiny) >= 0.07

%description
Test::Fatal is an alternative to the popular Test::Exception. It does much
less, but should allow greater flexibility in testing exception-throwing
code with about the same amount of typing.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
