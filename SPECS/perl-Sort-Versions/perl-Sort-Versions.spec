# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Sort-Versions
Version:        1.62
Release:        %autorelease
Summary:        Perl 5 module for sorting of revision-like numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Sort-Versions
#!RemoteAsset:  sha256:bf5f3307406ebe2581237f025982e8c84f6f6625dd774e457c03f8994efd2eaa
Source0:        https://www.cpan.org/authors/id/N/NE/NEILB/Sort-Versions-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
Sort::Versions allows easy sorting of mixed non-numeric and numeric
strings, like the 'version numbers' that many shared library systems and
revision control packages use. This is quite useful if you are trying to
deal with shared libraries. It can also be applied to applications that
intersperse variable-width numeric fields within text. Other applications
can undoubtedly be found.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
