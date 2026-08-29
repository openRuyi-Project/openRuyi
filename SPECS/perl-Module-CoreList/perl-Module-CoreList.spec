# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Module-CoreList
Version:        5.20260601
Release:        %autorelease
Summary:        What modules shipped with versions of perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Module-CoreList
#!RemoteAsset:  sha256:b3c70d3e868c3cd230f558c4d2774bfd56777c9d4c1414867ef8bd28b9be7496
Source0:        https://www.cpan.org/authors/id/B/BI/BINGOS/Module-CoreList-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version) >= 0.88

Requires:       perl(version) >= 0.88

%description
Module::CoreList provides information on which core and dual-life modules
shipped with each version of perl.

%files -f %{name}.files
%doc Changes corelist identify-dependencies README

%changelog
%autochangelog
