# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Devel-Hide
Version:        0.0016
Release:        %autorelease
Summary:        Forces the unavailability of specified Perl modules (for testing)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Devel-Hide
#!RemoteAsset:  sha256:7830b4a57f7ec7410620d6c0150185449d7b4c9964c39a7dc397056032c32a08
Source0:        https://www.cpan.org/authors/id/D/DC/DCANTRELL/Devel-Hide-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.82

Requires:       perl(Test::More) >= 0.82

%description
Given a list of Perl modules/filenames, this module makes require and
use statements fail (no matter the specified files/modules are
installed or not).

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
