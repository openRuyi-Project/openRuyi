# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Time-Local
Version:        1.35
Release:        %autorelease
Summary:        Efficiently compute time from local and GMT time
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Time-Local
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/Time-Local-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(warnings)

%description
This module provides functions that are the inverse of built-in perl
functions localtime() and gmtime(). They accept a date as a six-element
array, and return the corresponding time(2) value in seconds since the
system epoch (Midnight, January 1, 1970 GMT on Unix, for example). This
value can be positive or negative, though POSIX only requires support for
positive values, so dates before the system's epoch may not work on all
operating systems.

%prep
%setup -q -n Time-Local-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc azure-pipelines.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md perlcriticrc perltidyrc precious.toml README.md

%changelog
%autochangelog
