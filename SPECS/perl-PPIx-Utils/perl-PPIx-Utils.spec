# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-PPIx-Utils
Version:        0.004
Release:        %autorelease
Summary:        Utility functions for PPI
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/PPIx-Utils
#!RemoteAsset:  sha256:336918d56ac9482d248d2ca6e79ed7f2cc67403fbdecdd73a9c414a034adb3cf
Source0:        https://www.cpan.org/authors/id/D/DB/DBOOK/PPIx-Utils-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(B::Keywords) >= 1.09
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(PPI) >= 1.250
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(YAML::PP)
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(B::Keywords) >= 1.09
Requires:       perl(PPI) >= 1.250

%description
PPIx::Utils is a collection of utility functions for working with PPI
documents. The functions are organized into submodules, and may be imported
from the appropriate submodule or via this module.

%files -f %{name}.files
%doc Changes CONTRIBUTING.md prereqs.yml README

%changelog
%autochangelog
