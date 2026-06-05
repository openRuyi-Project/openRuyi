# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Business-ISSN
Version:        1.008
Release:        %autorelease
Summary:        Perl extension for International Standard Serial Numbers
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Business-ISSN
#!RemoteAsset:  sha256:b16b3a1b0e53cd45ed3328906d33ad4d59a13b57abf341424553aecf3e443aac
Source0:        https://www.cpan.org/authors/id/B/BR/BRIANDFOY/Business-ISSN-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 1

%description
new($issn)

%files -f %{name}.files
%doc Changes CITATION.cff INSTALL.SKIP SECURITY.md

%changelog
%autochangelog
