# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Scalar-Properties
Version:        1.100860
Release:        %autorelease
Summary:        Run-time properties on scalar variables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Scalar-Properties
#!RemoteAsset:  sha256:d1a7010d7871d8abfe72d4c1cf72e33780a6ef0ebc6acb0d2e6a44b9933f0a92
Source0:        https://www.cpan.org/authors/id/M/MA/MARCEL/Scalar-Properties-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(Test::More) >= 0.88

%description
Scalar::Properties attempts to make Perl more object-oriented by taking an
idea from Ruby: Everything you manipulate is an object, and the results of
those manipulations are objects themselves.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
