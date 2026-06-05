# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Filter
Version:        1.65
Release:        %autorelease
Summary:        Filter Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Filter
#!RemoteAsset:  sha256:cb70da7ae5e19138a0b22fb3b6387c3ae697a3cd3f3f6ecde425152e9124d1e6
Source0:        http://www.cpan.org/authors/id/R/RU/RURBAN/Filter-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Filter::Simple) >= 0.88
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(Filter::Simple) >= 0.88
Requires:       perl(Test::More) >= 0.88

%description
Source filters alter the program text of a module before Perl sees it, much as
a C preprocessor alters the source text of a C program before the compiler
sees it.

%files -f %{name}.files
%doc Changes mytest README

%changelog
%autochangelog
