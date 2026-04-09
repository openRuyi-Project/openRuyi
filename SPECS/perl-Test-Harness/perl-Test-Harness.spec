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
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/Test-Harness-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Usage) >= 1.12

Requires:       perl(Pod::Usage) >= 1.12

%description
This package allows tests to be run and results automatically aggregated and
output to STDOUT.
Although, for historical reasons, the Test::Harness distribution takes its
name from this module it now exists only to provide TAP::Harness with an
interface that is somewhat backwards compatible with Test::Harness 2.xx. If
you're writing new code consider using TAP::Harness directly instead.

%prep
%setup -q -n Test-Harness-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes Changes-2.64 MANIFEST.CUMMULATIVE perlcriticrc README

%changelog
%autochangelog
