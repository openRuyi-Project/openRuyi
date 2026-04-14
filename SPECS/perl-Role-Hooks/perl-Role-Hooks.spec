# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Role-Hooks
Version:        0.008
Release:        %autorelease
Summary:        Role callbacks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Role-Hooks
#!RemoteAsset:  sha256:28d66ea0a8dc306b76da83ff0879493d808f73185bcf9c4ed372f3946fb543ec
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Role-Hooks-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
Requires:       perl(List::Util) >= 1.45

%description
This module allows a role to run a callback when it is applied to a class
or to another role.

%prep
%setup -q -n Role-Hooks-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CREDITS Changes README doap.ttl
%license COPYRIGHT LICENSE

%changelog
%autochangelog
