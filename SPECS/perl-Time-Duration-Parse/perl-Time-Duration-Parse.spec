# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Time-Duration-Parse
Version:        0.16
Release:        %autorelease
Summary:        Parse string that represents time duration
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Time-Duration-Parse
#!RemoteAsset:  sha256:1084a6463ee2790f99215bd76b135ca45afe2bfa6998fa6fd5470b69e1babc12
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Time-Duration-Parse-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Time::Duration)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(Exporter) >= 5.57

%description
Time::Duration::Parse is a module to parse human readable duration strings
like 2 minutes and 3 seconds to seconds.

%prep
%setup -q -n Time-Duration-Parse-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
%autochangelog
