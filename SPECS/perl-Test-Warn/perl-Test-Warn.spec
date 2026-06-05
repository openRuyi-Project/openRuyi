# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Warn
Version:        0.37
Release:        %autorelease
Summary:        Perl extension to test methods for warnings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Warn
#!RemoteAsset:  sha256:98ca32e7f2f5ea89b8bfb9a0609977f3d153e242e2e51705126cb954f1a06b57
Source0:        https://www.cpan.org/authors/id/B/BI/BIGJ/Test-Warn-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp) >= 1.22
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Sub::Uplevel) >= 0.12
BuildRequires:  perl(Test::Builder) >= 0.13
BuildRequires:  perl(Test::Builder::Tester) >= 1.02
BuildRequires:  perl(Test::More)

Requires:       perl(Carp) >= 1.22
Requires:       perl(Sub::Uplevel) >= 0.12
Requires:       perl(Test::Builder) >= 0.13
Requires:       perl(Test::Builder::Tester) >= 1.02

%description
A good style of Perl programming calls for a lot of diverse
regression tests.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
