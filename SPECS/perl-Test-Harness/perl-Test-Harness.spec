# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Harness
Version:        3.52
Release:        %autorelease
Summary:        Run Perl standard test scripts with statistics
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Harness
#!RemoteAsset:  sha256:8fe65cfc0261ed3c8a4395f0524286f5719669fe305f9b03b16cf3684d62cd70
Source0:        https://www.cpan.org/authors/id/L/LE/LEONT/Test-Harness-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Usage) >= 1.12

Requires:       perl(Pod::Usage) >= 1.12

# don't use cpan2spec's description.
%description
This package allows tests to be run and results automatically aggregated and
output to STDOUT.

%files -f %{name}.files
%doc Changes Changes-2.64 MANIFEST.CUMMULATIVE perlcriticrc README

%changelog
%autochangelog
