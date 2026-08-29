# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Business-ISMN
Version:        1.205
Release:        %autorelease
Summary:        Work with International Standard Music Numbers
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Business-ISMN
#!RemoteAsset:  sha256:1c48e9b00bc32578b2176e6f79c4a11713d875befa8fbb7f48b7a9c8172fe8bd
Source0:        https://www.cpan.org/authors/id/B/BR/BRIANDFOY/Business-ISMN-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(Tie::Cycle) >= 1.21
BuildRequires:  perl(version) >= 0.86

Requires:       perl(Tie::Cycle) >= 1.21

%description
Methods

%files -f %{name}.files
%doc Changes INSTALL.SKIP ismns.txt SECURITY.md

%changelog
%autochangelog
