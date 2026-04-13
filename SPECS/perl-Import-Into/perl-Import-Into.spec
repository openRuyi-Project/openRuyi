# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Import-Into
Version:        1.002005
Release:        %autorelease
Summary:        Import packages into other packages
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Import-Into
#!RemoteAsset:  sha256:bd9e77a3fb662b40b43b18d3280cd352edf9fad8d94283e518181cc1ce9f0567
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Import-Into-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Loading Import::Into creates a global method import::into which you can call on
any package to import it into another package.

%prep
%setup -q -n Import-Into-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
