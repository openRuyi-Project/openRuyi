# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-experimental
Version:        0.036
Release:        %autorelease
Summary:        Experimental features made easy
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/experimental
#!RemoteAsset:  sha256:42612937c20f0c758547d0519bf535d7f378aa2a01fb20453b2a015a14d6720c
Source0:        https://www.cpan.org/authors/id/L/LE/LEONT/experimental-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.89
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)

%description
This pragma provides an easy and convenient way to enable or disable
experimental features.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
