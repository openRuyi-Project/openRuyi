# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Sub-Quote
Version:        2.006009
Release:        %autorelease
Summary:        Efficient generation of subroutines via string eval
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Sub-Quote
#!RemoteAsset:  sha256:967282d54d2d51b198c67935594f93e4dea3e54d1e5bced158c94e29be868a4b
Source0:        https://www.cpan.org/authors/id/H/HA/HAARG/Sub-Quote-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::More) >= 0.94

%description
This package provides performant ways to generate subroutines from strings.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
