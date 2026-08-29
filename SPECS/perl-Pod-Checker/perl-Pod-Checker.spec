# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Pod-Checker
Version:        1.77
Release:        %autorelease
Summary:        Check pod documents for syntax errors
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Pod-Checker
#!RemoteAsset:  sha256:131a7c049bed758cab29901792c999ca315d4e881c630d3f93bf6aae69e9e242
Source0:        https://www.cpan.org/authors/id/M/MA/MAREKR/Pod-Checker-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Pod::Simple) >= 3.4
BuildRequires:  perl(Test::More) >= 0.6

Requires:       perl(Pod::Simple) >= 3.4
Requires:       perl(Test::More) >= 0.6

%description
podchecker will perform syntax checking of Perl5 POD format documentation.

%files -f %{name}.files
%doc CHANGES README

%changelog
%autochangelog
