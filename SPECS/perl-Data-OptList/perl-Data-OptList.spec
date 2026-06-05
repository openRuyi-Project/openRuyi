# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Data-OptList
Version:        0.114
Release:        %autorelease
Summary:        Parse and validate simple name/value option pairs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Data-OptList
#!RemoteAsset:  sha256:9fd1093b917a21fb79ae1607db53d113b4e0ad8fe0ae776cb077a7e50044fdf3
Source0:        https://www.cpan.org/authors/id/R/RJ/RJBS/Data-OptList-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.12.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Install) >= 0.921
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(warnings)

Requires:       perl(Sub::Install) >= 0.921

%description
Hashes are great for storing named data, but if you want more than one
entry for a name, you have to use a list of pairs. Even then, this is
really boring to write:

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
