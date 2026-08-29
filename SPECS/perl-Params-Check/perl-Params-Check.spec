# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Params-Check
Version:        0.38
Release:        %autorelease
Summary:        Generic input parsing/checking mechanism
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Params-Check
#!RemoteAsset:  sha256:f0c9d33876c36b1bca1475276d26d2efaf449b256d7cc8118fae012e89a26290
Source0:        https://www.cpan.org/authors/id/B/BI/BINGOS/Params-Check-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Test::More)

%description
Params::Check is a generic input parsing/checking mechanism.

%files -f %{name}.files
%doc CHANGES README

%changelog
%autochangelog
