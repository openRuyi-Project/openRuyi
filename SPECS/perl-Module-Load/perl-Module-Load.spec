# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Module-Load
Version:        0.36
Release:        %autorelease
Summary:        Runtime require of both modules and files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Module-Load
#!RemoteAsset:  sha256:d825020ac00b220e89f9524e24d838f9438b072fcae8c91938e4026677bef6e0
Source0:        https://www.cpan.org/authors/id/B/BI/BINGOS/Module-Load-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.94

%description
Module::Load eliminates the need to know whether you are trying to require
either a file or a module.

%files -f %{name}.files
%doc CHANGES README

%changelog
%autochangelog
