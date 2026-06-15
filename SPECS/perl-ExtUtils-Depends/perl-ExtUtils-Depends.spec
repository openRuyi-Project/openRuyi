# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-ExtUtils-Depends
Version:        0.8002
Release:        %autorelease
Summary:        Easily build XS extensions that depend on XS extensions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/ExtUtils-Depends
#!RemoteAsset:  sha256:02b9a46450050ce19b325b23e46bb4ec644229d7f2d95044f67a86d8efacdc29
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/ExtUtils-Depends-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.44
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(ExtUtils::MakeMaker) >= 7.44

%description
ExtUtils::Depends helps XS extensions declare and consume build information
from other XS extensions.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
