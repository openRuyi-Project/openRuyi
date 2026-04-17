# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XXX
Version:        0.38
Release:        %autorelease
Summary:        See Your Data in the Nude
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XXX
#!RemoteAsset:  sha256:d10510ea00f619abf47ab299f148bd5b360cfa07dc0ed518138b7cec72692d2a
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/XXX-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(YAML::PP) >= 0.018
Requires:       perl(YAML::PP) >= 0.018

%description
XXX.pm exports a function called XXX that you can put just about anywhere
    in your Perl code to make it die with a YAML dump of the arguments to
    its right.

%prep
%setup -q -n XXX-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CONTRIBUTING Changes README
%license LICENSE

%changelog
%autochangelog
